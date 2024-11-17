# 1.NLP 기초.
## 4. 단어 빈도에서 의미 찾기: 의미 분석
### 1. 단어 빈도에서 주제 점수로
#### 5. LDA 분류기
- 다음은 무게 중심을 계산하기 위한 예제 코드
    - ```python
      mask = sms.spam.astype(bool).values
      spam_centroid=tfidf_docs[mask].mean(axis=0)
      ham_centroid=tfidf_docs[~mask].mean(axis=0)
      ```
- 다음으로 한 무게중심에서 다른 무게중심을 빼서 하나의 벡터를 계산. 이 벡터는 두를 잇는 하나의 직선을 나타냄. 그리고 이 직선에 대한 TF-IDF 벡터들의 투영 길이를 계산
  - ```python
    spamminess_score=tfidf_docs.dot(spam_centroid - ham_centroid)
    ```
- spamminess_score는 햄(비스팸) 무게중심과 스팸 무게중심을 잇는 직선에 상대적인 각 벡터의 길이들을 담은 배열. 그러한 상대 길이는 그 직선을 서술하는 벡터(두 무게중심의 차)에 TF-IDF 벡터를 투영한 길이로 구한 것. NumPy의 벡터화 연산 능력 덕분에 한 번의 .dot() 호출로 4,837개의 벡터에 대한 내적을 모두 계산 가능. 덕분에 파이썬에서 루프로 이들을 일일이 계산할 때보다 속도가 100배 빠름
- 다음 그림은 TF-IDF 벡터들과 문자 메시지 분류를 위한 두 무게중심을 3차우너 산점도(scatter plot)로 표시
- ![alt text](image-5.png)
- 비스팸 무게중심에서 스팸 무게중심을 향하는 화살표는 훈련된 모형을 정의하는 직선에 해당. 녹색 점들은 화살표의 뒤쪽에 있으므로, 무게중심들을 잇는 직선에 투영한 좌표(스팸 점수)는 음수.