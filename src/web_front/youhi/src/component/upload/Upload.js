import React, { Component } from 'react';
import UploadElementor from "./upload_elementor/UploadElementor";
import Dropzone from "./dropzone/Dropzone";
import Text from "./text/Text";
import "./Upload.css";

class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      uploaing: false,
      successfullUploaded: false,
    }
    this.onFilesAdded = this.onFilesAdded.bind(this);
  }

  onFilesAdded(files) {
    this.setState((prevState) => ({
      files: prevState.files.concat(files),
    }));
  }
  
  render() {
    return (
      <div className="Upload">
        <UploadElementor />
        <div className="Upload-outer-flex-items">
          <Dropzone 
            onFilesAdded={this.onFilesAdded}
            disabled={this.state.uploading || this.state.successfullUploaded}
          />  
          <div className="Upload-inner-flex-items">
            <Text />
          </div>
        </div>
      </div>
    );
  }
}

export default Upload;