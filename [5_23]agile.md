## 적응형 라이프사이클(I)
### 학습 내용
- 적응형 라이프 사이클 개요
- 반복형(Iterative)라이프 사이클
- 증분형(Incremental) 라이프 사이클
### 학습 목표
- 적응형 라이프 사이클의 종류를 설명할 수 있다.
- 반복형(Iterative) 라이프 사이클의 목표와 특징을 설명할 수 있다
- 증분형(Incremental) 라이프 사이클의 목표와 특징을 설명할 수 있다.
### 적응형 라이프 사이클 개요
- 예측형 라이프사이클 vs 적응형 라이프 사이클
  - 예측형이든 적응형이든 모든 프로젝트는 프로세스가 존재함
  - 표준 프로세스
    - 분석(Analysis)
    - 디자인(Design)
    - 개발(Code)
    - 테스트(Test)
  - 적응형은 예측형보다 주기가 더 짧음
  - 예측형 라이프 사이클(Predictive Life Cycle) = 폭포수 모델(Waterfall Model) = 중량 프로세스(Heavy Process)
    - 예측형 라이프 사이클(Predictive Life Cycle)은 체계적인 계획에 기반하여 예측 가능한 프로세스를 제시
    - 검증(Verification)과 검수(Validation)와 같은 통제 프로세스가 포함
  - 적응형 라이프 사이클(Adaptive Life Cycle) = 애자일(Agile) = 경량 프로세스(Light Process)
    - 적응형 라이프 사이클(Adaptive Life Cycle)은 체계적인 프로세스보다는 개인의 역량(Skills)에 의존함
    - 문서보다는 대화를 중요시 하며, 완벽한 산출물의 구현보다 보여줄 수 있는 작동 가능한 중간 결과물을 보여줌
    - 단기적인 목표를 달성하기 위한 간단한 프로세스를 제시
  - 예측형보다 적응형의 장점
    - 가시성(Visibility)
    - 변경에 유연한 대응(Adaptability to Change)
    - 사업적 가치 실현(Business Value)
    - 리스크(Risk)
<table>
    <tr>
        <th>구분</th>
        <th>예측형 라이프 사이클(Predictive Life Cycle)</th>
        <th>적응형 라이프 사이클(Adaptive Life Cycle)</th>
    </tr>
    <tr>
        <th>적용 환경</th>
        <td>기술 및 요구사항의 불확실성이 낮을때</td><td>기술 및 요구사항의 불확실성이 높을 때</td>
    </tr>
    <tr>
        <th>요구사항</th>
        <td>프로젝트 초기(착수,계획)</td>
        <td>실행 단계에 구체화</td>
    </tr>
     <tr>
        <th>초점</th>
        <td>Process Driven</td>
        <td>Human Driven</td>
    </tr>
    <tr>
        <th>인도물</th>
        <td>프로젝트 종료 시점에 하나의 제품과 서비스 제공</td>
        <td>프로젝트 실행 중 중간 산출물을 여러번 나누어 인도</td>
    </tr>
    <tr>
        <th>변경에 대한 인식</th>
        <td>변경을 최대한 제한함</td>
        <td>변경을 실시간으로 반영함</td>
    </tr>
    <tr>
        <th>이해관계자 참여</th>
        <td>사전에 정해진 마일스톤 시점에 참여</td>
        <td>프로젝트 실행 중 지속적으로 참여</td>
    </tr>
    <tr>
        <th>업무 수행</th>
        <td>관리자 주도 명령과 통제(개인 단위로 업무 수행)</td>
        <td>Self Organization 팀(팀 중심 업무 수행)</td>
    </tr>
    <tr>
        <th>조직</th>
        <td>Functional Team(분업화되고 역할이 한정)</td>
        <td>Cross Functional Team(T 자형 인재,1인 다역)</td>
    </tr>
    <tr>
        <th>성공의 척도</th>
        <td>계획 준수</td>
        <td>고객 가치 전달</td>
    </tr>
</table>
<table>
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
        <th>형태</th>
        <td>Plan Driven(계획 중심)</td>
        <td>Value Driven(가치중심)</td>
    </tr>
    <tr>
        <th>가변요소(Estimated)</th>
        <td>자원(Resources),시간(Time)</td>
        <td>기능(Features)</td>
    </tr>
    <tr>
        <th>특징</th>
        <td>요구사항을 확정하고, 요구사항에 따라 자원 투입량 계획과 일정 계획을 수립함<br>요구사항이 바뀌면, 자원 투입량과 일정이 직접적 영향을 받음</td>
        <td>스프린트 기간을 짧게 정의(Time Boxing)하고, 제한된 자원 내에서 개발할 요구사항(유저 스토리)을 수집함<br> 초기 요구사항은 변경될 수 있으며, 증분(Increment) 계획에 따라 기능(Feature)을 여러 번 나누어 인도함</td>
    </tr>
