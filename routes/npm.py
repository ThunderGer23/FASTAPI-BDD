from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from os import getcwd, remove, mkdir
from config.db import Mon
from shutil import rmtree
import json
import csv

npm = APIRouter()

@npm.post("/uploadfile/npm", tags=['npm'])
async def upload_file(file: UploadFile = File(...)):
    csvFilePath = getcwd() + '/document/npm/' + file.filename
    jsonFilePath = f'{csvFilePath.replace(".csv","")}.json'
    data = []
    
    try:
        mkdir(getcwd() + '/document/npm/')
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
    
@npm.delete("/delete/file_npm/{name_file}", tags=['npm'])
def delete_file(name_file: str):
    try:
        remove(getcwd() + '/document/npm/' + name_file)
        return JSONResponse(content = {
            "removed": True,
            "message": "File Remove Successfully"
        }, status_code = 200)
    except FileNotFoundError:
        return JSONResponse(content = {
            "removed": False,
            "message": "File not found"
        }, status_code = 404)

@npm.delete("/folder/npm/{folder_name}", tags=['npm'])
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