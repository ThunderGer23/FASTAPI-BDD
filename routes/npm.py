from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from models.npm import NpmDatesForGithub, NpmDatesForComplementary
from os import getcwd, remove, mkdir
from shutil import rmtree
from config.db import conDaphne
import json
import csv

npm = APIRouter()

def test(rows):          
    dependency_Name, repository, github_Stars, github_Forks, github_Watchers, abandoned, code_Coverage, linters, dependenats, npm_Stars, maintainers, contributors, dependencies, license, open_issues, security_Advisories =('Dependency Name', 'repository', 'github_Stars', 'github_Forks', 'github_Watchers', 'abandoned', 'code_Coverage', 'linters', 'dependenats', 'npm_Stars', 'maintainers', 'contributors', 'dependencies', 'license', 'open_issues', 'security_Advisories')(rows)

    id = create_npm({

    }) 

def create_npm(npm: NpmDatesForGithub):
    print('holi')
def create_npmcomplementary(npm: NpmDatesForComplementary):
    print('holi')


@npm.post("/uploadfile/npm", tags=['npm'])
async def upload_file(file: UploadFile = File(...)):
    csvFilePath = getcwd() + '/document/npm/' + file.filename
    jsonFilePath = f'{csvFilePath.replace(".csv","")}.json'    
    
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
            test(rows)  
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