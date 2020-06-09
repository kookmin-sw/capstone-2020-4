import React, { useState } from "react";
import ReactTransitionGroup from "react-addons-css-transition-group";
import { ToastContainer, toast } from "react-toastify";
import Login from "../login/login";
import "./FeedbackModal.css";
import "../upload/ReactToastify.css";

const FeedbackModal = ({ isOpen, close, emailAddress }) => {

  const notifySumbit = () => {
    toast.success("이의 신청이 완료되었습니다.")
  }

  const [submitButtonRef, setSubmitButtonRef] = useState(null);

  return (
    <div>
      <ToastContainer hideProgressBar={true} autoClose={3000} />
      {isOpen ? (
        <ReactTransitionGroup
          transitionName={"Modal-anim"}
          transitionEnterTimeout={200}
          transitionLeaveTimeout={200}
        >
          <div className="FeedbackModal-overlay" onClick={close} />
          <div className="FeedbackModal">
            <p className="title">이의신청 및 문의하기</p>
            <div className="content">
              <Login func={setSubmitButtonRef} />
            </div>
            <div className="button-wrap">
              <button
                onClick={() => {
                  close();
                  submitButtonRef.click();
                  notifySumbit();
                }}
              >
                제출
              </button>
            </div>
          </div>
        </ReactTransitionGroup>
      ) : (
        <ReactTransitionGroup
          transitionName={"Modal-anim"}
          transitionEnterTimeout={200}
          transitionLeaveTimeout={200}
        />
      )}
    </div>
  );
};
export default FeedbackModal;
