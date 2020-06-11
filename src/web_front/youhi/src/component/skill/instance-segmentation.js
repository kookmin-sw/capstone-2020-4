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
                Instance Segmentation(객체 분할)이란 Box 형태 안에 존재하는 실제
                고유의 클래스들이 가지는 모양 그대로 객체의 영역만을 탐지하는
                기술입니다. YouHi 검열 시스템에서는 오탐률을 낮추기 위해
                Instance Segmentation을 도입하였으며, 프레임에서 검열 라벨에
                관한 객체를 발견한 영상에 한해서만 Video Classification 단계로
                넘어가도록 하였습니다.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Instance_segmentation;
