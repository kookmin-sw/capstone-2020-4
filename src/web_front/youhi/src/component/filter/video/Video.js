import React , { Component , useState } from "react";
import './Video.css';

const Video = props => {
  return (
    <div className="Video">
      <button 
        className="Filter-box Filter-video-filter"
        disabled={!props.successfulFiltered}
      />
    </div>
  );
};

export default Video;
