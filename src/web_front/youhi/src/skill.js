import React, { Component } from 'react';
import Introduction from "./component/introduction/Introduction";
import Videoflow from "./component/skill/videoflow";
import Footer from "./component/footer/footer";
import Object_detection from "./component/skill/object-detection";
// import Instance_segmentation from "./component/skill/instance-segmentation";
// import Image_classification from "./component/skill/image-classification";
// import STT from "./component/skill/stt";
// import Web from "./component/skill/web";

const Skill =() => {
    return (
        <div>
            <Introduction/>
            <Videoflow/>
            <Object_detection/>
            {/* <Instance_segmentation/>
            <Image_classification/>
            <STT/>
            <Web/> */}
            <Footer/>
        </div>
    )
}

export default Skill;