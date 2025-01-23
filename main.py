from fastapi import FastAPI
name = FastAPI()

@name.get("/")
def read_root():
  return {"hello":"Shakir"}

