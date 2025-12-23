import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/physical-AI-humanoid-robotics/__docusaurus/debug',
    component: ComponentCreator('/physical-AI-humanoid-robotics/__docusaurus/debug', 'b48'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/__docusaurus/debug/config',
    component: ComponentCreator('/physical-AI-humanoid-robotics/__docusaurus/debug/config', '90e'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/__docusaurus/debug/content',
    component: ComponentCreator('/physical-AI-humanoid-robotics/__docusaurus/debug/content', '2f9'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/__docusaurus/debug/globalData',
    component: ComponentCreator('/physical-AI-humanoid-robotics/__docusaurus/debug/globalData', '6f9'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/__docusaurus/debug/metadata',
    component: ComponentCreator('/physical-AI-humanoid-robotics/__docusaurus/debug/metadata', '2e7'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/__docusaurus/debug/registry',
    component: ComponentCreator('/physical-AI-humanoid-robotics/__docusaurus/debug/registry', '48b'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/__docusaurus/debug/routes',
    component: ComponentCreator('/physical-AI-humanoid-robotics/__docusaurus/debug/routes', 'f16'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/Chapter/',
    component: ComponentCreator('/physical-AI-humanoid-robotics/Chapter/', '5f2'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/Chapter/%5Bslug%5D',
    component: ComponentCreator('/physical-AI-humanoid-robotics/Chapter/%5Bslug%5D', '468'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/Chapter/Chapter',
    component: ComponentCreator('/physical-AI-humanoid-robotics/Chapter/Chapter', 'a1a'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/search',
    component: ComponentCreator('/physical-AI-humanoid-robotics/search', '03e'),
    exact: true
  },
  {
    path: '/physical-AI-humanoid-robotics/textbook',
    component: ComponentCreator('/physical-AI-humanoid-robotics/textbook', '2b3'),
    routes: [
      {
        path: '/physical-AI-humanoid-robotics/textbook',
        component: ComponentCreator('/physical-AI-humanoid-robotics/textbook', '3d7'),
        routes: [
          {
            path: '/physical-AI-humanoid-robotics/textbook',
            component: ComponentCreator('/physical-AI-humanoid-robotics/textbook', '801'),
            routes: [
              {
                path: '/physical-AI-humanoid-robotics/textbook/chapters/chapter-1-introduction',
                component: ComponentCreator('/physical-AI-humanoid-robotics/textbook/chapters/chapter-1-introduction', '17d'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-AI-humanoid-robotics/textbook/chapters/chapter-2-sensors-actuators',
                component: ComponentCreator('/physical-AI-humanoid-robotics/textbook/chapters/chapter-2-sensors-actuators', '9e0'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-AI-humanoid-robotics/textbook/chapters/chapter-3-control-motion-planning',
                component: ComponentCreator('/physical-AI-humanoid-robotics/textbook/chapters/chapter-3-control-motion-planning', 'bb1'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-AI-humanoid-robotics/textbook/chapters/chapter-4-perception',
                component: ComponentCreator('/physical-AI-humanoid-robotics/textbook/chapters/chapter-4-perception', 'd1f'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-AI-humanoid-robotics/textbook/chapters/chapter-5-ai-agents-decision-making',
                component: ComponentCreator('/physical-AI-humanoid-robotics/textbook/chapters/chapter-5-ai-agents-decision-making', '7d9'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-AI-humanoid-robotics/textbook/chapters/chapter-6-human-robot-interaction-safety',
                component: ComponentCreator('/physical-AI-humanoid-robotics/textbook/chapters/chapter-6-human-robot-interaction-safety', '010'),
                exact: true,
                sidebar: "tutorialSidebar"
              },
              {
                path: '/physical-AI-humanoid-robotics/textbook/chapters/chapter-7-future-work-humanoid-robots',
                component: ComponentCreator('/physical-AI-humanoid-robotics/textbook/chapters/chapter-7-future-work-humanoid-robots', '378'),
                exact: true,
                sidebar: "tutorialSidebar"
              }
            ]
          }
        ]
      }
    ]
  },
  {
    path: '/physical-AI-humanoid-robotics/',
    component: ComponentCreator('/physical-AI-humanoid-robotics/', 'cd0'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
