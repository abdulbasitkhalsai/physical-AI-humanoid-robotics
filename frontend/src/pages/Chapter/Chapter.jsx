import React from 'react';
import { useParams } from 'react-router-dom';
import TextbookViewer from '../../components/TextbookViewer';

const Chapter = () => {
  const { slug } = useParams();

  return (
    <div className="chapter-page">
      <TextbookViewer slug={slug} />
    </div>
  );
};

export default Chapter;