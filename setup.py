from distutils.core import setup
import py2exe

import os
import sys
import pygame

sys.path.insert(1, "lib")
setup(console=['turbulentlake.py'],
	options={
		"py2exe":{
			"optimize":2,
			"bundle_files":1
		}
	},
	zipfile=None
)