# 2. 더 깊은 학습: 신경망 적용
## 6. 단어 벡터를 이용한 추론: word2vec 활용
### 2. 단어 벡터
#### 8. 단어 관계의 시각화.
- ```python
  import seaborn
  from matplotlib import pyplot as plt
  from nlpia.plots import offline_plotly_scatter_bubbl
  df = get_data('cities_us_wordvectors_pca2_meta')
  html = offlin_plotly_scatter_bubble(df.sort_values('population',ascending=False)[:350].copy().sort_values('population'),filename='plotly_scatter_bubble.html',x='x',y='y',size_col='population',text_col='name',category_col='timezone',xscale=None,yscale=None,layout={},marker={'sizeref':3000})
  ```
- 300차원 단어 벡터를 2차원으로 표시하려면 당연히 차원 축소가 필요. 여기서는 PCA를 사용. 300차원을 2차원으로 압축하는 과정에서 정보가 소실될 수밖에 없는데, 정보 소실을 줄이는 데는 입력 벡터에 담긴 정보의 범위를 좁히는 것도 도움. 지금 예제에선 도시와 관련된 단어 벡터들만 포함함으로써 입력의 정보 범위 축소. 이는 TF-IDF나 BOW 벡터를 계산할 때 말뭉치의 영역이나 주제를 제한하는 것과 유사.
- 정보량이 더 많고 좀 더 다양한 주제의 벡터들의 차원을 축소해야 하는 경우에는 t-SNE같은 비선형적인 내장 알고리즘이 필요. 이후에 t-SNE와 기타 신경망 기법들을 소개
