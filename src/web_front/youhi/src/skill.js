import React, { Component } from 'react';
import Intsroduction from "./component/introduction/Introduction";
import Videoflow from "./component/skill/videoflow";
import Footer from "./component/footer/footer";
import Object_detection from "./component/skill/object-detection";
import Instance_segmentation from "./component/skill/instance-segmentation";

const Skill =() => {
    return (
        <div>
            <Intsroduction/>
            <Videoflow/>
            <Object_detection/>
            <Instance_segmentation/>
            <Footer/>
        </div>
    )
}

export default Skill;