import React, { Component } from "react";
import UploadElementor from "./upload_elementor/UploadElementor";
import Dropzone from "./dropzone/Dropzone";
import Progress from "./progress/Progress";
import Text from "./text/Text";
import "./Upload.css";

var signedURL;
const io = require("socket.io-client");
const ioClient = io.connect("http://13.125.127.181:4567");

class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
      uploaing: false,
      uploadProgress: {},
      successfullUploaded: false,
    };
    this.onFilesAdded = this.onFilesAdded.bind(this);
    this.uploadFiles = this.uploadFiles.bind(this);
    this.sendRequest = this.sendRequest.bind(this);
    this.renderActions = this.renderActions.bind(this);
  }

  onFilesAdded(files) {
    this.setState((prevState) => ({
      files: prevState.files.concat(files),
    }));

    ioClient.emit("ready", `${files[0].name}`);
  }

  async uploadFiles() {
    this.setState({ uploadProgress: {}, uploading: true });
    const promises = [];
    this.state.files.forEach((file) => {
      promises.push(this.sendRequest(file));
    });
    await Promise.all(promises);
    this.setState({ successfullUploaded: true, uploading: false });
  }

  sendRequest(file) {
    return new Promise((resolve, reject) => {
      var req = new XMLHttpRequest();

      req.upload.addEventListener("progress", (event) => {
        if (event.lengthComputable) {
          const copy = { ...this.state.uploadProgress };
          copy[file.name] = {
            state: "pending",
            percentage: (event.loaded / event.total) * 100,
          };
          this.setState({ uploadProgress: copy });
        }
      });

      req.upload.addEventListener("load", (event) => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "done", percentage: 100 };
        this.setState({ uploadProgress: copy });
        resolve(req.response);
      });

      req.upload.addEventListener("error", (event) => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "error", percentage: 0 };
        this.setState({ uploadProgress: copy });
        reject(req.response);
      });

      var xhr = new XMLHttpRequest();
      xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4) {
          signedURL = JSON.parse(this.responseText);
          console.log(signedURL.signed_url);
          console.log(signedURL.requestId);
          var data = new FormData();
          data.append("file", file, `${file.name}`);
          req.open("PUT", signedURL.signed_url);
          req.send(file);
        }
      });

      xhr.open(
        "GET",
        `https://j2s6y0lok9.execute-api.ap-northeast-2.amazonaws.com/prod/%7Bproxy+7D?name=${file.name}`
      );
      xhr.send();
    });
  }

  renderProgress(file) {
    const uploadProgress = this.state.uploadProgress[file.name];
    if (this.state.uploading || this.state.successfullUploaded) {
      return (
        <div className="Upload-progress">
          <Progress progress={uploadProgress ? uploadProgress.percentage : 0} />
          <img
            className="Upload-check-icon"
            alt="done"
            src={require("../../img/check_circle.png")}
            style={{
              opacity:
                uploadProgress && uploadProgress.state === "done" ? 0.5 : 0,
            }}
          />
        </div>
      );
    }
  }

  renderActions() {
    return (
      <div className="Actions">
        <button
          className="Upload-button Upload-upload-button"
          disabled={this.state.files.length < 0 || this.state.uploading}
          onClick={this.uploadFiles}
        >
          업로드
        </button>
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
            <div className="Upload-files">
              {this.state.files.map((file) => {
                return (
                  <div key={file.name} className="Upload-Row">
                    <span className="Upload-Filename">{file.name}</span>
                    {this.renderProgress(file)}
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
