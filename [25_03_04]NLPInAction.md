# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 3. gensimn.word2vec 모듈 사용법
- most_similar() 메소드에서, 벡터 덧셈과 뺄셈이 모두 관여하는 예시는 다음과 같으며, king+woman-man=queen을 most_similar()로 재현하느 예시. 뺄셈을 위해 negative 인수를 지정
- ```python
  word_vectors.most_similar(positive=['king','woman'],negative=['man'],topn=2)
  ```
- gensim 라이브러리는 또한 두 단어의 유사도를 계산하는 수단도 제공. similarity() 메서드는 두 단어의 코사인 유사도를 반환
  - ```python
    word_vectors.similarity('princess','queen')
    ```
- gensim에 없는 어떤 단어 벡터 연산을 직접 구현하려면 특정 단어의 단어 벡터 자체에 직접 접근할 수 있어야 함. 접근 방식은 두 가지이며, 하나는 파이썬의 대괄호 구문([])을 사용하는 것이고, 다른 하나는 KeyedVector 인스턴스의 get() 메서드를 사용하는 것. 적재된 단어 벡터 모형 객체는 파이썬 사전 객체처럼 작동. 특정 단어를 키로 해서 해당 단어 벡터에 접근 가능.예제의 단어 벡터 모형(구글 뉴스 문서들로 훈련한)의 경우 개별 단어 벡터는 1 $\times$ 300 차원의 NumPy 행벡터(성분이 300개인 1차원 배열)
  - ```python
    word_vectors['phone']
    ```
- 단어 벡터를 구성하는 수많은 수치 성분의 의미를 직접 파악하는 것도 불가능하지는 않지만, 많은 시간과 노력이 필요. 한 가지 방법은 몇 개의 동의어들을 선택하고 해당 단어 벡터들에서 '장소성'이나 '여성성'같은 주제들에 해당하는 것이 무엇인지 탐색하는 것도 가능.