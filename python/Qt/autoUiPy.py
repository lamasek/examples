

# region  autoUiPy - automatic QT Designer .ui to .py converter ------------------------------
# v 2023 , by Josef La Masek  masek2050@gmail.com
# 
# no needs to do manually run 'pyuc' or by creating setup in project in QT Designer / QT Creator
# just add this code to the begin of your main code
# during startup it checkes for given list, if generated .py files exists and are fresh,
# if they are not, it will regenerate them

autoUiPy_PYUIC = 'PyQt6.uic.pyuic'
autoUiPy_ui_list = ['ui_mainwindow', 'ui_tab_wattmeter']
autoUiPy_enabled = True

# --------------

import os.path
import subprocess
import sys

if autoUiPy_enabled:
	for i in autoUiPy_ui_list:
		if os.path.exists(i+'.py'):
			try:
				#print(os.path.getmtime(i+'.ui'))
				#print(os.path.getmtime(i+'.py'))
				if os.path.getmtime(i+'.ui') <= os.path.getmtime(i+'.py'):
					continue
			except:
				print('autoUiPy: something wrong with given filename')
		
		# python -m PyQt6.uic.pyuic -x mainwindow.ui -o ui_mainwindow.py
		autoUiPy_PYUIC_CALL = [sys.executable, '-m', autoUiPy_PYUIC, '-x', i+'.ui', '-o', i+'.py']
		print('autoUiPy: Calling: ', autoUiPy_PYUIC_CALL)
		try:
			subprocess.check_call(autoUiPy_PYUIC_CALL)
		except Exception as e:
			print('autoUiPy: subprocess call failed: ', e)

# endregion ----------------------------------------------------------------