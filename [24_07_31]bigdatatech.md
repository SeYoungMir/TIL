# 부록 - 유용한 라이브러리
## 2. 파이참(PyCharm) 사용
### 4. 파이참 설정을 원하는 대로 변경
2. 에디터의 외관 변경
   - 메뉴에서 [PyCharn]$\rarr$[Preferences]를 선택. [Preferences]화면에서 [Editor]$\rarr$[General]$\rarr$[Appearance]를 선택 시 외관을 변경할 수 있는 화면 출력. 예를 들여 공백을 출력하고 싶을 때에는 'Show whitespaces'에 체크
3. PEP8 위반 경고 레벨
   - 파이참은 파이썬 표준 콘텐츠 코딩 규약인 PEP8 위반 경고를 출력해줌, 기본값으로  설정된 경고 레벨이 너무 낮으므로 1단계 올려서 'Warning'으로 설정하는 것이 좋음.
   - 메뉴에서 [PyCharm]$\rarr$[Preferences] 를 선택, [Preferences]창을 염. [Editor]$\rarr$[Inspections]를 선택
   - 오른쪽 목록에서 [Python] 드롭 다운을 열고, [PEP8 coding style violation]을 선택. [Weak Warning]을 [Warning]으로 변경
   - [PEP8 coding style violation]아래에 있는 [PEP 8 naming convention violation] 레벨도 동시에 함께 올려줄 것. [Apply] 버튼을 클릭해 적용.