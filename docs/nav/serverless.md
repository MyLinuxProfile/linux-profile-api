## Resume

Develop, deploy, troubleshoot and secure your serverless applications with radically less overhead and cost by using the Serverless Framework. The Serverless Framework consists of an open source CLI and a hosted dashboard. Together, they provide you with full serverless application lifecycle management.

- Website: [https://www.serverless.com/](https://www.serverless.com/)
- Exemples: [https://github.com/serverless/examples](https://github.com/serverless/examples)

## Instalation

Install the serverless CLI via NPM:

```
npm install -g serverless
```

## Configuration

```
serverless config credentials -p aws -k {KEY} -s {SECRET_KEY} -n linuxprofile
```

## Deploy

- Dev
```
serverless deploy --aws-profile linuxprofile --region us-east-1 --stage dev
```

- Prod
```
serverless deploy --aws-profile linuxprofile --region us-east-1 --stage prod
```