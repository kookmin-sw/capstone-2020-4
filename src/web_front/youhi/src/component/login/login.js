import React, { useRef, useEffect } from "react";
import emailjs from "emailjs-com";
import "./login.css";

const Login = ({ func }) => {
  const submitButtonRef = useRef(null);

  function sendEmail(e) {
    e.preventDefault();
    console.log(e.target);
    emailjs
      .sendForm(
        "gmail",
        "template_Qluu9LSn",
        e.target,
        "user_Rt0JXi92RLGoTk0lybQIX"
      )
      .then(
        (result) => {
          console.log(result.text);
        },
        (error) => {
          console.log(error.text);
        }
      );
  }

  useEffect(() => {
    func(submitButtonRef.current);
  });

  return (
    <div className="Login">
      <form className="Login-form" method="post" onSubmit={sendEmail}>
        <div className="Login-category">
          <div className="Login-title">이름</div>
          <div className="Login-input-container-wrapper">
            <div className="Login-input-container">
              <input className="Login-input" type="text" name="user_name" />
            </div>
          </div>
        </div>
        <div className="Login-category">
          <div className="Login-title">이메일 주소</div>
          <div className="Login-input-container-wrapper">
            <div className="Login-input-container">
              <input className="Login-input" type="email" name="user_email" />
            </div>
          </div>
        </div>
        <div className="Login-category">
          <div className="Login-title">휴대폰 번호</div>
          <div className="Login-input-container-wrapper">
            <div className="Login-input-container">
              <input className="Login-input" type="text" name="user_phone" />
            </div>
          </div>
        </div>
        <div className="Login-category">
          <div className="Login-title">파일 첨부</div>
          <input type="file" name="user_file" />
        </div>
        <div className="Login-category">
          <div className="Login-title">문의 내용</div>
          <textarea className="Login-input" name="message" />
        </div>
        <input
          ref={submitButtonRef}
          className="Login-send"
          type="submit"
          value="Submit"
          style={{ display: "none" }}
        />
      </form>
    </div>
  );
};

export default Login;
