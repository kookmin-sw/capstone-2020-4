import React, { Component } from 'react';
import Introduction from "./component/introduction/Introduction";
import Videoflow from "./component/skill/videoflow";
import Footer from "./component/footer/footer";
import ObjectDetection from "./component/skill/object-detection";
import InstanceSegmentation from "./component/skill/instance-segmentation";
// import Image_classification from "./component/skill/image-classification";
// import STT from "./component/skill/stt";
// import Web from "./component/skill/web";

const Skill =() => {
    return (
        <div>
            <Introduction/>
            <Videoflow/>
            <ObjectDetection/>
            <InstanceSegmentation/>
            {/* <Image_classification/>
            <STT/>
            <Web/> */}
            <Footer/>
        </div>
    )
}

export default Skill;