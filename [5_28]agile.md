## 스크럼 팀
### 학습 내용
- 스크림 팀의 구성원
- 스크럼 팀의 관리
### 학습 목표
- 스크럼 팀 구성원의 역할과 책임을 명확하게 이해
- 스크럼 팀 관리 방법 이해

### 스크럼 팀의 구성원
- 애자일 조직과 관계된 Agile Manifesto의 3대 원칙
  - 애자일 원칙 1조
    - 고객을 만족
  - 애자일 원칙 5조
    - 동기부여된 개인들 중심
  - 애자일 원칙 11조
    - 자기조직화(Self-Organizing)되어 있는 팀(Team)
- 기능 조직(Functional Organization) vs 애자일 조직(Agile Organization)
- 스크럼 팀(Scrum Team)
  - 긴밀한 상호 협력
    - 제품 책임자(Product Owner)
      - 제품 리더십(Product Leadership)
        - 제품 비전(Product Vision)
        - 유저 스토리(User Story)
        - 제품 백로그 작성과 우선순위 부여
        - 이해관계자 관리
        - 스프린트 목표 제시
        - 인수 기준: 증분의 수락 여부 결정
    - 개발 팀(Development Team)
      - 디자인과 기술 리더십
        - UX 디자인
        - 개발(아키텍처,QA 포함)
        - 자기 조직화(Self-Organization)
    - 스크럼 마스터(Scrum Master)
      - 프로세스 리더십(Process Leadership)
        - 프로세스와 기법 코칭
        - 협업 촉진
        - 조직 변화 유도
- 스크럼 책임 할당 매트릭스
- <table>
        <tr>
            <th>스크럼 역할 구분</th>
            <th>백로그 상세화(Backlog Refinement)</th>
            <th>스프린트 계획(Sprint Planning)</th>
           <th>일일 스크럼(Daily Scrum)</th>
           <th>스프린트 리뷰(Sprint Review)</th>
          <th>스프린트 회고(Sprint Retrospective)</th>
        </tr>
        <tr>
            <th>제품 책임자(Product Owner)
            </th>
            <td>Own</td>
            <td>Own</td>
            <td>Help</td>
            <td>Own</td>
            <td>Own</td>
        </tr>
        <tr>
            <th>개발 팀(Development Team)
            </th>
            <td>Help</td>
            <td>Own</td>
            <td>Own</td>
            <td>Help</td>
            <td>Own</td>
        </tr>
        <tr>
            <th>스크럼 마스터(Scrum Master)
            </th>
            <td>Help</td>
            <td>Help</td>
            <td>Help</td>
            <td>Help</td>
            <td>Own</td>
        </tr>
    </table>

  - Own : 책임을 지고, 주도하는 분야
  - Help : 참여하고 지원하는 분야

- 제품 책임자(Product Owner)
  - 제품 책임자(Product Owner) = 제품 소유자
    - 제품의 가치 극대화를 담당함(Maximize product value)
    - 개발한 최종 제품(End Product)에 궁극적으로 책임짐
    - 제품의 성공(Product Success)을 위하여 리더십을 발휘함
- 훌륭한 제품 책임자(Product Owner)란?
  - 고객의 니즈를 파악하기 위한 활동 지속적으로 수행 $\rarr$ 시장 분석(Market Analysis)
  - 시장에 팔릴 수 있는 제품을 정의하고 ROI를 확보 $\rarr$ 사업 분석(Business Analysis)
  - 고객의 관점에서 제품을 체험하고 분석 $\rarr$ 사용자 경험(User Experience)
  - 제품 백로그(Product Backlog)를 시각화, 스크럼 팀과 공유 $\rarr$ 프로젝트 관리(Project Management)
  - 제품 백로그의 우선순위(Priority)에 대한 주도권을 확보 $\rarr$ 리더십(Leadership)
  - 인수 기준(Acceptance Criteria):증분(Increment)의 수락 여부 결정
- 제품 책임자(Product Owner)의 역할
  - 제품 비전(Product Vision) : 대상 고객(시장)정보와 제품의 가장 중요한 속성, 방향
  - 제품 로드맵(Product Roadmap) : 에픽(Epic) 중심으로 증분형 라이프 사이클과 마일스톤 제시
  - 제품 백로그(Product Backlog) 작성 : 고객의 요구사항을 수집하여 제품 백로그를 시각화하고 팀과 함께 유저 스토리(User Story)로 발전시킴
  - 제품 백로그의 우선순위 (Priority) 부여 : 바로 다음 스프린트에 실행할 유저 스토리 선정
  - 이해관계자 관리 : 이해관계자 참여 유도, 이해관계자와 팀 간 의사소통 전달, 개발팀에게 지시
  - 스프린트 목표(Sprint Goal) 제시 : 스크럼 프로세스를 추적하고 통제
  - 인수 기준(Acceptance Criteria):증분(Increment)의 수락 여부 결정
