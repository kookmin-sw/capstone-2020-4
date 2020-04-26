import React, { Component } from "react";
import FilterElement from "./filter_elementor/FilterElementor";
import "./Filter.css";
import NewWindow from "react-new-window";
import { makeStyles } from "@material-ui/core/styles";
import Modal from "@material-ui/core/Modal";
import LoginModal from "../filter/exception/exception";
import FilterResult from "./FilterResult/FilterResult";


function Filter() {
  return (
    <div className="Filter-container">
      <FilterElement />
      <div className="filter-wrapper">
        <div className="Filter-filter-box">
          {FilterResult()}
          <div className="filter-box-space"></div>
          <div className="inner-filter-wrapper">
            <button className="Filter-box Filter-voice-filter" />
          </div>
        </div>
        {LoginModal()}
      </div>

    </div>
  );
}

export default Filter;
