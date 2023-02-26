## 학습 내용
1. 애자일 소개
2. 애자일 프로젝트의 특징
## 학습 목표
- 애자일 프로젝트의 의미 이해
- 애자일 프로젝트의 특징 이해, 목표 올바르게 설정
### 애자일 소개
- 프로젝트 관리 방법론
  - 경량 방법론들을 통칭
    - 주로 scrum
  - 애자일(Agile)의 정의
    - 애자일이란? 
      - 신속하고(Fast) 변화에 유연하며(Flexible to Change) 적응적인(Adaptive) 개발을 목표로 하는 다양한 경량(Light) 개발 방법론 전체를 일컫는 총칭
      - 이때 신속하다는 것은 특정 시점의 일정을 의미, 자체가 빠르다는 게 아니라 일정까지 충분하게 개발.
      - 증분(Increment)
        - 여러 하위 프로젝트를 통해서 점진적으로 프로젝트 범위와 일정을 개발하고 프로젝트 산출물을 빠르게 인도(Fast Delivery)함
      - 반복(Iteration)
        - 단기 단위를 채용함으로써 리스크(Negative Risk)를 최소화함
  - 애자일 방법론(Agile Methodology)
    - Agile은 하나의 방법론이 아님
    - Agile은 신속하고 예측 가능하게 개발하기 위한 여러 접근법을 통틀어 일컫는 경량 개발 방법론(Light Development Methodologies)임
    - 대표적인 애자일
      - 스크럼(Scrum)
      - 칸반(Kanban)
      - 스크럼반(Scrumban)
      - XP(eXtreme Programming)
      - 크리스털(Crystal)
      - 린 개발(Lean Development)
      - 기능중심 개발(Feature Driven Development,FDD)등
  - 애자일(Agile)의 오해
<table>
    <tr>
        <th>오해</th><th>올바른 인식</th>
    </tr>
    <tr>
        <td>"만능 해결책"(Silver Bullet)이다.</td>
        <td>애자일은 "만능 해결책"(Silver Bullet)이 아님 <br>프로젝트의 일부 시기 또는 특정 프로젝트의 전체 시기에 적용될 수 있는 선택적 방법론임</td>
    </tr>
    <tr>
        <td>문서화가 없다.</td>
        <td>문서 격식주의가 적을 뿐임(Less Ceremony)</td>
    </tr>
    <tr>
        <td>혼돈을 없애는 표준을 제시해 줄 것이다</td>
        <td>수 많은 애자일 방법론이 존재하며, 애자일에는 표준이 없음 <br>각 조직에 맞게 테일러링(Tailoring)해야 함</td>
    </tr>
    <tr>
        <td>친절하고 명확한 프로세스와 지침을 제시해 줄 것이다.</td>
        <td>애자일은 명쾌한 프로세스를 제시하지 않음<br>애자일 선언문(Agile Manifesto)을 통해서 공포된 4대 가치(4 Value)와 12대  원칙(12 Principles)을 중심으로 "마음 가짐"(Mindset)을 갖추는 것이 중요함</td>
    </tr>
