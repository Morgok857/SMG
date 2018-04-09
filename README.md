# Script para administrar conexiones en Linux

## Versión 1.07

## Requerimientos:
- python3
- sshpass (Opcional, solo en caso de necesitar almacenar passwords para el ssh)

## Descripcion

Script originalmente diseñado para gestionar las conexiones ssh pero puede ser utilizado para gestionar accesos a diferentes servicios. 


## Parametros:

	optional arguments:
	  -h, --help            show this help message and exit
	  -l, --list            Lista todos los Hosts disponibles
	  -a, --hidden          Muestra el string de conexion al listar los hosts
	  -s SEARCH, --search SEARCH  Busca entre todos los hosts
	  -r RUN, --run RUN     Inicia la conexion con el Host
	  -f FILE, --file FILE  Utiliza el archivo de sesiones especificado
	  -cfg, --cfg           Lista los archivos de configuracion
	  -c COMMAND, --command COMMAND  Run command


## Ejemplos de uso:
    
	$ python3 /home/ptessarolo/SMG/main.py --run PRD1_prod
    
	$ python3 /home/ptessarolo/SMG/main.py -s QA


## Configuración:
**Habilitar el modo DEBUG:**
	
	En caso de necesitar habilitar el modo debug deben ingresar en el archivo **main.py** buscar la variable "log_level=" y cambiar el valor asignado de INFO a DEBUG
**Agregar/Modificar/Eliminar Host**
	
	Los hosts deben ser configurados en el archivo **ssh_connection.cfg**.
	Dentro del archivo se deben declarar los hosts debajo de la línea  **[Sshkey]**
	Cada Host debe declararse en una nueva línea.
	
	El host se debe declararse de la siguiente forma:
		
			$nombre_del_referencia = '$string_de_conexion'
	
	Ejemplo del contenido del archivo:
	
	$ cat ssh_connection.cfg
	[Sshkey]
	servidor1 = sysadmin@192.168.3.1

## Instalación:
- Descargar el repositorio: 

	    git clone https://github.com/Morgok857/SMG.git

- Ingresar al directorio creado:
		
    	$ cd SMG

- Copiar el archivo de configuración base:
	
	    $ cp ssh_connection.cfg.template ssh_connection.cfg
	
- Agregar el o los hosts en la configuración.
	
- Se recomienda crear un alias agregando en el archivo .bashrc o .bash_alias la siguiente línea:

	    alias SMG='python3 /home/ptessarolo/SMG/main.py'
			

## Manejando varios archivos de host.
	
	La aplicación puede manejar varios archivos para separar los hosts por "cliente".

	Para esto se debe crear en el directorio donde está el script los diferentes archivos de cada "cliente".

	Para utilizar un archivo de host diferente al por defecto se debe utilizar el parámetro -f Nombre_del_archivo.
		
		Ejemplo:
	
			$ python3 /home/ptessarolo/SMG/main.py -f proyecto_x.cfg -l
			PRD1
			QA1
			QA2
			DEV1
    
    Para lista los archivos de configuración se puede utilizar el parametro --cfg.
        
        Ejemplo:
        
            $ python3 /home/ptessarolo/SMG/main.py --cfg
            ssh_connection.cfg
            cliente1.cfg
            clente1.cfg
            aws.cfg
            docker1.cfg
            
## Ejecución de script en un host remoto
	Con el parámetro -c o --command se puede enviar un comando para que lo ejecute en el host seleccionado

	Ej:
		python3 /home/ptessarolo/SMG/main.py -r miweb_prod -c "sudo ps axu| grep ngnix"

## Temas pendientes:
- Implementar compatibilidad con sistemas Windows.
- Implementar mejora en el sistema de almacenamiento de las credenciales.
- Separar las configuración del código principal
- Terminar control de errores.
- Agregar la posibilidad de ejecutar scripts en varios hosts remotos a la vez.
- Mejorar los comentarios en el código.


    
