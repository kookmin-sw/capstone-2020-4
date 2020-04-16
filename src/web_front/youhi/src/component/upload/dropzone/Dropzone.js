import React, { Component } from 'react';
import "./Dropzone.css"

class Dropzone extends Component {
  constructor(props) {
    super(props);
    this.state = { highlight: false };
    this.fileInputRef = React.createRef();

    // this.openFileDialog = this.openFileDialog.bind(this);
    // this.onFilesAdded = this.onFilesAdded.bind(this);
    // this.onDragOver = this.onDragOver.bind(this);
    // this.onDragLeave = this.onDragLeave.bind(this);
    // this.onDrop = this.onDrop.bind(this);
  }

  render() {
    return (
      <div className={`Dropzone ${this.state.highlight ? "Highlight" : ""}`}>
        <input ref={this.fileInputRef}
        className="Dropzone-FileInput"
        type="file"
        multiple
        onChange={this.onFilesAdded}
        / >
      </div>
    );
  }
}

export default Dropzone;