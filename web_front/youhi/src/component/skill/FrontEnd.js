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
              <div className="Front-end-title">
                Front End
              </div>
              <div className="Front-end-title-bar" />
              <p className="Front-end-text">
                React는 페이스북에서 개발한 유저인터페이스 라이브러리로 개발에게
                재사용 가능한 UI를 생성 할 수 있도록 해준다. 이 라이브러리는
                현재 페이스북, 인스타그램, 야후, 넷플릭스를 포함한 많은
                서비스에서 사용되고 있다. Web Page 특성상 기능별 컴포넌트들이
                필요하고, 컴포넌트끼리의 연결도 용이해야한다. React Js는
                컴포넌트 별 관리가 편하고, 디버깅 및 코드 수정이 비교적 간단하기
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default FrontEnd;
