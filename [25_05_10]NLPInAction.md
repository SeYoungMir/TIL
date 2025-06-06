# 2. 더 깊은 학습: 신경망 적용
## 7. 단어 순서를 고려한 의미 분석: 합성곱 신경망
### 1. 의미의 학습
- 다층 퍼셉트론(multilayer perceptron)이라고도 하는 기본적인 순방향 신경망(feedforward network)은 자료에서 패턴들을 식별하는 능력을 갖추고 있음. 그러나 순방향 신경망은 입력의 성분들에 연관된 가중치들을 통해서 패턴을 발견, 토큰들의 공간적 또는 시간적 관계를 잘 포착하지 못함. 다행히 순방향 신경망은 가장 기초적인 다층 신경망일 뿐, 현재 자연어 처리에 주로 쓰이는 것은 합성곱 신경망과 순환 신경망(그리고 이 둘의 여러 변형)
- 예시의 순방향 신경망의 입력층은 세 개의 토큰을 받음. 입력층의 각 뉴런은 은닉층의 모든 뉴런과 완전히 연결, 각 연결에는 가중치가 부여.
- "See Jim run"의 단어 순서를 바꾼 "run See Jim"을 신경망에 입력 시 이전과는 다른 출력이 발생. 이는 입ㅊㅍ력 성분마다 부여된 연결 가중치가 서로 다르기 때문
- 순방향 신경망은 이처럼 같은 단어들이 서로 다른 순서로 배열된 문장들로부터 특정한 관계들을 학습 가능. 그러나 토큰의 수가 길어지고 문장이 더 길어지면 모든 가능한 단어 순서 조합의 수도 폭발적으로 증가, 사실상 처리 불가능한 수준이 됨. 다행히 순방향 신경망 외에도 여러 신경망 존재