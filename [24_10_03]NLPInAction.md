# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축
#### 5. 어휘 정규화
- 대소문자 합치기
  - 문서 전체에서 대소문자 구성을 정규화하는 것이 바람직하다는 점이 확실한 경우에는 원문 텍스트 전체에 대해 lower()를 실행한 후 토큰화를 수행하면 됨.
  - 그러나 그러면 "WordPerfect"나 "FedEx","stringVariableName"같은 낙타 표기법(camel case) 단어를 지능적으로 분할하는 고급 토큰 생성 기능이 무의미. 물론 응용에 따라서는 "WordPerfect" 를 분리하지 않고 하나의 고유한 토큰으로 간주하는 것이 나을 수도 있음. 즉, 대소문자 합치기를 언제 어떻게 적용할 것인지는 개발자의 재량에 달려 있음.
  - 대소문자 정규화를 적용한다는 것은 토큰들을 문법 규칙들과 문장 안에서의 토큰의 위치가 대문자화에 영향을 미치기 이전의 '정규'상태로 되돌리려 하는 것에 해당. 텍스트 문자열의 대소문자 구성을 정규화하는 가장 간단하고도 흔히 쓰이는 방법은 그냥 파이썬의 내장 str.lower()같은 함수로 모든 문자를 소문자로 바꾸는 것. 안타깝게도 이 접근 방식은 그냥 문장의 첫 단어라서 대문자가 쓰인별 의미 없는 대문자 단어들 뿐만 아니라 저자가 의돕적으로 대문자를 적용한 의미 있는 대문자 단어까지도 정규화.
  - 더 나은 대소문자 정규화 방법은 문장의 첫 단어만 소문자로 만들고, 그 외의 모든 단어는 대소문자 구성을 그대로 유지.
  - 문장 첫 단어만 소문자화 하는 방법은 문장 중간에 있는 "Joe Smith"가 "Joe"와 "Smith"로 이루어진 하나의 고유 명사라는 정보를 유지. 또한, 이 방법에서는 어떤 단어가 단지 문장의 처음에 나와서 대문자화 된것이지, 원래부터 고유 명사는 아니라는 점도 파이프라인이 인식 가능. 
  - 예를 들면 "Joe"는 사람 이름, "joe"는 커피를 뜻하는 일종의 속어. 토큰화에서 문장 첫 단어만 소문자화하면 파이프라인이 이 둘을 혼동하지 않음.
  - 마찬가지로 이 접근 방식은 대장장이 등을 뜻하는 "smith"와 고유 명사 "Smith"를 구분. 이를테면 "A word smith had a cup of joe" 같은 문장을 제대로 처리하려면 이런 접근 방식이 필요. 이처럼 문장 첫 단어만 소문자화 하는 세심한 대소문자 정규화를 적용한다고 해도, 하필이면 고유 명사가 문장의 처음에 나오는 경우에는 문제가 생길 수 있음.
  - 이는 바람직한 일은 아니며, 대소문자 구분이 없는 언어에서는 이런 대소문자 정규화가 무의미.
