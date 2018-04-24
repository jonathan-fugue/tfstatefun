provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "/Users/Jonathan/.aws/credentials"
  profile                 = "business-unit-security"
}
resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  tags {
    Name = "testing"
    Terraform = "true"
  }
}
