import React, { Component } from 'react';
import UploadElementor from "./upload_elementor/UploadElementor"
import Dropzone from "./dropzone/Dropzone"
import "./Upload.css";

class Upload extends Component {

  render() {
    return (
      <div className="Upload">
        <UploadElementor />
        <div className="Upload-content">
          <Dropzone />  
        </div>
      </div>
    );
  }
}

export default Upload;