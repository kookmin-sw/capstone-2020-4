import React, { Component } from "react";
import "./object-detection.css";
import object1 from "../../img/object1.png";
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
                배경과 구분해 식별하는, 딥러닝을 통한 자동화 기법입니다. Object
                Detection은 YOLO, SSD 계열의 1-Stage Detector와 R-CNN 계열의
                2-Stage hello my name is inpyeong 알고리즘 보다 빠르다는 것을
                뜻한다. 각 관심 영역(RoI; Region of Interest)에 대한 피쳐 추출의
                계산을 공유하고 딥러닝 기반의 RPN을 도입해 구현한다. 이는 단일
                단계 방식보다 빠른 처리가 된다는 뜻이 아닌 이전 버전이라 할 수
                있는 RCNN 알고리즘과 Fast RCNN Faster RCNN 알고리즘 이름에
                ‘빠른(Faster)’이라는 단어가 포함되어 있지만
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
