## 4. 보안 기능 - 이어서
4. 소프트웨어 개발보안 계획 수립
   1. 소프트웨어 개발 보안 계획 단계 : 시작 $\rarr$ 분석 $\rarr$ 설계 $\rarr$ 구현 $\rarr$ 시험 단계
   2. 소프트웨어 보안 요구공학 프로세스
      - 시작 단계
        - 개발 목적 계획, 전략 수렴
          - 업무 현황 파악(보안 특성)
          - 보안 정책 검토
          - 보안 계획 수립
        - 상위 모델 정의
       - 분석 단계
         - 사용자 요구사항 정의
           - 보안 요구사항 정의
         - 프로세스와 요구사항의 관계 정의
           - 보안 요구사항 분석
       - 설계 단계
         - 상세 요구사항 명세서 작성
           - 보안 요구사항 반영
           - 보안 구현 설계서
         - 상세 기능 정의
       - 구현 단계
         - 환경 보안 요건
         - 개발 보안 요건
       - 시험 단계
         - 프로그램 통합 시험
           - 보안성 평가
         - 보안 인증
5. 지속적 소프트웨어 보아 개선을 위한 점검 사항
   1. 테스트 주기와는 별개로 테스트를 실시한 모든 애플리케이션의 비율
   2. 각 항목마다 강력한 특성 및 위험 데이터를 포함하는 소프트웨어 인벤토리 적용
   3. 소프트웨어 보안 정책 또는 규제 준수 요구사항 등에 부합하지 않기 때문에 요구되는 분산 수치
   4. 각각의 유형 및 수준의 위험 기반 테스트를 실시한 애플리케이션 갯수
   5. 생산 단계까지 해결되지 않은 보안 버그 및 설계 오류의 갯수
   6. 다양한 유형의 보안 결함을 수정해야 하는 시점
   7. 개발자가 취약점 수정 이외의 활동에 할애하는 시간
   8. 개발, 조달 등 모든 secure SDLC 게이트를 통과하는 소프트웨어 프로젝트 비율
   9. 규제 요구사항을 충족하거나 또는 초과하는 애플리케이션의 개수
   10. 해당 직무에 적합한 기술 수준을 보유한 소프트웨어 보안 이해 관계자의 인원 수
   11. 요구 사항 단계에서 생산 단계까지, 소프트우에어 보안 문제로부터 파생된 지연 빈도
* 참고
  * 소프트웨어 보안 결함의 종류
    <table>
        <tr>
            <th>보안 결함의 종류</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>SW 보안 결함</td>
            <td>소프트웨어 제품의 보안 품질이 정의된 특성과 일치하지 않는 모든 행위</td>
        </tr>
        <tr>
            <td>잠재적 보안 결함</td>
            <td>설치 및 운영되어지는 환경에 전달된 소프트웨어 보안 결함</td>
        </tr>
        <tr>
            <td>발견된 보안 결함</td>
            <td>설치 및 운영되어지기 전에 발견된 소프트웨어 보안 결함</td>
        </tr>
        <tr>
            <td>SW의 특이한 고장</td>
            <td>잠재 보안 결함들이 소프트웨어의 운영 중에 나타나서 발생하게 되는 하나 이상의 이상 징후들의 집합</td>
        </tr>
    </table>
* 참고
  * 소프트웨어 보안 결함 관리 프레임워크 및 단계
    - SW 개발 보안 프로세스
      - 여러개의 결함 관련 계획 활동
      - 결함 DB 구축
      - 결함 상태 추적 · 모니터링 활동