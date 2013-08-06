# Find instances that have been running longer than X days and display to console
# code based off of http://bevyrender.blogspot.com/2011/04/amazon-ec2-usage-monitor-and-smart.html
# Josh Gilmour, jgilmour <at> techsmog.com, 2013
# http://techsmog.com

import time
import sys
import argparse
import boto
from boto import ec2
from datetime import datetime

__author__ = 'Josh Gilmour'

def check_aws(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, UPTIME_LENGTH):
  ec2conn = ec2.connection.EC2Connection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
  reservations = ec2conn.get_all_instances()
  instances = [i for r in reservations for i in r.instances]
  l=[]
  for i in instances:
   if i.state=='running':
    l.append(i)
  try:
    if (l!=[]):
      for i in l:
        str_launch_time = datetime.strptime(i.launch_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        str_time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
        fmt = '%Y-%m-%d %H:%M:%S'
        runtime_in_days = (datetime.strptime(str(str_time_now), fmt) - datetime.strptime(str(str_launch_time), fmt)).days
        if (runtime_in_days >= int(UPTIME_LENGTH)):
            print "id: %s, instance type: %s, runtime (in days): %s, ip address: %s" % (i.id, i.instance_type, runtime_in_days, i.private_ip_address)

  except:
    print "Unexpected error:", sys.exc_info()[0]

def main():
  parser = argparse.ArgumentParser(description='Find AWS EC2 Instances running longer than X days')
  parser.add_argument('-a', '--accesskey', help='AWS Access Key ID', required=True)
  parser.add_argument('-s', '--secretaccesskey', help='AWS Secret Access Key ID', required=True)
  parser.add_argument('-d', '--numberofdays', help='Number of Days', required=True)
  args = parser.parse_args()
  check_aws(args.accesskey, args.secretaccesskey, args.numberofdays)

if __name__ == "__main__":
    main()
