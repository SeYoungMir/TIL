## 자바(이클립스)에서 공공API 요청 및 출력(1)

### 이클립스 (Eclipse) 사용하기

- New
  - Dynamic WebProject
  - Project Name~
    - Resource
      - src
        - package
          - Name~
        - new Java Class
          - name~

- 기본 java 파일 형성
```java
package data.api.json;
Import java.io.BufferedReader;
Import java.net.HttpURLConnection;
Import java.net.URL;
public class ApiJson{
    public static void main(String[] args){
        //버퍼 이용: BufferedReader --> 버퍼를 이용해서 읽고 쓰는 함수
        //버퍼(Buffer) : 입출력 속도 향상을 위해서 데이터를 일시적으로 메모리 영역의 한 곳에 모아두는 것
        //버퍼의 장점 : 버퍼를 이용하기 때문에 입출력 관련 처리작업을 매우 빠르게 할 수 있다
        BufferedReader br = null;
        try {
            //공공 API 인증키 및 전체 풀 주소
            //변수에 여러 값을 넣어서 주소 체계를 만들어야 한다면 -->StringBuilder를 사용
            //String:불변(Immutable)성을 가지므로 문자열을 더할 때 매번 새로운 객체를 생성해서 참조하는 방식 -->값 변경 X
            //StringBuilder: 문자열을 더해 나갈 때 새로운 객체를 매번 생성하는 것이 아니라 기존 데이터 값에 추가해가는 방식이고, 속도가 빠르다.
            //            :mutable 속성이고,append(),insert(),delete() 등을 사용해서 값을 변경
            //보통 공공 API방식 --> StringBuilder 사용
            String urlStr:"API 미리보기 풀주소";
            //URL 클래스로 객체 생성 --> 2가지 방법: 절대 경로, 상대 경로
            URL url=new URL(urlStr);
            //openConnection() 메서드를 이용한 연결
            //URL 주소의 원격 객체에 접속한 뒤 --> 통신할 수 있는 URLConnection 객체 리턴
            HttpURLConnection urlConn =(HttpURLConnection) url.openConnection();
            urlConn.setRequestMethod("GET");
            urlConn.setRequestProperty("Content-type","application/json")
            System.out.print("Response code:" +urlConn.getResponseCode());
            //응답코드 200 출력
        }
        catch(Exception e){
            System.out.print(e.getMessage());
        }
        //ctrl + shift + O > 빠른 Import
    }
}
```
- Window
  - Preference에서 설정 조작
  - Java
    - code style
      - formatter
        - edit에서 변경 가능
          - tabsize
          - 변경 시 bulit in 은 변경 불가능하므로 이름을 바꾸어 저장해야함
- 