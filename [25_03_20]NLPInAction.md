# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 8. 단어 관계의 시각화.
- "state"나 "city"와의 코사인 유사도를 잉요해서 주 이름과 도시 이름을 찾을 수도 있지만, 단어가 300만개나 되므로 시간이 걸릴 것. 그보다는 미리 만들어진 도시 정보를 활용하는 것이 편할 것. NLPIA 패키지에 미국 도시 정보 자료를 포함.
- ```python
  from nlpia.data.loaders import get_data
  cities=get_data('cities')
  cities.head(1).T
  ```
- GeoCites가 만든 이 자료 집합에는 전 세계 도시의 다양한 정보가 들어 있음. 특히 위도와 경도 정보가 포함되어 있기 때문에 두 도시의 지리적 거리를 구하는 것도 가능. 도시의 지리적 거리를 word2vec 거리와 비교한 그래프를 만드는 것도 재미있겠지만 예제에서는 word2vec거리만 2차원으로 표시. 전 세계 도시 정보에서 미국의 도시들만 추출, 또한 미국 주 정보도 웹에서 다운로드.
- ```python
  us = cities[(cities.country_code=='US')&(cities.admin1_code.notnull())].copy()
  states = pd.read_csv('http://www.fonz.net/blog/wp-content/uploads/2008/04/states.csv')
  states = dict(zip(states.Abbreviation,states.State))
  us['city']=us.name.copy()
  us['st']=us.admin1_code.copy()
  us['state']=us.st.map(states)
  us[us.columns[-3:]].head()
  ```
- 이제 미국 여러 도시의 이름과 그 도시가 속한 주의 이름 및 약자(TX 등)가 갖춰짐. 그럼 이 주 이름과 도시 이름 중 word2vec 어휘에 포함된 것들은 무엇인지 조회.
- ```python
  vocab=pd.npconcatenate([us.city,us.st,us.state])
  vocab=np.array([word for word in vocab if word in wv.wv])
  vocab[:5]
  ```
- 전 세계는 물론, 미국에서도 같은 이름의 도시 존재. 예를 들어 포틀랜드 시는 오리건주에도 있고 메인주에도 있음. 따라서 도시와 그 도시가 속한 주를 연결하는 것이, 다른 말로 하면 도시 벡터를 해당 주 벡터의 정보로 '증강(augumentation)'하는 것이 바람직. word2vec에서 두 단어의 의미를 묶기 위해서는 그냥 해당 벡터들을 더하면 됨. 이것이 벡터 지향적 추론의 위력.