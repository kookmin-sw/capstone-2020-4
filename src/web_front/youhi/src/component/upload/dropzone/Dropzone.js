import React, { Component } from 'react';
import "./Dropzone.css"

class Dropzone extends Component {
  constructor(props) {
    super(props);
    this.state = { highlight: false };

  }

  render() {
    return (
      <div className={`Dropzone ${this.state.highlight ? "Highlight" : ""}`}>
        
      </div>
    );
  }
}

export default Dropzone;