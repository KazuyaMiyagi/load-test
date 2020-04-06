Prepare
====================================================================================================

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

Create stack
====================================================================================================

```
$ aws cloudformation create-stack --stack-name load-test-stack --template-body file://load-test-stack.yml --capabilities CAPABILITY_IAM
{
    "StackId": "..."
}
```
