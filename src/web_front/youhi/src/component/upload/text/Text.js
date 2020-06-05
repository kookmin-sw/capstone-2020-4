import React from "react";

import "./Text.css";

const Text = () => {
  return (
    <div className="Text-wrapper">
      <div className="Text-title">도움말 및 제안사항</div>
      <div className="Text-box">
        <ul>
          <li>
            필터링에 소요되는 시간은 약 10분이며, 사용자의 인터넷 환경에 따라
            달라질 수 있습니다.
          </li>
          <li>재생 시간이 1분 미만인 영상만 업로드 가능합니다.</li>
          <li>업로드 파일 형식은 mp4로 제한합니다.</li>
          <li>
            검열이 진행되는 동안 브라우저를 종료하거나 새로고침을 하면 모든 작업은 중지됩니다. 검열이 완료될 때까지 기다려주세요.
          </li>
        </ul>
      </div>
    </div>
  );
};

export default Text;
