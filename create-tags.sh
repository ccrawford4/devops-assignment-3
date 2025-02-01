#!/bin/bash

RESOURCE_ID=""
TAG_NAME="DevOps-Assignment-3"

aws ec2 create-tags --resources $RESOURCE_ID --tags Key=Name,Value=$TAG_NAME