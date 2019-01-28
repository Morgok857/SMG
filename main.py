#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, os
import logging
from configparser import ConfigParser
from argparse import ArgumentParser
from lib.function import *
from lib.logging import *

#Config argument
parser = ArgumentParser(description='Centraliza las conexiones ssh \n Version 1.07 ')

parser.add_argument('-l','--list',help='Lista todos los Hosts disponibles',action='store_true')
parser.add_argument('-a','--hidden',help='Muestra el string de conexion al listar los hosts',action='store_true')
parser.add_argument('-s','--search',help='Busca entre todos los hosts',nargs=1)
parser.add_argument('-r','--run',help='Inicia la conexion con el Host',nargs=1)
parser.add_argument('-f','--file',help='Utiliza el archivo de sesiones especificado',nargs=1)
parser.add_argument('-cfg','--cfg',help='Lista los archivos de configuracion',action='store_true')
parser.add_argument('--default_env',help='Configura el entorno por defecto',nargs=2) ## Recebe 2 parametros, el primero es el nombre del item a cambiar y el segundo es el valor a configurar
parser.add_argument('-c','--command',help='Run command',nargs=1)

args = parser.parse_args()

#Config load
diripath = os.path.dirname(os.path.realpath(__file__))
global_config_file=diripath + "/global_config.cfg"
if not os.path.isfile(global_config_file):
	print("No se encuentra el archivo 'global_config.cfg'")
	exit(1)
global_config=ConfigParser()
global_config.read(global_config_file)

#Load Log config
log_level=global_config.get("GENERAL","log_level")

try:
	logging.basicConfig(filename=global_config.get("GENERAL","log_path") + '/ssh-error.log',format=formatter,level=log_level)
except PermissionError as err:
		print("No se puede escribir en el log")

#Configura el archivo de entorno por defecto
if not args.default_env == None:
	config_set(args.default_env,global_config,global_config_file,logging)
	exit(0)

# Open file ssh-key

if not args.file == None:
	pathcfg = diripath + '/env/' + args.file[0] + '.cfg'
else:
	pathcfg = diripath + "/env/" + global_config.get("GENERAL","default_env") 
logging.debug(pathcfg)
config = ConfigParser()
config.read(pathcfg)


#List host files
if not args.cfg == False:
	list_config_file(diripath,config,logging)

if args.list == True:
	try:
		for ky in config.items('Sshkey'):
			if args.hidden == True:
				print("Host = " + ky[0] + " String connection = " + ky[1])
			else:
				print(ky[0])
	except:
		print("No se encuentra el entorno")
		exit()

if not args.search == None:
	search_conf(args.search[0],args.hidden,config,logging)
	exit()

if not args.run == None and not args.command == None and not args.command == ' ':
	logging.debug(args.run)
	logging.debug(args.command)
	run_remote_command(args.run[0],args.command,config,logging)
	exit()

if not args.run == None:
	for ky in config.items('Sshkey'):
		if args.run[0] ==  ky[0]:
			logging.debug(ky[1])
			os.system(ky[1])
			break

	search_conf(args.run[0],args.hidden,config,logging)
