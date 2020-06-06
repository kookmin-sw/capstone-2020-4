import React, { Component } from 'react';
import Intsroduction from "./component/introduction/Introduction";
import Videoflow from "./component/skill/videoflow";
import Footer from "./component/footer/footer";
import Object_detection from "./component/skill/object-detection";

const Skill =() => {
    return (
        <div>
            <Intsroduction/>
            <Videoflow/>
            <Object_detection/>
            <Footer/>
        </div>
    )
}

export default Skill;