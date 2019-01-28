# Script para administrar conexiones en Linux

## Versión 1.09

## Requerimientos:
- python3
- sshpass (Optional)
        
## Parámetros:

	optional arguments:
	  -h, --help            show this help message and exit
	  -l, --list            Lista todos los Hosts disponibles
	  -a, --hidden          Muestra el string de conexion al listar los hosts
	  -s SEARCH, --search SEARCH  Busca entre todos los hosts
	  -r RUN, --run RUN     Inicia la conexion con el Host
	  -f FILE, --file FILE  Utiliza el archivo de sesiones especificado
	  -cfg, --cfg           Lista los archivos de configuracion
	  -c COMMAND, --command COMMAND  Run command
  	  --default_env DEFAULT_ENV DEFAULT_ENV  Configura el entorno por defecto


## Ejemplos de uso:
    
	$ python3 /home/ptessarolo/SMG/main.py --run gitlab_prod
    
	$ python3 /home/ptessarolo/SMG/main.py -s gitlab


## Configuración:
**Habilitar el modo DEBUG:**
	
	En caso de necesitar habilitar el modo debug se debe utilizar el parámetro "--default_env" 
	indicando que necesitamos alterar el valor de log_level. Este los valores permitidos son de INFO a DEBUG

    Ej: 
            python3 /home/ptessarolo/SMG/main.py --default_env log_level DEBUG
    
    
**Agregar/Modificar/Eliminar Host**
	
	Los hosts deben ser configurar en un archivo *.cfg (Ej: **myhost.cfg**) dentro del subdirectorio **env/**
	Dentro del archivo se deben declarar los hosts debajo de la línea **[Sshkey]**
	Cada Host debe declararse en una nueva linea.
	
	El host se debe declararse de la siguiente forma:
		
			$nombre_del_referencia = '$string_de_conexion'
	
	Ejemplo del contenido del archivo:
	
	$ cat myhost.cfg
	[Sshkey]
	servidor1 = sysadmin@192.168.3.1
	
## Instalación:
- Descargar el repositorio: 

	    git clone https://github.com/Morgok857/SMG.git

- Ingresar al directorio creado:
		
    	    $ cd SMG

- Copiar el archivo de configuración base:
	
	    $ mv global_config.cfg.template global_config.cfg
	
- Agregar el o los hosts en la configuración.
	    $ cd env
	    $ mv myhost.template myhost.cfg 
	
- Se recomienda crear un alias agregando en el archivo .bashrc o .bash_alias la siguiente línea:

	    alias ssh_manager='python3 /home/ptessarolo/SMG/main.py'

- Configuramos el Path para guardar los Logs en el directorio Home del usuario:
		
	   $ /home/ptessarolo/SMG/main.py --default_env log_path $(echo $HOME)

- Validamos su funcionamiento listando los hosts disponibles:
	   $ /home/ptessarolo/SMG/main.py -l

## Manejando varios archivos de host.
	
	La aplicación puede manejar varios "entornos" para separar los hosts por cliente, entorno, tipo de servidor, etc.

	Para esto se debe crear en el subdirectorio env/ los diferentes archivos de cada "entorno".

	Para utilizar un entorno diferente al por defecto se debe utilizar el parámetro -f Nombre_del_archivo.
		
		Ejemplo:
	
			$ python3 /home/ptessarolo/SMG/main.py -f linux_proxys -l
			proxy7
			proxy8
			proxy9
    
    Para lista los archivos de configuración, se puede utilizar el parámetro --cfg.
        
        Ejemplo:
        
            $ python3 /home/ptessarolo/SMG/main.py --cfg
            myhost.cfg
            linux_proxys.cfg
            Windows_AD.cfg
            
## Ejecución de script en un host remoto
	Con el parámetro -c o --command se puede enviar un comando para que lo ejecute en el host seleccionado

	Ej:
		python3 /home/ptessarolo/SMG/main.py -r proxy8 -c "sudo ps axu| grep java"

## Modificar configuración

	Para modificar los valores de la configuración podemos usar el parámetro --default_env. Este parámetro recibe 2 argumentos. 
	El primero es el nombre de la configuración que queremos cambiar y el segundo es el valor que queremos configurar.

	Ej:
		python3 /home/ptessarolo/SMG/main.py --default_env default_env PROD-host.cfg


## Temas pendientes:
- Terminar control de errores
- Agregar la posibilidad de ejecutar scripts en varios hosts remotos a la vez
- Mejorar los comentarios en el código
- Actualizar la documentación
- Agregar comando para auto configurar el entorno.
    
