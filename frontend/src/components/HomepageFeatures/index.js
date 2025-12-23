import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';

const FeatureList = [
  {
    title: 'Advanced Robotics Concepts',
    Svg: require('../../static/img/robot-icon.svg').default,
    description: (
      <>
        Comprehensive coverage of Physical AI, sensors, actuators, control systems,
        perception, and human-robot interaction fundamentals.
      </>
    ),
  },
  {
    title: 'AI Integration',
    Svg: require('../../static/img/ai-icon.svg').default,
    description: (
      <>
        Learn how artificial intelligence powers modern humanoid robots with
        decision-making and adaptive behaviors.
      </>
    ),
  },
  {
    title: 'Future-Focused Learning',
    Svg: require('../../static/img/future-icon.svg').default,
    description: (
      <>
        Explore cutting-edge research and future directions in humanoid
        robotics and embodied AI.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}