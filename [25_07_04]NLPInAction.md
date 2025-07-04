# 2. 더 깊은 학습: 신경망 적용
## 7. 단어 순서를 고려한 의미 분석: 합성곱 신경망
### 4. 다시 텍스트로
#### 1. 케라스로 합성곱 신경망 구현: 자료 준비
- 그럼 파이썬으로 합성곱 신경망을 구현, 이 예제는 케라스 문서화에 있는 1차원 합성곱 신경망 분류 예제에 기초
- 원래의 예제는 IMDB 영화평 자료 집합, 합성곱 신경망을 훈련해서 주어진 영화평의 감정(긍정적 또는 부정적)을 예측함. 자료 집합의 각 자료점에는 분류명 0 (부정적)또는 1(긍정적)이 붙어 있음. 그러나 여기서는 자료의 전처리 과정도 체험해보기 위해, 케라스가 만들어둔 IMDB 자료 집합 대신 해당 영화평 원본 텍스트로 이루어진 자료를 사용. 자료는 잠시 후에 이야기, 우선 합성곱 신경망에 필요한 ㅇ여러 모듈과 클래스를 호출.
- ```python
  import numpy as np
  from keras.preprocessing import sequence
  from keras.models import Sequential
  from keras.layers import Dense, Dropout,Activation
  from keras.layers import Conv1D, GlobalMaxPooling1D
  ```
- 다음으로, https://ai.stanford.edu/%7eamaas/data/semtiment/ 에서 스탠퍼드 대학교 인공지능 연구팀의 원본 자료 집합을 다운로드. 이 자료 집합은 2011년 논문 Learning Word Vectors for Sentiment Analysis를 위해 만든 것. 내려받은 압축 파일을 적당한 디렉터리에 풀고 내용물을 살펴볼 것. 이 예제는 train/ 디렉터리만 사용, 그 외에도 재미잇는 파일들이 있으니 휴식 겸 자유로이 둘러보아도 좋음.