# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 8. 단어 관계의 시각화.
- 다음 코드는 주에 대한 word2vec 단어 벡터들을 도시에 대한 단어 벡터들에 더한 결과를 모두 하나의 큰 DataFrame 객체에 저장. 주 이름에 해당하는 단어 벡터가 있으면 그것을 사용, 없으면 주 약자의 단어 벡터를 사용.
- ```python
  city_plus_state=[]
  from c, state, st in zip(us.city,us.state,us.st):
    if c not in vocab:
        continue
    row = []
    if state in vocab:
        row.extend(wv[c]+wv[state])
    else:
        row.extend(wv[c]+wv[st])
    city_plus_state.append(row)
  us_300D = pd.DataFrame(city_plus_state)
  ```
- 말뭉치에 따라서는 단어 관계가 서로 다른 특성들(이를테면 지리적 가까움, 문화적, 경제적 유사성 등)을 대표할 것. 그런 관계들은 훈련에 쓰인 말뭉치에 크게 의존, 따라서 말뭉치를 반영.
- 단어 벡터는 훈련용 말뭉치에 기초해서 단어 관계들을 학습. 예를 들어 금융에 대한 말뭉치로 무형을 훈련 시 "bank"라는 단어의 단어 벡터는 예금이나 대출과 관련된 업무에 관한 단어들의 단어 벡터와 가까울 것. 반면 말뭉치가 지리에 관한 것이라면 "bank"는 강이나 시냇물과 관련이 클 것.
- 그리고 만일 은행을 주로 여성들이 운영하고, 남성들은 강에서 빨래하는 모계 사회에 관한 말뭉치로 훈련 시 bank에 대한 단어 벡터는 그러한 성편향(gender bias)을 반영.
- 다음은 구글 뉴스 기사로 훈련한 단어 모형의 성편향을 비교하는 예시. "man"과 "nurse"의 거리를 "woman"과 "nurse"의 거리와 비교해보면 성편향 확인 가능.
- ```python
  word_model.distance('man','nurse')
  word_model.distance('woman','nurse')
  ```
- 이런 편향을 식별해서 보정하는 것은 편향된 세상에서 작성된 편향된 문서들로 모형을 훈련할 수 밖에 없는 NLP 실무자에게 까다로운 난제.