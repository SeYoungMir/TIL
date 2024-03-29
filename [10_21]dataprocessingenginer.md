# 12. 제품 소프트웨어 패키징 - 이어서
## 1. 개요
9. 버전 관리 도구 활용상의 유의점
   1. 형상 관리 지침에 의거 버전에 대한 정보로의 접근이 언제든지 가능해야 함
   2. 제품 소프트웨어 개발자, 배포자 이외에 불필요한 사용자가 소스를 수정할 수 없도록 해야 함
   3. 동일한 프로젝트에 대해 여러 개발자들이 동시에 개발할 수 있어야 함
   4. 에러 발생 시에 최대한 빠른 시간 내에 복구해야 함
10. 버전 관리 도구 활용 시의 자료 백업 정책 및 방법
    <table>
        <tr>
            <th>버전 관리 항목</th>
            <th>내용</th>
        </tr>
        <tr>
            <td>백업 정책</td>
            <td>버전 관리 라이브러리에 대한 백업 파일은 버전 관리 라이브러리가 저장된 Disk 및 분리된 Disk에 저장해야 함
            <br>Disk 백업은 1일 1회 실시해야 함
            <br>CD 백업은 1주일 1회 실시해야 함
            <br>실수에 의한 삭제를 예방하기 위해 백업은 최소 D-2일분 이상 보관해야 함</td>
        </tr>
        <tr>
            <td>백업 방법</td>
            <td>변경된 부분만 백업하는 경우 편리해 보이지만, 복구 시에는 복잡한 과정을 거치며, 증분 백업 파일에 문제가 발생되는 경우 어려움이 생길 수 있으므로 버전 라이브러리의 백업은 빠른 복구를 위해 Full 백업을 해야 함
            <br>백업 작업에 대한 임시/ 신규 요청 똔느 중지 요청은 절차에 따라 실시해야함
            <br>백업 결과는 버전 관리를 담당하는 CMO(Change Mgt Officer)가 주기적으로 점검하며, 해당 결과를 버전 관리 정기 보고 시에 함께 보고해야 함</td>
        </tr>
    </table>
## 2. 릴리즈 노트
1. 개념
   1. 릴리즈 정보를 SW의 최종 사용자인 고객과 공유하기 위한 문서 
   2. 상세 서비스를 포함, 회사가 제공하는 제품을 만들어 이를 수정, 변경 또는 개선하는 일련의 작업들이며, 릴리즈 정보들이 이러한 문서를 통해 제공됨. 이러한 정보들은 철저하게 테스트를 진행하고 개발 팀에서 제공하는 사양에 관해 최종적으로 승인된 후에 문서를 통해 배포되어짐
2. 특징
   - 전체 기능, 서비스 내용, 개선 사항 등을 사용자와 공유
   - SW의 버전 관리, 릴리즈 정보 관리
3. 초기 버전 작성 시 고려 사항
 - 현재 시제로 작성
 - 변경·개선된 항목에 대한 이력 정보 작성
4. 추가 버전 작성 
 - 중대한 오류가 발생하여 긴급하게 수정하는 경우
 - SW에 대한 기능 업그레이드를 완료한 경우
 - 사용자로부터 접수된 요구 사항에 의해 추가나 수정된 경우
5. 작성 순서 
 - 모듈 식별 $\rarr$ 릴리즈 정보 확인 $\rarr$ 릴리즈 노트 개요 작성 $\rarr$ 영향도 체크 $\rarr$ 정식 릴리즈 노트 작성 $\rarr$ 추가 개선 항목 식별
 * 참고
   * 릴리즈 노트의 중요성
     * 사용자들에게 보다 더 명확한 정보를 제공함
     * 전체적 제품의 수행 기능 및 서비스의 변화 등을 공유함
     * 자동화의 개념과 함께 적용이 가능하며, 이를 통해 전체적인 버전 관리 및 릴리즈 정보 등을 체계적으로 관리할 수 있음
     * 릴리즈 노트에는 테스트 결과 및 정보 등이 포함되며 ,사용자에게 최종 배포되어진 릴리즈 노트를 보면 테스트가 어떠한 방식으로 진행되었는지 개발 팀의 제공 사양 등을 얼마만큼 준수했는지에 대한 확인이 가능함
     * 릴리즈 노트 작성 시에 현재 시제로 작성되어야 하고 명확하면서도 완전한 정보를 제공할 수 있어야 함