import React, { useState, useEffect } from 'react';
import { useLocation, Link } from 'react-router-dom';
import styles from './TextbookViewer.module.css';
import apiClient from '../../services/api_client';

const TextbookViewer = ({ chapterId, slug }) => {
  const [chapter, setChapter] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [allChapters, setAllChapters] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);
  const [showSearchResults, setShowSearchResults] = useState(false);
  const location = useLocation();

  // Extract slug from URL if not provided as prop
  const chapterSlug = slug || location.pathname.split('/').pop();

  useEffect(() => {
    const loadChapter = async () => {
      try {
        setLoading(true);
        const data = await apiClient.getChapter(chapterSlug);
        setChapter(data);
        setError(null);
      } catch (err) {
        setError('Failed to load chapter content');
        console.error('Error loading chapter:', err);
      } finally {
        setLoading(false);
      }
    };

    // Load all chapters for navigation
    const loadAllChapters = async () => {
      try {
        const data = await apiClient.getChapters();
        setAllChapters(data.chapters || []);
      } catch (err) {
        console.error('Error loading chapters for navigation:', err);
      }
    };

    if (chapterSlug) {
      loadChapter();
    }
    loadAllChapters();
  }, [chapterSlug]);

  // Handle search functionality
  const handleSearch = (term) => {
    setSearchTerm(term);
    if (term.trim() === '') {
      setSearchResults([]);
      setShowSearchResults(false);
      return;
    }

    const results = allChapters.filter(chapter =>
      chapter.title.toLowerCase().includes(term.toLowerCase()) ||
      (chapter.tags && chapter.tags.some(tag =>
        tag.toLowerCase().includes(term.toLowerCase())
      ))
    );
    setSearchResults(results);
    setShowSearchResults(true);
  };

  // Find current chapter index for navigation
  const currentChapterIndex = allChapters.findIndex(ch => ch.slug === chapterSlug);
  const prevChapter = currentChapterIndex > 0 ? allChapters[currentChapterIndex - 1] : null;
  const nextChapter = currentChapterIndex < allChapters.length - 1 ? allChapters[currentChapterIndex + 1] : null;

  if (loading) {
    return (
      <div className={styles.textbookViewer}>
        <div className={styles.loading}>Loading chapter...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className={styles.textbookViewer}>
        <div className={styles.error}>{error}</div>
      </div>
    );
  }

  if (!chapter) {
    return (
      <div className={styles.textbookViewer}>
        <div className={styles.noContent}>Chapter not found</div>
      </div>
    );
  }

  return (
    <div className={styles.textbookViewer}>
      {/* Search Bar */}
      <div className={styles.searchContainer}>
        <input
          type="text"
          placeholder="Search chapters..."
          value={searchTerm}
          onChange={(e) => handleSearch(e.target.value)}
          onFocus={() => setShowSearchResults(true)}
          className={styles.searchInput}
        />
        {showSearchResults && searchResults.length > 0 && (
          <div className={styles.searchResults}>
            {searchResults.map((result, index) => (
              <Link
                key={index}
                to={`/chapter/${result.slug}`}
                className={styles.searchResultItem}
                onClick={() => {
                  setSearchTerm('');
                  setShowSearchResults(false);
                }}
              >
                {result.title}
              </Link>
            ))}
          </div>
        )}
      </div>

      {/* Navigation Bar */}
      <nav className={styles.chapterNavigation}>
        {prevChapter ? (
          <Link to={`/chapter/${prevChapter.slug}`} className={`${styles.navLink} ${styles.prev}`}>
            ← {prevChapter.title}
          </Link>
        ) : (
          <span className={`${styles.navLink} ${styles.prev} ${styles.disabled}`}>← Previous</span>
        )}

        <select
          className={styles.chapterSelect}
          value={chapterSlug}
          onChange={(e) => window.location.href = `/chapter/${e.target.value}`}
        >
          {allChapters.map((ch, index) => (
            <option key={ch.slug} value={ch.slug}>
              {index + 1}. {ch.title}
            </option>
          ))}
        </select>

        {nextChapter ? (
          <Link to={`/chapter/${nextChapter.slug}`} className={`${styles.navLink} ${styles.next}`}>
            {nextChapter.title} →
          </Link>
        ) : (
          <span className={`${styles.navLink} ${styles.next} ${styles.disabled}`}>Next →</span>
        )}
      </nav>

      {/* Chapter Content */}
      <article className={styles.chapterContent}>
        <header className={styles.chapterHeader}>
          <h1>{chapter.title}</h1>
          <div className={styles.chapterMeta}>
            <span className={styles.difficulty}>
              Difficulty: <span className={`${styles.level} ${styles[chapter.difficulty_level] || styles.beginner}`}>
                {chapter.difficulty_level || 'Beginner'}
              </span>
            </span>
          </div>
        </header>

        <div
          className={styles.chapterBody}
          dangerouslySetInnerHTML={{ __html: chapter.content }}
        />

        {chapter.tags && chapter.tags.length > 0 && (
          <footer className={styles.chapterFooter}>
            <div className={styles.tags}>
              {chapter.tags.map((tag, index) => (
                <span key={index} className={styles.tag}>
                  {tag}
                </span>
              ))}
            </div>
          </footer>
        )}
      </article>

      {/* Chapter Navigation Footer */}
      <nav className={`${styles.chapterNavigation} ${styles.footer}`}>
        {prevChapter ? (
          <Link to={`/chapter/${prevChapter.slug}`} className={`${styles.navLink} ${styles.prev}`}>
            ← Previous: {prevChapter.title}
          </Link>
        ) : (
          <span className={`${styles.navLink} ${styles.prev} ${styles.disabled}`}>← Previous</span>
        )}

        {nextChapter ? (
          <Link to={`/chapter/${nextChapter.slug}`} className={`${styles.navLink} ${styles.next}`}>
            Next: {nextChapter.title} →
          </Link>
        ) : (
          <span className={`${styles.navLink} ${styles.next} ${styles.disabled}`}>Next →</span>
        )}
      </nav>
    </div>
  );
};

export default TextbookViewer;