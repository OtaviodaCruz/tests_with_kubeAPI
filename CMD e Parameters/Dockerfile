FROM ndn_microservice/base:latest
COPY CS_ST /CS_ST
RUN cd /CS_ST && cmake . && make -j2 && mv bin/CS / && cd / && rm -r /CS_ST
ENTRYPOINT ["/CS"]
#CMD ["-n", "cs1", "-s", "100000", "-p", "6363", "-C", "10000"]