</table>

  - 인도 주기와 변경의 정도에 따른 Approach 구분
<table>
    <tr>
        <th>구분</th>
        <th>낮다</th>
        <th>변경의 정도(Degree of Change)</th>
        <th>높다</th>
    </tr>
    <tr>
        <th>높다</th>
        <td>증분형(Incremental)</td>
        <td><br></td>
        <td>애자일(Agile)</td>
    </tr>
    <tr>
        <th>인도 횟수(Frequency of Delivery)</th>
        <td><br></td>
        <td>상호 연속성이 존재함(Continum)</td>
        <td><br></td>
    </tr>
    <tr>
        <th>낮다</th>
        <td>예측형</td>
        <td><br></td>
        <td>반복형</td>
    </tr>
</table>
<table>
    <tr colspan=5>
        <th>특징(Characteristics)</th>
    </tr>
    <tr>
        <th>접근 방식(Approach)</th>
        <th>요구사항(Requirements)</th>
        <th>활동(Activities)</th>
        <th>인도(Delivery)</th>
        <th>목표(Goal)</th>
    </tr>
    <tr>
        <th>예측형(Predictive)라이프 사이클</th>
        <td>고정됨(Fixed)</td>
        <td>프로젝트 기간 중 한 번만 수행(Performed once for the entire project)</td>
        <td>한 번의 인도(Single delivery)</td>
        <td>원가 관리(Manage cost)</td>
    </tr>
    <tr>
        <th>반복형(Iterative) 라이프 사이클</th>
        <td>역동적(Dynamic)</td>
        <td>정상이 될 때까지 반복됨(Repeated until correct)</td>
        <td>한 번의 인도(Single delivery)</td>
        <td>솔루션의 정확한 개발(Correctness of Solution)</td>
    </tr>
    <tr>
        <th>증분형(Incremental)라이프 사이클</th>
        <td>역동적(Dynamic)</td>
        <td>프로젝트 기간 중 한 번만 수행(Performed once for the entire project)</td>
        <td>여러 번의 더 작은 인도(Frequent smaller Deliveries)</td>
        <td>속도(Speed)</td>
    </tr>
    <tr>
        <th>애자일(Agile) 라이프 사이클</th>
        <td>역동적(Dynamic)</td>
        <td>정상이 될 때까지 반복됨(Repeated until correct)</td>
        <td>여러 번의 더 작은 인도(Frequent smaller Deliveries)</td>
        <td>여러 번의 인도와 피드백을 통한 고객 가치 제공(Customer value via frequent deliveries and feedback)</td>
    </tr>
</table>

### 반복형(Iterative)라이프 사이클
- 반복(Iterations)이란?
  - 일련의 반복적인 주기를 통해 제품을 개발하는 것을 의미
- 반복형(Iterative)라이프 사이클의 특징
  - 프로젝트 초기에 프로젝트 요구사항(Requirement)을 수집하고 범위를 결정함
  - 프로토타입(Prototype)을 통해서 분석(Analyze)와 설계(Design)을 반복
  - 개발(Develop)과 테스트(Test)를 여러 번 반복 수행하여 제품이나 서비스를 구체화하고 개선(Refine)
  - 반복(Iterations)를 통해서 요구사항이 충족되면, 마지막에 한 번 인도(Single Delivery)
  - 프로젝트 팀의 제품 이해도가 높아지면,일상적으로 프로젝트와 시간과 원가 산정치를 수정함
