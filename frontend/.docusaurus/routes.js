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
    path: '/physical-AI-humanoid-robotics/docs',
    component: ComponentCreator('/physical-AI-humanoid-robotics/docs', 'f89'),
    routes: [
      {
        path: '/physical-AI-humanoid-robotics/docs',
        component: ComponentCreator('/physical-AI-humanoid-robotics/docs', '143'),
        routes: [
          {
            path: '/physical-AI-humanoid-robotics/docs',
            component: ComponentCreator('/physical-AI-humanoid-robotics/docs', '6ea'),
            routes: [
              {
                path: '/physical-AI-humanoid-robotics/docs/intro',
                component: ComponentCreator('/physical-AI-humanoid-robotics/docs/intro', '47f'),
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
    path: '/physical-AI-humanoid-robotics/textbook',
    component: ComponentCreator('/physical-AI-humanoid-robotics/textbook', 'e26'),
    routes: [
      {
        path: '/physical-AI-humanoid-robotics/textbook',
        component: ComponentCreator('/physical-AI-humanoid-robotics/textbook', '02e'),
        routes: [
          {
            path: '/physical-AI-humanoid-robotics/textbook',
            component: ComponentCreator('/physical-AI-humanoid-robotics/textbook', 'f94'),
            routes: [
              {
                path: '/physical-AI-humanoid-robotics/textbook/intro',
                component: ComponentCreator('/physical-AI-humanoid-robotics/textbook/intro', '565'),
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
    path: '*',
    component: ComponentCreator('*'),
  },
];
