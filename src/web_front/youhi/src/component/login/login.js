import React, { useState, useRef, useEffect } from "react";
import emailjs from "emailjs-com";
import "./login.css";

const Login = ({ func }) => {
  const [file, setFile] = useState(null);
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

  const onFilesAdded = (evt) => {
    const file = evt.target.files;
    setFile(file);
    console.log("file", file);
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
              <input
                className="Login-input"
                type="email"
                name="user_email"
                placeholder="example@gmail.com"
              />
            </div>
          </div>
        </div>
        <div className="Login-category">
          <div className="Login-title">휴대폰 번호</div>
          <div className="Login-input-container-wrapper">
            <div className="Login-input-container">
              <input
                className="Login-input"
                type="text"
                name="user_phone"
                placeholder="010-1234-5678"
              />
            </div>
          </div>
        </div>
        <div className="Login-category">
          <div className="Login-title">파일 첨부</div>
          <div className="Login-attachment-wrapper">
            <div className="Login-attachment">
              <span className="txt-placeholder">{file !== null ? file[0].name : "첨부파일 추가"}</span>
              <span className="Login-attachment-icon" />
              <input type="file" name="user_file" onChange={onFilesAdded}/>
            </div>
          </div>
        </div>
        <div className="Login-category">
          <div className="Login-title">문의 내용</div>
          <div className="Login-input-container-wrapper">
            <div className="Login-input-container Login-textarea">
              <textarea className="Login-input" name="message" />
            </div>
          </div>
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
