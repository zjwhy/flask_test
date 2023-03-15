from playhouse.pool import PooledMySQLDatabase
from config import *

sqldb = PooledMySQLDatabase(**mysql_config)