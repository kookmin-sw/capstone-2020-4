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
  render() {
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
              controls={true}
            />
          </div>
        </section>
      </div>
    );
  }
}
export default Player;