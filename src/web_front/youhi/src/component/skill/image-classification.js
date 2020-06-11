import React, { Component } from "react";
import "./image-classification.css";
import cnn from "../../img/cnn.PNG";

class Image_classfication extends Component {
  render() {
    return (
      <div className="Image-classification">
        <div className="Image-classification-container-wrapper">
          <div className="Image-classification-container">
            <div className="Image-classification-title-text-container">
              <div className="Image-classification-title">
                Image Classification
              </div>
              <div className="Image-classification-title-bar" />
              <p className="Image-classification-text">
                Image Classification이란 합성곱 신경망(Convolutional Neural
                Network; CNN)을 이용하여 시각적 내용에 따라 이미지를 분류하는
                것을 말합니다. YouHi 검열 시스템에서는 Instance Segmentati on
                단계에서 여성의 가슴 그리고 게임의 총이 탐지된 프레임에 한하여
                Image Classification을 진행하여, 여성의 가슴 노출 그리고 피가
                튀기는 게임 캐릭터를 검열하도록 했습니다.
              </p>
            </div>
            <div className="Image-classification-image">
              <img src={cnn} alt="" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Image_classfication;
