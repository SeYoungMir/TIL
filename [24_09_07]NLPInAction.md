# 1.NLP 기초.
## 1. 사고의 단위: NLP 개요
### 9. 자연어 IQ - 이어서
- 특화된 지식 영역 안에서 대화를 진행하는 능력을 갖춘 챗봇을 위한 파이프라인을 점진적으로 구축하는 과정에서 두 접근 방식(신경망과 손수 작성한 알고리즘)을 모두 사용해 볼 것. 이러한 과정을 통해서 관심 영역에서 자연어 처리 과제를 수행하는 데 필요한 기술들을 충분히 배울 수 있음. 이 과정에서 우리의 NLP 파이프라인(점점 개선해 나가는 하나의 NLP 파이프라인)이 할 수 있는 일들의 깊이와 너비를 더욱 확장할 착안을 획득 가능.
- 다음 그림은 NLP 파이프라인(NLPIA)이 기존 자연어 처리 시스템들과 비교해서 어느 위치에 있는지 보여줌. 이후의 장들에서는 챗봇에 대해 IQ 테스트 문제나 어려운 질문을 제시해서 지능을 측정하는 시험을 수행.
- ![alt text](image-3.png)

- 챗봇의 여러 구성요소를 점차 구축해 나가며, 하나의 챗봇이 제대로 작동하려면 다음과 같은 NLP 기능을 모두 갖추어야 함.
  - 특징 추출 - 일반적으로 하나의 벡터 공간 모형을 산출
  - 정보 추출 - 사실 관계에 관한 질문에 답하려면 이것이 필요
  - 의미 검색 - 이전에 기록된 자연어 텍스트나 대화에서 뭔가를 배우는 데 필요.
  - 자연어 생성 - 새로운 의미 있는 문장을 작성하는데 필요.
- 기계 학습 기법을 이용하면 사람이 오랜 시간동안 수백 개의 복잡한 정규 표현식이나 알고리즘을 작성해야 가능할 복잡한 행동을 컴퓨터가 하게 만들 수 있음.
- 그냥 사용자가 입력한 문장과 그에 대해 챗봇이 출력할 만한 응답문으로 이루어진 견본(example)들로 컴퓨터를 훈련하면 컴퓨터는 사람이 정규 표현식으로 정의한 패턴들과 비슷한 패턴들에 반응. 그리고 기계 학습이 산출한 언어 '모형', 즉 FSM은 이전에 사람이 직접 만든 것보다 훨씬 나으며, 학습으로 얻은 FSM들은 오타나 철자 오류에 좀 더 유연하게 반응.
- 기계 학습 NLP 파이프라인은 '프로그래밍'하기도 더 쉬움. 대상 언어를 구성하는 기호들의 모든 가능한 용법을 사람이 일일이 예측할 필요가 없음. 
- 그냥 부합하는 견본 문구들과 부합하지 않는 견본 문구들을 훈련 파이프라인에 공급하기만 하면 되고, 부합하는 것과 부합하지 않는 것을 구분할 수 있도록 적절한 분류명(label)을 달아 두기만 한다면, 챗봇은 두 부류의 자료를 구분하는 방법을 배우게됨. 심지어 그런 "분류된(분류명이 달린)"자료를 거의 필요로 하지 않는 기계 학습 접근 방식도 있음.