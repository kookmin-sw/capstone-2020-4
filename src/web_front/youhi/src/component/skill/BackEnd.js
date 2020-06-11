import React, { Component } from "react";
import "./BackEnd.css";
import aws from "../../img/aws.png";

class BackEnd extends Component {
  render() {
    return (
      <div className="Back-end">
        <div className="Back-end-container-wrapper">
          <div className="Back-end-container">
            <div className="Back-end-title-text-container">
              <div className="Back-end-title">Back-End</div>
              <div className="Back-end-title-bar" />
              <p className="Back-end-text">
                딥러닝 모델 학습, 그리고 검열 서비스를 제공하는데 있어서 높은
                성능의 Back-End가 요구됐습니다. 따라서 YouHi 검열 시스템은
                강력한 기능을 제공하는 Amazon Web Services를 통해 Back-End를
                구축했습니다. Amazon Lambda, Gateway API를 통해 웹에서 Amazon S3
                영상 업로드 기능을 구현했으며, Amazon EC2 instan ce를 통해
                딥러닝 모델 학습, 검열 등을 진행할 수 있었습니다.
              </p>
            </div>
            <div className="Back-end-image">
              <img src={aws} alt="" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default BackEnd;
