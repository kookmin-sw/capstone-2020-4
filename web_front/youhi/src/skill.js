import React from 'react';
import Introduction from "./component/introduction/Introduction";
import Videoflow from "./component/skill/videoflow";
import Footer from "./component/footer/footer";
import ObjectDetection from "./component/skill/object-detection";
import InstanceSegmentation from "./component/skill/instance-segmentation";
import ImageClassification from "./component/skill/image-classification";
import VideoClassification from "./component/skill/VideoClassification";
import STT from "./component/skill/stt";
import Khaiii from "./component/skill/Khaiii";
import FastText from "./component/skill/FastText";
import FrontEnd from "./component/skill/FrontEnd";
import BackEnd from "./component/skill/BackEnd";

const Skill =() => {
    return (
        <div>
            <Introduction/>
            <Videoflow/>
            <ObjectDetection/>
            <InstanceSegmentation/>
            <ImageClassification/>
            <VideoClassification />
            <STT/>
            <Khaiii />
            <FastText />
            <FrontEnd/>
            <BackEnd/>
            <Footer/>
        </div>
    )
}

export default Skill;