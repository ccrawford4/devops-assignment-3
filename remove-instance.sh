#!/bin/bash

INSTANCE_ID=""

AWS_PROFILE=devops aws ec2 terminate-instances --instance-ids $INSTANCE_ID