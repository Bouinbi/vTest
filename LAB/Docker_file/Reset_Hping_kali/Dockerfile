FROM kalilinux/kali-rolling

RUN apt-get update
RUN apt-get install net-tools
RUN apt-get install -y iputils-ping
RUN  apt install iproute2 -y
RUN apt-get update && apt-get install -y hping3

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:rootroot' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile