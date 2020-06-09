import React, { Component } from "react";
import VoiceModal from "./Modal";
import "./Voice.css";

class Voice extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isModalOpen: false,
      check: false,
      imgArray: [],
      swearArray: [],
    };
  }

  go = async () => {
    const clientID = this.props.clientID;
    var res,
      data,
      swearArrayCopy = [],
      imgArrayCopy = [];
    res = await fetch(`./static/${clientID}/subtitle_result.txt`);
    data = await res.text();
    imgArrayCopy = data.length ? this.returnimgArray(data) : imgArrayCopy;

    res = await fetch(`./static/${clientID}/${clientID}_filter.txt`);
    data = await res.text();
    swearArrayCopy = data.length ? this.returnSwearArray(data) : swearArrayCopy;

    this.setState({ imgArray: imgArrayCopy, swearArray: swearArrayCopy, check: true }, () => {
      console.log("imgArray", this.state.imgArray);
      console.log("swearArray", this.state.swearArray);
    });
  };

  returnimgArray = (data) => {
    var dataArray = data.split("\n");
    var returnArray = [];
    var i = 0;
    if (data[0] !== "<") {
      for (; i < data.length; i++) {
        if (dataArray[i] !== "") {
          returnArray.push(dataArray[i]);
        }
      }
    }
    return returnArray;
  }

  returnSwearArray = (data) => {
    var copy = [];
    if (data[0] !== "<") {
      const dataArray = data.split("\n");
      var i = 0;
      for (; i < dataArray.length; i++) {
        const dataArrayElement = dataArray[i].split("/");
        console.log(dataArrayElement);
        copy.push([[dataArrayElement[0].trim()], [dataArrayElement[1].trim()]])
      }
    } else {
      copy.push("There's no result!");
    }
    return copy;
  }

  openModal = () => {
    document.querySelector("body").style.overflow = "hidden";
    this.setState({ isModalOpen: true });
  };

  closeModal = () => {
    document.querySelector("body").style.overflow = "";
    this.setState({ isModalOpen: false });
  };

  renderVoiceModal = () => {
    if (this.state.check) {
      return (
        <VoiceModal
          isOpen={this.state.isModalOpen}
          close={this.closeModal}
          imgArray={this.state.imgArray}
          swearArray={this.state.swearArray}
          clientID={this.props.clientID}
        />
      );
    }
  }

  render() {
    return (
      <div className="Voice">
        <button
          className="Filter-box Filter-voice-filter"
          onClick={() => {
            this.openModal();
            this.go();
          }}
        ></button>
        {this.renderVoiceModal()}
      </div>
    );
  }
}

export default Voice;
