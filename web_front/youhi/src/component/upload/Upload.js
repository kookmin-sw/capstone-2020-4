import React, { Component } from "react";
import UploadElementor from "./upload_elementor/UploadElementor";
import Dropzone from "./dropzone/Dropzone";
import "./Upload.css";
import Progress from "./progress/Progress";
import Text from "./text/Text";
import io from "socket.io-client";
import { ToastContainer, toast } from 'react-toastify';
import './ReactToastify.css';
import getBlobDuration from "get-blob-duration";

var signedURL;

const ioClient = io.connect("http://13.209.93.181:4567");

class Upload extends Component {
  constructor(props) {
    super(props);
    this.state = {
      files: [],
      fileName: "",
      uploading: false,
      uploadProgress: {},
      successfullUploaded: false,
      filterButtonDisable: true,

      testState: false,
      account: null,
      successfulVideoFiltered: false,
      successfulVoiceFiltered: false,
    };

    this.onFilesAdded = this.onFilesAdded.bind(this);
    this.uploadFiles = this.uploadFiles.bind(this);
    this.sendRequest = this.sendRequest.bind(this);
    this.orderFilter = this.orderFilter.bind(this);
    this.renderActions = this.renderActions.bind(this);
  }

  notifyVideoCntError = () => {
    toast.error("하나의 영상만 업로드 가능합니다.");
  }

  notifyFormatError = () => {
    toast.error(".mp4 영상만이 허용됩니다.");
  }

  notifyVideoDurationError = () => {
    toast.error("영상 재생시간이 1분을 초과하였습니다.")
  }

  notifyUploading = () => {
    toast.info("영상 업로드중입니다.");
  }

  notifySuccessfulUploaded = () => {
    toast.info("검열 준비가 완료될 때까지 기다려주세요.");
  }

  notifyFiltering = () => {
    toast.info("검열 중입니다.")
  }

  notifySuccessfulFiltered = () => {
    toast.success("검열을 완료하였습니다.");
  }

  onFilesAdded(files) {
    if (files.length === 1 && this.state.files.length === 0) {
      if (files[0].type === "video/mp4") {
        getBlobDuration(files[0]).then((duration) => {
          if (duration <= 60) {
            this.setState((prevState) => ({
              files: prevState.files.concat(files),
            }));  
            ioClient.emit("ready", `${files[0].name}`);
            ioClient.on(
              "number",
              function (data) {
                this.setState({ account: data });
              }.bind(this)
            );
            // ioClient.emit("complete", `hi`); //lambda event
            ioClient.on(
              "upload",
              function (data) {
                console.log(data);
                this.setState({ filterButtonDisable: false, testState: false });
              }.bind(this)
            );
          } else {
            this.notifyVideoDurationError();
          }
        });        
      } else {
        this.notifyFormatError();
      }
    } else {
      this.notifyVideoCntError();
    }
  }

  async uploadFiles() {
    this.setState({ uploadProgress: {}, uploading: true });
    const promises = [];
    this.state.files.forEach((file) => {
      promises.push(this.sendRequest(file));
    });
    try {
      await Promise.all(promises);

      this.setState({
        successfullUploaded: true,
        uploading: false,
      });
    } catch (e) {
      // Not Production ready! Do some error handling here instead...
      this.setState({ successfullUploaded: true, uploading: false });
    }
  }

  sendRequest(file) {
    return new Promise((resolve, reject) => {
      const req = new XMLHttpRequest();
      const clientID = this.state.account.value;

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
        this.notifySuccessfulUploaded();
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "done", percentage: 100 };
        this.setState({ uploadProgress: copy, testState: true });
        resolve(req.response);
      });

      req.upload.addEventListener("error", (event) => {
        const copy = { ...this.state.uploadProgress };
        copy[file.name] = { state: "error", percentage: 0 };
        this.setState({ uploadProgress: copy });
        reject(req.response);
      });

