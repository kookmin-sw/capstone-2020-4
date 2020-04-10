import React from "react";
import "./Introduction.css";

const Introduction = () => {
  return (
    <div className="Introduction">
      <div className="Introduction-first-flex-items-container">
        <div className="Introduction-first-flex-items">
          <div className="Introduction-text-header">YouHi</div>
          <div className="Introduction-text-description">
            Video upload filtering application <br />
            designed to provide safe video for minors.
          </div>
        </div>
      </div>
    </div>
  );
};

export default Introduction;
