import React from "react";
import Navbar from "./component/navbar/Navbar";
import Introduction from "./component/introduction/Introduction";
import Upload from "./component/upload/Upload";
import Filter from "./component/filter/Filter";
import "./App.css";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Introduction />
      <Upload />
      <Filter />
    </div>
  );
}

export default App;
