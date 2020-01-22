#!/bin/usr/python
from fabric import Connection
for host in ('centos'):
    result = Connection(host).run("uname -s ")
    print("{}: {}".format(host, result.stdout.strip()))
