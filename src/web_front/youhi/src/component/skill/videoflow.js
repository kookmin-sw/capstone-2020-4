import React, { Component } from "react";
import "./videoflow.css";

import Filteringflow from "../../img/filteringflow.png";



class Videoflow extends Component {
  render() {
    return (
      <div className="ob-con">
        <div className="object-detection">
          <div className="object-title"> Youhi Filtering Flow </div>
        </div>
        <div className="flow_flow">
          <div>
            <div className="video_flow_text">filtering flow </div>
            <img src={Filteringflow} alt="" className="flow-img" />
          </div>
        </div>
      </div>
    );
  }
}

export default Videoflow;
