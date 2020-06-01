import React, { Component } from "react";
import ReactPlayer from "react-player";
import { Scrollbars } from "react-custom-scrollbars";
import "./Player.css";

class Player extends Component {
  constructor(props) {
    super(props);
    this.state = {
      url: "./static/0/0.mp4",
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

      adultDropDown: false,
      bloodDropDown: false,
      knifeDropDown: false,
      smokeDropDown: false,
    };

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
              url="https://www.youtube.com/watch?v=oUFJJNQGwhk"
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
          <div className="Player-info-dropdown" onClick={this.adultClickFunc}>
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
                  </Scrollbars>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default Player;
