FROM progrium/busybox

RUN opkg-install nmap
RUN opkg-install net-tools
RUN mkdir /data
VOLUME /data
WORKDIR /data

ENTRYPOINT ["nmap"]

