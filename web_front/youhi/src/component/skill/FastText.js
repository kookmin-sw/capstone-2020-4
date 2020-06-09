import React, { Component } from "react";
import "./FastText.css";
import fastTextImg from "../../img/fasttext.png"

class FastText extends Component {
  render() {
    return (
      <div className="FastText">
        <div className="FastText-container-wrapper">
          <div className="FastText-container">
            <div className="FastText-title-text-container">
              <div className="FastText-title">
                FastText
              </div>
              <div className="FastText-title-bar" />
              <p className="FastText-text">
                Image Classification이란 딥러닝을 통해 시각적 내용에 따라
                이미지를 분류하는 것을 말한다. 딥러닝 신경망의 한 종류인
                CNN(Convolutional Neural Network)을 이용하며 이미지를 입력으로
                받고 그에 대한 class 값과 입력 이미지가 특정 class라는 것에 대한
                확률 값을 출력한다. CNN은 크게 input layer, output layer,
              </p>
            </div>
            <div className="FastText-image">
              <img src={fastTextImg} alt="" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default FastText;
