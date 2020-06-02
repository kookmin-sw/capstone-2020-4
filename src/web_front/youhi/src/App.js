import React, {useState} from "react";
import Introduction from "./component/introduction/Introduction";
import Upload from "./component/upload/Upload";
import Filter from './component/filter/Filter';
import './App.css';
import Navbar from './component/navbar/Navbar';

const App = () => {
  const [showResult, setShowResult] = useState(false);

  return (
    <div className="App">
      <Navbar />
      <div className="Total">
      <Introduction />
      <Upload func={setShowResult} />
      <Filter showResult={showResult} />
      </div>
    </div>
  )
}

export default App;