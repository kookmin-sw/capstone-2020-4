import React, { Component } from "react";
import ReactPlayer from "react-player";
import { Scrollbars } from "react-custom-scrollbars";
import Duration from "./Duration";
import "./Player.css";

class Player extends Component {
  constructor(props) {
    super(props);
    this.state = {
      url: `./static/${this.props.clientID}/${this.props.clientID}.mp4`,
      pip: false,
      playing: false,
      controls: false,
      light: false,
      volume: 0.8,
      muted: false,
      played: 0,
      loaded: 0,
      duration: 0,
      playbackRate: 1.0,
      loop: false,

      ended: false,
      checkedTime: null,
      elapsed: 0,
      result: this.props.result,

      adultDropDown: false,
      bloodDropDown: false,
      knifeDropDown: false,
      smokeDropDown: false,
    };

    this.adultDivWrapper = React.createRef();
    this.bloodDivWrapper = React.createRef();
    this.knifeDivWrapper = React.createRef();
    this.smokeDivWrapper = React.createRef();

    this.adultDivRef = React.createRef();
    this.bloodDivRef = React.createRef();
    this.knifeDivRef = React.createRef();
    this.smokeDivRef = React.createRef();
  }

  load = (url) => {
    this.setState({
      url,
      played: 0,
      loaded: 0,
    });
  };

  handlePause = () => {
    console.log("onPause");
    this.setState({ playing: false });
  };

  handleSeek = (e) => {
    console.log("onSeek", e);
  };

  handleProgress = (state) => {
    console.log("onProgress", state);
    var condition = false;
    const data = this.state.result.labelArray;
    const checkedTime = this.state.checkedTime;
    const current = Math.floor(state.playedSeconds);

    if (this.state.playing && data[current] !== undefined) {
      if (data[current] === "adult") {
        document.getElementById("0").style.backgroundColor = "red";
      } else if (data[current] === "blood") {
        document.getElementById("1").style.backgroundColor = "red";
      } else if (data[current] === "knife") {
        document.getElementById("2").style.backgroundColor = "red";
      } else if (data[current] === "smoke") {
        document.getElementById("3").style.backgroundColor = "red";
      }
      condition = true;
    }

    if (checkedTime !== null && current - checkedTime === 3 && !condition) {
      if (data[checkedTime] === "adult") {
        document.getElementById("0").style.backgroundColor = "";
      } else if (data[checkedTime] === "blood") {
        document.getElementById("1").style.backgroundColor = "";
      } else if (data[checkedTime] === "knife") {
        document.getElementById("2").style.backgroundColor = "";
      } else if (data[checkedTime] === "smoke") {
        document.getElementById("3").style.backgroundColor = "";
      }
    }
    if (condition) {
      this.setState({ checkedTime: current });
    }

    // if (this.state.ended) {
    //   document.getElementById("0").style.fontWeight = "";
    //   document.getElementById("1").style.fontWeight = "";
    //   document.getElementById("2").style.fontWeight = "";
    //   document.getElementById("3").style.fontWeight = "";
    // }

    if (!this.state.seeking) {
      this.setState({ state: state, played: state.played });
    }
  };

  handlePlay = () => {
    console.log("onPlay");
    this.setState({ playing: true, ended: false });
  };

  handleEnded = () => {
    this.setState({ idx: 0, ended: true });
  };

  handleDuration = (duration) => {
    console.log("onDuration", duration);
    this.setState({ duration });
  };

  ref = (player) => {
    this.player = player;
  };

