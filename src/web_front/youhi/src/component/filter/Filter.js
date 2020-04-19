import React, { Component } from "react";
import FilterElement from "./filter_elementor/FilterElementor";
import "./Filter.css";
import NewWindow from "react-new-window";

class Filter extends Component {
  constructor(props) {
    super(props);
    this.state = {};

    this.showFilterResult = this.showFilterResult.bind(this);
  }

  showFilterResult() {
    var wFeature =
    'width=500, height=500, location=no,toolbar=no,menubar=no,scrollbars=yes,resizable=yes';
    var w = window.open("/filter", "_blank", wFeature);
    w.document.write(`<title>Filter</title>`);
    w.document.write(`<img src="static/media/background_img.3ccc4efd.png" width="300px"> 안녕`)

  } 

  render() {
    return (
      <div className="Filter-container">
        <FilterElement />
        <div className = "filter-wrapper">
          <div className="Filter-filter-box">
            <div className = "inner-filter-wrapper">
              <button
                className="Filter-box Filter-video-filter"
                onClick={this.showFilterResult}
              />
            </div>
            <div className = "filter-box-space"></div>            
            <div className = "inner-filter-wrapper">
              <button className="Filter-box Filter-voice-filter" />
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Filter;