</table>

  - 모든 애자일(Agile)방법론의 공통점
    - 고객이 프로젝트에 적극 참여함(Customer is an active participant)
    - 프로젝트의 리스크를 관리함(Manage Project Risk)
    - 역동적인 일정 관리에 초점을 맞춤(Focus on Dynamic Schedule Management)
    - 반복(Iteration)에 기반한 프로세스를 활용함(Follows Processes based on Iteration)
    - 문서보다는 대화를 주로 사용함(Generally using a dialog,not a document)
    - 간단하고 속기로 기능을 설명함(Recording simple,shorthand feature descriptions)
    - 지속적으로 요구사항을 수집하고 변경을 수용함(Collects requirements continuously)
    - 개발팀의 협업에 초점을 맞춤(Focus on development team's collaboration)
  - 애자일(Agile)의 기대 효과
    - 변화하는 비즈니스 요구에 적응할 수 있으며, 요구사항의 추가, 변경 또는 삭제 결정에 대한 조직의 영향력을 증대시킴(Adaptive to changing business needs, giving the organization more influence over adding, changing, or removing requirements)
    - 빠르고 지속적인 고객 피드백을 통해서 개발 프로세스 전반에 결쳐 의사소통을 개선함, 또는 프로젝트 방향을 정하는 의사 결정에 필요한 중요 정보를 받아 처리하는 사업 담당자에게 권한을 강화(Empowering)함(Ealry and continuous customer feedback improves communication and empowers business owners who can receive and review critical information necessary to make decisions to steer the project throughout the development process)
    - 프로젝트 진척 상황에 대한 높은 가시성과 영향력으로 조기에 문제를 감지함(High visibility and influence over the project progress leading to early indications of problems)
    - 프로젝트를 종료하는 시점에 한 번만의 완제품 인도가 아닌 여러 번의 증분(Increment)인도 방식으로 제품과 프로세스의 낭비를 감소시킴(Incremental delivery rather than a single complete delivery at the end of the project reduces product and process waste)
  - Agile Method & Practices 사용 현황
    - 58%가 Scrum을 활용
    - 26%가 Scrum과 타 methods를 조합
- IT 프로젝트 실패의 교훈
  - 고객은 자기가 진짜 원하는 것을 올바로 제시하지 못함
    - 요구사항(Requirements)과 기대사항(Expectations)을 구분해야함
    - 고객과 개발자 간의 협력을 통해서 요구사항의 불확실성을 줄이고 고객이 수용할 수 있는 대안을 지속적으로 제시해야 함
  - IT 프로젝트 = 팀 플레이
    - T자형 인재(1인 다역)들이 공통된 역량을 갖추어야 함
    - 자기 조직화 팀(Self Organizing Team)이 되어야 함
  - 산출물을 관리해야함
    - 애자일에서도 산출물 문서는 매우 중요함
    - 상황을 정확하게 공유하고 시각화해야 함
  - 요구사항 정의는 프로젝트 팀이 주도해야 함
    - 고객의 요구사항이 재미라고 주장했을 때 안전이라는 "교차 기능 요구사항"(Cross Functional Requirements)를 정의할 수 있어야 함
    - 핵심 요구사항을 프로젝트 전 단계에 걸쳐 발전시켜야 함
  - IT 프로젝트에서 가장 중요한 것은 리스크 관리 역량
    - 프로젝트 목표에 영향을 주는 변수를 파악하고 관리해야 함
    - 리스크 관리의 명확한 원칙이 포함된 프로젝트 리스크 관리 계획을 수립함
    - 리스크 식별 정보, 정성적 분석, 정량적 분석, 예방 계획, 비상 계획이 포함된 리스크 대응 계획을 수립함
    - 리스크 보고서와 대시보드를 관리하고 예방 조치와 비상 조치를 실시함
  - 소프트 웨어 개발 방식의 재검토 필요
    - 성공을 기대하기보다는 실패를 관리
      - Successful:납기 준수, 예산 준수, 만족할 만한 기능 제공
      - Failed: 완성되기 전에 취소되거나 사용하지 않음
      - Challenged: 지연, 예산초과, 필수 기능 제공 미흡
    - 실패율은 항상 존재
    - 실패에 대한 인식 수정
      - 오늘날 디지털 시대에서 Fail이란 무엇인가?
- CHAOS Report
  - 프로젝트의 30%는 완료 전 취소됨 ->Feasibility Study
  - 프로젝트의 54%는 계획보다 예산이 초과됨 -> Cost Management
  - 프로젝트의 66%는 성공적으로 완료되지 못한 것으로 평가되고 있음 ->Quality Management
  - 프로젝트의 90%는 계획보다 일정이 지연된 -> Schedule Management
  - 프로젝트 관리의 우선 순위 
    - Feasibility Study < cost Management < Quality Management < Schedule Management
  - 규모가 클 수록 실패함
  - 규모가 작을 수록 성공함
  - 프로젝트의 리스크 대응 계획이 있는가?
    - 큰 실패를 겪기보다는 작은 실패를 반복하며 큰 실패 회피하는 전략
    - 팀원의 규모, 예산, 등등을 관리하기 힘들기 때문에 분할해서 작게 만들어라
    - 두 달 이내에 성과가 나올 수 있도록 분할하라
  - 애자일의 우선 관리 대상
    - 애자일의 1차적인 목표 = 프로젝트 리스크 관리(Project Risk Management)
      - 프로젝트 리스크 관리를 위한 애자일의 기법은 반복(Iteration)임
      - 리스크 대응과 품질 통제에 유효한 반복(Iteration)프로세스를 개발해야함
    - 애자일의 2차적인 목표 = 프로젝트 일정 관리(Project Schedule Management)
      - 프로젝트 일정 관리를 위한 애자일의 기법은 증분(Increment)
      - 보고 주기(스프린트)이내에 작동 가능한 제품을 릴리스 할 수 있도록 일정을 역동적으로 관리해야 함
- 