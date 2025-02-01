import connect

def create_ec2_instance(ec2_id):
    ec2 = connect.connect_to_ec2()
    response = ec2.terminate_instances(InstanceIds=[ec2_id])
    print(f"Response from AWS: {response} for instance ID: {ec2_id}")

if __name__ == "__main__":
    ec2_id = "i-07b55927e0a0b501c"
    create_ec2_instance(ec2_id=ec2_id)