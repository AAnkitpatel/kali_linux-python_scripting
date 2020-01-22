#!/usr/bin/python
import stat, sys, os, string, commands

pattern = raw_input("Enter the file pattern to search for:\n")
commandString = "find" + pattern
commandOutput = commands.getoutput(commandString)
findResults = string.split(commandOutput, "\n")
print "files:"
print commandOutput
print"========================================================================="
