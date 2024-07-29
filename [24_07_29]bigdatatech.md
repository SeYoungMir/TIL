# 부록 - 유용한 라이브러리
## 2. 파이참(PyCharm) 사용
### 3. 편리한 기능
- 파이참에는 편리한 기능이 굉장히 많음. 몇 가지 소개
1. 코드 자동 정렬
   - 표준적인 코딩 스타일에 따라 형식을 자동으로 가공해주는 기능
   - 메뉴에서 [File] $\rarr$ [New]선택, 새로운 파일 생성.
   - 이어서 'hello.py'라는 이름으로 저장, 다음과 같은 코드 입력
   - ```python
      array = [[1,2,3],
      [4, 5,   6],
      [7, 8 , 9]]
     ```
   - 메뉴에서 [code] $\rarr$ [Reformat Code]를 선택하거나, [Option] + [Command] + [L] 키 입력시 코드 자동 가공.
2. virtualenv 관리
   - 프로젝트를 새로 만들 때 virtualenv(venv)로 만든 환경을 선택할 수도 있으며, 프로젝트 생성한 후에도 이를 변경할 수 있음.
   - 메뉴에서 [PyCharm] $\rarr$ [Preferences]를 선택, [Preferences] 화면에서 [Project(<프로젝트 이름)] $\rarr$ [Project Interpreter]를 선택하면 기존의 virtualenv 환경을 지정하거나 새로운 virtualenv 환경을 생성 가능
   - 어떤 라이브러리가 설치되어 있는지도 확인 가능, 여러 환경을 변경하면서 사용할 수 있는 편리한 기능
3. 타입 힌트
   - 함수 이름 선택 후 [option] + [enter] 키를 누르면 컨텍스트 메뉴 출력. 여기서 [Specify return type in docstring]을 선택
   - 반환 값과 매개 변수의 타입 힌트를 지정하는 서식이 자동 생성. 반환 값은 :rtype:으로 지정하고, 매개 변수는 :param <자료형><이름>: 또는 :type <매개변수명>:<자료형>: 으로 지정.