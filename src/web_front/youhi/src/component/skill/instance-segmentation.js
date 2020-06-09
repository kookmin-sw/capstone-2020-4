import React, { Component } from "react";
import "./instance-segmentation.css";
import seg from "../../img/seg.png";

class Instance_segmentation extends Component {
  render() {
    return (
      <div className="Instance-segmentation">
        <div className="Instance-segmentation-container-wrapper">
          <div className="Instance-segmentation-container">
            <div className="Instance-segmentation-image">
              <img src={seg} alt="" />
            </div>
            <div className="Instance-segmentation-title-text-container">
              <div className="Instance-segmentation-title">
                Instance Segmentation
              </div>
              <div className="Instance-segmentation-title-bar" />
              <p className="Instance-segmentation-text">
                Instance segmentation(객체 분할)이란 경계 상자(Bounding Box)로
                각 클래스들을 탐지하는 Object Detection(객체 탐지)보다 더
                발전하여, Box 형태 안에 존재하는 실제 고유의 클래스들이 가지는
                모양 그대로 객체의 영역만을 탐지하는 기술이다. Instance
                segmentation은 주어진 이미지 내 각 위치 상의 픽셀들을 하나씩
                조사하며, 현재 조사 대상인 픽셀이 어느 특정한 라벨에 해당하는
                사물의 일부인 경우 해당 픽셀의 위치에 그 클래스를 나타내는
                ‘값’을 표기하는 방식으로 예측 결과물을 생성한다. 반대로 조사
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Instance_segmentation;
