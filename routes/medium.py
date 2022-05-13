from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from os import getcwd, remove, mkdir
from shutil import rmtree
import json
import csv

medium = APIRouter()

@medium.post("/uploadfile/medium")
async def upload_file(file: UploadFile = File(...)):
    csvFilePath = getcwd() + '/docs/medium/' + file.filename
    jsonFilePath = f'{csvFilePath.replace(".csv","")}.json'
    data = []
    
    try:
        mkdir(getcwd() + '/docs/medium/')
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
    
@medium.delete("/delete/file_medium/{name_file}")
def delete_file(name_file: str):
    try:
        remove(getcwd() + '/docs/medium/' + name_file)
        return JSONResponse(content = {
            "removed": True,
            "message": "File Remove Successfully"
        }, status_code = 200)
    except FileNotFoundError:
        return JSONResponse(content = {
            "removed": False,
            "message": "File not found"
        }, status_code = 404)

@medium.delete("/folder/medium/{folder_name}")
def delete_folder(folder_name: str):
    try:
        rmtree(getcwd() + '/docs/' + folder_name)
        return JSONResponse(content = {
            "removed": True,
            "message": "File Remove Successfully"
        }, status_code = 200)
    except FileNotFoundError:
        return JSONResponse(content = {
            "removed": False,
            "message": "Folder not found"
        }, status_code = 404)