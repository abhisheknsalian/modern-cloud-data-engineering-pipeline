variable "aws_region" {
  description = "AWS region where resources will be created"
  type        = string
}

variable "bucket_name" {
  description = "S3 bucket name"
  type        = string
}

variable "project_name" {
  description = "Project name used for tagging resources"
  type        = string
}