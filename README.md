ec2-longrun
===========

notes
===========
the ip address displayed is the private ip address (private_ip_address). this can be changed to the public ip address, however I'm using it for vpc instances w/o a public address. 


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
