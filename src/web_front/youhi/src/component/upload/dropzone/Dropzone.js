import React, { Component } from "react";
import "./Dropzone.css";

class Dropzone extends Component {
  constructor(props) {
    super(props);
    this.state = { highlight: false };
    this.fileInputRef = React.createRef();

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
    this.setState({ highlight: false});
  }

  fileListToArray(list) {
    const array = [];
    for (var i = 0; i < list.length; i++) {
      array.push(list.item(i));
    }
    return array;
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
      >
        <input
          ref={this.fileInputRef}
          className="Dropzone-FileInput"
          type="file"
          multiple
          onChange={this.onFilesAdded}
        />
        <img
          alt="dropzone img"
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

export default Dropzone;