      const xhr = new XMLHttpRequest();
      xhr.addEventListener("readystatechange", function () {
        if (xhr.readyState === 4) {
          signedURL = JSON.parse(xhr.responseText);
          console.log(signedURL.signed_url);
          const data = new FormData();
          data.append("file", file, `${clientID}.mp4`);

          req.open("PUT", signedURL.signed_url);
          req.send(file);
          // this.notifyUploading();
        }
      });
      xhr.open(
        "GET",
        `https://j2s6y0lok9.execute-api.ap-northeast-2.amazonaws.com/prod/%7Bproxy+7D?name=${clientID}.mp4`
      );
      xhr.send();
    });
  }

  renderProgress(file) {
    const uploadProgress = this.state.uploadProgress[file.name];
    if (this.state.uploading || this.state.successfullUploaded) {
      return (
        <div className="ProgressWrapper">
          <Progress progress={uploadProgress ? uploadProgress.percentage : 0} />
          <img
            className="CheckIcon"
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

  orderFilter() {
    // 로딩 에니메이션 출력
    this.setState({ testState: true, filterButtonDisable: true });

    const clientID = this.state.account.value;
    // 검열을 시작하라는 이벤트를 등록한다.
    ioClient.emit("filter", `${clientID}.mp4`);
    this.notifyFiltering();
    ioClient.on(
      "voice_result",
      function (data) {
        console.log(data);
        this.setState({ successfulVoiceFiltered: true }, () => {
          // this.notifySuccessfulFiltered();
          // this.props.func([true, this.state.account.value]);
        });
      }.bind(this)
    );
    ioClient.on(
      "video_result",
      function (data) {
        this.setState({ successfulVideoFiltered: true })
      }.bind(this)
    );
    // 검열이 끝나면 소켓 서버로부터 수신받는 코드, 검열 확인 박스를 활성화 시켜야함.
    // ioClient.on("??", function(data) {
    //   this.props.func();
    // });
  }

  renderActions() {
    if (this.state.successfullUploaded) {
      return (
        <div className="Actions">
          <button
            className="Upload-button Upload-upload-button"
            onClick={() =>
              this.setState(
                {
                  files: [],
                  successfullUploaded: false,
                  filterButtonDisable: true,
                },
                () => {
                  // this.props.func([false, null]);
                  window.location.reload(false);
                }
              )
            }
          >
            Clear
          </button>
          <button
            className="Upload-button Upload-filter-button"
            onClick={this.orderFilter}
            disabled={this.state.filterButtonDisable}
          >
            검열
          </button>
        </div>
      );
    } else {
      return (
        <div className="Actions">
          <button
            className="Upload-button Upload-upload-button"
            disabled={this.state.files.length === 0 || this.state.uploading}
            onClick={this.uploadFiles}
          >
            업로드
          </button>
          <button
            className="Upload-button Upload-filter-button"
            disabled={true}
          >
            검열
          </button>
        </div>
      );
    }
  }

  componentDidUpdate() {
    if (this.state.successfulVideoFiltered && this.state.successfulVoiceFiltered) {
      if (this.state.testState) {
        this.setState({ testState: false }, () => {
          this.notifySuccessfulFiltered();
          this.props.func([true, this.state.account.value]);
        });
      }
    }
  }

  render() {
    return (
      <div className="Upload-wrapper">
        <UploadElementor />
        <div className="Content">
          <ToastContainer
            hideProgressBar={true}
            autoClose={3000}
          />
          <Dropzone
            onFilesAdded={this.onFilesAdded}
            disabled={this.state.uploading || this.state.successfullUploaded}
            filesLength={this.state.files.length}
          />
          <div className="Upload-text-buttons-container">
            <Text />
            <div className="Files">
              {this.state.files.map((file) => {
                return (
                  <div key={file.name} className="Row">
                    <span className="Filename">{file.name}</span>
                    {this.renderProgress(file)}
                  </div>
                );
              })}
            </div>
            <div className="wrap">
              {this.renderActions()}
              <span
                className={`test-icon-container loading-spinner ${
                  this.state.testState ? "" : "hide"
                }`}
              >
                <div className="test-icon loading-spinner-icon" />
              </span>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Upload;
