from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from os import getcwd, remove, mkdir, getenv
from shutil import rmtree
import json
import csv

files = APIRouter()

@files.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    csvFilePath = getcwd() + '/docs/' + file.filename
    jsonFilePath = f'{csvFilePath.replace(".csv","")}.json'
    data = []
    
    try:
        mkdir(getcwd() + '/docs/')
    except FileExistsError:
        pass

    with open(csvFilePath, 'wb') as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
                
        text_keys = list(csvReader)[0].keys()
        for key in list(csvReader)[0].keys():
            if(len(csvReader[key]) > len(csvReader[text_keys])):
                text_keys = key
        print(text_keys)

        for rows in csvReader:
            data.append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
    return "Success!"
    
@files.delete("/delete/{name_file}")
def delete_file(name_file: str):
    try:
        remove(getcwd() + '/docs/' + name_file)
        return JSONResponse(content = {
            "removed": True,
            "message": "File Remove Successfully"
        }, status_code = 200)
    except FileNotFoundError:
        return JSONResponse(content = {
            "removed": False,
            "message": "File not found"
        }, status_code = 404)

@files.delete("/folder/{folder_name}")
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