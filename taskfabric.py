#!/bin/usr/python
from fabric import Connection
for host in ('centos', 'ubuntu'):
    result = Connection(host).run('ifconfig')
    print("{}: {}".format(host, result.stdout.strip()))
