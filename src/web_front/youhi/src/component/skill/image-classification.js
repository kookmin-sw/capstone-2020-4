import React, { Component } from "react";
import "./image-classification.css";

class Image_classfication extends Component {
  render() {
    return (
      <div className="ob-con">
        <div className="object-detection">
          <div className="object-title"> Image-classification </div>
        </div>
        <div className="object1">
          <div className="image-text">
            Image Classification이란 딥러닝을 통해 시각적 내용에 따라 이미지를
            분류하는 것을 말한다. 딥러닝 신경망의 한 종류인 CNN(Convolutional
            Neural Network)을 이용하며 이미지를 입력으로 받고 그에 대한 class
            값과 입력 이미지가 특정 class라는 것에 대한 확률 값을 출력한다.
            CNN은 크게 input layer, output layer, hidden layers로 나눌 수 있고,
            hidden layers는 보통 convolution 연산을 입력 이미지에 적용 후 다음
            층으로 전달하는 Convolutional layers, CNN의 출력을 결정하는 ReLU
            layers, 뉴런 군집의 출력을 단일 뉴런으로 결합하여 데이터의 차수를
            감소시키는 Pooling layers, 이전 층의 모든 노드를 다음 층의 모든
            노드에 연결하는 Fully connected layer으로 구성된다. 
            <br/> <br/>
            이번
            프로젝트에서 원래 Object Detection만을 이용하여 게임 장면에서
            등장하는 혈흔과 여성의 과도한 노출을 검열하려 하였으나, 빨간 옷을
            입고 있는 게임 캐릭터 그리고 살색과 비슷한 옷을 입은 여성도 검열되는
            문제를 확인하였다. 이러한 문제를 해결하기 위해서는 각 class마다
            특징점을 찾아 이미지를 분류하는 Image Classification이 적합하다고
            판단했고, 따라서 Object Detection 검열 이후 해당 프레임에 대한 Image
            Classification 검열 과정을 추가하여 혈흔과 빨간 색의 옷, 나체와
            살색의 옷의 구분이 가능하도록 했다.
          </div>
          <div></div>
        </div>
      </div>
    );
  }
}

export default Image_classfication;
