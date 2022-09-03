import React from "react";

export default function Heading({ text }) {
  return (
    <span>
      {text.split(" ").map((word) => {
        return (
          <>
            <span style={{ color: "#080808" }}>{word[0]}</span>
            {word.substr(1) + " "}
          </>
        );
      })}
    </span>
  );
}
