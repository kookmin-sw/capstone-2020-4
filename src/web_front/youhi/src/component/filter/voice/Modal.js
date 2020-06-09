import React, { useRef } from "react";
import "./Modal.css";
import ReactTransitionGroup from "react-addons-css-transition-group";
import { Scrollbars } from "react-custom-scrollbars";

const Modal = ({ isOpen, close, imgArray, swearArray, clientID }) => {

  return (
    <div>
      {isOpen ? (
        <ReactTransitionGroup
          transitionName={"Modal-anim"}
          transitionEnterTimeout={200}
          transitionLeaveTimeout={200}
        >
          <div className="Modal-overlay" onClick={close} />
          <div className="Modal">
            <p className="title">음성, 자막 검열 결과</p>
            <div className="content">
              <Scrollbars
                className="Modal-left-scrollbars"
                style={{ width: "45%", height: "93.7%" }}
                renderTrackHorizontal={(props) => (
                  <div
                    {...props}
                    style={{ display: "none" }}
                    className="track-horizontal"
                  />
                )}
              >
                {printImgArrayData(imgArray, clientID)}
              </Scrollbars>
              <div className="Modal-vertical-line" />
              <div className="Modal-right">
                <Scrollbars
                  className="Modal-right-scrollbars"
                  style={{ width: "100%", height: "80%" }}
                  renderTrackHorizontal={(props) => (
                    <div
                      {...props}
                      style={{ display: "none" }}
                      className="track-horizontal"
                    />
                  )}
                >
                  {printSwearArrayData(swearArray)}
                </Scrollbars>
                <div className="Modal-buttons">
                  <audio controls src={`./static/${clientID}/${clientID}_mute.wav`}>
                    Your browser does not support the
                    <code>audio</code> element.
                  </audio>
                  <ul className="Modal-buttons-description">
                    <li>검열된 음성은 플레이어를 이용하여 들을 수 있습니다.</li>
                    <li>음량 우측버튼을 누르면 wav 형식의 음성파일이 다운로드됩니다.</li>
                  </ul>
                </div>
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
export default Modal;

const printImgArrayData = (imgArray, clientID) => {
  console.log(clientID);
  const data = imgArray;
  if (data.length !== 0) {
    return data.map((element, index) => {
      const id = `img_${index}`;
      const src = `./static/${clientID}/subtitle_img/${element}`;
      if (element) {
        return (
          <div id={id} className="Modal-scrollbars-left-element">
            <img src={src} alt="" />
          </div>
        );
      } else {
        return null;
      }
    });
  } else {
    return (
      <div className="Modal-empty-labels">
        자막에서 욕설이 검열되지 않음
      </div>
    );
  }
};

const printSwearArrayData = (swearArray) => {
  const data = swearArray;
  console.log(data);
  if (data[0] === "There's no result!" || data.length === 0) {
    return (
      <div className="Modal-empty-labels">
        음성에서 욕설이 검열되지 않음
      </div>
    );
  } else {
    return data.map((element, index) => {
      const id = `swear_${index}`;
      if (element) {
        return (
          <div id={id} className="Modal-scrollbars-right-element">
            <span className="Modal-swear-text">'{element[0]}'</span>
            <span className="Modal-swear-time">{element[1]}</span>
          </div>
        );
      } else {
        return null;
      }
    });
  }
};
