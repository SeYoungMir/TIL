# 1.NLP 기초.
## 1. 사고의 단위: NLP 개요
### 4. 컴퓨터 입장으로 언어 읽기 
#### 3. 간단한 챗봇 - 이어서
- 코드 첫 줄의 정규 표현식에는 수많은 논리(logic)가 밀집되어 있음.
- 이 정규 표현식은 놀랄 만큼 다양한 인사말을 인식, 그러나 "Morning"의 오타인 "Manning"을 인식하지는 못하는데, 이는 NLP가 어려운 이유 중 하나. 기계 학습과 의료 진단 검사 분야에서는 이런 문제를 거짓 음성(가음성)분류 오류(false negative classification error)라고 부름. 이 정규 표현식은 사람이라면 말하지 않을 몇 가지 문장도 인사말로 받아들임. 이는 거짓 양성(가양성)오류에 해당.
- 거짓 양성도 거짓 음성과 같이 정확도를 떨어뜨리는 예시 중 하나, 거짓 음성 오류와 거짓 양성 오류가 모두 있다는 것은 이 정규 표현식이 너무 느슨함과 동시에 너무 엄격하다는 뜻.
- 이런 문제점 때문에 챗봇이 다소 둔하고 기계적인 느낌을 줌. 챗봇이 좀 더 사람처럼 보이도록 하려면 챗봇이 인식하는 문구들을 더욱 다듬어야하며, 이는 갈 길이 멈.
- 정규 표현식을 계속해서 확장하고 정련해도 사람들이 사용하는 모든 속어와 오타를 잡아내는 것은 현실적으로 불가능, 정규 표현식을 손수 만드는 것이 챗봇을 훈련하는 유일한 방법은 아니며, 이는 챗봇의 행동을 정밀하게 제어해야 할 때나 유용.
- 챗봇은 사용자의 말에 반응해서 뭔가를 출력해야 하므로, 출력 생성기를 추가할 필요가 있음.
- 파이썬의 문자열 서식화(포메팅)기능을 사용, 챗봇의 응답을 위한 '틀(template)'을 생성.
- ```python
  my_names = set(['rosa','rose','chatty','chatbot','bot','chatterbot'])
  curt_names = set(['hal','you','u'])
  greeter_name=''

  match = re_greeting.match(input())

  if match:
    at_name = match.groups()[-1]
    if at_name in curt_names:
        print("Good one.")
    elif at_name.lower() in my_names:
        print("Hi {}, How are you".format(greeter_name))
  ```