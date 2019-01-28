#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os

#Defined Search method to fund host into host files
def search_conf (text,hidden,config,logging):
	logging.debug(text)
	for ky in config.items('Sshkey'):
		if text in ky[0] or text in ky[1]:
			if hidden == True:
				print("Host = " + ky[0] + " String connection = " + ky[1])
			else:
				print(ky[0])

#List host fils
def list_config_file (diripath,config,logging):
	from glob import glob
	cfg_path = diripath + "/env/*.cfg"
	for config in glob(cfg_path):
		_tmp = config.split("/")
		print(_tmp[-1])

#Defined run_remote_command
def run_remote_command (hostt,commandd,config,logging):
	hssh = ""
	for ht in config.items('Sshkey'):
		if hostt ==  ht[0]:
			hssh = hostt
			execc = ht[1] + ' "' + ' '.join(commandd) + '"'
			logging.debug(execc) 
			os.system(execc)
			break

# Wirte config into File
def config_set (New_value,global_config,global_config_file,logging):
	logging.debug('Try write ' + New_value[1] + ' for ' + New_value[0])
	global_config.set('GENERAL',New_value[0],New_value[1])
	with open(global_config_file, "w+") as configfile:
		global_config.write(configfile)
	print("El valor de " + New_value[0] + " se a actualizado a " + New_value[1] )
	
