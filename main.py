"""
Copyright (c) 2024 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

import csv
import requests
import json
import config

# Your ThousandEyes API access token
headers = {
    'Authorization': f'Bearer {config.access_token}',
    'Content-Type': 'application/json'
}

# Endpoint for the GET request to fetch endpoint agents
get_url = 'https://api.thousandeyes.com/v7/endpoint/agents'

# Perform the GET request
response = requests.get(get_url, headers=headers)
if response.status_code != 200:
    print(f"Failed to fetch endpoint agents: {response.text}")
    exit()

# Convert the response to JSON
agents = response.json()

# Path to your CSV file containing hostnames that need to be updated
csv_file_path = 'data.csv'

# Read the CSV file and create a list of hostnames
hostnames = []
with open(csv_file_path, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        hostnames.append(row['Hostname'])  # Adjust the key if necessary

# Map each hostname to its agent ID
hostname_agent_id_map = {}
for agent in agents['agents']:
    if agent['computerName'] in hostnames:
        hostname_agent_id_map[agent['computerName']] = agent['id']

# Initialize a list to store the results
update_results = []

# Endpoint for the PATCH request to update endpoint agents
patch_url_template = 'https://api.thousandeyes.com/v7/endpoint/agents/{}'

# Loop through each hostname-agent ID pair and perform a PATCH request
for hostname, agent_id in hostname_agent_id_map.items():
    patch_url = patch_url_template.format(agent_id)
    patch_body = {
        "licenseType": "advantage"
    }
    response = requests.patch(patch_url, headers=headers, json=patch_body)
    result = {
        "hostname": hostname,
        "agent_id": agent_id,
        "status_code": response.status_code,
        "response": response.json() if response.status_code == 200 else response.text
    }
    update_results.append(result)
    if response.status_code == 200:
        print(f"Successfully updated agent {hostname}")
    else:
        print(f"Failed to update agent {hostname}: {response.text}")

# Write results to a JSON file
with open('update_results.json', 'w') as json_file:
    json.dump(update_results, json_file, indent=4)

# Write results to a CSV file
with open('update_results.csv', mode='w', newline='') as csv_file:
    fieldnames = ['hostname', 'agent_id', 'status_code', 'response']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for result in update_results:
        writer.writerow(result)