  printLabelArrayData = (label) => {
    const resultCopy = this.state.result;
    const data = resultCopy.labelArray;
    const dataCnt = resultCopy.cntArray;
    const labelNum =
      label === "adult" ? 0 : label === "blood" ? 1 : label === "knife" ? 2 : 3;
    if (dataCnt[labelNum] > 0) {
      return data.map((element, index) => {
        const date1 = new Date(index * 1000);
        const mm1 = date1.getUTCMinutes();
        const ss1 = ("0" + date1.getUTCSeconds()).slice(-2);

        const diff = Math.floor(this.state.duration - index);
        const date2 =
          diff < 3
            ? new Date((index + diff) * 1000)
            : new Date((index + 3) * 1000);
        const mm2 = date2.getUTCMinutes();
        const ss2 = ("0" + date2.getUTCSeconds()).slice(-2);

        if (element === label) {
          if (diff < 3) {
            return (
              <div className="Player-label-time">
                {`${mm1}:${ss1}`} ~ {`${mm2}:${ss2}`}
              </div>
            );
          } else {
            return (
              <div className="Player-label-time">
                {`${mm1}:${ss1}`} ~ {`${mm2}:${ss2}`}
              </div>
            );
          }
        } else {
          return null;
        }
      });
    } else {
      return (
        <div className="Player-empty-labels">
          영상에서 해당 레이블이 검열되지 않음
        </div>
      );
    }
  };

  adultClickFunc = () => {
    this.setState({ adultDropDown: !this.state.adultDropDown }, () => {
      const obj = this.adultDivRef.current;
      obj.removeAttribute("style");
      if (!this.state.adultDropDown) obj.style.height = "0";
      else obj.style.maxHeight = "800px";
    });
  };

  bloodClickFunc = () => {
    this.setState({ bloodDropDown: !this.state.bloodDropDown }, () => {
      const obj = this.bloodDivRef.current;
      obj.removeAttribute("style");
      if (!this.state.bloodDropDown) obj.style.height = "0";
      else obj.style.maxHeight = "800px";
    });
  };

  knifeClickFunc = () => {
    this.setState({ knifeDropDown: !this.state.knifeDropDown }, () => {
      const obj = this.knifeDivRef.current;
      obj.removeAttribute("style");
      if (!this.state.knifeDropDown) obj.style.height = "0";
      else obj.style.maxHeight = "800px";
    });
  };

  smokeClickFunc = () => {
    this.setState({ smokeDropDown: !this.state.smokeDropDown }, () => {
      const obj = this.smokeDivRef.current;
      obj.removeAttribute("style");
      if (!this.state.smokeDropDown) obj.style.height = "0";
      else obj.style.maxHeight = "800px";
    });
  };

  componentDidMount() {
    console.log("componentDidMount");
    this.props.func([
      this.adultDivWrapper.current,
      this.bloodDivWrapper.current,
      this.knifeDivWrapper.current,
      this.smokeDivWrapper.current,
    ]);
  }

  componentDidUpdate(prevProps, prevState) {
    const condition =
      prevState.adultDropDown !== this.state.adultDropDown ||
      prevState.bloodDropDown !== this.state.bloodDropDown ||
      prevState.knifeDropDown !== this.state.knifeDropDown ||
      prevState.smokeDropDown !== this.state.smokeDropDown;
    if (condition) {
      console.log("componentDidUpdate");
      console.log(this.state.adultDropDown);
      console.log(this.state.bloodDropDown);
      console.log(this.state.knifeDropDown);
      console.log(this.state.smokeDropDown);
      this.props.func2([
        this.state.adultDropDown,
        this.state.bloodDropDown,
        this.state.knifeDropDown,
        this.state.smokeDropDown,
      ]);
    }
  }

