#!/usr/bin/env python
'''
Node-OpenDroneMap Node.js App and REST API to access OpenDroneMap. 
Copyright (C) 2016 Node-OpenDroneMap Contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import imp
import argparse
import json

imp.load_source('context', sys.argv[2] + '/opendm/context.py')
odm = imp.load_source('config', sys.argv[2] + '/opendm/config.py')

options = {}
class ArgumentParserStub(argparse.ArgumentParser):
	def add_argument(self, *args, **kwargs):
		argparse.ArgumentParser.add_argument(self, *args, **kwargs)
		options[args[0]] = {}
		for name, value in kwargs.items():
			options[args[0]][str(name)] = str(value)
			
odm.parser = ArgumentParserStub()
odm.config()
print json.dumps(options)
