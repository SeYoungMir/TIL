# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축
#### 5. 어휘 정규화
- 가장 널리 쓰이는 어간 추출 알고리즘으로는 포터 어간추출기와 스노볼 어간 추출기를 들 수 있음. 
- 포터 어간 추출기는 컴퓨터 과학자 마틴 포터의 이름을 딴 것이고, 스노볼 어간 추출기 역시 포터가 자신의 포터 어간 추출기를 좀 더 개선해서 만든 것. 포터는 자신의 긴 경력의 상당 부분을 어간 추출기를 문서화하고 개선하는 데 바침. 이는 이 어간 추출기들이 정보 조회(키워드 검색) 에서 대단히 가치가 있음. 이 어간 추출기들은 우리의 단순한 정규 표현식보다 훨씬 복잡한 규칙들을 구현한 덕분에 복잡한 영어 철자 규칙과 단어 어미 규칙을 잘 처리. 다음은 포터 어간 추출기 사용 예
- ```python
  >>> from nltk.stem.porter import PorterStemmer
  >>> stemmer = PorterStemmer()
  >>> ' '.join([steammer.stem(w).strip("'")for w in "dish washer's washed disges".split()])
  ```
- 참고로 포터 어간 추출기는 앞의 정규 표현식 어간 추출기처럼 후행 아포스트로피(')를 유지. 이 예제에서는 미리 아포스트로피를 명시적 제거.
- 소유격 단어와 비소유격 단어를 구분할 필요가 있을때에는 아포스트로피를 유지하는 것이 바람직. 소유격 형태의 고유 명사도 많으므로, 그런 이름들을 다른 보통명사와 다르게 취급해야 한다면 아포스트로피를 유지해야 함.
  - 포터 어간 추출기를 줄리아 멘차베스라는 사람이 순수 파이썬으로 구현한 코드를 공유했음(https://github.com/jedijulia/porter-stemmer/blob/master/stemmer.py)
  - 포터 어간 추출 알고리즘은 크게 여덟 단계로 구성. 
    - 1. 단어 끝의 "s"와 "es" 처리.
    - 2. 단어 끝의 "ed","ing","at"을 처리
    - 3. 단어 끝의 "y" 처리
    - 4. "ational","tional","ence","able" 같은 '명사화'접미사 처리
    - 5. "icate","ful","alize"같은 형용사화 또는 동사화 접미사 처리
    - 6. "ive","ible","ent","ism"같은 형용사화 또는 명사화 접미사 처리
    - 7. 그래도 남아있는 어미 "e"제거
    - 8. 후행 이중 자음들을 처리(어간이 하나의 "l"로 끝나야 하는 단어 등.)