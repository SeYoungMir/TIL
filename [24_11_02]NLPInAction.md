# 1.NLP 기초.
## 3. TF-IDF 벡터
### 4. 주제 모형화
#### 2. 관련성 순위
- document_tfidf_vector에는 말뭉치의 각 문서를 표현하는 K차원 벡터들이 들어 있음. 이들을 이용해서 간단한 검색 수행.
- 한 벡터 공간의 두 벡터가 얼마나 비슷한지 추정하는 한 가지 방법은 둘의 방향을 보는 것. 각 벡터가 원점에서 특정 방향으로 특정 거리만큼 나아가는 화살표라고 할 때, 비슷한 두 벡터는 비슷한 방향을 가리킴.
- 방향이 비슷한 두 벡터는 둘 사이의 각도가 작으므로 코사인 유사도가 1에 가까움. 두 벡터의 코사인 유사도를 구하는 공식은 다음과 같음.
- $cos\Theta=\frac{A\cdot B}{|A||B|}$
- TF-IDF 값들과 코사인 유사도가 있으면 간단한 문서 검색이 가능. 검색 질의 문구 자체를 하나의 문서로 간주, 그것의 TF-IDF 문서 표현 벡터를 구하고, 말뭉치의 문서 표현 벡터 중 검색 질의 문서 표현 벡터와의 코사인 유사도가 큰 것을 찾아서 순서대로 제시.
- 다음은 해리 말뭉치에 대해 "How long does it take to get to the store?"라는 질의 문구로 검색을 수행하는 예시 코드
    - ```python
      >>> query = "How long does it take to get to the store?"
      >>> query_vec = copy.copy(zero_vector)
      >>> query_vec = copy.copy(zero_vector)
      # 같은 객체를 여러 번 덮어쓰지 않기 위하여

      >>> tokens = tokenizer.tokenize(query.lower())
      >>> token_counts = Counter(tokens)
      >>> for key,value in token_counts.items():
      ...       doc_containing_key=0
      ...       for _doc in docs:
      ...           if key in _doc.lower():
      ...               docs_containing_key+=1
      ...           if docs_containing_key == 0:
      ...               continue
      ...           tf = value/len(tokens)
      ...           idf = len(documents)/docs_containing_key
      ...           query_vec[key]=tf*idf
      >>> cosine_sim(query_vec,document_tfidf_vectors[0])
      >>> cosine_sim(query_vec,document_tfidf_vectors[1])
      >>> cosine_sim(query_vec,document_tfidf_vectors[1])

      ```
- 세 문서의 코사인 유사도들을 보면 첫 문서(0번)가 주어진 질의 문구와 가장 관련성이 큰 문서. 어떤 졸류으 말뭉치라도 이런 식으로 관련 문서 검색을 수행 가능.
- 앞의 예제는 말뭉치의 모든 문서 표현 벡터를 일일이 훑어서 가장 관련성이 큰 문서를 탐색. 이런 선형 검색은 시간 복잡도가 O(N)인 알고리즘.
- 구글을 비롯한 대부분의 검색 엔진은 상수 시간(O(1))으로 검색을  수행, 그 비결은 역색인(inverted index)임. 역색인을 아직 구현할 수는 업ㅄ지만 시험해보기 원한다면 Whoosh라는 파이썬 역색인 구현 패키지를 참고.
- 전통적인 키워드 기반 검색 엔진의 구현 방법을 이야기 하지는 않음. 다음 장에서는 텍스트의 의미를 고려해서 검색을 수행하는 좀 더 최신의 의미론적 색인화 접근 방식을 살펴봄.
  - 예제 코드에서는 주어진 키(토큰)이 어휘집에 없으면 0으로 나누기를 피하기 위해 다음 키로 넘어감. 더 나은 접근 방식은 IDF를 계산 시 항상 분모에 1을 더하는 것. 그러면 분모가 0이 되는 일이 없음. 이런 기법을 가산적 평활화(additive smoothing) 또는 라플라스 평활화(Laplace smoothing)이라고 부름. 일반적으로 이 기법 적용 시 TF-IDF 키워드 기반 검색의 결과 개선.
  - 키워드 검색은 NLP로 할 수 있는 일 중 하나. 최종 목표는 챗봇. 대부분의 챗봇은 검색 기능에 크게 의존.
  - 심지어 검색 기능 하나만으로 응답문을 생성하는 챗봇도 있음. 단순한 색인(TF-IDF)검색 기능으로챗봇을 구현하려면 단순한 말뭉치가 아니라, 의문문(또는 제시문)과 그에 대한 적절한 응답문의 쌍들로 이루어진 훈련 자료가 필요. 사용자가 텍스트를 입력하면 챗봇은 그것에 가장 가까운 제시문을 TF-IDF로 찾음.
  - 검색 엔진이라면 그 제시문 자체를 결과로 출력, 챗봇은 그 제시문과 짝을 이루는 응답문을 반환해야함. 이 문제도 간접층(layer of indirection)을 하나 더 추가함으로써 해결 가능.