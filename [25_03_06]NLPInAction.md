# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 4. 영역 특화 단어 벡터 모형 생성
##### 영역 특화 word2vec 모형의 훈련
- 먼저 gensim의 word2vec 모듈을 불러옴
  - ```python
    from gensim.models.word2vec import Word2Vec
    ```
- 다음으로 훈련을 위한 몇 가지 매개변수 설정
  - ```python
    num_features=300
    min_word_count=3
    num_workers=2
    window_size=6
    subsampling = 1e-3
    ```
- 훈련을 시행
  - ```python
    model = Word2Vec(token_list,workers=num_workers,size=num_features,min_count=min_word_count,wondow=window_size,sample=subsampling)
    ```
- 말뭉치 크기와 CPU 성능에 따라 다르겠지마느 훈련에 시간이 꽤 걸림. 말뭉치가 작으면 몇 분 만에 끝날 수 있지만 상세한 단어 벡터 모형을 얻으려면 말뭉치의 문장 수가 몇백만 정도는 되어야 함. 단어의 의미를 제대로 포착하려면 말뭉치의 단어마다 그 단어가 다양한 방식으로 쓰인 다수의 견본 필요. 위키백과 말뭉치 같은 큰 말뭉치를 처리 시 시간과 메모리 훨씬 많이 소비.
- word2vec 모형의 훈련은 상당히 많은 메모리 요구. 궁극적으로 필요한 것은 은닉층의 가중치 행렬. 훈련을 마치고 단어 모형을 동결하면 불필요한 정보들을 모두 폐기 가능. 그러면 메모리 요구량이 절반. 다음은 신경망에서 불필요한 출력 가중치들을 폐기하는 명령.
  - ```python
    model.init_sims(replace=True)
    ```
- init_sims 메서드는 모형을 동결(freezing)하고 은닉층의 가중치들을 저장, 단어 공동 출현 확률들을 예측하는 출력 가중치들을 폐기. 대부분의 word2vec 응용에서 이 출력 가중치들은 단어 벡터의 일부가 아님. 그러나 이렇게 출력층 가중치들을 폐기하고 나면 모형을 더 훈련할 수 없음.
- 훈련된 단어벡터 모형을 저장해두면 매번 모형을 훈련할 필요가 없으며 그 명령은 다음과 같음.
  - ```python
    model_name= "domain_specific_word2vec_model"
    model.save(model_name)
    ```
- 다음은 저장한 단어 벡터 뫃령을 적재해서 사용하는 예시 코드. 
  - ```python
    from gensim.models.word2vec import Word2Vec
    model_name="domain_specific_word2vec_model"
    model = Word2Vec.load(model_name)
    model.most_smiliar('radiology')
    ```