- 스크럼 마스터(Scrum Master)
  - 스크럼 마스터(Scrum Master) = 전체를 지원하고 관리하는 사람
    - 스크럼 마스터(Scrum Master) = (사실상) 프로젝트 관리자 (Project Manager) = 촉진자(Facilitator) = 서번트 리더(Servant Leader) = 프로젝트 팀 리더 (Project Team Leader) = 팀 코치(Team Coach) = 팀 촉진자(Team Facilitator) = 애자일 코치(Agile Coach)
    - 스크럼 마스터는 프로젝트 전체를 관리하는 역할이지만 프로젝트를 지휘하는 담당자는 아님
    - 오히려 팀원들이 활동하기 편하도록 장애물(Impediments)을 제거하는 역할로 서번트 리더십(Servant Leadership)을 발휘
  - 스크럼 마스터(Scrum Master)의 역할
    - 프로세스와 기법 코칭 : 스크럼 프로세스를 촉진, 팀에 스크럼을 이해시키고 적용 $\rarr$ 선도와 봉사
    - 협업 촉진(Facilitate Collaboration)
      - 제품 책임자 지원 : 백로그 관리, 스토리 평가, 의사소통 개선, 보고
      - 개발팀 지원 : 팀 토론 참여, 팀원 독려, 회고에서 토론 촉진
    - 조직 변화 유도 : 기존 상명하달식 조직 문화를 자기조직화팀(Self Organizing Team)으로 변화시킴
  - 스크럼 마스터의 서번트 리더십(Scrum Master as Servant Leader)
    - 존중(Respect) : 팀원을 존중하는 만큼 성과가 나옴 $\rarr$ 최대한 인간적으로 다른 사람들을 존중
    - 초점(Focus) : 다른 사람들의 위대함에 초점을 맞춤 $\rarr$ 방향을 제시하고 해결할 수 있도록 유도
    - 헌신(Commitment) : 자발적으로 최선을 다함 $\rarr$ 자신의 요구를 내려 놓고 다른 사람을 위해 헌신함
    - 용기(Courage) : 말하기 불편하더라도 진실을 말하는 용기를 발휘함 $\rarr$ 시장과 고객의 요구를 관철하기 위하여 팀원들과 토론할 때 발생하는 갈등을 관리할 수 있어야 함
    - 개방성(Openness) : 정직하고 투명하게 정보를 공유함 $\rarr$ 자신의 약점도 말할 수 있는 솔직함
    - 윤리(Moral) : 모범을 보임으로써 리더십을 행사하고, 도덕적 권위를 유지함
  - 서번트 리더십(Servant Leadership)의 전제 조건
    - 조직의 문화(Culture)
    - 리더의 자질(Leader Attributes)
    - 팔로워의 수용성(Follower Receptivity)
  - 서번트 리더십(Servant Leadership)의 성과(Output)
    - 팔로워의 성과와 성장(Follower Performance and Growth)
    - 조직의 성과(Organizational Performance)
    - 조직 내 사회적 효과(Societal Impact)
   - 힘(Power)의 종류
    - 지위의 힘
      - Formal
      - Reward
      - Penalty
      - Information
    - 개인의 힘
      - Expert Power(중요)
      - Referent Power(강력)
  - 이 때 개인의 힘을 강조하는 것이 스크럼!
- 스크럼 마스터(Scrum Master) $\rarr$ 자기 조직화 팀(Self Organizing Team)을 구축할 수 있도록 도움
  - 개발 시 사용할 수행 방법은 스크럼 마스터가 아닌 개발 팀이 결정
  - 스크럼 마스터가 상세하게 지시를 내리는 것이 아니라, 팀원들이 스스로 결정하면서 자율적인 팀을 만드는 것이 생산성을 향상시키는 열쇠
  - 스크럼에서는 이렇게 자율적으로 움직이는 팀을 자기 조직화 팀(Self Organizing Team)이라고 함
  - 스크럼을 도입한다는 것은 조직 전체가 지시 관리(Command Control)형 문화가 아닌 리더십 협업(Leadership Collaboration)형 문화로 의식 개혁을 해야 하는 것을 의미함
