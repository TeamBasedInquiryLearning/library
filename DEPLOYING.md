Install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

```
/root/.local/bin/aws login --remote
/root/.local/bin/aws s3 cp [path/to/year] s3://BUCKET_NAME/[year]/ --recursive
```