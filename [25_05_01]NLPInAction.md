# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 10.doc2vec을 이용한 문서 유사도 추정
- 문서 벡터 훈련
  - doc2vec 문서 벡터들을 형성하도록 모형을 훈련하는 방법은 단어 벡터를 위한 훈련과 유사.
  - 다음은 gensim 패키지에 있는 doc2vec을 위한 함수들을 사용, 문서 벡터들을 만드는 방법 예시 코드
  - ```python
    import multiprocessing
    num_cores = multiprocessing.cpu_count()
    from gensim.models.doc2vec import TaggedDocument,Doc2Vec
    from gensim.utils import simple_preprocess
    corpus = ['This is the first document...',...,'another document...']
    training_corpus = []
    for i, text in enumerate(corpus):
        tagged_doc = TaggedDocument(simple_preprocess(text),[i])
        training_corpus.append(tagged_doc)
    model = Doc2Vec(size=100,min_count=2,workers=num_cores,iter=10)
    model.bulid_vocab(training_corpus)
    model.train(training_corpus,total_examples=model.corpus_count,epochs=model.iter)
    ```
- RAM이 충분치 않으며 문서의 수를 미리 알고 있다면(즉, 말뭉치 객체가 반복자나 생성기(generator)가 아닌 고정 길이 자료 구조라면),training_corpus를 파이썬의 목록 대신 미리 할당된 NumPy배열로 두는 것이 나음.
  - ```python
    training_corpus=np.empty(len(corpus),dtype=object);
    
        ... training_corpus[i]=...
    ```