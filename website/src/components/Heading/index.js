import React from "react";

export default function Heading({ text }) {
  return (
    <span>
      {console.log(text.split(" "))}
      {text.split(" ").map((word) => {
        {
          console.log(word[0], word.substr(1), word);
        }
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
