## 스크럼 계획 수립(II)
### 학습 내용
- 유저 스토리(User Story)
- 페르소나(Persona)
### 학습 목표
- 유저 스토리의 가치와 작성 방법 이해
- 페르소나의 목적 이해

### 유저 스토리(User Story)
- 유저 스토리(User Story) = 사용자 스토리
  - 유저 스토리는 유저(User) 입장에서 정의한 기능에 대한 간단한 설명
  - 유저 스토리는 한 두 문장으로 구성됨 $\rarr$ 사용자의 언어(사용자가 잘 이해할 수 있는 표현)로 작성하며, 역할과 목표 정도만 표현함
  - 유저 스토리는 작업량 산정(Estimation)의 용도로 사용됨
- 유저 스토리(User Story)의 핵심 구성 요소
  - 역할(Role) : 누가 원하는가?
  - 목표(Goal) : 무엇을 원하는가?
  - 이유(Reason) : 왜 원하는가?
- 스토리 카드(Story Cards)
  - 대화의 증거(Tokens for conversations)
  - 공식 문서가 아님(NOT official documents)
- 유저 스토리(User Story)의 역할
  - 토론(Discussion)
  - 일정 관리(Schedulling)
  - 산정(Estimation)
  - 기능 테스트(Functional testing)
  - 완료 여부 판단(Completion)
- 유저 스토리(User Story) 관리
  - 유저 스토리는 카드 또는 포스트잇에 쓰여짐
  - 유저 스토리는 하나의 스프린트(Iteration, Timebox, Iteration) 안에서 구현하고 테스트함
  - 유저 스토리는 제품 책임자 또는 고객이 작성, 고객이 작성하면 좀 더 쉽게 쓸 수 있음
  - 유저 스토리를 만들기 위하여 자주 고객을 만날 수 있어야 함
  - 기능(Feature) 관련 유저 스토리는 인수 테스트(Acceptance Test)를 포함함
- 애자일 WBS(Work Breakdown Structure)
  - 테마(Theme) > 에픽(Epic) > 기능(Feature) > 유저 스토리(User Story)
  - 에픽(Epic) : 유저 스토리(User Story)의 상위 개념 $\rarr$ 유저 스토리와 관계된 기능(Feature) 또는 모듈(Module)의 집합
  - 테마(Theme) : 에픽(Epic)의 상위 개념. 서브 시스템(Sub System), 제품 구성 요소, 서비스 등
- 제품 책임자(Product Owner)
  - 제품 책임자(Product Owner)는 전반적인 제품 리더십을 발휘하여 의사결정을 함
  - 제품 전략(Product Strategy), 제품 로드맵(Product Roadmap), 제품 백로그(Product Backlog),이해관계자 관리(Stakeholder Management)
  - 제품 백로그(Product Backlog)로부터 해당 스프린트에 할당할 스프린트 백로그(Sprint Backlog)를 도출한 후에, 팀은 스프린트 내에서 이를 구현할 것을 결정함
  - 제품 책임자(Product Owner)는 우선순위(Priority)에 따라 다음 스프린트에 작업할 백로그(Sprint Backlog)를 선정함
- 기능 책입자(Feature Owner)
  - 개발팀의 팀원은 기능 책임자(Feature Owner)역할을 함
  - 기능 책임자(Feature Owner)는 각 기능을 정의하고, 개발하고, 스스로 검증하고, 관리함
- 프로젝트 초기에는 제품 책임자(Product Owner)가 기능(Feature) 정의를 주도함
- 스프린트(Sprint)를 시작하면, 개발팀(Development Team)의 각 기능 책임자(Feature Owner)가 기능(Feature) 정의를 주도함
- 제품 백로그는 사용자(고객)가 이해하는 언어로 작성해야 하며, 이 목록은 제품 책임자(Product Owner)가 관리함
- 제품 백로그의 구성 요소인 유저 스토리(User Story)에는 역할 (Role),목표(Goal), 이유(Reason)을 기술함
  - 역할(Role) : 누가 원하는가?
  - 목표(Goal) : 무엇을 원하는가?
  - 이유(Reason) : 왜 원하는가?
  - 인수 기준(Acceptance Criteria)
  - 중요도(Importance)
  - 작업량(Estimate)
  - 종류(Type)
- 유저 스토리(User Story)를 효과적으로 수집하려면
  - 고객이 협력적(Collaborative)이어야 함
  - 고객사 담당자가 대표성(Representative)이 있어야 함
  - 고객사가 유저 스토리를 공식적으로 제공(Authorized)해야 함
  - 프로젝트 팀 뿐만 아니라 고객도 열정적으로(Committed)참여해야 함
  - 고객도 제품에 대한 이해(Knowledgeable)를 가지고 있어야 함
