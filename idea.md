
# Long Term Vision

## 활용되어야 할 연구 주제
1. Anomaly Detecion
   - 거동 수상자 (이하 거수자)) 탐지
   - 이상 행동 예측 (월담, 방화, etc)
2. Pedestrian Attribute Recognition
   - 보행자의 속성 인식 (서류 봉투를 들고 걸어가는 적색 롱패딩의 여성)
   - scenario : 식별된 거수자의 상세 불명의 서류철/가방 등의 이슈
3. Object Tracking
   - 식별된 거수자 위치 추적 목표
4. Scene Description
   - 거수자 혹은 이상징후가 포착된 영상에 대한 설명
5. VQA
   - 예측할 수 있는 이상 징후에 대해 미리 지정하고 발생시 알림을 위함
   - 기 발생되거나, 녹화된 영상의 문제상황 검토 
6. Face Detection
   - 차량 내부, 스피드게이트 등의 출입구에서 인허가되지 않은 인적요소 검출 목표
7. Face Recognition
   - 차량 내부, 스피드 게이트 등의 출입구에서 인허가되지 않은 인적요소 식별 목표
8. LLM (agentic AI)
   - 상기 항목들을 종합적으로 판단하는 AGENTIC AI
   - 상기 항목들에 대한 보고서 작성 AGENTIC AI
   - 이상징후 탐지 등의 사건 발생 시 경보음 및 내부망 메신저 활용 메시지 송부 모듈로 활용
   - 거수자 위치 추적을 위한 카메라 틸팅 및 로테이팅 
   - 단일 폐쇄회로카메라 시야외의 객체 추적을 위한 Multi Camera Object Tracking 모듈


## MEMO

1. 적외선 차단 썬팅과 적외선 카메라의 관계

(1) 적외선 차단 썬팅의 작동 원리
 - 대부분의 고급 세라믹 필름이나 금속 코팅 필름은 1000nm ~ 2200nm 근적외선(NIR) 영역을 효과적으로 차단함.
 - 하지만, 열화상 카메라(FLIR)에서 사용하는 중적외선(MIR, 35μm) 및 원적외선(FIR, 814μm) 차단 성능은 상대적으로 낮음.
 - 즉, 필름의 차단 스펙이 근적외선 차단용(NIR 차단) 위주라면, MIR/FIR 대역에서 운전자의 윤곽이 보일 가능성이 있음.

(2) 적외선 카메라의 유형과 파장대별 분석
- 근적외선 카메라(NIR, 850~950nm)
- 	고급 세라믹 썬팅의 경우 차단율 90~99% → 운전자 보이지 않을 가능성이 높음.
- 저가형 썬팅(탄소 기반)은 차단율이 낮아 일부 투과 가능.
- 중적외선(MIR, 3~5μm)
- 금속 및 세라믹 썬팅도 이 영역에서는 차단율이 낮음 → 촬영 가능성이 높음.
- 군용/산업용 적외선 센서에 주로 사용됨.
- 원적외선(FIR, 8~14μm)
- 열화상 카메라(FLIR) 사용 시, 차량 내부의 열 패턴이 보일 가능성 큼.
- 사람이 내뿜는 복사열은 차단이 어렵기 때문에, 윤곽이 보일 수 있음.
- 단, 썬팅 필름의 두께 및 재질에 따라 감쇄될 가능성 있음.

2. 실험 및 연구 가능성

(1) 실험할 가치가 있는가?
- 만약 연구 목적이 썬팅이 운전자의 프라이버시를 실제로 보호할 수 있는가? 또는 적외선 카메라로 실내를 볼 수 있는가? 라면, 연구할 가치가 있음.
- 자동차 썬팅업체들은 “적외선 차단”을 강조하지만, 실제 MIR/FIR 영역 차단 성능을 제대로 검증하는 연구는 부족함.
- 따라서, 썬팅 종류별로 NIR/MIR/FIR 투과율 실험을 하면 의미 있는 연구가 될 가능성이 있음.

(2) 연구 난이도 및 실험 설계
- 실험 대상: 다양한 썬팅 필름(금속 코팅, 세라믹, 나노세라믹 등) 부착 차량.
- 사용 장비:
- 850nm~950nm 근적외선 카메라 (일반 보안용 IR 카메라)
- 3~5μm 중적외선 카메라 (산업용 열화상 카메라)
- 8~14μm 원적외선 카메라 (FLIR 열화상 카메라)
- 테스트 환경: 야간/주간, 거리별 촬영, 썬팅 투과율 비교.

3. 결론 및 연구 필요성 평가

1) 운전자가 적외선 카메라에 보일 가능성
- 근적외선(NIR, 850~950nm): 고급 썬팅 필름 사용 시, 거의 차단됨. → 촬영 어려움.
- 중적외선(MIR, 3~5μm): 대부분의 썬팅 필름이 완벽 차단하지 못함. → 촬영 가능성 높음.
- 원적외선(FIR, 8~14μm, 열화상 카메라): 차량 내부 열 복사로 인해 운전자의 윤곽이 보일 가능성 큼.


