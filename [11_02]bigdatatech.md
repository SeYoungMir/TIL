# 1. 빅데이터 이해하기
## 5. 빅데이터 기술의 변화
* 가트너의 2019년 이머징 기술 하이프 사이클
- 초기 빅데이터 기술은 낮은 비용의 스토리지를 구축하기 위한 솔루션으로 인식
- 빅데이터가 기존 RDBMS의 기술적 한계로 수행하지 못했던 대규모 작업들을 저비용 고효율로 완수하기 시작
- 머신러닝, 텍스트 마이닝 등 고급 분석을 통해 다양한 산업 분야에 깊숙이 관여, 가치를 만들어내기 시작하여 단순 토리지 사이클이 아닌 이머징 기술로 주목
- 가트너의 이머징 기술 하이프 사이클에서 빅데이터는 제외됨.
- 2015년 기점으로 각성기 진입한 빅데이터, 이는 빅데이터가 새로운 이미징 기술들의 제반 기술로 자리 잡았음을 시사함
- 빅데이터 기술의 변화
  - 초기: 대용량 저장소와 배치 처리 기술에 집중
  - 중기 : 실시간 처리 및 온라인 분석 기술들의 개발
  - 최근 : 데이터 마이닝 및 AI의 고급 분석을 위한 전처리와 분석 마트를 구성하는 기술에 집중
- 빅데이터 기술의 ㅏ키텍처 관점
  - 인프라 스트럭처 : 하드웨어 영역으로 저비용의 X86 장비를 대규모(수십~수천대)로 구성해 선형적 확장으로 설계하는 특징.
  - 소프트웨어 플랫폼 : 하둡을 기반으로 오픈소스 생태계 형성, AI로까지 확대
  - IT서비스 : 빅데이터의 기술적/비즈니스적 기대 수준이 커지고, 빅데이터의 구축 기술 뿐 아니라 컨설팅, 유지보수,교육, 데이터 서비스 등의 응용 기술 분야로 확대 발전
<table>
    <tr>
        <th colspan=2>빅데이터 전문 영역</th>
        <th>설명</th>
        <th>국내외 사업자</th>
    </tr>
    <tr>
        <td rowspan=3>인프라스트럭처</td>
        <td>서버</td>
        <td>x86급의 CPU,메모리,디스크 등을 장착한 서버 <br>리눅스 운영체제가 설치된 서버(RedHat,Cent OS 등)</td>
        <td>HP<br>IBM<br>Cisco<br>Dell<br>RedHat등</td>
    </tr>
    <tr>
        <td>네트워크</td>
        <td>대규모 빅데이터 서버및 스토리지 지원을 위한 대용량(10G)네트워크</td>
    </tr>
    <tr>
        <td>스토리지</td>
        <td>대규모 데이터를 저장하기 위한 내외부 스토리지 장치</td>
    </tr>
    <tr>
        <td colspan=2>소프트웨어 플랫폼</td>
        <td>빅데이터의 전방위 기술을 포괄한는 스택 구성(순수 오픈소스 스택 또는 기업 배포판 스택)<br>빅데이터 수집/적재/처리/분석 등의 지원 솔루션<br>빅데이터 시스템 관리 및 모니터링 툴 제공<br>빅데이터 +AI 플랫폼 확장</td>
        <td>Cloudera<br>MapR<br>HortonWorks<br>KT넥스알<br>그루터<br>클라우다인 등</td>
    </tr>
    <tr>
        <td colspan=2>IT 서비스</td>
        <td>빅데이터 컨섩팅 및 구축 이행 <br> 빅데이터전문 운영 및  유지 보수<br>빅데이터 데이터/분석 서비스
        <br>빅데이터 교육 센터 운영 및 인력 양성</td>
        <td>KT DS<br>LG CNS<br>삼성 SDS <br> SK C&C <br> 다음 소프트 등</td>
    </tr>
</table>

  - 빅데이터 기술들은 거대한 오픈소스 소프트웨어 생테계로 만들어져 있음
  - 글로벌 기업들의 과감한 투자와 마케팅으로 상업화 빠르게 진행
  - 빅데이터 글로벌 BIG3 업체는 클라우데라, 호튼웍스,맵알 이있음
- 빅데이터 기술의 핵심에는 하둡이라는 소프트웨어가 있음