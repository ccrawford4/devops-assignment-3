import connect

def create_ec2_instance():
    ec2 = connect.connect_to_ec2()
    conn = ec2.run_instances(InstanceType="t2.micro",
                            MaxCount=1,
                            MinCount=1,
                            ImageId="ami-0c614dee691cbbf37")
    print("New EC2 Instance Created: ", conn['Instances'][0]['InstanceId'])

if __name__ == "__main__":
    create_ec2_instance()