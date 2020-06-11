import React, { Component } from "react";
import "./stt.css";
import stt_img from "../../img/stt.png";

class STT extends Component {
  render() {
    return (
      <div className="STT">
        <div className="STT-container-wrapper">
          <div className="STT-container">
            <div className="STT-image">
              <img src={stt_img} alt="" />
            </div>
            <div className="STT-title-text-container">
              <div className="STT-title">STT</div>
              <div className="STT-title-bar" />
              <p className="STT-text">
                업로드된 영상의 음성에서 욕설을 검열하기 위해서는 음성에서
                문장을 텍스트로 추출할 수 있는 STT 기술이 필요했습니다. 따라서
                YouHi 검열 시스템은 유료 STT 서비스를 제공하는 Google Speech
                API를 사용하였습니다. 각 단어에 대한 발화 시간 정보도 얻을 수
                있기 때문에, 원본 음성 파일에서 등장하는 욕설에 마스킹을
                적용시키는데 사용할 수 있었습니다.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default STT;