- 반복형(Iterative)라이프 사이클 리스크 완화(Risk Mitigation)
  - 반복형(Iterative) 라이프 사이클이 필요한 경우
    - 프로젝트가 상대적으로 복잡한 경우
    - 잦은 변경이 발생하는 경우
    - 프로젝트 팀과 이해관계자가 프로젝트 범위에 대해서 기대하는 것이 다를 경우
      - 요구사항(Requirement)
      - 프로토타입(Prototype)의 반복
        - 분석(Analyze)
        - 디자인(Design)
      - 구체화와 개선(Refine)의 반복
        - 개발(Build)
        - 테스트(Test)
      - 인도(Deliver)
  - 스토리보드(Storyboard)
    - 스토리보드 기법(Storyboarding)이란?
      - 연속적인 이미지나 도해를 통해 이동 또는 전환 순서를 보여주는 프로토타입 기법을 스토리보드 기법이라고 함
    - 스토리보드 사용 분야
      - 영화
      - 광고
      - 교수법 설계
      - 애자일 소프트웨어 개발
      - 기타 소프트웨어 개발
    - 소프트웨어 개발에서 스토리보드 활용
      - 모형을 사용하여 웹 페이지, 화면 또는 그 밖의 사용자 인터페이스를 통한 탐색 경로를 표시함
  - 프로토타입(Prototypes)
    - 프로토타입(Prototypes) = 시제품 = 작동 모형(Working Model) = 예상 제품의 핵심 요구사항을 갖춘 시범적 모델
    - 고객의 요구사항을 가장 정확하게 확인할 수 있음
    - 프로토타입 제작(Prototyping)은 실제 결과물을 만들기 전에 예상 제품의 핵심 요구사항을 갖춘 시범적인 모델(작동 모형)을 만들어 제공함으로써, 요구사항에 대한 조기 피드백(Early feedback on requirements)를 확보할 수 있는 방법임
    - 프로토타입은 유형의 모형이므로 이해관계자가 요구사항 요약서를 놓고 토론하는데 그치지 않고 최종 제품의 모형으로 실험(experiment with a model of the final product)할 수 있는 기회를 제공함
      - 공격적 정교함(Aggressive Details)의 개념을 지원함
    - 요구사항 수집(Collect Requirements)프로세스
      - 가장 정확한 요구사항 수집 방법
    - 리스크 대응 계획 수립(Plan Risk Responses) 프로세스
      - 부정적 리스크(위협)에 대응하는 완화(Mitigation) 전략의 일환
  - 충분한 프로토타입 주기를 거쳐야 함
    - 프로토타입을 1회성으로, 또는 형식적으로 하면 설계 또는 제작 단계로 들어가면 안됨
    - 충분한 피드백 주기를 거쳤을 때 비로소 프로토타입에서 확인된 요구사항들이 설계 또는 제작 단계로 투입되기에 충분히 완벽한 수준에 도달함
  - 요구사항 수집을 위하여 프로토타입 적용 시 주의해야 할 점
    - 고객이 비현실적인 일정과 성능을 기대할 수 있음
    - 내용보다는 외형만을 중심으로 검토할 수 있음
    - 프로토타입에 많은 시간을 낭비할 수 있음
    - 무리한 기대 사항을 갖지 않도록 적절한 수준에서 프로토타입을 작성해야함
      - 모형 제작(Mock-up Creation)
      - 사용자 실험(User Experimentation)
      - 피드백 취합(Feedback Generation)
      - 프로토타입 개정(Prototype Revision)
### 증분형(Incremental) 라이프 사이클
- 증분형(Incremental) 라이프 사이클 = 점층적 라이프 사이클
  - 증분형(Incremental) 라이프 사이클의 특징
    - 증분형 라이프 사이클에서는 사전에 정해진 기간 내에 기능을 계속 추가해 나가는 일련의 반복 과정을 통해 인도물이 산출됨
    - 프로젝트 인도물에는 역량도 포함되어야 하며, 이러한 조치는 일반적으로 최종 반복(Iteration) 이후에 진행됨
      - 최종 반복 단계 이후에만 완성된 것으로 간주되는 필요충분 역량이 인도물에 포함
- 증분형(Incremental) 라이프 사이클의 목표
  - 증분형(Incremental) 라이프 사이클은 여러 번 고객에게 인도(Deliver)함
  - 증분형(Incremental) 라이프 사이클은 제품의 빠른 인도, 즉 속도(Speed)가 가장 중요한 개발 모델임
    - 요구사항(Requirement)
    - 분석(Analyze),디자인(Design),개발(Build),테스트(Test),인도(Deliver)
    - 분석(Analyze),디자인(Design),개발(Build),테스트(Test),인도(Deliver)
    - 분석(Analyze),디자인(Design),개발(Build),테스트(Test),인도(Deliver)
- 반복형(Iterative) vs 증분형(Incremental)
  - 반복형(Iterative) 라이프 사이클의 초점
    - 반복형(Iterative) 라이프 사이클은 프로젝트 리스크 관리(Project Risk Management)에 초점을 맞춤
    - 반복형(Iterative)라이프 사이클은 다른 라이프 사이클에 비하여 상대적으로 일정이 늦어지는 문제가 있음
    - 반복형(Iterative)라이프 사이클에는 프로토타입(Prototype) 프로세스가 포함됨
    - 프로토타입(Prototype)를 통해서 개발 목표를 단순화하여 반복하면, 정확도를 높일 수 있음
  - 증분형(Incremental)라이프 사이클의 초점
    - 증분형(Incremental)라이프 사이클은 프로젝트 일정 관리(Project Schedule Management)에 초점을 맞춤
    - 우선순위(Priority)가 높은 범위를 점진적으로 개발(Incremental Development)하여 더 빨리 인도(Faster Delivery)하는 것을 목표로 함
    - 프로젝트를 스프린트(Sprint)라고 부르는 여러 개의 타임 프레임(Time Frame)으로 나눔
    - 스프린트(Sprint)내에서 우선 순위가 높은 범위를 먼저 개발하여 인도함