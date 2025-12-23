"""Initial tables

Revision ID: 001
Revises:
Create Date: 2025-12-10 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create User table
    op.create_table('users',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password_hash', sa.String(), nullable=False),
        sa.Column('technical_proficiency', postgresql.JSONB(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('last_activity_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('data_retention_until', sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )

    # Create TextbookChapter table
    op.create_table('textbook_chapters',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('title', sa.String(length=500), nullable=False),
        sa.Column('slug', sa.String(length=500), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('content_urdu', sa.Text(), nullable=True),
        sa.Column('difficulty_level', sa.String(length=20), nullable=True),
        sa.Column('prerequisite_chapters', postgresql.ARRAY(postgresql.UUID(as_uuid=True)), nullable=True),
        sa.Column('tags', postgresql.ARRAY(sa.String()), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('version', sa.Integer(), nullable=False, server_default=sa.text('1')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug')
    )

    # Create UserProgress table
    op.create_table('user_progress',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('chapter_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=True),
        sa.Column('completion_percentage', sa.Float(), nullable=True),
        sa.Column('time_spent_seconds', sa.Integer(), nullable=True),
        sa.Column('last_accessed_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('quiz_scores', postgresql.JSONB(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.ForeignKeyConstraint(['chapter_id'], ['textbook_chapters.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'chapter_id')
    )

    # Create ChatbotSession table
    op.create_table('chatbot_sessions',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('session_token', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id'),
        sa.CheckConstraint('user_id IS NOT NULL OR session_token IS NOT NULL', name='user_id_or_session_token')
    )

    # Create ChatbotMessage table
    op.create_table('chatbot_messages',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('session_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('role', sa.String(length=20), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('timestamp', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('source_chunks', postgresql.JSONB(), nullable=True),
        sa.Column('is_fallback_response', sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(['session_id'], ['chatbot_sessions.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # Create TranslationCache table
    op.create_table('translation_cache',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
        sa.Column('content_id', sa.String(length=500), nullable=False),
        sa.Column('content_type', sa.String(length=100), nullable=False),
        sa.Column('source_language', sa.String(length=10), nullable=False),
        sa.Column('target_language', sa.String(length=10), nullable=False),
        sa.Column('source_content_hash', sa.String(length=64), nullable=False),
        sa.Column('translated_content', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Create indexes
    op.create_index('ix_users_email', 'users', ['email'])
    op.create_index('ix_textbook_chapters_slug', 'textbook_chapters', ['slug'])
    op.create_index('ix_textbook_chapters_order', 'textbook_chapters', ['version'])
    op.create_index('ix_user_progress_user', 'user_progress', ['user_id'])
    op.create_index('ix_user_progress_chapter', 'user_progress', ['chapter_id'])
    op.create_index('ix_translation_cache_content', 'translation_cache', ['content_id', 'source_language', 'target_language'])
    op.create_index('ix_chatbot_sessions_user', 'chatbot_sessions', ['user_id'])
    op.create_index('ix_chatbot_sessions_token', 'chatbot_sessions', ['session_token'])
    op.create_index('ix_chatbot_messages_session', 'chatbot_messages', ['session_id'])
    op.create_index('ix_chatbot_messages_created', 'chatbot_messages', ['timestamp'])


def downgrade() -> None:
    # Drop indexes
    op.drop_index('ix_chatbot_messages_created', table_name='chatbot_messages')
    op.drop_index('ix_chatbot_messages_session', table_name='chatbot_messages')
    op.drop_index('ix_chatbot_sessions_token', table_name='chatbot_sessions')
    op.drop_index('ix_chatbot_sessions_user', table_name='chatbot_sessions')
    op.drop_index('ix_translation_cache_content', table_name='translation_cache')
    op.drop_index('ix_user_progress_chapter', table_name='user_progress')
    op.drop_index('ix_user_progress_user', table_name='user_progress')
    op.drop_index('ix_textbook_chapters_order', table_name='textbook_chapters')
    op.drop_index('ix_textbook_chapters_slug', table_name='textbook_chapters')
    op.drop_index('ix_users_email', table_name='users')

    # Drop tables
    op.drop_table('chatbot_messages')
    op.drop_table('chatbot_sessions')
    op.drop_table('translation_cache')
    op.drop_table('user_progress')
    op.drop_table('textbook_chapters')
    op.drop_table('users')