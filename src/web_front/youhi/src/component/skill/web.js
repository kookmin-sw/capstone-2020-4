import React, { Component } from "react";
import "./web.css";
import react from "../../img/react.png";

class Image_segmentation extends Component {
  render() {
    return (
      <div className="ob-con">
        <div className="object-detection">
          <div className="object-title"> Front End</div>
        </div>
        <div className="object1">
          <div className="object-text">
            React는 페이스북에서 개발한 유저인터페이스 라이브러리로 개발에게
            재사용 가능한 UI를 생성 할 수 있도록 해준다. 이 라이브러리는 현재
            페이스북, 인스타그램, 야후, 넷플릭스를 포함한 많은 서비스에서
            사용되고 있다. Web Page 특성상 기능별 컴포넌트들이 필요하고,
            컴포넌트끼리의 연결도 용이해야한다. React Js는 컴포넌트 별 관리가
            편하고, 디버깅 및 코드 수정이 비교적 간단하기 때문에 React Js로
            구현을 진행한다.
            <br />
            <br />
            React Js의 Rendering은 기존 HTML 문법과 상당히 유사하기 때문에, 많은
            개발자에게 익숙하여 협업을 진행하기에 적합하다. 웹 구현에 있어 가장
            중요한 것은 기능과 디자인이다. react는 다양한 라이브러리를
            제공하는데 개발자는 이 라이브러리들을 쉽게 다운받아 쓸 수 있고 자체
            커스텀하기도 편리하기 때문에 react js로 구현을 진행한다.
          </div>
          <div className="object-space"></div>
          <div>
            <img src={react} alt="" className="object1-img" />
          </div>
        </div>
        <div className="object-detection">
          <div className="object-title"> Back End</div>
        </div>
        <div className="object1">
          <div className="image-text">
            딥러닝 모델 학습과 모델의 영상, 음성 검열 과정에 필요한 Amazon EC2
            instance, Amazon S3, Amazon Lambda, Amazon Gateway API를 생성한다.
            웹 페이지의 배포를 위해 웹서버를 구축한다. 웹서버, 웹페이지, AWS의
            원활한 상호작용을 위해 Socket 통신을 활용한다. 동영상이 업로드 되는
            공간, 업로드 된 동영상의 프레임 추출, 딥러닝 모델에 넣는 작업을 위한
            Amzon S3, Amazon Lambda, Amazon Gateway API를 이용한다. 단순 S3에
            업로드하는 방식을 채택할 경우, IAM 사용자의 Access Key 및 Secret
            Key가 노출될 가능성이 높으므로 Gateway Api와 Lambda를 통해 업로드를
            진행한다. S3에 업로드가 완료되면 Lambda함수에서는 프레임을 추출하고,
            전처리를 진행하는 코드를 실행한다. AWS EC2 instance는 AWS Deep
            Learning AMI를 채택하여 딥러닝 모델의 학습을 진행한다. 모델 학습에
            있어 필요한 데이터셋은 Amazon S3에 저장한다. Apache 서버를 통해
            웹페이지를 배포한다. 웹페이지 이용자와 AWS를 통해 얻어진 데이터의
            주체가 동일인물인지 파악하고 Back End에서 일처리(검열 작업)의 종료를
            웹페이지에 알려주기 위해 Socket 서버를 구축하여 통신한다. Socket은
            SocketIo 라이브러리를 활용한다.
          </div>
        </div>
        <div className = "web-margin"></div>
      </div>
    );
  }
}

export default Image_segmentation;
