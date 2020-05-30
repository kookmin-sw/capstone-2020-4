import React, { Component } from "react";
import ReactPlayer from "react-player";
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
    };
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
    
    return(
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
      </div>
    );
  }
}
export default Player;