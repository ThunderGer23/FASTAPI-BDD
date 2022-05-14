from sqlite3.dbapi2 import _Parameters
from pymongo import MongoClient

# ? Todas las claves de acceso que tiene este archivo deben eliminarse y accederse desde variables de entorno dedicadas para el repositorio

MonClient = [{
    'ThunderGer': 'mongodb://mongo:8A58CKJLY90VZ54mXAxt@containers-us-west-52.railway.app:6953',
    'Daphne' : 'mongodb://mongo:9uqlMcN0A2sto2QdgWc5@containers-us-west-52.railway.app:6888',
    'Melissa' : 'mongodb://mongo:Dk9kXqiOWXEpOgPvwDMm@containers-us-west-32.railway.app:5627'

}]   

SQLClient = [{
    'ThunderGer': 'postgresql://postgres:1AhTI248pPGdta2fLGuu@containers-us-west-52.railway.app:7012/railway',
    'Daphne' : '', #TODO: Add link por connection in this area
    'Melissa' : 'mysql://root:48NJIAl2aPaASmGPqNsK@containers-us-west-53.railway.app:6445/railway'
}]


#TODO: Check link for connection
#MySQL_Daphne="-hcontainers-us-west-54.railway.app -uroot -pmE73tnaYDSaTByOIJHZh --port 6848 --protocol=TCP railway"

Mon = MongoClient(MonClient)
#MySQL = MongoClient(mongo_url) -> this is for MySQL