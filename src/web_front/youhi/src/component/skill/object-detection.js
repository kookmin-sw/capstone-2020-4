import React, { Component } from "react";
import "./object-detection.css";
import object1 from "../../img/object1.png";
import rcnn from "../../img/rcnn.png";

class Object_detection extends Component {
  render() {
    return (
      <div className="ob-con">
        <div className="object-detection">
          <div className="object-title"> Object Detection </div>
          <div className = "object-bar"></div>
        </div>
        <div className="object1">
          <div className="object-text">
            객체 탐지는 이미지에서 찾고 싶은 관심 객체를 배경과 구분해 식별하는
            자동화 기법이다. 이 기술은 아래의 사진처럼 이미지에서 새와 사람 등의
            객체를 자동으로 탐지해낸다. 이러한 객체 탐지는 딥러닝을 통해
            이루어진다. <br />
            <br />
            객체 탐지 기술은 2개 이상, 즉 N개의 객체를 탐지해 분류할 수 있어야
            한다. 많은 객체를 탐지하는 데 한계가 있으므로 다수의 사각형 상자
            위치와 크기를 가정해 컨볼루션 신경망을 변형한 후 이를 객체
            분류(Object Classification)에 활용한다. 이러한 사각형 상자를
            ‘윈도우(Window)’라고 부른다. 각 창의 크기와 위치는 객체의 존재
            여부에 따라 결정될 수 있고 객체가 있는 경우에는 그 범주도 결정할 수
            있다. 본 프로젝트에서는 다음과 같은 알고리즘을 사용한다.
          </div>
          <div className="object-space"></div>
          <div>
            <img src={object1} alt="" className="object1-img" />
          </div>
        </div>
        <div className="rcnn">
          <div className="object1-img">
            <img src={rcnn} alt="" className="rcnn-img" />
          </div>
          <div className="object-space"></div>
          <div className="object-text">
            <div className="font-in">2단계 방식의 객체 탐지 알고리즘,</div>{" "}
            Faster RCNN 알고리즘 이름에 ‘빠른(Faster)’이라는 단어가 포함되어
            있지만 이는 단일 단계 방식보다 빠른 처리가 된다는 뜻이 아닌 이전
            버전이라 할 수 있는 RCNN 알고리즘과 Fast RCNN 알고리즘 보다 빠르다는
            것을 뜻한다. 각 관심 영역(RoI; Region of Interest)에 대한 피쳐
            추출의 계산을 공유하고 딥러닝 기반의 RPN을 도입해 구현한다.
          </div>
        </div>
      </div>
    );
  }
}

export default Object_detection;
