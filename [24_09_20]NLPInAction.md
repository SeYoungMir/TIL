# 1.NLP 기초.
## 2. 단어 토큰화
### 2. 토큰 생성기를 이용한 어휘 구축
#### 3. 토큰 개선
- 때에 따라서는 문장의 단어들을 공백 문자 이외의 문자로 구분하는 것이 나을 수 잇음. 예를 들어 현재의 토큰 생성기는 문장 끝의 마침표가 들러붙은 "26."을 하나의 토큰으로 간주.
- 이런 문제를 해결하려면 공백 문자뿐만 아니라 마침표나 쉼표, 따옴표, 세미콜론 같은 문장 부호들을 토큰을 구분하는 문자로 사용해야 함. 심지어는 하이픈(대시)을 구분자로 사용해야 할 수도 있음. 그러나 이런 문장 부호를 다른 단어들처럼 독립적인 토큰으로 다루어야 할 때도 있고, 문장 부호들을 아예 제거하는 게 나을 수도 있음.
- 앞의 예제에서 문장의 마지막 의미 단위인 "26"에 문장 끝의 마침표가 붙어서 "26."이라는 그리 바람직하지 않은 토큰이 만들어짐. 이런 후행 마침표는 NLP 파이프라인의 이후 단계들을 혼란에 빠뜨릴 위험이 있음. 예를 들어 일관된 단어 철자에 기초해서 비슷한 단어들을 하나의 그룹으로 묶으려 하는 어간 추출 단계에서 이런 후행 마침표가 나쁜 영향을 미칠 수 있음.
- 다음은 후행 마침표 없이 토큰들을 산출하는 한 방법을 보여주는 예제 코드
- ```python
  >>> import re
  >>> sentence = """Thomas Jefferson began building Monticello at the age of 26."""
  >>> tokens = re.split(r'[-\s.,;!?]+',sentence)
  >>> tokens
  ```
- 앞에서 말했듯 여기서는 정규 표현식이 자주 등장. 제 1장에서 처음 보았을 때보다 정규 표현식이 덜 생소함. 정규 표현식을 좀 더 공부하기위해서는 뒤쪽의 부록을 참고.
- 예제의 정규 표현식 설명
  - 위의 정규 표현식이 작동하는 방식은 다음과 같음. 
  - 대괄호 ([와  ])는 주어진 텍스트가 부합해야 할 문자들의 집합을 지정. 이를 문자 부류(character class)라고 부름. 오른쪽 대괄호 (])다음의 더하기 기호(+)는 주어진 문자 부류의 문자들(대괄호 쌍 안에 지정된 문자들)이 하나 이상 부합해야 함을 뜻함. 문자 부류 안의 \s 는 키보드에서 스페이스바나 탭 키, Enter 키를 눌렀을 때 입력되는 문자들 같은 다양한 공백 문자들을 대표.
  - 다른 말로 하면 r'[\s]'라는 문자 부류는 r'[ \t\n\r\f\v]'와 같고. 여기서 제일 앞은 빈칸. \t는 수평 탭, \r는 캐리지 리턴(carriage return),\n은 새 줄(newline),\f는 폼피드(form-feed),\v는 수직 탭 문자에 해당.
  - 예에서는 쓰이지 않았지만 문자 부류에서 문자 범위 지정 가능. 문자 범위(character range)는 문자 부류 안에서 특정 범위의 문자들을 간결하게 지정하는 수단. 예를 들면 r'[a-z]'는 모든 소문자를, r'[0-9]'는 0에서 9까지의 십진 숫자들을 뜻함.
  - 한 문자 부류에 여러 개별 문자와 문자 범위를 함께 쓸 수 있는데 예를 들면 r'[_a-zA-Z]'는 밑줄 문자나 영문 소문자, 대문자와 부합.
