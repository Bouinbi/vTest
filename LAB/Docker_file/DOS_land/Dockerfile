FROM ubuntu 
RUN apt-get update && apt-get install -y hping3 
CMD hping3 -S -p 80 172.19.0.3 -a 127.0.0.1
