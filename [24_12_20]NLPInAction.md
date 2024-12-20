# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 5. 잠재 디리클레 할당(LDiA)
#### 2. 문자 메시지 말뭉치에 대한 LDiA 주제 모형
- LDiA는 확률적 알고리즘으로, 단어들을 주제들에 할당할 때 난수에 기초해서 통계적 결정을 내림. 따라서 얻은 주제-단어 가중치가 아래의 가중치와 같다는 보장이 없음. 그래도 크기는 대체로 비슷할 것. 난수 발생 종잣값(seed)을 고정시키지 않는 한, sklearn.LatentDirichletAllocation을(또는 다른 어떤 LDiA 알고리즘을)실행할 때마다 다른 결과가 나옴.
- ```python
  pd.set_option('display.width',75)
  components = pd.DataFrame(ldia.components_.T, index = terms, columns=columns)
  components.round(2).head(3)
  ```
- 가장 많은 주제에 할당된 용어는 느낌표(!), 특히 topic3에 많이 할당. 그 주제에서 큰따옴표(")와 해시 기호(#)은 거의 없는 것이나 마찬가지. 아마도 3번 주제는 수치(#)이나 인용문보다는 격렬한 감정이나 강조에 관한 것일 가능성이 큼. 실제로 확인
- ```python
  components.topic3.sort_values(ascending=False)[:10]
  ```
- 위 주제의 상위 토큰 10개는 누군가에게 뭔가를 하게 할 때, 특히 뭔가를 사게 만들 때 사용할 만한 감정적인 명령문에 쓰이는 종류의 단어들. 만일 이 주제가 비스팸 메시지들보다 스팸 메시지들에서 더 많이 쓰인다면 이 주제는 스팸성과 관련이 있음. 이상의 예에서 보듯이, LDiA의 결과(단어들을 주제에 할당한 수치들)는 사람이 보고 주제를 파악하거나 추론하기 쉬움
- 다음으로 할 일은 이러한 주제 할당 수치들을 이용, 모든 문서(기존 문자 메시지)의 LDiA 주제 벡터들을 계산하는 것. 그런 다음 그 벡터들을 LDA(선형 판별 분석)에 적용, 문자 메시지를 스팸 또는 비스팸으로 분류 하면 됨. 다음은 LDiA의 주제 벡터들을 계산하는 예, 같은 문서들에 대한 SVD와 PCA의 주제 벡터들과도 비교 요함.
- ```python
  ldia16_topic_vectors = ldia.transform(bow_docs)
  ldia16_topic_vectors = pd.DataFrame(ldia16_topic_vectors,index=index,columns=columns)
  ldia16_topic_vectors.round(2).head()
  ```
- 각 메시지에 대한 주제 할당 수치를 보면 0들이 더 많이 있음. 이는 다른 기법의 주제 벡터들보다 이 주제 벡터들이 주제들을 좀 더 깔끔하게 분리한다는 뜻. 이 점이 LDiA 주제 벡터를 상사나 동료에게 설명하기 더 쉬운 이유 중 하나. NLP 파이프라인의 결과에 기초, 사업상의 결정을 내릴 때 이는 중요한 장점.
- 이상에서 보듯 LDiA의 주제 벡터들은 사람이 이해하기 쉬움. 컴퓨터에게도 쉬울지, LDA 스팸 분류기와 얼마나 잘 맞을지 다음에서 확인.