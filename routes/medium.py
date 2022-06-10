import re
from turtle import title
from fastapi import APIRouter, UploadFile, File
from numpy import load
from schemas.medium import mediumEntity, mediumsEntity, mediumRepoEntity, mediumDatesEntity, mediumsDatesEntity
from models.medium import MediumDatesForRepo, MediumText
from fastapi.responses import JSONResponse
from os import getcwd, remove, mkdir
from pymongo import MongoClient
from bson import ObjectId
from config.db import MonClient
import requests
from shutil import rmtree
import json
from operator import itemgetter as ig
import csv

medium = APIRouter()

def test(rows):          
    text, tags, title, url, authors, timestamp = ig('text', 'tags', 'title', 'url', 'authors', 'timestamp')(rows)         
    id = create_medium({
        'text': text,
        'tags': tags})

    return create_medium_Dates_For_Medium({
        'idMediumText': id,
        'title': title,
        'url': url,
        'authors': authors,
        'timestamp': timestamp})

def create_medium(medium: MediumText):    
    new_medium = dict(medium)    
    Mon = MongoClient(MonClient["ThunderGer"])
    id = Mon.bdd.medium.insert_one(new_medium).inserted_id
    return str(id)

def create_medium_Dates_For_Medium(medium: MediumDatesForRepo):
    new_medium = dict(medium)    
    Mon = MongoClient(MonClient["Daphne"])
    id = Mon.bdd.medium.insert_one(new_medium).inserted_id
    return str(id)

@medium.post("/uploadfile/medium", tags=['Medium'])
async def upload_file(file: UploadFile = File(...)):
    csvFilePath = getcwd() + '/document/medium/' + file.filename
    jsonFilePath = f'{csvFilePath.replace(".csv","")}.json'    
    
    try:
        mkdir(getcwd() + '/document/medium/')
    except FileExistsError:
        pass

    with open(csvFilePath, 'wb') as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()

    with open(csvFilePath, encoding='utf-8') as csvf:               
        csvReader = csv.DictReader(csvf)        
        for rows in csvReader:            
            test(rows)            
        return "Success!"    
    
@medium.delete("/delete/file_medium/{name_file}", tags=['Medium'])
def delete_file(name_file: str):
    try:
        remove(getcwd() + '/document/medium/' + name_file)
        return JSONResponse(content = {
            "removed": True,
            "message": "File Remove Successfully"
        }, status_code = 200)
    except FileNotFoundError:
        return JSONResponse(content = {
            "removed": False,
            "message": "File not found"
        }, status_code = 404)

@medium.delete("/folder/medium/{folder_name}", tags=['Medium'])
def delete_folder(folder_name: str):
    try:
        rmtree(getcwd() + '/document/' + folder_name)
        return JSONResponse(content = {
            "removed": True,
            "message": "File Remove Successfully"
        }, status_code = 200)
    except FileNotFoundError:
        return JSONResponse(content = {
            "removed": False,
            "message": "Folder not found"
        }, status_code = 404)

@medium.get("/repoMedium/{id}", tags=['Medium'])
def get_medium(id: str):
    Mon = MongoClient(MonClient["ThunderGer"])
    medium = Mon.bdd.medium.find_one({"_id": ObjectId(id)})
    return mediumRepoEntity(medium)

@medium.get("/repoDatesMedium/{author}", tags=['Medium'])
def get_medium(author: str):
    Mon = MongoClient(MonClient["Daphne"])
    medium = Mon.bdd.medium.find({"authors": author})
    return mediumsDatesEntity(medium)

@medium.get("/repoCountMedium", tags=['Medium'])
def get_medium(author: str):
    Mon = MongoClient(MonClient["Daphne"])
    medium = Mon.bdd.medium.count_documents({"authors": author})
    return medium

@medium.get("/repoMediumtitle/{title}", tags=['Medium'])
def get_medium(title: str):
    Mon = MongoClient(MonClient["Daphne"])
    medium = Mon.bdd.medium.find({"title": title})
    consulta2 = mediumsDatesEntity(medium)
    id = consulta2[0]['idMediumText']    
    Mon = MongoClient(MonClient["ThunderGer"])
    medium = Mon.bdd.medium.find_one({"_id": ObjectId(id)})    
    return mediumRepoEntity(medium)