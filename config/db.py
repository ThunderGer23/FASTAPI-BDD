from pymongo import MongoClient

mongo_Daphne= "mongodb://mongo:9uqlMcN0A2sto2QdgWc5@containers-us-west-52.railway.app:6888"
MySQL_Daphne="-hcontainers-us-west-54.railway.app -uroot -pmE73tnaYDSaTByOIJHZh --port 6848 --protocol=TCP railway"
conn1= MongoClient(mongo_Daphne)

mongo_ThunderGer = 'mongodb://mongo:8A58CKJLY90VZ54mXAxt@containers-us-west-52.railway.app:6953'

PostgreSQL_ThunderGer = 'postgresql://postgres:1AhTI248pPGdta2fLGuu@containers-us-west-52.railway.app:7012/railway'

<<<<<<< HEAD
conn2 = MongoClient(mongo_url)

mongo_Melissa = 'mongodb://mongo:Dk9kXqiOWXEpOgPvwDMm@containers-us-west-32.railway.app:5627'
MySQL_Melissa = 'mysql://root:48NJIAl2aPaASmGPqNsK@containers-us-west-53.railway.app:6445/railway'
=======
conn = MongoClient(mongo_ThunderGer)
>>>>>>> ThunderGer
