## 테스트 방법

### 1. 패키지 설치, 환경변수 설정 후 실행
- python3 -m venv venv  
- source venv/bin/activate && pip3 install -r requirements.txt
- .env 파일 생성하고 환경변수로 QUEUE_URL 추가
- aws configure로 키 등록 (sqs를 만든 aws key)

### 2. producer와 consumer 실행
메시지를 만들고, 소비하는 구조

python producer/producer.py
python consumer/consumer.py


---

### 3. 확장
SQS + lambda 사용

주문 요청을 SQS에 적재 → 백엔드가 순차적으로 주문 처리
(주문량이 많아도 서버가 버틸 수 있음)

SQS처럼 "메시지를 던지고 가져가는 구조"는
비동기 처리,
트래픽 완충,
시스템 decoupling,
장애 복원력,
작업 분산


---

컨슈머(워커)의 수를 늘리거나 줄이면서,
처리 속도를 상황에 맞게 "유연하게" 조절할 수 있습니다.
예를 들어, 트래픽이 많을 때는 워커를 여러 대 띄워서 빠르게 처리하고,
트래픽이 적을 때는 워커 수를 줄여 리소스를 아낄 수 있습니다.
즉, 메시지 생산 속도와 소비 속도를 분리해서 관리할 수 있다는 점이 큰 장점입니다.


SQS에 메시지를 넣으면,
컨슈머가 정상적으로 메시지를 받아서 "삭제(delete)"하기 전까지는
메시지가 큐에 안전하게 남아 있습니다.
컨슈머가 처리 중 장애가 나도,
메시지는 다시 큐에 남아 있다가 다른 컨슈머가 재처리할 수 있습니다.
즉, 메시지 유실 위험이 거의 없습니다.


생산자(Producer)와 소비자(Consumer)가 완전히 분리되어,
서로의 상태에 영향을 받지 않습니다.
장애 복원력(Resilience)이 높고,
시스템 확장(Scalability)도 쉽습니다.
