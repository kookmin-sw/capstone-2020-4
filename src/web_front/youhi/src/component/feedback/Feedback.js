import React, { Component } from "react";
import GoogleLogin from "react-google-login";
import FeedbackModal from "./FeedbackModal";
import "./Feedback.css";

class Objection extends Component {
  constructor(props) {
    super(props);
    this.state = {
      check: false,
      isModalOpen: false,
      emailAddress: null,
    };
    this.feedBackButtonDiv = React.createRef();
  }

  success = (response) => {
    const emailAddress = response.Ut.Eu;
    this.setState({ emailAddress: emailAddress }, () => {
      this.openModal();
    });
  };

  error = (response) => {
    console.error(response);
  };

  openModal = () => {
    document.querySelector("body").style.overflow = "hidden";
    this.setState({ isModalOpen: true }, () => {
      this.renderFeedbackModal();
    });
  };

  closeModal = () => {
    document.querySelector("body").style.overflow = "";
    this.setState({ isModalOpen: false });
  };

  clickFunc = () => {
    this.feedBackButtonDiv.current.children[0].click();
    console.log(this.feedBackButtonDiv.current.children[0]);
  };

  renderFeedbackModal = () => {
      return (
        <FeedbackModal
          isOpen={this.state.isModalOpen}
          close={this.closeModal}
          emailAddress={this.state.emailAddress}
        />
      );
  };

  render() {
    return (
      <div className="Feedback">
        <button className="Feedback-button" onClick={this.clickFunc}>
          이의신청 및 문의하기
        </button>
        {this.renderFeedbackModal()}
        <div
          className="Feedback-google-login"
          style={{ display: "none" }}
          ref={this.feedBackButtonDiv}
        >
          <GoogleLogin
            clientId="935198554711-21ljbdchpkmt5f3p1hcun6tnjr2mgqpf.apps.googleusercontent.com"
            buttonText="Login"
            onSuccess={this.success}
            onFailure={this.error}
          />
        </div>
      </div>
    );
  }
}

export default Objection;
