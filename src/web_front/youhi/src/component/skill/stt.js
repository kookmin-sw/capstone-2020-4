import React, { Component } from "react";
import "./stt.css";
import stt_img from "../../img/stt.PNG";

class STT extends Component {
  render() {
    return (
      <div className="STT">
        <div className="STT-container-wrapper">
          <div className="STT-container">
            <div className="STT-title-text-container">
              <div className="STT-title">STT</div>
              <div className="STT-title-bar" />
              <p className="STT-text">
                딥러닝 기반의 음성인식 기술은 크게 언어모델과 음향모델이라는 두
                가지 중요한 지식원(Knowledge source)을 사용해 음성 신호로부터
                문자 정보를 출력한다. 언어모델은 단어 시퀀스에 확률을
                할당(assign) 하는 일을 하는 모델이다. 이는 가장 자연스러운 단어
                시퀀스를 찾는 역할을 한다. 음향모델은 언어의 소리단위를 딥러닝을
                통해 학습하여 어떤 단어가 어떤 소리로 나는지를 확률적으로
                변환한다.
              </p>  
              <div className="STT-image">
                <img src={stt_img} alt="" />
              </div>
              <p className="STT-text">
                이 두가지 모델이 동시에 작용하여 높은 확률을 보인 단어를
                출력한다. STT(Speech To Text) 는 잡음처리와 특징 추출과정을 거친
                음성 데이터가 언어모델과 음향모델이 결합된 디코더를 통과한 후
                문장 형태로 출력되면 이를 텍스트로 저장한다.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default STT;
