# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 6. fastText
- 페이스북의 연구자들은 word2vec의 개념에서 출발, 새로운 방식의 모형 훈련 알고리즘을 고안. word2vec은 한 단어의 주변 단어들을 예측, 페이스북이 제시한 fastText라는 이름의 새 알고리즘은 각 단어를 n문자 그램들로 분할해서 한 n문자 그램의 주변 n문자 그램들을 예측. 예를 들어 단어 "whisper"를 2문자 그램들과 3문자 그램들로 분할.
- fastText는 모든n문자 그램에 대한 벡터 표현 훈련을 훈련, "모든" n문자 그램에는 단어, 철자가 틀린 단어, 부분 단어는 물론 개별 글자들도 포함. 이 접근 방식의 장점은 드물게쓰이는 단어들을 원래의 word2vec보다 훨씬 잘 처리
- fastText 알고리즘을 발표하면서 페이스북은 294개의 언어에 대해 미리 훈련한 fastText 모형들을 공개. 다양한 언어의 단어 벡터 모형을 페이스북 연구팀의 GitHub 저장소에서 내려받을 수 있음. 심지어 소수의 독일인만 사용하는 언어 모형도 있음 .페이스북이 제공하는 미리 훈련된fastText 모형들은 각각 해당 언어의 위키백과 말뭉치로만 훈련되었기 때문에, 어휘와 모형의 정확도가 어휘마다 다름.