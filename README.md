# Welcome to YouHa! 



## 팀소개 및 페이지를 꾸며주세요.

- 프로젝트 소개
  - 프로젝트 설치방법 및 데모, 사용방법, 프리뷰등을 readme.md에 작성.
  - Api나 사용방법등 내용이 많을경우 wiki에 꾸미고 링크 추가.

- 팀페이지 꾸미기
  - 프로젝트 소개 및 팀원 소개
  - index.md 예시보고 수정.

- GitHub Pages 리파지토리 Settings > Options > GitHub Pages 
  - Source를 marster branch
  - Theme Chooser에서 태마선택
  - 수정후 팀페이지 확인하여 점검.

**팀페이지 주소** -> https://github.com/kookmin-sw/capstone-2020-4 


### 1. 프로젝트 소개

본 프로젝트는 현 유튜브의 미성년자 시청 불가 영상에 대한 필터링 시스템의 단점을 보완하는 것을 목표로 한다. 현재 유튜브의 영상 검열 시스템은 사용자의 신고 혹은 운영자의 모니터링을 통한 수동 검열로 이루어진다. 이러한 방식은 새로 업로드된 영상을 즉각적으로 필터링 할수 없으며 사용자의 신고를 받거나 운영자의 모니터링에 의해 검열 되기 전까지 청소년들에게 무방비 상태로 노출된다. 이를 방지하기 위하여 영상이 업로드되기 전에 사전 필터링을 하여 가이드라인(유튜브 커뮤니티 가이드라인, 방송통신심의위원회)에 위배되는 내용이 영상에 포함되어 있을 경우, 청소년 시청 불가 컨텐츠로 분류한다. 사전 필터링 과정을 통해 청소년에게 유해한 컨텐츠가 노출되는 것을 예방한다.  

유튜브나 다양한 플랫폼에서 적용가능한 영상 필터링 시스템을 구현하는 것이다. 구체적으로는 영상과 음성을 모두 필터링 하는데, 영상 필터링은 선정적이거나 폭력적인 장면, 미성년자들에게 유해한 담배, 술, 마약 등을 적극 권장하는 장면을 감지하는 시스템이다. 또한 음성 필터링은 욕설을 감지하는 시스템이다.

영상 필터링: CRNN 딥러닝 모델을 사용하여 영상 분류 학습을 실시하는데, 선정적이거나 폭력적인 장면, 흡연, 마약, 술을 적극 권장하는 장면들을 데이터셋으로 하여 학습한다. 학습 결과, 유튜브 정책과 한국 방송통신위원회가 설정한 심의 기준에 저촉하는 장면들을 감지하고 업로드에 제한을 두는 것이다. 또한 동영상 해당 감지부분을 출력하여, 업로드하는 이용자에게 제공한다.
음성 필터링: API 또는 Kaldi - Zeroth 딥러닝 모델을 이용해 STT(Speech To Text)를 개발하고, 정확한 텍스트로 출력이 되면 해당 텍스트에서 욕설이 들어가있는지 문맥을 고려한 순환 신경망인 FastText 모델을 이용하여 감지한다. 욕설이 감지되면 업로드에 제한이 된다. 또한 음성에서 해당 감지부분을 출력하여, 업로드하는 이용자에게 제공한다.
이러한 영상과 음성 필터링을 통해, 동영상 플랫폼을 통해 동영상을 시청하는 사람들이 부적합한 영상을 접하지 않게 1차 검열하는 것이 목표이다.


1. 프로젝트 개요
현재 사람들은 유튜브 뿐만 아니라 다양한 플랫폼에서 동영상을 쉽게 업로드하고 그것을 시청하고 있다. 심지어 유튜브 크리에이터, 스트리머, BJ등 다양한 직업들도 파생되었고, 그들의 파급력 또한 상당하다. 그런데, 그러한 웹사이트에 업로드된 영상들 중 미성년자들 뿐만 아니라 일반 성인들에게도 부적합한 영상들이 많고, 이를 제재하거나 차단하는 시스템 자체가 구현이 안되어있기 때문에 이를 굉장히 접하기 쉽다. 따라서 우리는 영상들의 유해성을 탐지하는 기능의 구현 필요성을 느껴, 동영상을 필터링하는 주제를 설정하게 되었다. 우리의 목표는 유튜브나 다양한 플랫폼에서 적용가능한 영상 필터링 시스템을 구현하는 것이다. 구체적으로는 영상과 음성을 모두 필터링 하는데, 영상 필터링은 선정적이거나 폭력적인 장면, 미성년자들에게 유해한 담배, 술, 마약 등을 적극 권장하는 장면을 감지하는 시스템이다. 또한 음성 필터링은 욕설을 감지하는 시스템이다.

