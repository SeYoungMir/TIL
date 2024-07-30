# 부록 - 유용한 라이브러리
## 2. 파이참(PyCharm) 사용
### 4. 파이참 설정을 원하는 대로 변경
1. 파이참의 메모리 설정
   - 파이참은 자바로 만들어져 있으므로 메모리가 넉넉한 머신을 사용하고 있다면 힙 사이즈를 늘려서 조금 더 쾌적하게 사용 가능
   - 메뉴에서 [Help] $\rarr$ [Edit Custom VM Options]를 선택
   - 처음 실행 시 File Create 화면이 출력되기도 함. 이러한 경우에는 [Yes]를 클릭해서 설정 파일 생성
   - 다음 코드는 기본적으로 생성되는 설정 파일. 이 파일을 변경하면 자바에서 사용하는 메모리 크기(힙 사이즈)를 설정 가능
   - ```java
     # custom  PyCharm Community Edition VM Options

     -Xms128m
     -Xmx750m 
     -XX:ReservedCodeCacheSize=240m
     -XX:+UseCompressedOops
     -Dfile.encoding=UTF-8
     -XX:+UseConcMarkSweepGC
     -XX:SoftRefLRUPolicyMSPerMB=50
     -ea
     -Dsun.io.useCanonCaches=false
     -Djava.net.preferIPv4Stack=true
     -XX:+HeapDumpOnOutOfMemoryError
     -XX:-OmitStackTraceInFastThrow
     -Xverify:none

     -XX:ErrorFile=$USER_HOME/java_error_in_pycharm_%p.log
     -XX:HeampDumpPath=$USER_HOME/java_error_in_pycharm.hprof
     -Xbootclasspath/a:../lib/boot.jar
     ```

     - 파이참의 버전에 따라서 내용에 약간의 차이가 있을 수도 있지만, '-Xmx'가 최대 메모리 크기를 나타냄. 750m은 750MB를 나타내므로 이 값을 크게 설정 시 파이참을 조금 더 쾌적하게 사용 가능
     - 머신에 탑재된 메모리 크기에 따라서 값을 어느정도로 지정해야할지 다를 수 있으므로 변경하면서 맞추기를 추천.