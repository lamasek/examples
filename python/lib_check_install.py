#!python3


# region   lib_check_install v3 by Josef La Masek ----------------------------
import importlib.util
import subprocess
import sys
#import pip
def lib_check_install(MODULEname, PACKAGEname=None): 
	#
	# check if module MODULEname is avalable for include, if not, it try to install it via pip
	# if MODname name is different than package name, you have to provide PACKAGEname too
	#
	#  if there is package which is not able to include, use (MODULEname=None, PACKAGENAME)
	#
	# useful especially when you dont have package for your soft, but need to install it on more computers
	#
	#
	# examples:
	#
	# lib_check_install('pyvisa')
	# import pyvisa
	#
	# lib_check_install(None, 'pyvisa-py')
	#
	# lib_check_install('qdarktheme', 'pyqtdarktheme')
	# import qdarktheme


	if PACKAGEname == None:
		PACKAGEname = MODULEname

	if MODULEname is not None:
		spec = importlib.util.find_spec(MODULEname)
		if spec is not None:
			return()
		print(MODULEname + ' is not import able, trying to install PKG ' + PACKAGEname)
	else: # non importable package is checked via pip
		reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
		installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
		if PACKAGEname.lower() in map(str.lower, installed_packages):
			return()
		print(PACKAGEname + ' is not installed, trying to install...')
		
	try:
		subprocess.check_call([sys.executable, '-m', 'pip', 'install', PACKAGEname])
	except:
		None
	#pip.main(['install', p]) # old deprecated way
# endregion   --------------------------------------------------------------------