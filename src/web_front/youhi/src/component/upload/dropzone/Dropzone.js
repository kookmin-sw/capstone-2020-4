import React, { Component } from "react";
import ReactPlayer from "react-player";
import "./Dropzone.css";

class Dropzone extends Component {
  constructor(props) {
    super(props);
    this.state = { 
      highlight: false,
      fileUrl: null,
    };
    this.fileInputRef = React.createRef();
    this.inputDivRef = React.createRef();

    this.openFileDialog = this.openFileDialog.bind(this);
    this.onFilesAdded = this.onFilesAdded.bind(this);
    this.onDragOver = this.onDragOver.bind(this);
    this.onDragLeave = this.onDragLeave.bind(this);
    this.onDrop = this.onDrop.bind(this);
  }

  openFileDialog() {
    if (this.props.disabled) return;
    this.fileInputRef.current.click();
  }

  onFilesAdded(evt) {
    if (this.props.disabled) return;
    const files = evt.target.files; 
    console.log("files", files);
    if (this.props.onFilesAdded) {
      const array = this.fileListToArray(files);
      this.props.onFilesAdded(array);
    }
  }

  onDragOver(event) {
    event.preventDefault();
    if (this.props.disabled) return;
    this.setState({ highlight: true });
  }

  onDragLeave(event) {
    this.setState({ highlight: false });
  }

  onDrop(event) {
    event.preventDefault();
    if (this.props.disabled) return;
    const files = event.dataTransfer.files;
    if (this.props.onFilesAdded) {
      const array = this.fileListToArray(files);
      this.props.onFilesAdded(array);
    }
    this.setState({ highlight: false });
  }

  fileListToArray(list) {
    const fileUrl = window.URL.createObjectURL(list[0]);
    const array = [];
    for (var i = 0; i < list.length; i++) {
      array.push(list.item(i));
    }
    this.setState({ fileUrl: fileUrl });
    return array;
  }

  renderView = () => {
    const condition = this.props.filesLength ? true : false;
    if (condition) {
      return (
        <ReactPlayer url={this.state.fileUrl} />
      );
    } else {
      return (
        <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
          <img
            alt="upload"
            className="Icon"
            src={require("../../../img/dropzone.png")}
          />
          <span>
            동영상을 '여기' 끌어다 놓거나
            <br />
            '여기'를 클릭하세요.
          </span>
        </div>
      );
    }
  }

  componentDidUpdate() {
    if (this.props.filesLength) {
      this.inputDivRef.current.style.border = "none";
    } else {
      this.inputDivRef.current.style.border = "1px dashed rgb(142, 123, 123)";
    }
  }

  render() {
    return (
      <div
        className={`Dropzone ${this.state.highlight ? "Highlight" : ""}`}
        onDragOver={this.onDragOver}
        onDragLeave={this.onDragLeave}
        onDrop={this.onDrop}
        onClick={this.openFileDialog}
        style={{ cursor: this.props.disabled ? "default" : "pointer" }}
        ref={this.inputDivRef}
      >
        <input
          ref={this.fileInputRef}
          className="FileInput"
          type="file"
          multiple
          onChange={this.onFilesAdded}
        />
        {this.renderView()}
      </div>
    );
  }
}

export default Dropzone;
