import React, { Component } from "react";
import "./Khaiii.css";

class Khaiii extends Component {
  render() {
    return (
      <div className="Khaiii">
        <div className="Khaiii-container-wrapper">
          <div className="Khaiii-container">
            <div className="Khaiii-title-text-container">
              <div className="Khaiii-title">Khaiii</div>
              <div className="Khaiii-title-bar" />
              <p className="Khaiii-text">
                형태소 분석기는 텍스트 형태의 데이터를 형태소 단위로 분리한다.
                형태소 단위로 분리된 데이터는 비속어 여부를 판단하기에 유리하다.
                카카오에서 개발한 세 번째 형태소 분석기인 khaiii는 형태소 분석
                시 입력된 각 음절에 대해 하나의 출력 태그를 결정하는 분류 문제로
                접근하게 된다. 일정 텍스트의 형태소 분석 결과는 다음 이미지와
                같이 생성된다.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Khaiii;
