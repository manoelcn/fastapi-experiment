from fastapi import FastAPI


app = FastAPI()

cars = {
    1: {"brand": "Toyota", "model": "Corolla", "year": 2022, "price": 120000},
    2: {"brand": "Honda", "model": "Civic", "year": 2021, "price": 110000},
    3: {"brand": "Ford", "model": "Mustang", "year": 2023, "price": 300000},
    4: {"brand": "Chevrolet", "model": "Onix", "year": 2020, "price": 70000},
    5: {"brand": "Volkswagen", "model": "Gol", "year": 2019, "price": 60000},
}

@app.get('/')
def home():
    return {'message': 'welcome'}


@app.get('/cars')
def car():
    return cars


@app.get('/cars/{car_id}')
def get_car(car_id: int):
    if car_id in cars:
        return cars[car_id]
    else:
        return {'message': 'car not found'}
