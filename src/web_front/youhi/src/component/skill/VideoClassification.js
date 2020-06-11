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
                Video Classification이란 딥러닝을 이용한 영상 태깅을 의미합니다.
                Spatial Stream ConvNet과 Temporal Stream ConvNet으로 각각 예측된
                결과를 Average, Conv Fusion을 통해 결합한 후 최종 태깅을
                진행합니다.
              </p>
              <div className="Video-classification-image">
                <img src={videoClassificationImg} alt="" />
              </div>
              <p className="Video-classification-text">
                YouHi 검열 시스템에서는 Instance Segmentation 단계에서 칼과
                담배가 발견된 프레임이 포함된 영상들에 한해서 Video
                Classification을 적용하며, 사람이 칼에 찔리는 장면, 흡연하는
                장면이 등장하면 각 장면에 해당하는 라벨을 태깅합니다.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default VideoClassification;
