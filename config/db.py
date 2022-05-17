# ? Todas las claves de acceso que tiene este archivo deben eliminarse y accederse desde variables de entorno dedicadas para el repositorio

MonClient = {
    'ThunderGer': 'mongodb://mongo:8A58CKJLY90VZ54mXAxt@containers-us-west-52.railway.app:6953',
    'Daphne' : 'mongodb://mongo:9uqlMcN0A2sto2QdgWc5@containers-us-west-52.railway.app:6888',
    'Melissa' : 'mongodb://mongo:Dk9kXqiOWXEpOgPvwDMm@containers-us-west-32.railway.app:5627'

}

SQLClient = [{
    'ThunderGer': 'postgresql://postgres:1AhTI248pPGdta2fLGuu@containers-us-west-52.railway.app:7012/railway',
    'Daphne' : 'mysql://root:mE73tnaYDSaTByOIJHZh@containers-us-west-54.railway.app:6848/railway',
    'Melissa' : 'mysql://root:48NJIAl2aPaASmGPqNsK@containers-us-west-53.railway.app:6445/railway'
}]


#TODO: Check link for connection
#MySQL_Daphne="mysql://root:mE73tnaYDSaTByOIJHZh@containers-us-west-54.railway.app:6848/railway"

#Mon = MongoClient(MonClient)
#MySQL = MongoClient(mongo_url) -> this is for MySQL