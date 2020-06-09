import React, { Component } from "react";
import "./videoflow.css";

import Filteringflow from "../../img/filteringflow.png";



class Videoflow extends Component {
  render() {
    return (
      <div className="flow-container">
        <div className="object-detection">
          <div className="object-title"> Youhi Filtering Flow </div>
          <div className="object-bar" />
        </div>
        <div className="flow_flow">
          <div>
            <img src={Filteringflow} alt="" className="flow-img" />
          </div>
        </div>
      </div>
    );
  }
}

export default Videoflow;
