import React, { Component } from "react";
import FilterElement from "./filter_elementor/FilterElementor";
import "./Filter.css";
import VideoBox from "./video/Video";
import VoiceBox from "./voice/Voice";
import Feedback from "../feedback/Feedback";

class Filter extends Component {
  constructor(props) {
    super(props);
    this.state = {
      socketConnection: false,

    };
    this.filterWrapperRef = React.createRef();
  }

  notYetText = () => {
    if (!this.props.showResult[0]) {
      return (
        <div className="Filter-not-yet">
          결과는 검열이 끝난 후 확인 가능합니다.
        </div>
      );
    }
  };

  componentDidUpdate() {
      const obj = this.filterWrapperRef.current;
      obj.removeAttribute("style");
      if (!this.props.showResult[0]) 
        obj.style.height = "0";
      else 
        obj.style.maxHeight = "800px";
  }
  

  render() {
    return (
      <div className="Filter-container">
        <FilterElement />
        {this.notYetText()}
        <div
          className={`${
            this.props.showResult[0] ? "Filter-wrapper" : "Filter-wrapper-closed"
          }`}
          ref={this.filterWrapperRef}
        >
          <div className="Filter-filter-box">
            <div className="inner-filter-wrapper">
              <VideoBox clientID={this.props.showResult[1]} />
            </div>
            <div className="inner-filter-wrapper">
              <VoiceBox clientID={this.props.showResult[1]} />
            </div>
          </div>
        </div>
        <Feedback />
      </div>
    );
  }
}

export default Filter;
