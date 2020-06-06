import React, {useState} from "react";
import Introduction from "./component/introduction/Introduction";
import Upload from "./component/upload/Upload";
import Filter from './component/filter/Filter';
import "./App.css";

import Loginmodal from "./component/filter/exception/exception";

function Home() {
    const [showResult, setShowResult ] = useState(false);

  return (
    <div className="App">
      <div className="Total">
        <Introduction />
        <Upload func={setShowResult}/>
        <Filter showResult={showResult}/>
      </div>
    </div>
  );
}

export default Home;
