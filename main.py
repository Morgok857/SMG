#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os
import logging
from configparser import ConfigParser
from argparse import ArgumentParser

#Config argument
parser = ArgumentParser(description='Centraliza las conexiones \n Version 1.07 ')

parser.add_argument('-l','--list',help='Lista todas las conexiones disponibles',action='store_true')
parser.add_argument('-a','--hidden',help='Muestra el string de conexion al listar el o los hosts',action='store_true')
parser.add_argument('-s','--search',help='Busca entre todos los hosts',nargs=1)
parser.add_argument('-r','--run',help='Inicia la conexion con el Host',nargs=1)
parser.add_argument('-f','--file',help='Utiliza el archivo de sesiones especificado',nargs=1)
parser.add_argument('-cfg','--cfg',help='Lista los archivos de configuracion',action='store_true')
parser.add_argument('-c','--command',help='Run command',nargs=1)

args = parser.parse_args()

#Config Log
log_level="INFO"


formatter = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
try:
	logging.basicConfig(filename=os.environ['HOME'] + '/ssh-error.log',format=formatter,level=log_level)
except PermissionError as err:
		print("No se puede escribir en el log")

#Class log

class logg ():
        def __init__(self):
                logging.info("Start process")

        def inf (self, message):
                logging.info(message)

        def db (self, message):
                logging.debug(message)
logger=logg()

# Open file ssh-key
diripath = os.path.dirname(os.path.realpath(__file__))

if not args.file == None:
	pathcfg = diripath + '/' + args.file[0]
else:
	pathcfg = diripath + "/ssh_connection.cfg"
logging.debug(pathcfg)
config = ConfigParser()
config.read(pathcfg)

#Defined Search method to fund host into host files
def search_conf (text):
	logging.debug(text)
	for ky in config.items('Sshkey'):
		if text in ky[0] or text in ky[1]:
			if args.hidden == True:
				print("Host = " + ky[0] + " String connection = " + ky[1])
			else:
				print(ky[0])

#List host fils
def list_config_file ():
	from glob import glob
	cfg_path = diripath + "/*.cfg"
	for config in glob(cfg_path):
		_tmp = config.split("/")
		print(_tmp[-1])

#Remove '\n'
def cleanexit(text):
	_t = text.split('\n')
	return _t[0]

#Defined run_remote_command
def run_remote_command (hostt,commandd):
	hssh = ""
	for ht in config.items('Sshkey'):
		if hostt ==  ht[0]:
			hssh = hostt
			execc = ht[1] + ' "' + ' '.join(commandd) + '"'
			break
	logging.debug(execc) 
	os.system(execc)

#List host fils
if not args.cfg == False:
	list_config_file()

if args.list == True:
	for ky in config.items('Sshkey'):
		if args.hidden == True:
			print("Host = " + ky[0] + " String connection = " + ky[1])
		else:
			print(ky[0])

if not args.search == None:
	search_conf(args.search[0])
	exit()

if not args.run == None and not args.command == None and not args.command == ' ':
	logging.debug(args.run)
	logging.debug(args.command)
	run_remote_command(args.run[0],args.command)
	exit()

if not args.run == None:
	for ky in config.items('Sshkey'):
		if args.run[0] ==  ky[0]:
			logging.debug(ky[1])
			os.system(ky[1])
			break