- 스크럼 마스터가 제품 책임자를 위해 하는 일들
  - 스크럼 마스터는 제품 책임자를 다음과 같은 여러 방법으로 도움
    - 목표, 개발 및 제품 도메인을 스크럼 팀의 모든 사람이 이해할 수 있도록 확인
    - 제품 백로그를 효과적으로 관리하기 위한 기술을 찾음
    - 제품 백로그 항목들이 명확하고 간결할 필요가 있다는 점을 스크럼 팀이 이해할 수 있도록 도움
    - 경험적인 환경(empirical environment)에서 사용하는 제품 계획을 이해
    - 최상의 가치를 내기 위해 제품 백로그를 어떻게 조정해야 할지를 제품 책임자가 알고있는지 확인
    - 애자일(Agility)를 이해하고 실행
    - 요청이나 필요에 따라 스크럼 이벤트를 원활하게 진행
- 스크럼 마스터가 개발팀을 위해 하는 일들
  - 스크럼 마스터는 개발 팀을 다음과 같은 여러 방법으로 도움
    - 자기 조직화한 교차 기능 팀으로 거듭나기 위해 개발팀을 코칭(Coaching)함
    - 개발팀이 가치 있는 제품들을 만들어 낼 수 있도록 도움을 줌
    - 개발팀의 개발 진행에 있어 장애 요소들(Impediments)를 제거함
    - 요청이나 필요에 따라 스크럼 이벤트를 원활하게 진행함
    - 스크럼이 아직 완전히 자리 잡지 않고 이해되지 않은 조직 환경에서의 개발팀을 코칭함
- 스크럼 마스터가 조직을 위해 하는 일들
  - 스크럼 마스터는 조직을 다음과 같은 여러 방법으로 도움
    - 해당 조직에 스크럼이 잘 자리 잡을 수 있도록 안내하고 코칭함
    - 조직 내에서 스크럼 실행을 계획함
    - 직원 및 이해 관계자들이 스크럼과 경험적 제품 개발에 대해 잘 이해하고 확립할 수 있도록 도움을 줌
    - 스크럼 팀의 생산성을 향상하기 위한 변화를 만듦
    - 조직에서 스크럼 적용의 효과를 높이기 위해 다른 스크럼 마스터들과 협력
- 개발팀(Development Team)
  - 개발팀(Development Team)
    - 스프린트 계획(Sprint Plan),일일 스크럼(Daily Scrum),개발(Development),회고(Retrospective)의 스프린트 활동에 주도적으로 참여해야 함
    - 팀원 전원이 각자의 전문성과 리더십을 가지고 있어야 함
      - UX 디자인
      - 개발(아키텍쳐, 코딩)
      - QA(Quality Assurance)
    - 자기 조직화 팀(Self Organizing Team)으로 활동해야 함
      - 제품 책임자(Product Owner)로부터 받은 유저 스토리를 작업으로 정의하고, 본인의 작업에 대해서는 권한을 가지고 어떻게 할 지(How to do)결정함
      - 스크럼 보드(Scrum Board)에 스프린트 백로그(Sprint Backlog)를 작성함
      - 빠르게(Quickly) 헌신적으로(Dedicated) 작업함
      - 상호 협력적으로 일해야 하며, 함께 책임짐
      - 작업량(스토리 포인트)을 산정함
      - 반복(Iteration)프로세스를 위하여 제품 책임자 및 스크럼 마스터와 협력함
      - 일일 스크럼(Daily Scrum)에 자발적으로 적극적으로 참여함
### 스크럼 팀의 관리
- 애자일 조직(Agile Organiztion)의 운영
  - 트라이브(Tribe)
    - 스크럼 팀(Squad)여러개
  - 챕터(Chapter)마다 스크럼 마스터가 스크럼 팀 여러개를 돌아다니며 분야 별 기능별 상태 확인
