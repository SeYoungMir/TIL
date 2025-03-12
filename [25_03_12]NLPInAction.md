# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 6. fastText
- 미리 훈련된 fastText 모형을 사용하려면
  - fastText 모형을 사용하는 방법은 구글의 word2vec 모형을 사용하는 방법과 비슷함. 우선, 앞에서 언급한 GitHub 저장소에서 원하는 언어의 모형 압축 파일(링크 텍스트가 bin+text인 것)을 내려받아 적당한 디렉터리에 압축을 품. 그런 다음 파이썬에서 gensim의 FastText 모듈을 이용, 해당 파일들로부터 단어 벡터 모형을 메모리로 호출
  - ```python
    from gensim.models.fasttext import FastText
    ft_model = FastText.load_fasttext_format(model_file='모형 파일 디렉터리')
    ft_model.most_similar('soccer')
    ```
  - gensim의 fastText API는 word2vec 구현과 거의 비슷한 기능 제공. 이번 장에서 word2vec 모형에 사용했던 모든 메서드를 fastText 모형에도 적용 가능.