from pydantic import BaseModel



class input(BaseModel):
    recipients: list[str]
    template:str

class BroadcastListCreate(BaseModel): 
    name:str
    template:str
    contacts:list[str]
    success:int
    failed:int
    status:str
    
