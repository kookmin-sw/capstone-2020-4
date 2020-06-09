import React, { Component } from "react";
import "./BackEnd.css";
import aws from "../../img/aws.png";

class BackEnd extends Component {
  render() {
    return (
      <div className="Back-end">
        <div className="Back-end-container-wrapper">
          <div className="Back-end-container">
            <div className="Back-end-image">
              <img src={aws} alt="" />
            </div>
            <div className="Back-end-title-text-container">
              <div className="Back-end-title">Instance Segmentation</div>
              <div className="Back-end-title-bar" />
              <p className="Back-end-text">
                딥러닝 모델 학습과 모델의 영상, 음성 검열 과정에 필요한 Amazon
                EC2 instance, Amazon S3, Amazon Lambda, Amazon Gateway API를
                생성한다. 웹 페이지의 배포를 위해 웹서버를 구축한다. 웹서버,
                웹페이지, AWS의 원활한 상호작용을 위해 Socket 통신을 활용한다.
                동영상이 업로드 되는 공간, 업로드 된 동영상의 프레임 추출,
                딥러닝 모델에 넣는 작업을 위한 Amzon S3, Amazon Lambda, Amazon
                Gateway API를 이용한다. 단순 S3에 업로드하는 방식을 채택할 경우,
                IAM 사용자의 Access Key 및 Secret Key
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default BackEnd;
