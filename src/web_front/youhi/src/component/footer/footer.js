import React from 'react';
import "./footer.css";

const Footer =() => {
    return(
        <div className="foot-wrapper">
            <div className = "foot-wrapper2">
                <div className="foot1">
                    <h1 className = "footer-main">안내</h1>
                    <h4 className = "foot-sub-col">콘텐츠 규정</h4>
                    <h4 className = "foot-sub-col">문의하기</h4>
                    <h4 className = "foot-sub-col">테스트</h4>
                </div>
                <div className="foot2">
                    <h1 className = "footer-main">Team YouHi</h1>
                    <h4 className = "foot-sub-col">Kookmin University Computer Science</h4>
                    <h4 className = "foot-sub-col">서울특별시 성북구 정릉로 77</h4>
                    <h4 className = "foot-sub-col">Developed by Team YouHi</h4>
                </div>
            </div>
         </div>
    )
}

export default Footer;