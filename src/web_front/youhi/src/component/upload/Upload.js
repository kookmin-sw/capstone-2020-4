import React, { Component } from 'react';
import UploadElementor from "./upload_elementor/UploadElementor";
import Dropzone from "./dropzone/Dropzone";
import Text from "./text/Text";
import "./Upload.css";

class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
      uploaing: false,
      successfullUploaded: false,
    }
    this.onFilesAdded = this.onFilesAdded.bind(this);
    this.renderActions = this.renderActions.bind(this);
  }

  onFilesAdded(files) {
    this.setState((prevState) => ({
      files: prevState.files.concat(files),
    }));
  }

  renderActions() {
    return (
      <div className="Actions">
        <button className="Upload-button Upload-upload-button">업로드</button>
        <button className="Upload-button Upload-filter-button">필터</button>
      </div>
    );
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
            <div>
              {this.state.files.map((file) => {
                return (
                  <div key={file.name}>
                    <span>{file.name}</span>
                  </div>
                );
              })}
            </div>
            {this.renderActions()}
          </div>
        </div>
      </div>
    );
  }
}

export default Upload;