## 4. 네트워크 계층 구조 - 이어서
### 2. OSI(Open System Interconnection) 7계층
2. OSI 7계층에서 사용하는 데이터 단위
   1. 계층에 상관없이 사용할 때는 통칭하여 PDU(Protocol Data Unit)이라고 부름
   2. APDU(Application Protocol Data Unit) : 응용 계층에서 사용하는 데이터의 단위
   3. PPDU(Presentation Protocol Data Unit) : 표현 계층에서 사용하는 데이터의 단위
   4. SPDU(Session Protocol Data Unit) : 세션 계층에서 사용하는 데이터의 단위
   5. TPDU(Transport Protocol Data Unit) 
      1. 전송 계층에서 사용하는 데이터의 단위
      2. TCP에서는 세그먼트(Segment)라 부름
      3. UDP에서는 데이터그램(Datagram)이라 부름
   6. NPDU(Network Protocol Data Unit) : 네트워크 계층에서 사용하는 데이터의 단위로 패킷(Packet)이라 부름
   7. DPDU(Data Link Protocol Data Unit) : 데이터 링크 계층에서 사용하는 데이터의 단위로 프레임(Frame)이라 부름
3. 네트워크 주요 장비
   1. 허브 : 여러 대의 컴퓨터를 연결하여 네트워크로 보내거나 하나의 네트워크로 수신된 정보를 여러 대의 컴퓨터로 송신하기 위한 장비임
   2. 리피터 : 디지털 신호를 증폭시켜 주는 역할을 하여 신호가 약해지지 않고 컴퓨터로 수신되도록 함
   3. 브리지 : 두 시스템을 연결하는 네트워킹 장치이며 두 개의 LAN을 연결하여 훨씬 더 큰 LAN을 만들어 줌. 스위치는 하드웨어 기반으로 처리하기 때문에 속도가 빠르며, 브리지는 소프트웨어 방식으로 처리하기 때문에 속도가 느림. 브리지는 포트들이 같은 속도를 지원하는 반면, 스위치는 각기 다른 속도를 지원하도록 제어할 수 있음
   4. 스위치 : 두 시스템을 연결하는 네트워킹 장치이며 제공하는 포트 수가 수십, 수백개로 2~3개의 포트를 제공하는 브리지보다 많음. 브리지는 Store and Forwarding 전송 방식 만을 사용하나, 스위치는 Cut Through와 Fragment Free 방식을 같이 사용함
   5. 라우터
      - 라우터는 망 연동 장비임
      - PC 등의 로컬 호스트가 LAN에 접근할 수 있도록 하며, WAN 인터페이스를 사용하여 WAN에 접근하도록 함
      - 라우팅 프로토콜은 경로 설정을 하여 원하는 목적지까지 지정된 데이터가 안전하게 전달되도록 함