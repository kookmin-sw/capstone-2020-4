import React, { Component } from "react";
import "./object-detection.css";
import rcnn from "../../img/rcnn.png";

class Object_detection extends Component {
  render() {
    return (
      <div className="Object-detection">
        <div className="Object-detection-first-container-wrapper">
          <div className="Object-detection-first-container">
            <div className="Object-detection-title-text-container">
              <div className="Object-detection-title"> Object Detection </div>
              <div className="Object-detection-title-bar" />
              <p className="Object-detection-text">
                Object Detection(객체 탐지)는 이미지에서 찾고 싶은 관심 객체를
                배경과 구분해 식별한 후 Bounding box 처리를 통해 관심 객체의
                위치를 나타내는, 딥러닝을 통한 자동화 기법입니다. YouHi 검열
                시스템에서는 우측 이미지에 나와있는 Faster RCNN 모델을 이용하여
                Object Detection을 구현하였으며, Instance Segmentation 단계에서
                총이 발견된 프레임에 한해서만 Object Detection을 적용하여 게임의
                존재하는 캐릭터 객체를 탐지하도록 했습니다.
              </p>
            </div>
            <div className="Object-detection-image">
              <img src={rcnn} alt="" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Object_detection;
