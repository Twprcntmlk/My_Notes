# How to Setup Amazon AWS S3 for File Storage
- https://www.youtube.com/watch?v=oaZ3R4NCRu8

## What are Objects and Buckets?
- Fundamental entities stored in S3 cannot access the content or data (just knows metadata)

- Buckets are containers for objects
  - While there are files there is NO hierarchy
  - We have pre-fixes to organize


## Creating Objects and Buckets on AWS Site
1) Create Acount
2) Look for S3 - Scaleable Storage
3) Create Bucket
   1) Bucket Name (MM-Statement-Storage)
   2) Select Region
   3) Options
   4) Create Buckets
4) Click on Buckets
5) Upload Files
   1) Upload Confirm
6) Pick Storage Class (I might use s3 Standard-IA for this )

7) AWS Policy Generator
   1) Effect Allow
   2) Principal
      1) Can fine tune
         1)
      2) Copy Amazon Resource Name (ARN)
         1) Policy Json Copy into Generator

## Prefix
- {EID}/{Year}/{Month}/{file.jpg}
