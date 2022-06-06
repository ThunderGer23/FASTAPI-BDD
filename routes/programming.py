from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from os import getcwd, remove, mkdir
from shutil import rmtree
import json
import csv

programming = APIRouter()

@programming.post("/uploadfile/programming", tags=['Programming'])
async def upload_file(file: UploadFile = File(...)):
    csvFilePath = getcwd() + '/document/programming/' + file.filename
    jsonFilePath = f'{csvFilePath.replace(".csv","")}.json'
    data = []
    
    try:
        mkdir(getcwd() + '/document/programming/')
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
    
@programming.delete("/delete/file_programming/{name_file}", tags=['Programming'])
def delete_file(name_file: str):
    try:
        remove(getcwd() + '/document/programming/' + name_file)
        return JSONResponse(content = {
            "removed": True,
            "message": "File Remove Successfully"
        }, status_code = 200)
    except FileNotFoundError:
        return JSONResponse(content = {
            "removed": False,
            "message": "File not found"
        }, status_code = 404)

@programming.delete("/folder/programming/{folder_name}", tags=['Programming'])
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