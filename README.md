## Build the VPC with Terraform

```
terraform init
terraform plan
terraform apply --auto-approve
```

## Transcribe the VPC

```
fugue-transcriber --filter-file filter.yaml vpc.lw
fugue run vpc.lw -a vpc --import
```

## Update your vpc.tf with a new tag

* Note: Just ignore the Fugue ID tag deletions ( I guess )
```
vim vpc.tf  # Add tag
fugue release vpc
terraform apply
fugue-transcriber --filter-file filter.yaml vpc.lw
fugue run vpc.lw -a vpc --import
```

## In the event of drift events

```
fugue status vpc --json | ./genStateFile.py > terraform.tfstate
```
