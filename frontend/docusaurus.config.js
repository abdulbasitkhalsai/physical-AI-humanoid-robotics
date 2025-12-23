// @ts-check
// `@type` JSDoc annotations allow IDEs and type checkers
// to scan the JS code and display type information.

// Note: type annotations allow type checking and IDEs autocompletion

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics Textbook',
  tagline: 'Interactive textbook on Physical AI and Humanoid Robotics with AI-powered learning support',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://abdulbasitkhalsai.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/physical-AI-humanoid-robotics/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'abdulbasitkhalsai', // Usually your GitHub org/user name.
  projectName: 'physical-AI-humanoid-robotics', // Usually your repo name.
  deploymentBranch: 'gh-pages', // Branch to deploy to

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  markdown: {
    format: 'detect',
    mermaid: false,
    mdx1Compat: {
      comments: true,
      admonitions: true,
      headingIds: true,
    },
  },

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'ur'], // Support English and Urdu as per requirements
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl: 'https://github.com/abdulbasitkhalsai/physical-AI-humanoid-robotics/edit/main/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
          path: 'docs',        // Source dir for doc files
          routeBasePath: 'textbook', // URL Route for docs
        },
        blog: false, // Disable blog as per textbook focus
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  plugins: [
    // Plugin for custom remark/rehype processing if needed
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/textbook-social-card.jpg',
      navbar: {
        title: 'Physical AI & Humanoid Robotics',
        logo: {
          alt: 'Physical AI & Humanoid Robotics Textbook',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Textbook Chapters',
          },
          {
            to: '/textbook/chapters/chapter-1-introduction',
            label: 'Textbook',
            position: 'left'
          },
          {
            to: '/textbook/chapters/chapter-1-introduction', // Updated for MVP static site
            label: 'API',
            position: 'left'
          },
          {
            type: 'localeDropdown',
            position: 'right',
          },
          {
            href: 'https://github.com/abdulbasitkhalsai/physical-AI-humanoid-robotics',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Textbook',
            items: [
              {
                label: 'Introduction',
                to: '/textbook/chapters/chapter-1-introduction',
              },
              {
                label: 'Sensors & Actuators',
                to: '/textbook/chapters/chapter-2-sensors-actuators',
              },
              {
                label: 'Control & Motion Planning',
                to: '/textbook/chapters/chapter-3-control-motion-planning',
              },
              {
                label: 'Perception',
                to: '/textbook/chapters/chapter-4-perception',
              },
            ],
          },
          {
            title: 'Features',
            items: [
              {
                label: 'AI-Powered Chatbot',
                to: '/textbook/chapters/chapter-1-introduction', // Placeholder for MVP
              },
              {
                label: 'Personalized Learning',
                to: '/textbook/chapters/chapter-1-introduction', // Placeholder for MVP
              },
              {
                label: 'Urdu Translation',
                to: '/textbook/chapters/chapter-1-introduction', // Available in MVP
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'GitHub Discussions',
                href: 'https://github.com/abdulbasitkhalsai/physical-AI-humanoid-robotics/discussions',
              },
              {
                label: 'Issues',
                href: 'https://github.com/abdulbasitkhalsai/physical-AI-humanoid-robotics/issues',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Abdul Basit Khalasi. Built with Docusaurus for the Physical AI & Humanoid Robotics Textbook.`,
      },
      prism: {
        theme: require('prism-react-renderer').themes.github,
        darkTheme: require('prism-react-renderer').themes.dracula,
        additionalLanguages: ['python', 'javascript', 'json', 'bash'],
      },
      algolia: {
        // The application ID provided by Algolia
        appId: 'YOUR_ALGOLIA_APP_ID',

        // Public API key: it is safe to commit it
        apiKey: 'YOUR_ALGOLIA_API_KEY',

        indexName: 'physical-ai-humanoid-robotics',

        // Optional: see doc section below
        contextualSearch: true,

        // Optional: Specify domains where the navigation should occur through window.location instead on history.push. Useful when our Algolia config crawls multiple documentation sites and we want to navigate with window.location.href to them.
        externalUrlRegex: 'external\\.com|domain\\.com',

        // Optional: Replace parts of the item URLs from Algolia. Useful when using the same search index for multiple deployments using a different baseUrl. You can use regexp or string in the `from` param. For example: localhost:3000 vs myCompany.com/docs
        replaceSearchResultPathname: {
          from: '/docs/', // or as RegExp: /\/docs\//
          to: '/textbook/',
        },

        // Optional: Algolia search parameters
        searchParameters: {},

        // Optional: path for search page that enabled by default (`false` to disable it)
        searchPagePath: 'search',
      },
    }),
};

module.exports = config;