# 4. 빅데이터 적재 I - 대용량 로그 파일 적재
## 2. 빅데이터 적재에 활용하는 기술
### 1. 하둡 - 이어서
- 하둡의 기본 요소
<table>
    <tr>
        <td colspan=3>공식 홈페이지</td>
        <td>http://hadoop.apache.org</td>
    </tr>
    <tr>
        <td rowspan=15>주요 구성 요소</td>
        <td colspan=2>DataNode</td>
        <td>블록(64MB or 128MB 등)단위로 분할된 대용량 파일들이 DataNode의 디스크에 저장 및 관리</td>
    </tr>
    <tr>
        <td colspan=2>NameNode</td>
        <td>DataNode에 저장된 파일들의 메타 정보를 메모리상에서 로드해서 관리</td>
    </tr>
    <tr>
        <td colspan=2>EditsLog</td>
        <td>파일들의 변경 이력(수정, 삭제 등) 정보가 저장되는 로그 파일</td>
    </tr>
    <tr>
        <td colspan=2>FsImage</td>
        <td>NameNode의 메모리 상에 올라와있는 메타 정보를 스냅샷 이미지로 만들어 생성한 파일</td>
    </tr>
    <tr>
        <td rowspan=4>Ver .1.x</td>
        <td>SecondaryNameNode</td>
        <td>NameNode의 FsImage와 EditsLog 파일을 주기적으로 유지관리해주는 체크 포인팅 노드</td>
    </tr>
    <tr>
        <td>MapReduce v1</td>
        <td>DataNode에 분산 저장된 파일이 스필릿(Map)되어 다양한 연산(정렬,그루핑,집계 등)을 수행한 뒤 그 결과를 다시 병합(Reduce)하는 분산 프로그래밍 기법</td>
    </tr>
    <tr>
        <td>JobTracker</td>
        <td>맵리듀스의 잡을 실행하면서 태스크에 할당하고, 전체 잡에 대해 리소스 분배 및 스케줄링</td>
    </tr>
    <tr>
        <td>TaskTracker</td>
        <td>JobTracker가 요청한 맵리듀스 프로그램이 실행되는 태스크이며, 이 때 맵 태스크와 리듀스 태스크가 생성</td>
    </tr>
    <tr>
        <td rowspan=7>Ver .2.x</td>
        <td>Active/Stand-ByNameNode</td>
        <td>NameNode를 이중화해서 서비스 중인 Active NameNode와 실패 처리를 대비한 Standby NameNode로 구성</td>
    </tr>
    <tr>
        <td>MapReduce v2/YARN</td>
        <td>하둡 클러스터 내의 자원을 중앙 관리하고, 그 위에 다양한 애플리케이션을 실행 및 관리가 가능하도록 확장성과 호환성을 높인 하둡 2.x의 플랫폼</td>
    </tr>
    <tr>
        <td>ResourceManager</td>
        <td>하둡 클러스터 내의 자원을 중앙 관리하면서, 작업 요청 시 스케줄링 정책에 따라 자원을 분배해서 실행시키고 모니터링/td>
    </tr>
    <tr>
        <td>NodeManager</td>
        <td>하둡 클러스터의 DataNode마다 실행되면서 Container를 실행시키고 라이프 사이클을 관리</td>
    </tr>
    <tr>
        <td>Container</td>
        <td>DataNode의 사용 가능한 리소스(CPU,메모리, 디스크 등)를 Container 단위로 할당해서 구성</td>
    </tr>
    <tr>
        <td>ApplicationMaster</td>
        <td>애플리케이션이 실행되며 ApplicationMaster가 생성되며 ApplicationMaster는 NodeManager에게 애플리케이션이 실행될 Container를 요청하고, 그 위에서 애플리케이션을 실행 및 관리</td>
    </tr>
    <tr>
        <td>JournalNode</td>
        <td>3개 이상의 노드로 구성되어 EditsLog를 각 노드에 복제 관리 하며 Active NameNode는 EditsLog에 쓰기만을 수행하고 Standby NameNode는 읽기만을 실행</td>
    </tr>
    <tr>
        <td>라이선스</td>
        <td colspan=3>Apache</td>
    </tr>
    <tr>
        <td>유사 프로젝트</td>
        <td colspan=3>GFS(Google File System),Gluster,MogileFS,GridFS,Lustre</td>
    </tr>
</table>

- 하둡의 최신 버전은 23년 11월 기준 3.3.6버전. 3.x에서는 2.x의 구성요소와 큰 차이가 없지만 네임노드 안정성을 강화, HDFS의 효율성과 맵 리듀스의 성능 등을 크개 개선
- 파일럿 프로젝트에서는 3.0.0을 사용, 3.x에 특화된 기능 사용 X
