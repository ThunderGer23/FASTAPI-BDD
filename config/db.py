from pymongo import MongoClient

mongo_ThunderGer = 'mongodb://mongo:8A58CKJLY90VZ54mXAxt@containers-us-west-52.railway.app:6953'

PostgreSQL_ThunderGer = 'postgresql://postgres:1AhTI248pPGdta2fLGuu@containers-us-west-52.railway.app:7012/railway'

conn = MongoClient(mongo_ThunderGer)