- 좋은 유저 스토리가 되기 위한 6가지 조건
  - 독립적임
  - 협상 가능함
  - 사용자와 고객에게 가치가 있음
  - 공수의 추정이 가능함
  - 작음
  - 테스트가 가능해야 함
1. 프로젝트 관리 시스템
- 액터(Actor)
  - 프로젝트 관리자(PM) : 프로젝트 관리의 책임을 지는 사람
  - 팀원(TM) : 프로젝트에서 작업을 하는 사람
1.1 프로젝트 관리자(As a project manager)
<table>
    <tr>
        <th>사용자 스토리 ID</th>
        <th>요구사항</th>
        <th>이유</th>
    </tr>
    <tr>
        <th>1</th>
        <td>프로젝트에 팀원을 추가함</td>
        <td>프로젝트에 팀원이 공수를 입력함</td>
    </td>
    <tr>
        <th>2</th>
        <td>프로젝트에 참여하는 총 공수에 관한 보고서를 볼 수 있음</td>
        <td>반복(Iteation)내에서 목표 일정과 원가를 관리함</td>
    </tr>
</table>
1.2 팀원(As at team menber)
<table>
    <tr>
        <th>사용자 스토리 ID</th>
        <th>요구사항</th>
        <th>이유</th>
    </tr>
    <tr>
        <th>3</th>
        <td>작업별 공수를 기록함</td>
        <td>프로젝트 관리자가 팀원의 공수를 볼 수 있도록 함</td>
    </td>
    <tr>
        <th>4</th>
        <td>주간 공수에 관한 보고서를 볼 수 있음</td>
        <td>본인의 전주 실적과 금주 예상을 검토함</td>
    </tr>
</table>
  
- Adaptive Software Development(ASD)
  - 적응형 소프트웨어 개발 방법론(Adaptive Software Development,ASD)
  - Feature Card
- 애자일(Agile) 방법론의 제품 정의
<table>
    <tr>
        <th>애자일 방법론</th>
        <th>제품의 정의 방법</th>
        <th>학자</th>
    </tr>
    <tr>
        <th>스크럼(Scrum)</th>
        <td>사용자 이야기(User Story)</td>
        <td>켄 슈와버, 제프 서덜랜드</td>
    </td>
    <tr>
        <th>익스트림 프로그래밍(eXtreme Programming,XP)</th>
        <td>사용자 이야기(User Story)</td>
        <td>켄트 백, 에릭 감마</td>
    </tr>
    <tr>
        <th>칸반(Kanban)</th>
        <td>칸반 카드(Kanban Card)</td>
        <td>다이이치 오노(Taiichi Ohno)</td>
    </tr>
    <tr>
        <th>크리스털(Crystal)</th>
        <td>유스 케이스(Use Case)</td>
        <td>앨리스테어 코번</td>
    </tr>
    <tr>
        <th>기능 주도 개발방법론(Feature Driven Development,FDD)</th>
        <td>피처 셋(Feature Sets)</td>
        <td>피터 코드, 제프 드루카</td>
    </tr>
    <tr>
        <th>적응형 소프트웨어 개발 방법론(Adaptive Software Development,ASD)</th>
        <td>피처 카드(Feature Cards)</td>
        <td>짐 하 이스미스</td>
    </tr>
</table>

- 애자일 제품 정의(Agile Product Definition)
  - 모든 애자일 방법론들은 제품을 정의하는 방법을 제시함
    - 고객이 제품의 범위를 결정하는데 적극적으로 참여함
    - 제품 범위는 체계적인 문서보다는 대화 형식으로 제시함
    - 간단하게 속기로 기능을 설명함
### 페르소나(Persona)
- 페르소나(Persona)는 가상의 사용자(User)프로필임
  - 유사한 특성이나 니즈를 가진 사용자 그룹의 표본을 보여주기 위하여 페르소나에는 가상의 개인 정보와 사진이 포함됨
  - 스크럼 팀은 사용자(User)와 이해관계자를 보다 잘 이해하기 위하여 유저 스토리와 작업을 정의할 때 페르소나를 검토함
  - 페르소나에 각 사용자(User)의 역할에 맞는 사진을 추가하고 사용자에게 동기를 부여하는 요소들을 기술함$\rarr$ 이렇게 함으로써 개발 대상(What to develop)과 개발 방식(How to develop)을 보다 구체화할 수 있음
- 페르소나를 에픽(Epic)과 유저 스토리로 발전시킴
- 스크럼 보드에 유저 스토리를 페르소나 별로 구성함
- 페르소나를 정의하는 방법 $\rarr$ 설문과 서베이, 박람회에서 인터뷰하기, 브레인 스토밍 등 