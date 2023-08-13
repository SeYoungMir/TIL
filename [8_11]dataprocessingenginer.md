## 9. UI 프로토 타입 제작 및 검토
4. UI 프로토타입 계획 및 작성 시 고려사항
   1. 프로토타입 계획 시 고려사항
      - 프로토타입 목표 확인
        - 가장 큰 목표는 아키텍처 검증임
        - 이외에 각종 가이드 확정, 개발 환경 세팅 완료, 공통 모듈 확보, 인력 양성 등을 들 수 있음
        - 분석, 설계 기법이 프로젝트 팀원들에게 익숙하지 않은 경우에는 그 개선을 프로토 타입의 목적으로 잡는 것을 권고
      - 프롵토 타입 환경 확인
        - 프로토 타입을 위한 솔루션, 인프라 환경을 마련해야 함
        - 분석과 설계 및 개발, 테스트 가이드 베타 버전을 확인함
        - 프로토 타입 개발에 필요한 환경을 마련해야 함
        - 인프라 아키텍트와 협의하여가급적 실제와 가까운 프로토 타입 인프라 환경을 구축하는 것이 좋음
        - 대형 프로젝트의 경우 개발용 서버를 미리 도입하여 진행하는 것도 좋은 방법임
      - 프로토 타입 일정 확인
        - 일반적으로 아키텍처가 확정된 이후 프로젝트의 실제 분석 작업이 완료되기 이전에 진행함
        - 프로토 타입의 목표를 아키텍처 검증만으로 한다면 프로젝트 개발 이전에 완료해도 무방함
        - 대형 프로젝트를 기준으로 프로토 타입은 대략 1개월 정도로 잡는 것이 좋음
        - 분석, 설계 가이드에 대한 검증을 목적으로 기간을 잡을 경우 2개월을 추가할 수도 있음.
      - 프로토타입 범위 확인
        - 아키텍처의 핵심이 되는 요소를 프로토 타입의 의 범위로 잡음
        - 아키텍처 요소 중에 위험이 많은 요소를 범위로 자블 수 있음. 핵심이 되는 요소를 판단할 때에는 많은 개발자들이 참여하여 개발하는 부분인가 하는 점을 기준으로 삼음
      - 프로토 타입 인원 확인
        - 프로토 타입 역할은 리더, 솔루션 담당자, 인프라 담당자, 개발 환경 리더, 공통 모듈 개발자, 프로토 타입 개발자가 있음. 대형 프로젝트를 기준으로 리더 1인, 솔루션 담당자 파트타임 2인 이상, 인프라 담당자 파트타임 1인, 개발 환경 리더 겸 공통 모듈 개발자 1인, 프로토 타입 개발자 3~4인으로 구성됨.
      - 프로토 타입 아키텍처 검증 확인
        - 기 수립된 아키텍처로 주어진 비즈니스 요구 사항을 모두 만족할 수 있는지 검증함
        - 인프라 환경이 가능하다면 아키텍처 요소 간의 성능을 측정하여 결과 보고함
        - 아키텍처에 대한 검증 요소는 품질 속성별로 존재할 수 있으나 프로토타입을 통해서 모든 품질 속성을 보여줄 수는 없음
        - 일반적으로 기능 요구사항을 만족시킬 수 있는지 여부와 일부 구간의 성능 측정을 하는 것을 권고함
      - 프로토 타입 이슈 및 해결
        - 프로토 타입을 통해서 발생하는 이슈를 모두 취합하여 보고함
        - 프로토 타입에서 나오는 이슈의 대부분은 아키텍처 요소 검증 중에 발생하며 분석, 설계 이슈와 개발 환경 등의 이슈가 추가될 수 있음
        - 프로토 타입은 이슈가 많이 발생할수록 좋은 것임
        - 따라서 프로토 타입을 통해서 발생한 이슈와 해결한 이슈의 종류별 개수를 취합하여 결과 보고하는 것이 좋음
        - 프로토 타입 리더가 날마다 이슈를 취합하고 해결 방법을 제시함
        - 이것을 모두 정리하여 결과보고에 반영함
      - 프로토 타입 가이드 확정
        - 프로토 타입에서 검증하려고 한 표준 가이드를 프로토 타입을 하면서 수정하여 최종 확정함
        - 프로토 타입은 실제 개발과 유사하여 각종 가이드를 실전에 가장 가깝게 만들 수 있으므로 가능한 모든 가이드를 적용하는 것이 좋음
      - 프로토 타입 개발 생산성 확인
        - 프로토 타입을 진행하면서 가장 많은 시간이 소요되는 구간을 찾아 그 원인을 찾고 시정할 수 있는 방법을 찾아 실제 프로젝트에 저굥하면 많은 시간을 절약할 수 잇음
        - 프로토 타입을 진행하면서 프로토 타입 개발자들이 분석, 설계, 개발, 테스트 하는 시간을 분 단위로 적게 하여 매일 취합함
        - 가장 많은 시간이 소요되는 부분을 찾고 그 원인을 분석하여 해결 방법을 제시함
      - 프로토 타입 결과 시연
        - 프로토 타입의 결과르 고객, PM, PL 개발자에게 시연함, 프로토 타입의 목적을 구체적으로 설명함
        - 개발이 완료된 화면 위주로만 시연하지 말고, 분석,설계, 개발, 테스트 과정을 모두 설명하면서 시연하는 것이 중요함
        - 확정된 가이드 및 개발 환경 구조, 그리고 재활용이 가능한 공통 모듈 등을 같이 소개하는 것이 좋음.
   2. 프로토타입 작성 시 고려사항
      - 프로토 타입 계획 작성
        - 프로젝트의 상황에 따라 다르지만 일반적으로 프로토 타입 작성은 계획을 수립하는 과정과 실행 후 결과를 보고하는 프로세스로 진행됨
        - 프로토 타입 계획을 세울 때 고려할 부분과 결과서를 작성할 때 고려할 부분을 고려해야함
      - 프로토 타입 범위 확인
        - 프로토 타입의 범위는 프로젝트의 범위나 리스크 상활 등의 주변 여건을 감안해서 정해야 함
        - 우선 목적을 명확히 하고 그 목적을 수행할 수 있는 환경이 마련되었는지 확인해야 함
        - 특히 프로토 타입 팀을 별도로 구성할 수 있는지 반드시 확인해야 함
      - 프로토 타입 목표 확인
        - 프로토 타입을 통해서 얻고자 하는 목표를 미리 준비해야 함. 기능과 관련된 것인지, 성능과 관련된 것인지, 개발 환경에 관련된 것인지 고객과 협의하여 준비 진행해야 함
      - 프로토 타입 기간 및 비용 확인
        - 가급적 프로토 타입에 투입되는 기간 및 비용은 최소화하여 목적을 달성할 수 있도록 계획하는 것이 좋음
        - 검증할 범위를 너무 넓게 잡거나 기간을 많이 잡으면 고객이 원하는 목표가 너무 커져서 오히려 문제가 될 수도 있으므로 주의해야 함
      - 프로토 타입 산출물 확인
        - 프로토 타입에서의 산출물은 실제 개발에 그대로 참조될 수 있는 수준이 되어야 함
        - 하지만 프로토 타입을 통해 개발된 UI를 실제 개발 범위에 넣는 것은 좋은 방법이 아님
        - 실제 기능 요구 사항을 가지고 개발되었다 하더라도 아키텍처 요소 검증을 위한 것이므로 실제 개발에서는 참조만 하는 수준으로 활용해야 함
      - 프로토 타입 유의사항 확인
        - 프로토 타입은 작은 범위와 적은 인원을 가지고 최소 기간 내에 위험 요소를 식별하고 해결하는 것이 중요함