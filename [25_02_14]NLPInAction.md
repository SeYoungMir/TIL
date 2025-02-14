# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 1. 의미 기반 질의와 비유
#### 1. 비유 질문
- 어떤 인물의 이름을 다른 인물에 빗대어서 질문하는 경우도 있음. 다음은 그런 질문의 예시
  - Who is to nuclear physics what Louis Pasteur is to germs?
- 구글이나 빙은 물런이고 덕덕고 조차도 이런 질문에는 별 도움이 되지 않음. 그러나 단어 벡터에서는 그냥 "Louis Pasteur"에서 "germs"를 빼고 "physics"를 더하면 됨
  - ```python
    answer_vector = wv['Louis Pasteur'] - wv['germs'] + wv['physics']
    ```
- 음악과 과학 같은 서로 무관한 분야의 인물에 관한 좀 더 까다로운 비유 질문도 생각해 볼 수 있음 예제는 다음과 같음.
  - Who is the Marie Curie of music?
- 위와 같은 질문은 단어 벡터 연산으로 표기하자면 다음과 같음
    - ```python
      answer_vector = wv['Marie Curie'] - wv['science'] + wv['music']
      ```
- SAT나 ACT,GRE같은 표준화된 영어 시험들에는 실제로 이와 비슷한 영어 비유 문제들이 나옴.