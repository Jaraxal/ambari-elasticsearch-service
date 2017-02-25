#!/usr/bin/env python

"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from resource_management import *
import os

# config object that holds the configurations declared in the -config.xml file
config = Script.get_config()

java64_home = config['hostLevelParams']['java_home']

hostname = config['hostname']

elastic_user = config['configurations']['elastic-env']['elastic_user']
elastic_group = config['configurations']['elastic-env']['elastic_group']

elastic_base_dir = config['configurations']['elastic-env']['elastic_base_dir']
elastic_conf_dir = config['configurations']['elastic-env']['elastic_conf_dir']
elastic_log_dir = config['configurations']['elastic-env']['elastic_log_dir']
elastic_pid_dir = config['configurations']['elastic-env']['elastic_pid_dir']
elastic_pid_file = format("{elastic_pid_dir}/elasticsearch.pid")

elastic_install_log = elastic_base_dir + '/elasticsearch-install.log'
elastic_download = 'https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.0.tar.gz'

cluster_name = config['configurations']['elastic-config']['cluster_name']
hostname = config['hostname']
node_attr_rack = config['configurations']['elastic-config']['node_attr_rack']
path_data = config['configurations']['elastic-config']['path_data']
path_logs = config['configurations']['elastic-config']['path_logs']

bootstrap_memory_lock = str(config['configurations']['elastic-config']['bootstrap_memory_lock'])

# Elasticsearch expetcs that boolean values to be true or false and will generate an error if you use True or False.
if bootstrap_memory_lock == 'True':
    bootstrap_memory_lock = 'true'
else:
    bootstrap_memory_lock = 'false'

network_host = config['configurations']['elastic-config']['{network_host']
http_port = config['configurations']['elastic-config']['http_port']

discovery_zen_ping_unicast_hosts = str(config['configurations']['elastic-config']['discovery_zen_ping_unicast_hosts'])

# Need to parse the comma separated hostnames to create the proper string format within the configuration file
# Elasticsearch expects the format ["host1","host2"]
master_node_list = discovery_zen_ping_unicast_hosts.split(',')
discovery_zen_ping_unicast_hosts = '[' +  ','.join('"' + x + '"' for x in master_node_list) + ']'

discovery_zen_minimum_master_nodes = config['configurations']['elastic-config']['discovery_zen_minimum_master_nodes']


gateway_recover_after_nodes = config['configurations']['elastic-config']['gateway_recover_after_nodes']
node_max_local_storage_nodes = config['configurations']['elastic-config']['node_max_local_storage_nodes']

action_destructive_requires_name = str(config['configurations']['elastic-config']['action_destructive_requires_name'])

# Elasticsearch expecgts boolean values to be true or false and will generate an error if you use True or False.
if action_destructive_requires_name == 'True':
    action_destructive_requires_name = 'true'
else:
    action_destructive_requires_name = 'false'

xpack_security_enabled = str(config['configurations']['elastic-config']['xpack_security_enabled'])

# Elasticsearch expects boolean values to be true or false and will generate an error if you use True or False.
if xpack_security_enabled == 'True':
    xpack_security_enabled = 'true'
else:
    xpack_security_enabled = 'false'
