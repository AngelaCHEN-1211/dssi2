<<<<<<< HEAD
import configparser
from pathlib import Path

appconfig = configparser.ConfigParser()
=======
import configparser
from pathlib import Path

appconfig = configparser.ConfigParser()
>>>>>>> 57097b94fc07d3df6e09f60402051accaa0fc643
appconfig.read(str(Path(__file__).parent)+'/config.ini')