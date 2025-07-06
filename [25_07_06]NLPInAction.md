# 2. 더 깊은 학습: 신경망 적용
## 7. 단어 순서를 고려한 의미 분석: 합성곱 신경망
### 4. 다시 텍스트로
#### 1. 케라스로 합성곱 신경망 구현: 자료 준비
- 파일에서 영화평들을 모두 불러왔다면, 다음으로 할 일은 각 영화평을 토큰화하고 벡터화하는 것. 단어 벡터 생성에는 구글 뉴스로 미리 훈련한 word2vec 단어 벡터들을 사용함. 해당 자료 집합을 NLPIA 패키지를 이용해서 혹은 구글 드라이브에서 직접 내려받기 사용.
- 직접 파일을 내려받았다면 앞의 제 6장에서 했던 것처럼 gensim을 이용해서 압축 파일로부터 벡터들을 적재. 메모리나 시간이 부족하다면 load_word2vec_format 호출 시 limit 인수로 단어 벡터 개수를 제어. 이 인수의 값이 클수록 더 많은 벡터를 사용할 수 있지만, 대신 메모리 요구량과 적재 시간이 증가
- 다음은 자료를 토큰화, 그 토큰들로부터 일단의 단어 벡터들을 생성하는 함수
- ```python
  from nltk.tokenize import TreebankWordTokenizer
  from gensim.models.keyedvectors import KeyedVectors
  from nlpia.loaders import get_data
  word_vectors = get_data('w2v',limit = 200000)
  def tokenize_and_vectorize(dataset):
        tokenizer = TreebankWordTokenizer()
        vectorized_data= []
        for sample in dataset:
            tokens =tokenizer.tokenize(sample[1])
            sample_vecs=[]
            for token in tokens:
                try:
                    sample_vecs.append(word_vectors[token])
                except: KeyError:
                    pass
            vectorized_data.append(samples_vecs)
    return vectorized_data
  ```
- 예시는 단어 벡터 20만개만 적재. 따라서 정보가 어느 정도 손실. 구글 뉴스 word2vec 어휘에는 불용어들이 어느 정도 포함. 이 예제가 적재하는 단어 벡터 20만개에는 "a"같은 흔한 단어들이 대거 빠져 있음. 이것이 이상적인 방식은 아니지만, 합성곱 신경망이 이런 손실 있는 자료에 대해서도 얼마나 잘 작동하는지 가늠할 기회이기도 함.
- 이런 정보의 손실을 피하는 한 방법은 주어진 응용에 관련이 있는 단어들이 좀 더 많이 포함되도록 word2vec 모형을 따로 훈련하는 것. 원본 영화평 자료에는 `<br/>` 같은 HTML 태그들도 많이 있는데, 일반적으로 이런 태그들은 영화평의 감정과 대체로 무관, 제거하는 것이 바람직
- 편의를 위해 목푯값 0(부정적 평)들과 1(긍정적 평)들을 뽑아서 해당 훈련 견본과 같은 순서로 따로 저장. 