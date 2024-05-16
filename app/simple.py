from fastapi import FastAPI

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': False}

@app.get('/predict')
def predict(day_of_week, time):
    total_time = int(day_of_week) + int(time)
    return {'wait': total_time}
