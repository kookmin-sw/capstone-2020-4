import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';
import Login from "../../login/login";

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
    position: 'absolute',
    width: 400,
    backgroundColor: theme.palette.background.paper,
    border: '2px solid #000',
    boxShadow: theme.shadows[5],
    padding: theme.spacing(2, 4, 3),
  },
}));

export default function LoginModal() {
  const classes = useStyles();
  // getModalStyle is not a pure function, we roll the style only on the first render
  const [modalStyle] = React.useState(getModalStyle);
  const [open, setOpen] = React.useState(false);

  const handleOpen2 = () => {
    setOpen(true);
  };

  const handleClose2 = () => {
    setOpen(false);
  };

  const loginbody = (
    <div style={modalStyle} className={classes.paper}>
      <Login/>
    </div>
  );

  return (
    <div className="Filter-feedback-button-wrapper">
        <button 
        onClick = {handleOpen2}
        className="Filter-feedback-button">이의신청 및 문의하기</button>
        <Modal
          open={open}
          onClose={handleClose2}
          aria-labelledby="simple-modal-title"
          aria-describedby="simple-modal-description"
        >
          {loginbody}
        </Modal>
    </div>
  );
}
