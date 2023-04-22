### 安装docker, docker-compose

```
yum install -y yum-utils device-mapper-persistent-data lvm2

yum-config-manager \
                  --add-repo \
                  http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

yum install -y docker-ce docker-ce-cli containerd.io

systemctl start docker
systemctl enable docker

pip3 install docker-compose

```

### 拉起容器

```
step1: 进入"influxdb_grafana.yaml" 文件所在目录
[root@rocky1 ~]# cd /python_homework_protocol/new_homework/day5/code/
[root@rocky1 code]# ls -an
~~~忽略其他~~~
-rw-r--r-- 1 0 0 803 11月 23 14:42  influxdb_grafana.yaml
~~~忽略其他~~~

step2: 拉起容器
[root@rocky1 code]# docker-compose -f influxdb_grafana.yaml up -d

step3: 查看容器运行状态
[root@rocky1 code]# docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED              STATUS              PORTS                                       NAMES
d3388cc6f568   grafana/grafana:7.5.11   "/run.sh"                About a minute ago   Up About a minute   0.0.0.0:3000->3000/tcp, :::3000->3000/tcp   code_qyt-grafana_1
42f39e81225f   influxdb:1.8.5           "/entrypoint.sh infl…"   About a minute ago   Up About a minute   0.0.0.0:8086->8086/tcp, :::8086->8086/tcp   code_qyt-influx_1

```