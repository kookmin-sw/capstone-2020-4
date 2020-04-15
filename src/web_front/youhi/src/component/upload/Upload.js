import React, { Component } from 'react';
import UploadElementor from "./upload_elementor/UploadElementor"
import "./Upload.css";

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