  render() {
    const {
      url,
      playing,
      volume,
      muted,
      played,
      loaded,
      duration,
    } = this.state;

    return (
      <div className="Player">
        <section className="section">
          <div className="player-wrapper">
            <ReactPlayer
              ref={this.ref}
              className="react-player"
              width="100%"
              height="100%"
              url={url}
              playing={playing}
              controls={true}
              volume={volume}
              muted={muted}
              onPause={this.handlePause}
              onSeek={this.handleSeek}
              onPlay={this.handlePlay}
              onEnded={this.handleEnded}
              onProgress={this.handleProgress}
              onDuration={this.handleDuration}
            />
          </div>
        </section>
        <div className="Player-info-wrapper">
          <div
            className="Player-info-dropdown"
            onClick={this.adultClickFunc}
            ref={this.adultDivWrapper}
          >
            <div className="Player-header">
              <div className="Player-icon-container">
                <span
                  className={`Player-dropdown-icon ${
                    this.state.adultDropDown ? "caret-down" : "caret-right"
                  }`}
                />
              </div>
              <div className="Player-main-title">Adult</div>
            </div>
            <div
              className={`${
                this.state.adultDropDown
                  ? "Player-menu-content"
                  : "Player-menu-content-closed"
              }`}
              ref={this.adultDivRef}
            >
              <div id="Player-adult">
                <div className="Player-label-boxes">
                  <Scrollbars
                    className="Player-scrollbars"
                    style={{ width: "100%", height: "80px", textAlign: "left" }}
                    renderTrackHorizontal={(props) => (
                      <div
                        {...props}
                        style={{ display: "none" }}
                        className="track-horizontal"
                      />
                    )}
                  >
                    {this.printLabelArrayData("adult")}
                  </Scrollbars>
                </div>
              </div>
            </div>
          </div>
          <div
            className="Player-info-dropdown"
            onClick={this.bloodClickFunc}
            ref={this.bloodDivWrapper}
          >
            <div className="Player-header">
              <div className="Player-icon-container">
                <span
                  className={`Player-dropdown-icon ${
                    this.state.bloodDropDown ? "caret-down" : "caret-right"
                  }`}
                />
              </div>
              <div className="Player-main-title">Blood</div>
            </div>
            <div
              className={`${
                this.state.bloodDropDown
                  ? "Player-menu-content"
                  : "Player-menu-content-closed"
              }`}
              ref={this.bloodDivRef}
            >
              <div className="Player-label-boxes">
                <Scrollbars
                  className="Player-scrollbars"
                  style={{ width: "100%", height: "80px", textAlign: "left" }}
                  renderTrackHorizontal={(props) => (
                    <div
                      {...props}
                      style={{ display: "none" }}
                      className="track-horizontal"
                    />
                  )}
                >
                  {this.printLabelArrayData("blood")}
                </Scrollbars>
              </div>
            </div>
          </div>
          <div
            className="Player-info-dropdown"
            onClick={this.knifeClickFunc}
            ref={this.knifeDivWrapper}
          >
            <div className="Player-header">
              <div className="Player-icon-container">
                <span
                  className={`Player-dropdown-icon ${
                    this.state.knifeDropDown ? "caret-down" : "caret-right"
                  }`}
                />
              </div>
              <div className="Player-main-title">Knife</div>
            </div>
            <div
              className={`${
                this.state.knifeDropDown
                  ? "Player-menu-content"
                  : "Player-menu-content-closed"
              }`}
              ref={this.knifeDivRef}
            >
              <div className="Player-label-boxes">
                <Scrollbars
                  className="Player-scrollbars"
                  style={{ width: "100%", height: "80px", textAlign: "left" }}
                  renderTrackHorizontal={(props) => (
                    <div
                      {...props}
                      style={{ display: "none" }}
                      className="track-horizontal"
                    />
                  )}
                >
                  {this.printLabelArrayData("knife")}
                </Scrollbars>
              </div>
            </div>
          </div>
          <div
            className="Player-info-dropdown"
            onClick={this.smokeClickFunc}
            ref={this.smokeDivWrapper}
          >
            <div className="Player-header">
              <div className="Player-icon-container">
                <span
                  className={`Player-dropdown-icon ${
                    this.state.smokeDropDown ? "caret-down" : "caret-right"
                  }`}
                />
              </div>
              <div className="Player-main-title">Smoke</div>
            </div>
            <div
              className={`${
                this.state.smokeDropDown
                  ? "Player-menu-content"
                  : "Player-menu-content-closed"
              }`}
              ref={this.smokeDivRef}
            >
              <div className="Player-label-boxes">
                <Scrollbars
                  className="Player-scrollbars"
                  style={{ width: "100%", height: "80px", textAlign: "left" }}
                  renderTrackHorizontal={(props) => (
                    <div
                      {...props}
                      style={{ display: "none" }}
                      className="track-horizontal"
                    />
                  )}
                >
                  {this.printLabelArrayData("smoke")}
                </Scrollbars>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Player;
