import React, { useState, useRef, useEffect } from "react";
import ReactTransitionGroup from "react-addons-css-transition-group";
import Player from "./react_player/Player";
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
            <div className="content">
              <div className="VideoModal-parallel-video-tabs">
                <div className="VideoModal-tab">
                  {getLabelsCnt(result.cntArray)}
                  <div className="VideoModal-tab-subtitle">전체 결과</div>
                </div>
                <div className="VideoModal-tab">
                  {result.cntArray[0]}
                  <div className="VideoModal-tab-subtitle">Adult</div>
                </div>
                <div className="VideoModal-tab">
                  {result.cntArray[1]}
                  <div className="VideoModal-tab-subtitle">Blood</div>
                </div>
                <div className="VideoModal-tab">
                  {result.cntArray[2]}
                  <div className="VideoModal-tab-subtitle">Knife</div>
                </div>
                <div className="VideoModal-tab">
                  {result.cntArray[3]}
                  <div className="VideoModal-tab-subtitle">Smoke</div>
                </div>
              </div>
              <div className="VideoModal-video-wrapper">
                <Player result={result}/>
              </div>
            </div>
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

const getLabelsCnt = (array) => {
  var i = 0;
  var sum = 0;
  for (; i < array.length; i++) {
    sum += array[i];
  }
  return sum;
};