#!/bin/bash

RESOURCE_ID="i-5203422c"
TAG_NAME="Tag-Name"

aws ec2 create-tags --resources $RESOURCE_ID --tags Key=Name,Value=$TAG_NAME