from fastapi import APIRouter, UploadFile, File
from os import getcwd

hero = APIRouter()

@hero.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):    
    with open(getcwd() + '/docs/' + file.filename, 'wb') as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return "Success!"