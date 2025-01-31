#!/bin/bash

KEY_PAIR_NAME=""
SECURITY_GROUP_ID=""
SUBNET_ID=""
AMI_ID=""
COUNT=
INSTANCE_TYPE="t2.micro"

aws ec2 run-instances --image-id $AMI_ID --count $COUNT --instance-type $INSTANCE_TYPE --key-name $KEY_PAIR_NAME --security-group-ids $SECURITY_GROUP_ID --subnet-id $SUBNET_ID
