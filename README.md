# OpenStack-Monthly-VM-Report
This is a monthly Jenkins job that can provide the number of projects which are running less then 5 vm instances under them.


This section highlighting projects with the least number of VM instances, helping administrators identify underutilized resources.

An OpenStack Monthly VM Report can be a valuable tool for administrators to monitor and manage virtual machine (VM) instances across different projects. 

You can list the vm instance in a particular project using the below command:

openstack server list --project devops_infra
