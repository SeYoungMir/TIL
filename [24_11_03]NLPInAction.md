# 1.NLP 기초.
## 3. TF-IDF 벡터
### 4. 주제 모형화
#### 3. 주요 도구 : scikit-learn
- 꽤 많은 예제 코드의 내용 중 대부분은 오래 전에 다른 사람들이 해결한 문제. 보통 scikit-learn 패키지를 사용하면 앞의 예제들에서 얻은 것과 같은 결과를 얻을 수 있음. 적절한 환결을 갖추었을때, 다음 두 명령을 실행하면 scikit-learn 패키지가 설치
- ```bash
  pip install scipy
  pip install sklearn
  ```
- scikit-learn을 이용해 TF-IDF 행렬 생성
- scikit-learn의 TF-IDF를 위한 클래스는 모든 기계 학습 모형이 따라야 할 scikit -learn API를 만족하는 하나의 모형에 해당. 이 클래스는 .fit()과 .transform() 이라는 메서드(그리고 그 둘을 한번에 수행하는 fit_transform() 메서드)를 제공.
- ```python
  from sklearn.feature_extraction.text import TfidfVectorizer
  corpus = docs
  vectorizer = TfidfVectorizer(min_df=1)
  model = vectorizer.fit_transform(corpus)
  print(model.todense().round(2))
  ### .todense() 메서드는 희소 행렬을 보통의 NumPy 행렬로 변환(즉, 정의되지 않은 성분을 0으로 설정) 
  ```
- 이처럼 scikit-learn을 이용 시 단 네 줄의 코드로 말뭉치의 각 문서와 어휘의 각 용어에 대한 TF-IDF 행렬을 생성 가능. 이 행렬(파이썬 구현상으로는 목록들의 목록)의 각 행은 말뭉치의 각 문서에 대한 각 용어의 TF-IDF 수치로 이루어져 있음. 이 예제에서 문서는 총 세 개. 용어(단어)는 총 16개. 어휘에 문장 부호(쉼표와 마침표)는 포함되지 않음.
- 이처럼 문장 부호들을 생략하는 등의 정규화를 수행해서 TF-IDF 모형을 미리 최적화하면 파이프라인 이후 단계들의 계산량 감소 가능.
- 말뭉치가 크다면 절약 효과 증가.