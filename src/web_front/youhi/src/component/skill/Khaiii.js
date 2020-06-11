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
                형태소 분석이 이루어진 텍스트 데이터는 그렇지 않은 데이터보다
                비속어 여부를 판단하기에 유리합니다. 따라서 YouHi 검열 시스템은
                카카오에서 개발한 세 번째 형태소 분석기인 Khaiii를 이용하여
                STT를 통해 음성으로부터 얻은 텍스트 데이터를 형태소 단위로
                분리하였습니다. Khaiii는 기계학습 기반의 알고리즘을 이용하여
                형태소를 분석하는데, 형태소 오분석에 대비하여 신경망 알고리즘에
                사용자 사전 장치를 제공합니다. 따라서 특정 욕설을 형태소로
                분리하지 못하더라도 이를 통해 극복이 가능하다는 장점이 있습니다.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Khaiii;