2. 배경기술
영상 필터링을 위해서는 먼저 Video Classfication에 해당되는 Deeplearning Model이 필요하고, 학습시킬 데이터셋이 필요하다. Video Classfication에 사용되는 Model은 CRNN모델이다. CRNN모델은 구체적으로 CNN(이미지를 학습시키는 모델)과 RNN(순환 신경망)이 결합된 모델이다. ----------사진------------- 우리는 여러 CRNN모델 중 성능과 학습시간을 고려해 우리에게 적합한 ResNetCRNN을 선택하였다. 학습환경은 AWS Deep Leanrnig AMI를 통해 학습시켰으며, 테스트 환경도 마찬가지로 AWS로 구성된다.

데이터셋은 유튜브 영상에서 수집했으며, 현재 우리가 감지하고자 하는 장면들은 선정적이거나, 폭력적인 장면 그리고 담배, 술, 마약이 지속적으로 노출되는 장면들이기 때문에 이를 데이터셋으로 설정하였다. 

음성 필터링을 위해서는 먼저 STT(Speech To Text)기술이 필요하다. 현재 STT 기술은 네이버, 구글 등 다양한 API가 존재하며, 만약 이 API들의 정확도가 다소 낮다고 판단되면, 직접 Kaldi - Zeroth 모델을 이용하여 학습시킨다. STT가 완료되면, 해당 텍스트에서 욕설을 감지해야한다. 욕설 감지 모델은 RNN을 사용했으며, 현재 FastText를 이용해서 학습시킨 후, 욕설 감지를 진행한다.

제한 요소는 위 과정을 진행하면서 총 3가지가 파악되었다. 
1. 폭력적인 장면의 데이터셋 구성 시 그 종류가 무척 다양하고 방대해서 우리는 2가지로 특정지었다. ( 1. 흉기로 찔리거나 베여서 피가 노출되는 장면 2. 18세 이상 등급 게임 플레이 영상 중 과도하게 피가 많이 노출되는 장면)
2. 욕설을 필터링할 때 정치적 혐오 발언과 인종차별적 발언 등 다양한 욕설이 있었으나, 이에 대한 데이터셋이 부족하고 필터링 기준을 명확하게 내리기가 어려워서 명확한 욕설( 사전에 명시된 욕설, 문맥상 욕설은 포함하지 않음 )만 필터링한다.
3. STT에 대한 API의 정확도가 낮을 시 Kaldi 모델을 통해 학습을 진행해야하는데, 학습을 시킬 수 있는 환경이 현재 로컬에서 마련하긴 힘들어서 AWS 서버를 이용해서 학습을 진행하기로 했다.






1. 선정적이거나 폭력적인 장면 및 술, 담배, 마약이 지속적으로 노출되는 장면이 학습된 Video Classification trained model

2. 욕설 필터링이 가능한 FastText trained model

### 2. 소개 영상

프로젝트 소개하는 영상을 추가하세요

### 3. 팀 소개

1. 20153216 이태훈 - 팀장 (says7869@gmail.com)  

   역할: Video Classification 모델링과 학습 및 AWS 서버를 이용한 전체적인 소프트웨어 설계

2. 20153211 이인평 (jinipyung@gamil.com) 

   역할: Video Classfication, FastText 학습을 위한 데이터셋 구축 및 FastText 모델링과 학습

3. 20153214 이주형 (srlee96@kookmin.ac.kr) 

   역할: STT(Speech To Text) API 적용 및 Video Classfication 데이터셋 구축

4. 20153158 김성수

   역할: Kaldi-Zeroth 모델링과 학습 및 웹페이지와 웹서버 구축

5. 김민재 (minjae103030@naver.com)

   역할: Video Classfication, FastText 학습을 위한 데이터셋 구축 및 웹페이지 디자인 UI 제작

### 4. 사용법

소스코드제출시 설치법이나 사용법을 작성하세요.

### 5. Abstract

My Project's goal is to prevent people who watch youtube or video platform website from watching a nasty videos. So we have to filter about video and voice. Video filter is filtered from CRNN DeepLearning Model. The scene we are trying to filter is either sensational or violent. We also want to include scenes of alchol, arug, and cigarettes. And then voice filter  is filtered through two processes. First we have to convert voice to text by using STT(Speech To text) technology. Second, use fasttext to detect whether the translated text contains swear words. After filtering, If any one is detected, uploading is restricted. Also we tell you where it was detected.


## Markdown을 사용하여 내용꾸미기

Markdown은 작문을 스타일링하기위한 가볍고 사용하기 쉬운 구문입니다. 여기에는 다음을위한 규칙이 포함됩니다.

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

자세한 내용은 [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Support or Contact

readme 파일 생성에 추가적인 도움이 필요하면 [도움말](https://help.github.com/articles/about-readmes/) 이나 [contact support](https://github.com/contact) 을 이용하세요.