- 스크럼 팀과 PM
  - 애자일에서도 프로젝트 관리자(Project Manager)는 존재함
  - PM(Project Manager)은 외부에서 스크럼 팀을 지원함
    - 애자일 프로젝트를 수행하는 조직에서 PM은 스크럼 팀의 일원이 아님
    - 스크럼 팀(Scrum Team)은 제품 책임자(Product Owner, PO),스크럼 마스터(Scrum Master, SM),개발 팀원(Development Team)으로 구성됨
    - 제품 책임자(Product Owner)나 스크럼 마스터(Scrum Master)는 PM이 아님
  - PM의 정의
    - 예측형(Waterfall)프로젝트에서 PM은 자세히 계획하고,지시하고,통제하는 프로젝트 책임자임
    - 반면에 애자일(Agile)프로젝트에서 PM은 비전을 제시하고, 격려하고, 지원하는 프로젝트 책임자임
    - 규모가 큰 프로젝트에서는 한 명의 프로젝트 관리자(Project Manager,PM)와 여러 명의 스크럼 마스터(Scrum Master,SM)가 존재할 수 있음
    - 원칙적으로 역할을 중복하면 안 됨.제품 책임자(Product Owner),스크럼 마스터(Scrum Master),프로젝트 관리자(Project Manager)는 각각 존재해야 함
    - 그러나 비교적 소규모 프로젝트라면, 역할을 구분하는 것이 무리이기 때문에 PM이 제품 책임자(Product Owner)와 스크럼 마스터(Scrum Master)의 여러 역할을 담당할 수도 있음
  - 스크럼의 사상으로 봤을 때 스크럼 팀(Scrum Team)에서 PM의 역할에 가장 근접한 사람은 스크럼 마스터임
- 스크럼 마스터 vs PM
<table>
    <tr>
        <th>구분</th>
        <th>스크럼 마스터(Scrum Master,SM)</th>
        <th>프로젝트 관리자(Project Manager,PM)</th>
    </tr>
    <tr>
        <th>적응 규모</th>
        <td>3~9명의 스크럼 팀을 관리함</td>
        <td>수십~ 수백명이 참여하는 규모가 큰 프로젝트의 모든 팀 구성원들을 관리함</td>
    </tr>
    <tr>
        <th>목표</th>
        <td>팀원들이 애자일 실무와 프로젝트 타임라인을 따르도록 스크럼 팀을 코치함</td>
        <td>프로젝트의 범위, 일정,예산과 같은 명확한 목표를 달성할 책임이 있음</td>
    </tr>
    <tr>
        <th>범위 관리</th>
        <td>각 스프린트마다 제품 책임자로부터 받은 프로젝트 범위를 보다 구체적인 유저 스토리로 상세화할 수 있도록 스크럼 팀을 도움</td>
        <td>요구사항을 수집하고 프로젝트 범위를 문서화함<br>제품 책임자와 협력하여 프로젝트 범위와 유저 스토리를 정의함</td>
    </tr>
    <tr>
        <th>자원 관리</th>
        <td>자기 조직화하는 팀(Self Organizing Team)을 구축할 수 있도록 도움 <br> 외부의 간섭으로부터 팀을 보호함</td>
        <td>인적 자원의 R&R과 재료 자원의 사양을 정의하고, 프로젝트 자원을 확보하고, 자원 투입량과 원가를 산정함</td>
    </tr>
    <tr>
        <th>의사소통</th>
        <td>스프린트 단위로 스크럼 프로세스를 촉진함<br>스프린트 진도(Sprint Progress)를 모니터링 함</td>
        <td>프로젝트의 착수부터 종료까지 모든 활동을 계획하고 실행하고 통제함 <br>프로젝트 진도(Project Progress)를 관리함</td>
    </tr>
</table>

- T자형 인재(T-Shaped People)
  - T자형 인재(T-Shaped People) = 다방면 전문가 = 다방면 이해자(Generalist) + 전문가(Specialist)
    - 다방면의 전문가 만들기(Generalizing Specialist)$\rarr$애자일 팀원들은 상호 지식을 공유하기 위하여 노력해야 함
    - T자형 인재는 애자일 팀별 서비스 독립성을 위하여 필요함
