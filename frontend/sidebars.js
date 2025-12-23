// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Textbook Chapters',
      items: [
        'chapters/chapter-1-introduction',
        'chapters/chapter-2-sensors-actuators',
        'chapters/chapter-3-control-motion-planning',
        'chapters/chapter-4-perception',
        'chapters/chapter-5-ai-agents-decision-making',
        'chapters/chapter-6-human-robot-interaction-safety',
        'chapters/chapter-7-future-work-humanoid-robots',
      ],
    },
  ],
};

module.exports = sidebars;