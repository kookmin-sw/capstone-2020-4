import React from "react";
import "./Navbar.css";

const Navbar = () => {
  return (
    <div className="nav-wrapper">
      <img id="main-logo" src={require("../../img/YouHi_logo.png")} alt="" />
      <div id="project-name">YouHi</div>
    </div>
  );
};

export default Navbar;
