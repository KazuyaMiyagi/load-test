Deploy to CodeBuild
====================================================================================================

add secret data

```
$ aws secretsmanager create-secret --name GitHub
{
    "ARN": "...",
    "Name": "GitHub"
}

$ aws secretsmanager put-secret-value --secret-id GitHub --secret-string file://secrets.json
{
    "ARN": "...",
    "Name": "GitHub",
    "VersionId": "...",
    "VersionStages": [
        "AWSCURRENT"
    ]
}
```

create stack

```
$ aws cloudformation create-stack --stack-name load-test-stack --template-body file://load-test-stack.yml --capabilities CAPABILITY_IAM
{
    "StackId": "..."
}
```

Deploy to Local
====================================================================================================

start grafana and influxdb

```
$ docker-compose up -d
```

open grafana dashboard

```
$ open http://127.0.0.1:3000
```

install k6

```
$ go get github.com/loadimpact/k6
```

exec test

```
$ k6 run --out influxdb=loculhost:8086 github.com/loadimpact/k6/samples/http_get.js
```
