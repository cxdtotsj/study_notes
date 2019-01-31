FROM ubuntu:18.04
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
    && apt-get clean \
    && apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*
# CMD [ "curl", "-s", "https://ip.cn" ]
ENTRYPOINT [ "curl", "-s", "https://ip.cn" ]