import React from "react";
import clsx from "clsx";
import styles from "./styles.module.css";

const FeatureList = [
  {
    title: "Fetch problems",
    demo: require("@site/static/gif/fetch.gif").default,
    description: (
      <>
        Retrieve testcase data from online judge and create source code file
        with boilerplate code.
      </>
    ),
  },
  {
    title: "Run testcases",
    demo: require("@site/static/gif/run.gif").default,
    description: <>Run your source code against the sample testcases.</>,
  },
  {
    title: "Stress test",
    demo: require("@site/static/gif/stress.gif").default,
    description: (
      <>Run your source code against randomly generated testcases.</>
    ),
  },
];

function Feature({ demo, title, description }) {
  return (
    <div className={clsx("col col--4")}>
      <div className="text--center">
        <img src={demo} alt="demo video" />
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
