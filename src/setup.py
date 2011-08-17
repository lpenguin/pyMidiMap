from py2exe.build_exe import py2exe
from distutils.core import setup
setup( windows=[{"script": "pyMidiMapper.py"}],
	   options = {"py2exe": {
		                  "compressed":  3,
                          "optimize": 1,
                          "bundle_files": 3,
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              } )