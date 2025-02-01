#!/bin/bash

AWS_PROFILE=devops aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro" "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].InstanceId"