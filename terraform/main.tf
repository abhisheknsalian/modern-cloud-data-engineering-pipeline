resource "aws_s3_bucket" "data_lake" {
  bucket = var.bucket_name

  tags = {
    Name    = var.project_name
    Project = "Modern Cloud Data Engineering Pipeline"
    Owner   = "Abhishek Salian"
  }
}

resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.data_lake.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {
  bucket = aws_s3_bucket.data_lake.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}