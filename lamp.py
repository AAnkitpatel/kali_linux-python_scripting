#!/usr/bin/env python
from fabric.api import env, run
env.hosts = ['192.168.100.130','192.168.100.128']
def deploy_lamp():
  run ("apt-get -y httpd mariadb-server php php-mysql")
