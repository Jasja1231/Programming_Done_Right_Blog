#! /Users/mikaeilorfanian/anaconda/bin/python

import os
import sys
import resource

if len(sys.argv) == 3:
	file_name = sys.argv[1]
	if sys.argv[2] == 'basic':
		os.system("ipython nbconvert --to html --template basic {}".format(file_name))
	if sys.argv[2] == 'full':
		os.system("ipython nbconvert --to html --template full {}".format(file_name))
elif len(sys.argv) == 2:
	file_name = sys.argv[1]
	os.system("ipython nbconvert --to html --template full {}".format(file_name))
	f = open('{}.html'.format(file_name[:file_name.find('.')]), 'r')
	try:
		content = f.read()
		f.close()
		html_head = """
		<!DOCTYPE html>
		<html>
		<head>
		<style type="text/css">

		"""
		for i in range(2):
			index = content.find('<style type="text/css">')
			content = content[index + len('<style type="text/css">'):]

		content = html_head + content

		output = open('{}.html'.format(file_name[:file_name.find('.')]), 'w')
		output.write(content)
	except IOError:
		print '****************** File was not converted! **************************'
	finally:
		f.close()

else:
	print "Wrong arguments!"

resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
