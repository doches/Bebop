from distutils.core import setup
import py2exe

import os
import sys
import pygame

sys.path.insert(1, "lib")
sys.path.insert(1, "screens")
setup(console=['init.py'],
	options={
		"py2exe":{
			"optimize":2,
			"bundle_files":1
		}
	},
	zipfile=None
)
