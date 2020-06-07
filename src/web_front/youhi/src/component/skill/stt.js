import React, { Component } from "react";
import "./stt.css";
import stt_img from "../../img/stt.png";
import analysis from "../../img/analysis.png";

class STT extends Component {
  render() {
    return (
      <div className="ob-con">
        <div className="object-detection">
          <div className="object-title"> Speech To Text </div>
        </div>
        <div className="object1">
          <div className="image-text">
            딥러닝 기반의 음성인식 기술은 크게 언어모델과 음향모델이라는 두 가지
            중요한 지식원(Knowledge source)을 사용해 음성 신호로부터 문자 정보를
            출력한다. 언어모델은 단어 시퀀스에 확률을 할당(assign) 하는 일을
            하는 모델이다. 이는 가장 자연스러운 단어 시퀀스를 찾는 역할을 한다.
            음향모델은 언어의 소리단위를 딥러닝을 통해 학습하여 어떤 단어가 어떤
            소리로 나는지를 확률적으로 변환한다. 이 두가지 모델이 동시에
            작용하여 높은 확률을 보인 단어를 출력한다.
          </div>
        </div>
        <div className="stt-con">
          <img src={stt_img} alt="" className="img-stt" />
        </div>
        <div className="text-con">
          <div className="stt-text">
            STT(Speech To Text) 는 잡음처리와 특징 추출과정을 거친 음성 데이터가
            언어모델과 음향모델이 결합된 디코더를 통과한 후 문장 형태로 출력되면
            이를 텍스트로 저장한다.
          </div>
        </div>
        <div className="object-detection">
          <div className="object-title"> morphological analysis </div>
        </div>
        <div className="object1">
          <div className="image-text">
            형태소 분석기는 텍스트 형태의 데이터를 형태소 단위로 분리한다.
            형태소 단위로 분리된 데이터는 비속어 여부를 판단하기에 유리하다.{" "}
            <br />
            <br />
            카카오에서 개발한 세 번째 형태소 분석기인 khaiii는 형태소 분석 시
            입력된 각 음절에 대해 하나의 출력 태그를 결정하는 분류 문제로
            접근하게 된다. 일정 텍스트의 형태소 분석 결과는 다음 이미지와 같이
            생성된다.
          </div>
        </div>
        <div className="stt-con">
          <img src={analysis} alt="" className="analysis-img" />
        </div>
        <div className="text-con">
          <div className="stt-text">
            khaiii는 기계학습 기반의 알고리즘을 이용하여 형태소를 분석한다.
            형태소 분석은 자연어 처리를 위한 가장 기본적인 전처리 과정이기
            때문에 빠른 시간 내에 이루어져야 하므로 신경망 알고리즘들 중 빠른
            속도로 진행되는 Convolutional Neural Network(CNN)을 사용하였다. <br/><br/>
            khaiii는 신경망 알고리즘의 앞단에 기분석 사전을, 뒷단에 오분석
            패치라는 두 가지 사용자 사전 장치를 제공한다. 기분석 사전은 단일
            어절에 대해 문맥에 상관없이 일괄적인 분석 결과를 갖게 하고 싶을 경우
            사용하고 오분석 패치는 여러 어절에 걸쳐 충분한 문맥과 함께 오분석을
            바로잡아야 할 경우에 활용한다. 이러한 두 기능으로 형태소 오분석
            확률을 줄일 수 있고 본 프로젝트에 맞게 형태소 분석을 진행할 수 있다.
          </div>
        </div>
      </div>
    );
  }
}

export default STT;
