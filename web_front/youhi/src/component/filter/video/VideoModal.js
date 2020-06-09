import React, { useState, useRef, useEffect } from "react";
import ReactTransitionGroup from "react-addons-css-transition-group";
import Player from "./react_player/Player";
import "./VideoModal.css";

const dropDown = new Array(4);

const VideoModal = ({ isOpen, close, result, clientID }) => {
  const [ref, setRef] = useState(null);

  const allTabRef = useRef(null);
  const adultTabRef = useRef(null);
  const bloodTabRef = useRef(null);
  const knifeTabRef = useRef(null);
  const smokeTabRef = useRef(null);

  const setDropDown = (paramDropDown) => {
    dropDown[0] = paramDropDown[0];
    dropDown[1] = paramDropDown[1];
    dropDown[2] = paramDropDown[2];
    dropDown[3] = paramDropDown[3];
  }

  useEffect(() => {
    console.log(ref);
    console.log(dropDown);
    if (ref !== null) {
      allTabRef.current.addEventListener("click", (event) => {
        console.log(ref);
        console.log(dropDown);
        if (dropDown[0] && dropDown[1] && dropDown[2] && dropDown[3]) {
          console.log("if");
          console.log(dropDown);
          ref[0].click();
          ref[1].click();
          ref[2].click();
          ref[3].click();
        } else {
          console.log("else");
          console.log(dropDown);
          if (!dropDown[0]) ref[0].click();
          if (!dropDown[1]) ref[1].click();
          if (!dropDown[2]) ref[2].click();
          if (!dropDown[3]) ref[3].click();
        }
      });
      adultTabRef.current.addEventListener("click", () => {
        ref[0].click();
      });
      bloodTabRef.current.addEventListener("click", () => {
        ref[1].click();
      });
      knifeTabRef.current.addEventListener("click", () => {
        ref[2].click();
      });
      smokeTabRef.current.addEventListener("click", () => {
        ref[3].click();
      });
    }
  }, [ref]);

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
                <div className="VideoModal-tab" ref={allTabRef}>
                  {getLabelsCnt(result.cntArray)}
                  <div className="VideoModal-tab-subtitle">전체 결과</div>
                  <div className="VideoModal-selected-indicator" />
                </div>
                <div className="VideoModal-tab" ref={adultTabRef}>
                  {result.cntArray[0]}
                  <div className="VideoModal-tab-subtitle">Adult</div>
                  <div id="0" className="VideoModal-selected-indicator" />
                </div>
                <div className="VideoModal-tab" ref={bloodTabRef}>
                  {result.cntArray[1]}
                  <div className="VideoModal-tab-subtitle">Blood</div>
                  <div id="1" className="VideoModal-selected-indicator" />
                </div>
                <div className="VideoModal-tab" ref={knifeTabRef}>
                  {result.cntArray[2]}
                  <div className="VideoModal-tab-subtitle">Knife</div>
                  <div id="2" className="VideoModal-selected-indicator" />
                </div>
                <div className="VideoModal-tab" ref={smokeTabRef}>
                  {result.cntArray[3]}
                  <div className="VideoModal-tab-subtitle">Smoke</div>
                  <div id="3" className="VideoModal-selected-indicator" />
                </div>
              </div>
              <div className="VideoModal-video-wrapper">
                <Player
                  result={result}
                  func={(info) => setRef(info)}
                  func2={(info) => {
                    setDropDown(info);
                    console.log(info);
                  }}
                  clientID={clientID}
                />
              </div>
            </div>
            <div className="button-wrap">
              <button onClick={close}>확인</button>
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
