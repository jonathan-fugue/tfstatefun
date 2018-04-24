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

## Update your vpc.tf with a new tag or something

* Note: Just ignore the Fugue ID tag deletions
```
vim vpc.tf  # Add tag or something
fugue release vpc
vim vpc.tf
terraform apply
fugue-transcriber --filter-file filter.yaml vpc.lw
fugue run vpc.lw -a vpc --import
```

## In the event of drift events

```
fugue status vpc --json | ./genStateFile.py > terraform.tfstate
```
