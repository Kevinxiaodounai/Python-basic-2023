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

```