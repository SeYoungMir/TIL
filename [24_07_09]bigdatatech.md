# 9. 목적에 맞는 크롤러 & 스크레이핑 개발 방법
## 2. 공개 데이터 사용
### 1. 공개 데이터란?
3. 공개 데이터 활용
   - 데이터의 구조
     - ```html
       <?xml version= "1.0" encoding = "UTF-8"?>
       <response>
            <header>

                    <resultCode>00</resultCode>
                    <resultMsg>NORMAL SERVICE.</resultMsg>
            </header>
            <body>
                <items>
                    <item>
                        <dataTime></dataTime>
                        (..생략>)

                    </item>
                </items>
                <numOfRows>10</numOfRows>
                <pageNo>1</pageNo>
                <totalCount>22</totalCount>
            </body>
       </response>
       ```
     - 위 구조는 데이터별로 달라, 데이터와 문서를 직접 보면서 스스로 분석. 이를 분석해보면 response>body>items 내부에 미세먼지와 관련된 데이터 포함.
     - 이를 추출하는 프로그램을 만드는 코드 작성