- 자기 조직화 팀(Self Organizing Team)
  - 스크럼 마스터의 리더십으로 얻어진 효과인 존중,초점,헌신,용기,개방성,윤리 
  - 개발팀은 스스로 일을 구성하고 관리할 수 있는 조직으로 구성되며 이러한 자기직화 권한도 위임받음
  - 그 결과로 얻어진 시너지 효과는 개발팀 전체의 능률과 효과를 최적화함
  - 자기 조직화 팀의 특징
    1. 모든 팀 구성원이 "반복"(Iteration)에 참여함
    2. 획일적인 역할 분담을 지양함
    3. 가능하면 동일 공간(Co-location)에서 일함
    4. 모든 팀 구성원이 프로젝트에 헌신적으로 일함
    5. 규율과 단속을 지양하고, 믿음(Trust)과 권한 부여(Empowerment)를 통해서 스스로 최선을 다함
    6. 변화에 능동적으로 선제적으로 대응함
 - 지시와 통제(Command and Control)
   - 프로젝트 팀이 모두 함께 할 일을 토론하고 정하는 대신에 경영진 또는 프로젝트 관리자가 작업에 담당자를 배정하는 것임
   - 프로젝트 관리자가 프로젝트를 지속적으로 감시하여 차이와 변경사항을 발견함
   - 팀원이 아니라 경영진과 프로젝트 관리자가 필요한 조치를 결정함
 - 자기 조직화(Self-Organizing)
   - 자기조직화 팀에서는 해야 할 일을 모두가 함께 계획함
   - 스프린트 시에는 팀원 스스로 필요한 작업을 찾아서  최선을 다해 실행함
- 개발팀의 크기(Development Team Size)
  - 적절한 개발팀의 크기는 3~9명
  - 최적의 개발팀 크기는 민첩하게 대응 할 수 있도록 충분히 작고, 한 스프린트 안에서 의미 잇는 작업을 끝낼 수 있을 정도로 충분히 커야 함
    - 3명 미만의 개발팀
      - 3명 미만의 개발 팀은 서로 간의 교류가 적기 때문에 결과적으로 적은 생산성을 얻게 됨
      - 작은 규모의 개발팀은 팀 내부에 필요한 기술 역량이 없을 수 있으므로 스프린트를 수행하는 동안 기술적인 제약이 발생하여 출시할 수 있는 기능이 포함된 제품 증분을 배포하지 못할 수도 있음
    - 9명 이상의 개발팀
      - 9명 이상의 개발팀은 너무 많은 상호 협조를 요구함
      - 큰 규모의 개발팀은 경험적 프로세스를 활용하기에는 너무 복잡함
    - 제품 책임자와 스크럼 마스터는 그들이 스프린트 백로그 작업에 참여하지 않는 이상 개발팀 인원수에 포함되지 않음
    - 의사소통의 당사자가 많아지면 이해(Stake)의 충돌과 노이즈(Noise)도 많아짐
- 의사소통 모델(Communication Model)
  - 의사소통에는 노이즈(Noise)와 이해(Stake)가 개입되기 때문에 의사소통의 채널은 적을 수록 좋음
  - 커뮤니케이션 채널 수 : N(N-1)/2
  - 인력 수가 산술급수적으로(Arithmetically)증가할 때 의사소통 채널 수는 기하급수적으로(geometrically)증가함
  - 의사소통 모델(Communication Model)은 송신자의 메시지가 수신자에게 전달되는 과정
    - 대 구성 요소 : 송신자(Sender),메시지(Message),미디엄(Medium),수신자(Receiver)
    - 미디엄(Medium) : 표현 수단, 예를 들면 전화, 구두 전달, 메모, 이메일, 문서, 소프트웨어, 정보시스템 등이 잇음
    - 송신자(Sender)의 정보와 아이디어는 기호화(Encoding)과정을 거쳐 메시지(Message)형태로 수신자(Receiver)에게 전달됨
    - 수신자는 교육 정도,경험,사용 언어, 문화적 배경에 따라 메시지를 해독하여 받아 들임
    - 환경과 상대방의 필요에 맞게 정보를 가공하여 표현하는 능력 중요
  - 의사소통 방해 요인(Communication Blockers) = 노이즈(잡음)(Noise) = 장벽(Barrier)
    - 의사소통 방해 요인은 메시지의 의도를 왜곡시킬 수 있는 모든 요인을 의미함
    - 노이즈(잡음)이라고도 함
    - 의사소통 방해 요인의 종류
      - 거리 상의 제약(Distance)
      - 익숙하지 않은 정보 통신 기술(Unfamiliar Technology),부적합한 인프라(Inadequate Infrastructure)
      - 배경지식의 부족(Lack of background Knowledge)
      - 언어(Language)
        1.  구두로 전달되는 메시지
        2.  얼굴 표정, 몸짓등의 Body Language
        3.  어조와 음색(목소리 톤)과 같은 준언어적 의사소통(Para-lingual Communication)
     - 문화적 차이(Cultral Differences)
     - 부적절한 메시지의 전달(Inadequate Message) : 요구사항과 관계 없는 메시지
     - 나쁜 아이디어라고 말하는 것(Saying it's a bad idea)
     - 적대감(Hostility)
     - 무관심(Indifferences)