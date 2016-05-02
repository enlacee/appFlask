import os
import sys
 
sys.path.append('/var/www/html/appFlask/web')

# Activate your virtual env
activate_env=os.path.expanduser("/var/www/html/appFlask/ENV/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from hello import app as application
