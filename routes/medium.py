from fastapi import APIRouter, UploadFile, File
from schemas.medium import mediumEntity, mediumsEntity
from models.medium import MediumDatesForRepo, MediumText
from fastapi.responses import JSONResponse
from os import getcwd, remove, mkdir
from pymongo import MongoClient
from config.db import MonClient
from shutil import rmtree
import json
import csv

medium = APIRouter()

@medium.get("/test", tags=['Testeo'])
def test():
    print(MonClient["ThunderGer"])
    return "successful"

@medium.post("/uploadfile/medium", tags=['Medium'])
async def upload_file(file: UploadFile = File(...)):
    csvFilePath = getcwd() + '/document/medium/' + file.filename
    jsonFilePath = f'{csvFilePath.replace(".csv","")}.json'
    data = []
    
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
            data.append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
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

@medium.get("/repoMedum", tags=['Medium'])
def get_all_repos():
    Mon = MongoClient(MonClient["ThunderGer"])
    return mediumsEntity(Mon.bdd.medium.find())

@medium.post("/repoMedum", tags=['Medium'])
def create_medium(medium: MediumText):
    new_medium = dict(medium)
    del medium["id"]
    Mon = MongoClient(MonClient["ThunderGer"])
    id = Mon.bdd.medium.insert_one(new_medium).inserted_id
    return str(id)

@medium.get("/repoMedium/{id}", tags=['Medium'])
def get_medium():
    Mon = MongoClient(MonClient["ThunderGer"])
    medium = Mon.bdd.medium.find_one({"_id": id})
    return mediumEntity(medium)