circular polarizer filter/film 으로 편광 시킨 결과

- https://www.quora.com/Is-possible-for-a-face-recognition-software-to-work-outside-of-a-moving-car-and-still-recognize-a-face
- https://youtu.be/ChQgV7DlkQo
- https://youtu.be/IHsuiOFOB-c
- https://www.youtube.com/shorts/1NJ7zU2sKdo?feature=share
- https://youtu.be/hcykzT_3KLE?t=277
- 1,000nm(1마이크로미터 또는 μm)부터 약 14,000nm(14μm)까지의 파장에 민감하다. 이것들이 제공하는 데이터를 캡처하고 분석하는 방식을 [열화상 측정](https://ko.wikipedia.org/w/index.php?title=%EC%97%B4%ED%99%94%EC%83%81_%EC%B8%A1%EC%A0%95&action=edit&redlink=1)[이라고 한다](https://ko.wikipedia.org/wiki/%EC%97%B4%ED%99%94%EC%83%81_%EC%B9%B4%EB%A9%94%EB%9D%BC)

- RGB-IR Camera의 가능성 
https://www.instagram.com/autocar_india/reel/DEjieLxIfxq/?locale=zh-TW


###### 설계부터 제조까지 인공지능으로? 두둥탁 

- 저 저 저 저 저 게 어떻게 되냐고


# MORE about anomaly detection

1. MULDE: Multiscale Log-Density Estimation via Denoising Score Matching for Video Anomaly Detection CVPR 2024 
   - github : https://github.com/jakubmicorek/MULDE-Multiscale-Log-Density-Estimation-via-Denoising-Score-Matching-for-Video-Anomaly-Detection
2. An Attribute-based Method for Video Anomaly Detection
   - github : https://github.com/talreiss/accurate-interpretable-vad
3. Diversity-Measurable Anomaly Detection
   - github : https://github.com/FlappyPeggy/DMAD

| 방법론 | 특징 | 사용된 데이터 | 아키텍처 |
|---|---|---|---|
| **MULDE: Multiscale Log-Density Estimation via Denoising Score Matching for Video Anomaly Detection** | - 비디오에서 추출한 특징 벡터를 고정된 분포의 확률 변수로 간주하고, 신경망을 통해 이 분포를 모델링하여 테스트 비디오의 우도를 추정하고, 이를 기반으로 이상을 탐지합니다.<br>- 다양한 노이즈 수준에서의 분포를 모델링하고, 서로 다른 노이즈 수준의 모델을 정렬하는 정규화를 도입하여 하이퍼파라미터 선택을 제거합니다. | - UCSD Ped2<br>- CUHK Avenue<br>- ShanghaiTech 등 5개의 인기 있는 비디오 이상 탐지 벤치마크 데이터셋을 사용하여 실험을 수행하였습니다. | - 비디오 특징 추출 후, 얕은 신경망과 가우시안 혼합 모델(GMM)을 통해 이상 탐지를 수행합니다.<br>- 추론 시에는 특징을 추출하고 이를 신경망과 GMM에 전달하여 최소한의 지연으로 이상을 탐지합니다. |
| **An Attribute-based Method for Video Anomaly Detection** | - 각 객체를 속도와 자세(pose)라는 두 가지 속성으로 표현하고, 밀도 추정을 통해 이상 점수를 계산합니다.<br>- 이러한 단순한 표현만으로도 ShanghaiTech 데이터셋에서 최첨단 성능을 달성하였습니다. | - UCSD Ped2<br>- CUHK Avenue<br>- ShanghaiTech 데이터셋을 사용하여 평가를 수행하였습니다. | - 객체의 속도와 자세를 추출하여 밀도 기반의 이상 탐지를 수행합니다.<br>- 사전 학습된 딥 러닝 표현과 결합하여 성능을 향상시킵니다. |
| **Diversity-Measurable Anomaly Detection (DMAD)** | - 재구성 기반의 이상 탐지 모델에서 정상 패턴의 다양성을 잘 재구성하지 못하는 문제를 해결하기 위해 다이버시티를 측정 가능한 프레임워크를 제안합니다.<br>- Pyramid Deformation Module (PDM)을 설계하여 다양한 정상 패턴을 모델링하고, 재구성된 참조에서 원본 입력으로의 다중 스케일 변형 필드를 추정하여 이상 정도를 측정합니다. | - 감시 비디오와 산업 이미지 데이터셋을 사용하여 실험을 수행하였습니다. | - 정보 압축 모듈(ICM)과 피라미드 변형 모듈(PDM)을 포함한 오토인코더 아키텍처를 사용합니다.<br>- PDM은 재구성 후 변형을 계산하며, PPDM은 재구성 전 변형을 예측합니다. |
