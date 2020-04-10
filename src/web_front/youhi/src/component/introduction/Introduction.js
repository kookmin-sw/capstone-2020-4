import React from "react";
import "./Introduction.css";

const Introduction = () => {
  return (
    <div className="Introduction">
      <div className="Introduction-first-flex-items-container">
        <div className="Introduction-first-flex-items">
          <div className="Introduction-text-title">YouHi</div>
          <div className="Introduction-text-description">
            Video upload filtering application <br />
            designed to provide safe video for minors.
          </div>
        </div>
      </div>
      <div className="Introduction-second-flex-items-container">
        <div className="Introduction-second-flex-items">
          <div className="Introduction-text-header">
            <div className="Introduction-text-title">YouHi is</div>
            <div className="Introduction-text-bar" />
          </div>
          <div className="Introduction-text-description">
            YouHi는 영상분류 신경망 모델을 이용한 정확한 필터링을 제공함으로써
            <br /> 업로더의 동영상에서 청소년에게 부적합한 내용을 모두
            걸러냅니다.
            <br />
            필터링의 기준은 YouTube 가이드라인의 연령 제한 콘텐츠에 명시되어
            있는
            <br />
            연령 제한 적용 고려 사항이며 자세한 내용은{" "}
            <a
              className="Introduction-link"
              href="https://support.google.com/youtube/answer/2802167?hl=ko"
              rel="noopener noreferrer "
              target="_blank"
            >
              여기
            </a>
            를 참고하세요.
          </div>
        </div>
      </div>
    </div>
  );
};

export default Introduction;
