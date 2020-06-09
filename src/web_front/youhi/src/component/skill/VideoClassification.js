import React, { Component } from "react";
import "./VideoClassification.css";
import videoClassificationImg from "../../img/video_classification.png";

class VideoClassification extends Component {
  render() {
    return (
      <div className="Video-classification">
        <div className="Video-classification-container-wrapper">
          <div className="Video-classification-container">
            <div className="Video-classification-title-text-image-container">
              <div className="Video-classification-title">
                Video Classification
              </div>
              <div className="Video-classification-title-bar" />
              <p className="Video-classification-text">
                Image Classification이란 딥러닝을 통해 시각적 내용에 따라
                이미지를 분류하는 것을 말한다. 딥러닝 신경망의 한 종류인
                CNN(Convolutional Neural Network)을 이용하며 이미지를 입력으로
                받고 그에 대한 class 값과 입력
              </p>
              <div className="Video-classification-image">
                <img src={videoClassificationImg} alt="" />
              </div>
              <p className="Video-classification-text">
                이미지가 특정 class라는 것에 대한 확률 값을 출력한다. CNN은 크게
                input layer, output layer, hidden layers로 나눌 수 있고, hidden
                layers는 보통 convolution 연산을 입력 이미지에 적용 후 다음
                층으로 전달하는 Convolutional
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default VideoClassification;
