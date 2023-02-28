## 빠른 데이터 분석을 위한 Spark
### Spark의 기반의 다양한 분석
#### Spark을 활용한 대화형 분석
- 실행 방식
  - 로컬 모드
    - $ bin/pyspark --master local
    - Shell을 실행하는 로컬 머신에서, 단일 프로세서로 Spark이 실행됨
    - Spark/PySpark Shell 모두 가능
  - 로컬 [N] 모드
    - $ bin/pyspark --master local[N]
    - Shell을 실행하는 로컬 머신에서, [N]개의 프로세서로 Spark이 병렬로 실행됨
    - Spark/PySpark Shell 모두 가능
  - 분산 모드
    - $ bin/spark-shell --master spark://master.host:7077 
    - Spark Master/Worker 데몬이 구동되고 있는 클러스터 환경에서, 분산+병렬로 실행됨
    - Spark Shell 만 가능
    - -> 클러스터 매니저를 Mesos를 사용할 경우
    - $ bin/spark-shell --master mesos://mesos.host:Port
- Spark 기능 구조도
  - 패키지
    - SparkSQL
    - GraphX
    - MLlib
    - Streaming
    - SparkR
  - 맵리듀스 실행 엔징
    - Spark Core
  - 자원 관리 시스템
    - YARN, Mesos, Spark Standalone Manager
  - 데이터 저장소
    - HDFS, NoSQL, RDBMS
- Spark의 주요 기능
<table>
    <tr>
        <th>구분</th>
        <th>모듈</th>
        <th>기능</th>
        <th>분야</th>
    </tr>
    <tr>
        <th>핵심</th>
        <td>Spark Core</td>
        <td>맵리듀스와 같은 병렬처리 및 반복 연산</td>
        <td>분산병렬처리</td>
    </tr>
    <tr>
        <th rowspan=4>주요 패키지</th>
        <td>Spark SQL</td>
        <td>하이브와 같은 SQL 분석</td>
        <td>데이터웨어하우스</td>
    </tr>
    <tr>
        <td>MLlib</td>
        <td>마훗과 같은 머신러닝라이브러리</td>
        <td>데이터 마이닝</td>
    </tr>
     <tr>
        <td>GraphX</td>
        <td>네트워크 분석 </td>
        <td>SNA 등 네트워크 분석</td>
    </tr>
     <tr>
        <td>Spark Streaming</td>
        <td>스톰과 같은 실시간 스트리밍 분석 </td>
        <td>스트리밍 처리 및 분석</td>
    </tr>
     <tr>
        <th rowspan=2>확장 프로젝트</th>
        <td>BlinkDB</td>
        <td>빠른 응답속도를 가진 SQL 쿼리 분석</td>
        <td>Ad-Hoc 분석
</td>
    </tr>
    <tr>
        <td>SparkR</td>
        <td>통계 패키지인 R과의 통합</td>
        <td>통계 분석</td>
    </tr>
</table>

- Spark SQL
  - SQL 쿼리 분석
    - 입력 : HDFS/Hive, RDBMS, NoSQL, Text File( Plain Text, JSON, XML 등 )
    - -데이터셋을 DB Table로 처리, 내부적으로는 DataFrame
### Spark의 데이터 처리
#### 데이터 Model
- Data Model
  - Spark 데이터 분석을 위해 필요한 Data Type의 분류
    - Spark Basic Type
      - vector, matrix, array
      - list, dataframe
    - MLlib Type
      - LabeledPoint
      - Rating
      - 알고리즘별 Model Class
  -  Spark Basic Type 
    - Vector
      - 동일한 Type의 데이터 N개, 1차원, 고정길이
        - // Create a dense vector (1.0, 0.0, 3.0). 
        - val dv: Vector = Vectors.dense(1.0, 0.0, 3.0)
        - [Note] 수학분야의 방향과 크기를 가지고 있는 데이터를 의미하지 않음
    - Matrix
      - 동일한 Type의 데이터, 2차원, M개의 행과 N개의 열로 구성( M*N 행열 )
        - // Create a dense matrix ((1.0, 2.0), (3.0, 4.0), (5.0, 6.0)) 
        - val dm: Matrix = Matrices.dense(3, 2, Array(1.0, 3.0, 5.0, 2.0, 4.0, 6.0))
    - Array
      - 동일한 Type의 데이터, N차원(1차원, 2차원, .... N차원), 고정길이
        - var z = new Array[String](3); z(0) = "Zara"; z(1) = "Nuha"; z(2) = "Ayan"
        - var z2 = Array("Zara", "Nuha", "Ayan")
    - List
      - 동일한 Type의 데이터, 1차원, 가변길이
    - DataFrame
      - 다양한 Type의 데이터, 2차원, 엑셀 Sheet or 데이터베이스 테이블 구조와 유사
  - Vector Type
    - Vector의 분류
      - 고밀도 : Dense -> 전체 데이터를 double type의 고정길이 배열에 저장
      - 저밀도 : Sparse -> 0.0이 아닌 값과 그 인덱스를 저장
    - Example
      - // Create the dense vector <1.0, 0.0, 2.0, 0.0>; 
      - val denseVec1 = Vectors.dense(1.0, 0.0, 2.0, 0.0)
      - val denseVec2 = Vectors.dense(Array(1.0, 0.0, 2.0, 0.0))
      - Create the sparse vector <1.0, 0.0, 2.0, 0.0>; 
      - val sparseVec1 = Vectors.sparse(4, Array(0, 2), Array(1.0, 2.0)) //(int size, int[] indices, double[] values)
    - Vectors 메소드
      - apply argmax asInstanceOf compressed copy 
      - foreachActive isInstanceOf numActives numNonzeros size 
      - toArray toDense toJson toSparse toString
  - LabeledPoint Type
    - LabeledPoint = ( Labeled : double, Features : vectors ) 
    - Labeled -> 
        1. Classification : 명목형 값(classes) 
           - double
           - Binary( True, False ) -> 1.0 / 0.0
           - MultiClass -> 0.0 1.0 2.0 .... N.0
        2. Regression : 연속형 값(수치형), double
    - Features -> 속성값 Vectors(double)
      - 명목형 Feature의 값은 double type으로 변환해야 함
