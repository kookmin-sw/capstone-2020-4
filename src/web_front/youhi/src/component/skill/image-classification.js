import React, { Component } from "react";
import "./image-classification.css";
import cnn from "../../img/cnn.PNG"

class Image_classfication extends Component {
  render() {
    return (
      <div className="Image-classification">
        <div className="Image-classification-container-wrapper">
          <div className="Image-classification-container">
            <div className="Image-classification-title-text-container">
              <div className="Image-classification-title">
                Instance Segmentation
              </div>
              <div className="Image-classification-title-bar" />
              <p className="Image-classification-text">
                Image Classification이란 딥러닝을 통해 시각적 내용에 따라
                이미지를 분류하는 것을 말한다. 딥러닝 신경망의 한 종류인
                CNN(Convolutional Neural Network)을 이용하며 이미지를 입력으로
                받고 그에 대한 class 값과 입력 이미지가 특정 class라는 것에 대한
                확률 값을 출력한다. CNN은 크게 input layer, output layer, hidden
                layers로 나눌 수 있고, hidden layers는 보통 convolution 연산을
                입력 이미지에 적용 후 다음 층으로 전달하는 Convolutional
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
