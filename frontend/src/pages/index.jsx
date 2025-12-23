import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">{siteConfig.title}</h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/textbook/chapters/chapter-1-introduction">
            Read the Textbook - 7 Chapters
          </Link>
          <Link
            className="button button--outline button--secondary button--lg"
            to="#features"
            style={{marginLeft: '1rem'}}>
            Learn More
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="Interactive textbook on Physical AI and Humanoid Robotics with AI-powered learning support">
      <HomepageHeader />
      <main>
        <section id="features" className={styles.featuresSection}>
          <div className="container padding-horiz--md">
            <div className="row">
              <div className="col col--4">
                <div className="text--center padding-horiz--md">
                  <h2>Advanced Topics</h2>
                  <p>Comprehensive coverage of Physical AI, sensors, actuators, control systems, perception, and human-robot interaction.</p>
                  <Link
                    className="button button--outline button--secondary button--sm"
                    to="/textbook/chapters/chapter-2-sensors-actuators">
                    Sensors & Actuators
                  </Link>
                  <Link
                    className="button button--outline button--secondary button--sm"
                    to="/textbook/chapters/chapter-3-control-motion-planning"
                    style={{marginLeft: '0.5rem'}}>
                    Control Systems
                  </Link>
                  <Link
                    className="button button--outline button--secondary button--sm"
                    to="/textbook/chapters/chapter-4-perception"
                    style={{marginLeft: '0.5rem'}}>
                    Perception
                  </Link>
                </div>
              </div>
              <div className="col col--4">
                <div className="text--center padding-horiz--md">
                  <h2>AI Integration</h2>
                  <p>Learn how artificial intelligence powers modern humanoid robots with decision-making and adaptive behaviors.</p>
                  <Link
                    className="button button--outline button--secondary button--sm"
                    to="/textbook/chapters/chapter-5-ai-agents-decision-making">
                    AI Agents & Decision Making
                  </Link>
                </div>
              </div>
              <div className="col col--4">
                <div className="text--center padding-horiz--md">
                  <h2>Future-Focused</h2>
                  <p>Explore cutting-edge research and future directions in humanoid robotics and embodied AI.</p>
                  <Link
                    className="button button--outline button--secondary button--sm"
                    to="/textbook/chapters/chapter-6-human-robot-interaction-safety">
                    HRI & Safety
                  </Link>
                  <Link
                    className="button button--outline button--secondary button--sm"
                    to="/textbook/chapters/chapter-7-future-work-humanoid-robots"
                    style={{marginLeft: '0.5rem'}}>
                    Future Work
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className={styles.chaptersOverview}>
          <div className="container padding-horiz--md">
            <div className="text--center padding-bottom--lg">
              <h2>Textbook Overview</h2>
              <p>Dive deep into the fascinating world of Physical AI and Humanoid Robotics</p>
            </div>

            <div className="row">
              <div className="col col--3 padding--sm">
                <div className="card">
                  <div className="card__header">
                    <h3>Chapter 1</h3>
                    <small>Introduction</small>
                  </div>
                  <div className="card__body">
                    <p>Fundamentals of Physical AI and humanoid robotics concepts.</p>
                  </div>
                  <div className="card__footer">
                    <Link
                      className="button button--primary button--block"
                      to="/textbook/chapters/chapter-1-introduction">
                      Read More
                    </Link>
                  </div>
                </div>
              </div>
              <div className="col col--3 padding--sm">
                <div className="card">
                  <div className="card__header">
                    <h3>Chapter 2</h3>
                    <small>Sensors & Actuators</small>
                  </div>
                  <div className="card__body">
                    <p>Understanding the hardware components that enable robot perception and movement.</p>
                  </div>
                  <div className="card__footer">
                    <Link
                      className="button button--primary button--block"
                      to="/textbook/chapters/chapter-2-sensors-actuators">
                      Read More
                    </Link>
                  </div>
                </div>
              </div>
              <div className="col col--3 padding--sm">
                <div className="card">
                  <div className="card__header">
                    <h3>Chapters 3-4</h3>
                    <small>Control & Perception</small>
                  </div>
                  <div className="card__body">
                    <p>Motion planning, control systems, and environmental perception techniques.</p>
                  </div>
                  <div className="card__footer">
                    <Link
                      className="button button--primary button--block"
                      to="/textbook/chapters/chapter-3-control-motion-planning">
                      Read More
                    </Link>
                  </div>
                </div>
              </div>
              <div className="col col--3 padding--sm">
                <div className="card">
                  <div className="card__header">
                    <h3>Chapters 5-7</h3>
                    <small>AI & Future</small>
                  </div>
                  <div className="card__body">
                    <p>Decision-making, safety, and future developments in humanoid robotics.</p>
                  </div>
                  <div className="card__footer">
                    <Link
                      className="button button--primary button--block"
                      to="/textbook/chapters/chapter-5-ai-agents-decision-making">
                      Read More
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className={styles.ctaSection}>
          <div className="container text--center padding-horiz--md">
            <h2>Start Your Journey in Physical AI & Robotics</h2>
            <p>Join thousands of students and professionals learning about the future of robotics</p>
            <Link
              className="button button--primary button--lg"
              to="/textbook/chapters/chapter-1-introduction">
              Begin Reading
            </Link>
          </div>
        </section>
      </main>
    </Layout>
  );
}