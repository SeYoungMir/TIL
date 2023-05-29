## 스크럼 계획 수립(I)
### 학습 내용
- 스프린트 계획(Sprint Planning)
### 학습 목표
- 스프린트 계획(Sprint Planning)에 포함되는 내용을 학습

### 스프린트 계획(Sprint Planning)
- 스크럼 계획(Scrum Plan) = 스프린트 계획(Sprint Plan)
  - 스크럼은 여러 번 스프린트를 반복함으로써 증분(Increment)을 인도함
  - 스프린트 계획(Sprint Plan)의 내용
    - 스프린트 백로그(Sprint Backlog) : 유저 스토리, 우선 순위, 스토리 포인트, 인수 기준
    - 스프린트 리스크(Sprint Risk)
    - 타임 박스(Time Box)와 스프린트 일정 계획(Sprint Schedulling)
- 스프린트(Sprint)
  - 스프린트를 설정하면 작은 단위의 개발 업무를 단기간 내에 전력 질주하듯이 개발할 수 있음
  - 스프린트(Sprint) = 케이던스(Cadence) = 반복(Iteration) = 시간 상자 주기(Time-boxed Period)
    - 반복 주기, 짧은 프로젝트 관리 주기, 보고 주기
    - 스프린트는 1~4주 내에서 결정함 $\rarr$ 일반적으로 2주가 스프린트의 적절한 기간
    - 스프린트(Sprint) 내에서 스프린트 계획(Sprint Plan),일일 스크럼(Daily Scrum),개발(Development),스프린트 리뷰(Sprint Review),회고(Retrospective) 등의 제품 개발을 수행함
    - 스크럼에서 반복 주기의 기간은 스프린트 계획 회의를 통해 결정하는데, 보통은 1~4주 정도로 수행함
    - 요구 사항이 안정적이고, 개발 팀이 애자일 방법에 대해 지식과 경험이 풍부하다면 2주 정도의 짧은 기간을 스프린트 주기로 함
    - 요구 사항의 변화가 많고, 개발 팀의 역량이 낮다면 4주정도의 기간을 스프린트 주기로 함
- 스프린트 계획 회의(Sprint Planning Meeting)
  - 스프린트 계획 회의(Sprint Planning Meeting)
    - 제품 백로그(Product Backlog)로부터 해당 스프린트에 할당할 스프린트 백로그(Sprint Backlog)를 도출
    - 백로그 항목 정의 기능(Feature),결함(Defect),기술적 작업(Technical Work),지식(Knowledge)
- 스프린트 계획(Sprint Planning)
  - 스프린트 계획의 주도(Own)역할 : 제품 책입자(Product Owner),개발팀(Development Team)
  - 스프린트 계획의 지원 역할 : 스크럼 마스터(Scrum Master)
  - 제품 책입자(Product Owner)는 스프린트 백로그(Sprint Backlog)항목의 우선순위(Priority)를 부여하며, 스크럼 팀 전체는 그것을 이해함
- 타임 박스 설정(Timeboxing)
  - 타임 박스(Time-box) = 스프린트(Sprint)
    - 시간 상자 주기(Time-box Period)는 팀이 목표를 완료할 때까지 지속되는 주기
    - 일반적으로 타임박스는 2주로 정의함
    - 스크럼은 짧은 주기(Short Cycles)를 사용하여 작업을 착수하고, 결과를 검토하며, 필요에 따라 적응해 나감
  - Increment의 구성
    - Backlog
      - Sprint 1~3
    - Backlog&UAT
      - Sprint 4
  - 명확한 결과물을 제공하는 기간이 짧을 수록
    - 작업량(Effort, Work)를 보다 정확하게 예측(Better Estimates)할 수 있음
    - 인도물의 접근 방식과 적합성에 대해 신속한 피드백(Rapid Feedback)을 제공
    - 프로젝트의 전반적인 리스크가 감소(Reduced Risk to Overall Project)
    - 작업의 버퍼(Buffer)를 보다 정확하게 산정하고 합리적으로 시간을 사용할 수 있음
    - 팀에서 필수적인 기능을 먼저 처리하고 다른 기능은 시간이 허락될 때 처리할 수 있음
    - 범위 추가(Score Creep)을 최대한 줄일 수 있음
    - 고객의 만족도(Customer Satisfaction)가 향상됨
    - <table>
    <tr>
        <th>구분</th>
        <th>예측형(Waterfall)</th>
        <th>적응형(Agile)</th>
    </tr>
    <tr>
        <th>확정 요소(Fixed)</th>
        <td>요구사항(Requirements)</td>
        <td>자원(Resources),시간(Time)</td>
    </tr>
    <tr>
        <th><br></th>
        <td>Plan Driven (계획 중심)</td>
        <td>Value Driven(가치 중심)</td>
    </tr>
     <tr>
        <th>가변 요소(Estimated)</th>
        <td>자원(Resources),시간(Time)</td>
        <td>기능(Features)</td>
    </tr>
    <tr>
        <th><br></th>
        <td>요구사항을 확정하고, 요구사항에 따라 자원 투입량 계획과 일정 계획을 수립함<br>요구사항이 바뀌면, 자원 투입량과 일정이 직접적 영향을 받음</td>
        <td>스프린트 기간을 짧게 정의(Time Boxing)하고, 제한된 자원 내에서 개발할 요구 사항(유저 스토리)를 수집함<br>초기 요구사항은 변경될 수 있으며, 증분(Increment)계획에 따라 기능(Feature)을 여러번 나누어 인도함</td>
    </tr>
</table>

