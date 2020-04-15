import React, { Component } from 'react';
import "./Upload.css";
import UploadElementor from "./upload_elementor/UploadElementor"

class Upload extends Component {
  render() {
    return (
      <div className="Upload">
        <UploadElementor />
      </div>
    );
  }
}

export default Upload;