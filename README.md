


#### virtualenv

	$ pip install virtualenv
	$ virtualenv ENV push


#### Crear virtual host

Agregar en /etc/hosts

	127.0.0.1    local.appflask.com

Agregar archivo `/etc/apache2/sites-available/local.appflask.conf`

	<virtualhost *:80>
	    ServerName local.appflask.com
	 
	    WSGIDaemonProcess hello user=www-data group=www-data threads=5 home=/var/www/html/appFlask/web/
	    WSGIScriptAlias / /var/www/html/appFlask/web/start.wsgi
	 
	    <directory /var/www/html/appFlask/web>
	        WSGIProcessGroup hello
	        WSGIApplicationGroup %{GLOBAL}
	        WSGIScriptReloading On
	        Order deny,allow
	        Allow from all
	    </directory>
	</virtualhost>

Agregar

	a2ensite /etc/apache2/sites-available/local.appflask.conf
	sudo /etc/init.d/apache2 restart


Fuentes:

	[configurar apache y flask](http://www.jakowicz.com/flask-apache-wsgi/)
	[configurar apache y django](http://thecodeship.com/deployment/deploy-django-apache-virtualenv-and-mod_wsgi/)