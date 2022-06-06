from fastapi import APIRouter, UploadFile, File
from os import getcwd, remove, mkdir, getenv
from fastapi.responses import JSONResponse
from shutil import rmtree
import json
import csv

files = APIRouter()

@files.post("/uploadfile", tags=['Testeo'])
async def upload_file(file: UploadFile = File(...)):
    csvFilePath = getcwd() + '/document/' + file.filename
    jsonFilePath = f'{csvFilePath.replace(".csv","")}.json'
    data = []
    
    try:
        mkdir(getcwd() + '/document/')
    except FileExistsError:
        pass

    with open(csvFilePath, 'wb') as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
                
        dictObj = list(csvReader)[0]
        text_keys = list(dictObj.keys())[0]
        for key in list(dictObj.keys()):
            if(len(dictObj[key]) > len(dictObj[text_keys])):
                text_keys = key
        # ->this is for recoder description or text for keys IA
        #print(text_keys + ":" + dictObj[text_keys])


        for rows in csvReader:
            data.append(rows)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
    return "Success!"
    
@files.delete("/delete/{name_file}", tags=['Testeo'])
def delete_file(name_file: str):
    try:
        remove(getcwd() + '/document/' + name_file)
        return JSONResponse(content = {
            "removed": True,
            "message": "File Remove Successfully"
        }, status_code = 200)
    except FileNotFoundError:
        return JSONResponse(content = {
            "removed": False,
            "message": "File not found"
        }, status_code = 404)

@files.delete("/folder/{folder_name}", tags=['Testeo'])
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