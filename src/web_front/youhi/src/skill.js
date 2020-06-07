import React, { Component } from 'react';
import Intsroduction from "./component/introduction/Introduction";
import Videoflow from "./component/skill/videoflow";
import Footer from "./component/footer/footer";
import Object_detection from "./component/skill/object-detection";
import Instance_segmentation from "./component/skill/instance-segmentation";
import Image_classification from "./component/skill/image-classification";
const Skill =() => {
    return (
        <div>
            <Intsroduction/>
            <Videoflow/>
            <Object_detection/>
            <Instance_segmentation/>
            <Image_classification/>
            <Footer/>
        </div>
    )
}

export default Skill;