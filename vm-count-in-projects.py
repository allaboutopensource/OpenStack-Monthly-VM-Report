#!/usr/bin/python3
import openstack.cloud
import argparse
import re
import os
import openstack
import csv
import sys

# Initialize connection to OpenStack
conn = openstack.connect(cloud='openstack')
conn2 = conn.connect_as(username = os.environ.get('OS_USERNAME'), password = os.environ.get('OS_PASSWORD'))
cloud2 = conn.connect_as_project('7b9b3c86a8ab4a6e9a1cdc8bb07ae190')

# Get all projects
projects = cloud2.identity.projects()

# Iterate over projects and count instances
for project in projects:
    servers = list(cloud2.compute.servers(details=True, all_projects=True, project_id=project.id))
    instance_count = len(servers)
    
    if instance_count < 5:
        print(f"{project.name} -> Instances: {instance_count}")

