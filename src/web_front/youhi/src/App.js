import React from "react";
import Navbar from "./component/navbar/Navbar";
import Introduction from "./component/introduction/Introduction"
import Upload from "./component/upload/Upload"
import "./App.css";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Introduction />
      <Upload />
    </div>
  );
}

export default App;
