## PJT 선택 4 . CSR vs SSR

### SPA vs MPA

- SPA
  - single page application
  - client side rendering(CSR)
    - Browser(client)에서 js에 의해 View(html)을 동적으로 생성
    - page 전환이 SSR 보다 상대적으로 빠름
    - 최초 접속 시, 모든 js와 static파일(html, image)를 가져와야 한다.
  - EX. Vue & React
- MPA
  - server side rendering(SSR)
    - Web Server에서 View를 생성.
    - Page가 전환 될 때마다, client가 server에 View 요청을 하고 server는 그것을 생성 후 client에게 보냄
    - view 전환 속도가 csr에 비해 상대적으로 늦음
    - page 요청이 빈번해 질수록 csr에 비해 서버 부하가 더 커짐
  - EX. PHP

- WIRESHARK
  - **와이어샤크**(Wireshark)는 [자유 및 오픈 소스](https://ko.wikipedia.org/wiki/자유_및_오픈_소스_소프트웨어) [패킷 분석](https://ko.wikipedia.org/wiki/패킷_가로채기) 프로그램이다. [네트워크](https://ko.wikipedia.org/wiki/컴퓨터_네트워크)의 문제, 분석, 소프트웨어 및 [통신 프로토콜](https://ko.wikipedia.org/wiki/통신_프로토콜) 개발, 교육에 쓰인다. 

