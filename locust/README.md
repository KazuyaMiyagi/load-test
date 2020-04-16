Requirements
===================================================================================================

### Tools

| Tools   | Version           | URL                                                                          |
|---------|-------------------|------------------------------------------------------------------------------|
| awscli  | 2.0.6.\* or later | https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html       |
| eksctl  | 0.16.\*  or later | https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html |
| kubectl | 1.18.\*  or later | https://kubernetes.io/docs/tasks/tools/install-kubectl/                      |

Deploy to EKS
====================================================================================================

create ecr image

```
$ aws ecr create-repository --repository-name locust
$ docker build -t <aws_account_id>.dkr.ecr.<region>.amazonaws.com/locust .
$ aws ecr get-login-password | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
$ docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/locust
```

create cluster

```
$ eksctl create cluster --name locust --fargate
```

edit yaml

```
$ sed -i -e "s;\[IMAGE\];<aws_account_id>.dkr.ecr.<region>.amazonaws.com/locust;g" *.yaml
$ sed -i -e "s;\[TARGET_URL\];http://<target_url>;g" *.yaml
```

deploy locust cluster

```
$ kubectl create -f locust-cluster.yaml
```

start proxy

```
$ kubectl proxy --port 8001
```


open locust dashboard

```
$ open http://localhost:8001/api/v1/namespaces/default/services/:locust-svc:8089/proxy/
```

Deploy to Local k8s
====================================================================================================

create docker image

```
$ docker build -t local/locust .
```

edit yaml

```
$ sed -i -e "s;\[IMAGE\];local/locust;g" *.yaml
$ sed -i -e "s;\[TARGET_URL\];http://<target_url>;g" *.yaml
```

deploy locust cluster

```
$ kubectl create -f locust-cluster.yaml
```

start proxy

```
$ kubectl proxy --port 8001
```


open locust dashboard

```
$ open http://localhost:8001/api/v1/namespaces/default/services/:locust-svc:8089/proxy/
```

Deploy to Local
====================================================================================================

edit env

```
$ cp .env.example .env
$ vim .env
```

start locust  cluster

```
$ docker-compose up -d
```

open locust dashboard

```
$ open http://127.0.0.1:8089
```
