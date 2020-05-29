import React, { useState, useRef, useEffect } from "react";
import ReactTransitionGroup from "react-addons-css-transition-group";
import "./VideoModal.css";

const VideoModal = ({ isOpen, close, result }) => {
  return (
    <div>
      {isOpen ? (
        <ReactTransitionGroup
          transitionName={"Modal-anim"}
          transitionEnterTimeout={200}
          transitionLeaveTimeout={200}
        >
          <div className="VideoModal-overlay" onClick={close} />
          <div className="VideoModal">
            <p className="title">영상 검열 결과</p>
            <div className="content"></div>
            <div className="button-wrap">
              <button onClick={close}>Confirm</button>
            </div>
          </div>
        </ReactTransitionGroup>
      ) : (
        <ReactTransitionGroup
          transitionName={"Modal-anim"}
          transitionEnterTimeout={200}
          transitionLeaveTimeout={200}
        />
      )}
    </div>
  );
};

export default VideoModal;
