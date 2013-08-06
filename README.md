ec2-longrun
===========
a python script that will login to aws and find instances that have been running longer than the number of days specified

notes
===========
the ip address displayed is the private ip address this can be changed to the public ip address, however I'm using it for vpc instances w/o a public address.

usage
===========

    usage: ec2-longrun.py [-h] -a ACCESSKEY -s SECRETACCESSKEY -d NUMBEROFDAYS
    
    Find AWS EC2 Instances running longer than X days
    
    optional arguments:
    
      -h, --help            show this help message and exit
    
      -a ACCESSKEY, --accesskey ACCESSKEY
    
                            AWS Access Key ID
    
      -s SECRETACCESSKEY, --secretaccesskey SECRETACCESSKEY
    
                            AWS Secret Access Key ID
    
      -d NUMBEROFDAYS, --numberofdays NUMBEROFDAYS
                            Number of Days

output
==========

output is brief and simple, example run below:

    jgilmour-mac:longrun jgilmour$ python ec2-longrun.py -a djdahsdhakjjkwdhkhkudu -s xjsjhdjskkaddkjj -d 2
    id: i-8s98bc93, instance type: m1.small, runtime (in days): 361, ip address: 10.2.0.254
    id: i-s47c51db, instance type: m1.small, runtime (in days): 827, ip address: 10.2.0.5
    id: i-0346446b, instance type: m1.small, runtime (in days): 417, ip address: 10.2.0.4
    id: i-49c481f8, instance type: m1.small, runtime (in days): 760, ip address: 10.2.0.8

