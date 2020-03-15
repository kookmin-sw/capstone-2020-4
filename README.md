# Welcome to YouH! 


**팀페이지 주소** -> https://kookmin-sw.github.io/capstone-2020-4/


## 1. 프로젝트 소개

본 프로젝트는 현 유튜브의 미성년자 시청 불가 영상에 대한 필터링 시스템의 단점을 보완하는 것을 목표로 한다. 현재 유튜브의 영상 검열 시스템은 사용자의 신고 혹은 운영자의 모니터링을 통한 수동 검열로 이루어진다. 이러한 방식은 새로 업로드된 영상을 즉각적으로 필터링 할수 없으며 사용자의 신고를 받거나 운영자의 모니터링에 의해 검열 되기 전까지 청소년들에게 무방비 상태로 노출된다. 이를 방지하기 위하여 영상이 업로드되기 전에 사전 필터링을 하여 가이드라인(유튜브 커뮤니티 가이드라인, 방송통신심의위원회)에 위배되는 내용이 영상에 포함되어 있을 경우, 청소년 시청 불가 컨텐츠로 분류한다. 사전 필터링 과정을 통해 청소년에게 유해한 컨텐츠가 노출되는 것을 예방한다.  

영상과 음성을 모두 필터링 하는데, 영상 필터링은 선정적이거나 폭력적인 장면, 미성년자들에게 유해한 담배, 술, 마약 등을 적극 권장하는 장면을 감지하는 시스템이다. 또한 음성 필터링은 욕설을 감지하는 시스템이다.

필터링 기준은 다음과 같이 Youtube 이용정책 - 연령별 제한 등급을 참고하였다.
<img src="/doc/img/guide_line.png">
## 2. 소개 영상

프로젝트 소개하는 영상을 추가하세요

## 3. 팀 소개

1. 20153216 이태훈 - 팀장 (says7869@gmail.com)  

   <img src="/doc/img/Lee_Tae_Hoon.jpg">

   역할: Video Classification 모델링과 학습 및 AWS 서버를 이용한 전체적인 소프트웨어 설계

2. 20153211 이인평 (jinipyung@gmail.com) 

   <img src="/doc/img/Lee_In_Pyeong.jpg">

   역할: Video Classfication, FastText 학습을 위한 데이터셋 구축 및 FastText 모델링과 학습

3. 20153214 이주형 (srlee96@kookmin.ac.kr) 

   <img src="/doc/img/Lee_Ju_Hyeong.jpg">

   역할: STT(Speech To Text) API 적용 및 Video Classification 데이터셋 구축

4. 20153158 김성수

   역할: Kaldi-Zeroth 모델링과 학습 및 웹페이지와 웹서버 구축

5. 김민재 (minjae103030@naver.com)

   <img src="/doc/img/Kim_Min_Jae.jpg">

   역할: Video Classfication, FastText 학습을 위한 데이터셋 구축 및 웹페이지 디자인 UI 제작

## 4. 사용법

소스코드제출시 설치법이나 사용법을 작성하세요.

## 5. Abstract

My Project's goal is to prevent people who watch youtube or video platform website from watching a nasty videos. So we have to filter about video and voice. Video filter is filtered from CRNN DeepLearning Model. The scene we are trying to filter is either sensational or violent. We also want to include scenes of alchol, arug, and cigarettes. And then voice filter  is filtered through two processes. First we have to convert voice to text by using STT(Speech To text) technology. Second, use fasttext to detect whether the translated text contains swear words. After filtering, If any one is detected, uploading is restricted. Also we tell you where it was detected. 
For our filtering criteria, we refer to the Youtube usage policy-Restriction level by age as follows.

