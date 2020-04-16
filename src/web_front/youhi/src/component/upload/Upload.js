import React, { Component } from 'react';
import UploadElementor from "./upload_elementor/UploadElementor";
import Dropzone from "./dropzone/Dropzone";
import Text from "./text/Text";
import "./Upload.css";

class Upload extends Component {

  render() {
    return (
      <div className="Upload">
        <UploadElementor />
        <div className="Upload-outer-flex-items">
          <Dropzone />  
          <div className="Upload-inner-flex-items">
            <Text />
          </div>
        </div>
      </div>
    );
  }
}

export default Upload;