import React, { Component } from "react";
import "./FastText.css";
import fastTextImg from "../../img/fasttext.png";

class FastText extends Component {
  render() {
    return (
      <div className="FastText">
        <div className="FastText-container-wrapper">
          <div className="FastText-container">
            <div className="FastText-title-text-container">
              <div className="FastText-title">FastText</div>
              <div className="FastText-title-bar" />
              <p className="FastText-text">
                형태소 분석을 통해 얻은 욕설을 욕설로 판단하기 위해 YouHi 검열
                시스템은 단어 임베딩 기법 중 하나인 FastText를 이용합니다. FastText는 텍스트의 최소 단위를 어휘를 구성하는 글자 n-grams로 설정했기 때문에, 모든 n-gram 벡터의 평균 벡터를 어휘 임베딩으로 보게 됩니다. 따라서 동일한 텍스트 데이터에서도 다른 임베딩 기법보다 더 많은 정보를 활용할 수 있었고, 그만큼 욕설 검열에서 높은 성능을 보였습니다.
              </p>
            </div>
            <div className="FastText-image">
              <img src={fastTextImg} alt="" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default FastText;
