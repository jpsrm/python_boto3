import boto3


ec2 = boto3.resource('ec2')
ec2client = boto3.client('ec2')


#-----Define Lambda function-----#
def lambda_handler(event, context):

#-----Check& filter Instances which  Instance State is running-----#
    instances = ec2client.describe_instances(
        Filters=[{
            'Name': 'instance-state-name',
            'Values': ['pending','running']
        }]
        )

#-----Define dictionary to store Tag Key & value------#
    dict={}
    dict2={}

    mytags = [{
        "Key" : "practice_test", "Value" : "001"
        }]
    #print(mytags)    

#-----Store Key & Value of Instance ------#
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            ec2.create_tags(Resources = [instance["InstanceId"] ],Tags = mytags)
            #print(id)
            for tag in instance['Tags']:
                if tag['Key'] == 'practice_test':
                    
                    print([instance['InstanceId']],tag['Key'],tag['Value'])
                    dict[instance['InstanceId']]=tag['Value']
    volumes =ec2.volumes.all()
    for volume in volumes:
        #print(volume)
        for a in volume.attachments:
            for key,value in dict.items():
                #print(key,value)
                if a['InstanceId']==key:
                    volume.create_tags(Tags=[{'Key':'practice_test','Value':'001'}])
                    
       

    
   

                
                   

    
