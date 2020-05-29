import React, { Component } from "react";
import "./Video.css";

class Video extends Component {
  constructor(props) {
    super(props);
    this.state = {
      check: false,
      isModalOpen: false,
      labelArray: [],
      adultCnt: 0,
      bloodCnt: 0,
      knifeCnt: 0,
      smokeCnt: 0,
      result: {}
    };
  }

  openModal = () => {
    document.querySelector("body").style.overflow = "hidden";
    this.setState({ isModalOpen: true });
  };

  closeModal = () => {
    document.querySelector("body").style.overflow = "";
    this.setState({ isModalOpen: false });
  };

  render() {
    return (
      <div className="Video">
        <button
          className="Filter-box Filter-video-filter"
          disabled={!this.props.successfulFiltered}
          onClick={() => {
            this.openModal();
          }}
        ></button>
      </div>
    );
  }
}

export default Video;