import React from "react";
import clsx from "clsx";
import styles from "./styles.module.css";

const FeatureList = [
  {
    title: "Fetch problems",
    description: (
      <>
        Retrieve testcase data from online judge and create source code file
        with boilerplate code.
      </>
    ),
  },
  {
    title: "Run testcases",
    description: <>Run your source code against the sample testcases.</>,
  },
  {
    title: "Stress test",
    description: (
      <>Run your source code against randomly generated testcases.</>
    ),
  },
  {
    title: "Manage testcases",
    description: (
      <>
        Add, view, edit, and delete testcases without filling up your workspace.
      </>
    ),
  },
];

function Feature({ demo, title, description }) {
  return (
    <div className={clsx("col col--4")}>
      <div className={clsx("text--center", styles.feature)}>
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section>
      <div className="container">
        <div className={styles["features-heading"]}>
          <h2>Key Features</h2>
        </div>
        <div className={clsx("row", styles["features-list"])}>
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
