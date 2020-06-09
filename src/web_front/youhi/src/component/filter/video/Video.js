import React, { Component } from "react";
import VideoModal from "./VideoModal";
import "./VideoModal.css";
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
      result: {},
    };
  }

  go = async () => {
    const clientID = this.props.clientID;
    var res,
      data,
      result = { labelArray: [], cntArray: [] };
    res = await fetch(`./static/${clientID}/adult_result.txt`);
    data = await res.text();
    result = data.length
      ? this.collectLabelData(result, data, "adult")
      : this.addZero(result);

    res = await fetch(`./static/${clientID}/blood_result.txt`);
    data = await res.text();
    result = data.length
      ? this.collectLabelData(result, data, "blood")
      : this.addZero(result);

    res = await fetch(`./static/${clientID}/knife_result.txt`);
    data = await res.text();
    result = data.length
      ? this.collectLabelData(result, data, "knife")
      : this.addZero(result);

    res = await fetch(`./static/${clientID}/smoke_result.txt`);
    data = await res.text();
    result = data.length
      ? this.collectLabelData(result, data, "smoke")
      : this.addZero(result);

    this.setState(
      {
        result: result,
        check: true,
      },
      () => { }
    );
  };

  addZero = (result) => {
    var resultCopy = result;
    resultCopy.cntArray.push(0);
    return resultCopy;
  };

  collectLabelData = (result, data, label) => {
    var resultCopy = result;
    if (data[0] !== "<") {
      const dataArray = data.split("\n");
      var i = 0;
      for (; i < dataArray.length; i++) {
        if (dataArray[i] !== "") {
          resultCopy.labelArray[parseInt(dataArray[i])] = label;
        }
      }
      resultCopy.cntArray.push(dataArray.length - 1);
    } else {
      resultCopy.cntArray.push(0);
    }
    return resultCopy;
  };

  openModal = () => {
    document.querySelector("body").style.overflow = "hidden";
    this.setState({ isModalOpen: true });
  };

  closeModal = () => {
    document.querySelector("body").style.overflow = "";
    this.setState({ isModalOpen: false });
  };

  renderVideoModal = () => {
    if (this.state.check) {
      return (
        <VideoModal
          isOpen={this.state.isModalOpen}
          close={this.closeModal}
          result={this.state.result}
          clientID={this.props.clientID}
        />
      );
    }
  };

  render() {
    return (
      <div className="Video">
        <button
          className="Filter-box Filter-video-filter"
          onClick={() => {
            this.openModal();
            this.go();
          }}
        ></button>
        {this.renderVideoModal()}
      </div>
    );
  }
}

export default Video;
