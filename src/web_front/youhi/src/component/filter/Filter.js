import React, { Component } from "react";
import FilterElement from "./filter_elementor/FilterElementor";
import "./Filter.css";
import NewWindow from "react-new-window";
import { makeStyles } from "@material-ui/core/styles";
import Modal from "@material-ui/core/Modal";

function rand() {
  return Math.round(Math.random() * 20) - 10;
}

function getModalStyle() {
  const top = 50 + rand();
  const left = 50 + rand();

  return {
    top: `${top}%`,
    left: `${left}%`,
    transform: `translate(-${top}%, -${left}%)`,
  };
}

const useStyles = makeStyles((theme) => ({
  paper: {
    position: "absolute",
    width: 400,
    backgroundColor: theme.palette.background.paper,
    border: "2px solid #000",
    boxShadow: theme.shadows[5],
    padding: theme.spacing(2, 4, 3),
  },
}));

function Filter() {
  const classes = useStyles();
  // getModalStyle is not a pure function, we roll the style only on the first render
  const [modalStyle] = React.useState(getModalStyle);
  const [open, setOpen] = React.useState(false);

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const body = (
    <div style={modalStyle} className={classes.paper}>
      test
    </div>
  );

  return (
    <div className="Filter-container">
      <FilterElement />
      <div className="filter-wrapper">
        <div className="Filter-filter-box">
          <div className="inner-filter-wrapper">
            <button
              className="Filter-box Filter-video-filter"
              onClick={handleOpen}/>
              <Modal
                open={open}
                onClose={handleClose}
                aria-labelledby="simple-modal-title"
                aria-describedby="simple-modal-description">
                {body}
              </Modal>
          </div>
          <div className="filter-box-space"></div>
          <div className="inner-filter-wrapper">
            <button className="Filter-box Filter-voice-filter" />
          </div>
        </div>
      </div>
      <div className="Filter-feedback-button-wrapper">
        <button className="Filter-feedback-button">이의신청 및 문의하기</button>
      </div>
    </div>
  );
}

export default Filter;
