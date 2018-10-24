# 增加linux文件

cat > x.txt <<EOF
requests==2.19.1
pymysql==0.9.2
EOF


apk add --no-cache --virtual bdep libffi-dev openssl-dev python3-dev g++ \
    && apk del bdep \
    && apk add --no-cache python3