import React, {useEffect, useState} from 'react';
import Title from "./components/title";

export default function App() {
  const [fact, setFact] = useState("");
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = () => {
    fetch("https://catfact.ninja/fact")
        .then((result) => result.json())
        .then((data) => setFact(data.fact));
  };

  return (
    <Title text={fact}/>
  );
}
