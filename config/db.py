# ? Todas las claves de acceso que tiene este archivo deben eliminarse y accederse desde variables de entorno dedicadas para el repositorio
from venv import create
from pymongo import MongoClient
from sqlalchemy import create_engine, MetaData
#mongodb ThunderGer with Cuando2son1
#mongodb Daphne with ThunderGer@outlook.com
#new mongo Melissa mongodb://mongo:UmLuEKwBKnh28xDgTwV1@containers-us-west-70.railway.app:6476
MonClient = {
    'ThunderGer': 'mongodb://mongo:u6d5NDsjxNjf95YziPFn@containers-us-west-65.railway.app:5934',
    'Daphne' : 'mongodb://mongo:hg4xMd0V2xrSjnI6gFaC@containers-us-west-65.railway.app:6129',
    'Melissa' : 'mongodb://mongo:Dk9kXqiOWXEpOgPvwDMm@containers-us-west-32.railway.app:5627'

}

SQLClient = [{    
    'Daphne' : 'mysql+pymysql://root:mE73tnaYDSaTByOIJHZh@containers-us-west-54.railway.app:6848/railway',
    'Melissa' : 'mysql+pymysql://root:48NJIAl2aPaASmGPqNsK@containers-us-west-53.railway.app:6445/railway'
}]
SQL = create_engine('mysql+pymysql://root:mE73tnaYDSaTByOIJHZh@containers-us-west-54.railway.app:6848/railway')
meta = MetaData()
conDaphne = SQL.connect()

#TODO: Check link for connection
#MySQL_Daphne="mysql://root:mE73tnaYDSaTByOIJHZh@containers-us-west-54.railway.app:6848/railway"

#Mon = MongoClient(MonClient)
#MySQL = MongoClient(mongo_url) -> this is for MySQL