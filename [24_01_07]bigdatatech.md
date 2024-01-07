# 7. 빅데이터 분석
## 3. 분석 파일럿 실행 1단계 - 분석 아키텍처
### 1. 분석 요구사항
 - 요구사항 1 : 차량의 다양한 장치로부터 발생하는 로그 파일을 수집해서 기능별 상태를 점검
 - 요구사항 2 : 운전자의 운행 정보가 담긴 로그를 실시간으로 수집해서 주행 패턴을 분석
 - 이미 전 장의 빅데이터 탐색을 통해 요구사항 1,2에 대한 기본적인 분석 요건을 해결, 이번 장에서는 기존 요구사항을 좀 더 확장, 빅데이터의 실시간 탐색 및 시각화와 머신러닝을 이용한 데이터 마이닝까지 진행
 - 분석은 단순한 기술적 분석에서 머신러닝 같은 고급 분석에 이르기까지 빅데이터 이전부터 오랜 기간동안 많은 연구가 이루어진 분야
 - 고급 분석 수행에 있어서는 분야별(통계학, 수학, 사회학, 언어학 등) 다양한 사전 지식 필요, 이러한 개론과 이론 최소화, 빅데이터 분석 결험 및 관련 기술 활용에 집중
### 2. 요구사항 구체화 및 분석
<table>
    <tr>
        <th>고급 분석 요구사항 구체화</th>
        <th>요구사항 분석 및 해결 방안</th>
    </tr>
    <tr>
        <td>1. 스마트카 데이터셋을 좀 더 빠르게 탐색 및 분석</td>
        <td>임팔라를 이용 기존 하이브 배치 쿼리를 임팔라의 온라인 쿼리로 실행해 결과 확인</td>
    </tr>
    <tr>
        <td>2. 스마트카 데이터셋의 탐색 결과를 이해하기 쉽도록 시각화</td>
        <td>제플린 이용해 스파크 -SQL로 탐색한 데이터셋을 다양한 차트로 표현</td>
    </tr>
    <tr>
        <td>3. 차량용품 구매 이력을 분석 최적의 상품 추천 목록을 만듦</td>
        <td>머하웃의 추천을 이용해 차량용품 구매 이력을 분석, 성향에 따른 상품 추천 목록을 생성</td>
    </tr>
    <tr>
        <td>4. 스마트카의 상태 정보 분석, 이상 징후 예측</td>
        <td>스파크ML의 머신러닝 기법 중 분류 감독 학습을 통해 이상 징후에 대한 예측 모델을 구성</td>
    </tr>
    <tr>
        <td>5.스마트카 운전자의 마스터 정보를 분석해 고객 군집을 도출</td>
        <td>머하웃과 스파크 ML로 비감독 학습인 군집 분석을 수행</td>
    </tr>
    <tr>
        <td>6. 분석된 결과는 외부 업무 시스템의 RDBMS에 제공</td>
        <td>스쿱의 데이터 익스포트 기능을 HDFS에 저장된 분석 결과를 RDBMS로 전달</td>
    </tr>
</table>