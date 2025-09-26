from fastapi import FastAPI,Request,Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f);
    return data

@app.get("/")
def hello():
    return {'message':"Hello World"}

@app.get("/Hello")
def hello():
    return {'message':"Hello FastAPI"}

@app.get("/view")
def view():
    data = load_data()
    return data;

@app.get('/patient/{patient_id}')
def view_parent(patient_id: str= Path(...,description='ID of patient in DB',example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail="Patient not found")
    
@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='Sort on the basis of height, weight or bmi'), order:str = Query('asc',description='sort in asc or desc order') ):

    valid_fields = ['height','weight','bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail='Invalid field, please select one frmo {valid_fields}')

    if order not in ['asc','desc']:
        raise HTTPException(status_code=400,detail="Invalid order")
    
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key = lambda x : x.get(sort_by,0),reverse=sort_order)

    return sorted_data



@app.post('/echo')
async def echo(body: dict):
    return body