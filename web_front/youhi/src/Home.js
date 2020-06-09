import React, {useState} from "react";
import Introduction from "./component/introduction/Introduction";
import Upload from "./component/upload/Upload";
import Filter from './component/filter/Filter';
import Footer from './component/footer/footer';
import "./App.css";



function Home() {
    const [showResult, setShowResult ] = useState(false);

  return (
    <div className="App">
      <div className="Total">
        <Introduction />
        <Upload func={setShowResult}/>
        <Filter showResult={showResult}/>
      </div>
      <Footer/>
    </div>
  );
}

export default Home;
