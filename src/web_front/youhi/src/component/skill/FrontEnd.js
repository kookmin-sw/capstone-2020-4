import React, { Component } from "react";
import "./FrontEnd.css";
import react from "../../img/react.png";

class FrontEnd extends Component {
  render() {
    return (
      <div className="Front-end">
        <div className="Front-end-container-wrapper">
          <div className="Front-end-container">
            <span className="Front-end-image">
              <img src={react} alt="" />
            </span>
            <div className="Front-end-title-text-container">
              <div className="Front-end-title">Front-End</div>
              <div className="Front-end-title-bar" />
              <p className="Front-end-text">
                React는 사용자 인터페이스를 만들기 위한 Facebook에서 제공해주는
                JavaScript 라이브러리로, 어플리케이션의 UI를 정의하는 Component
                기반입니다. 이러한 Component들을 조합하여 손쉽게 어플리케이션
                UI를 만들 수 있고 다양한 형식의 데이터를 어플리케이션 안에서
                쉽게 전달 가능합니다. YouHi 검열 시스템은 이러한 장점을 가진
                React를 통해 데모 서비스를 이용할 수 있는 웹을 제공합니다.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default FrontEnd;
