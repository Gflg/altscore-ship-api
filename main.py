import random
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.damaged_system = None

SYSTEMS = {
  "navigation": "NAV-01",
  "communications": "COM-02",
  "life_support": "LIFE-03",
  "engines": "ENG-04",
  "deflector_shield": "SHLD-05"
}


@app.get('/status')
def get_status():
    system = random.choice(list(SYSTEMS.keys()))
    app.damaged_system = system
    return {
        "damaged_system": system
    }


@app.get('/repair-bay', response_class=HTMLResponse)
def repair_bay():
    system = app.damaged_system
    system_code = SYSTEMS.get(system, '')
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Repair</title>
    </head>
    <body>
        <div class="anchor-point">{system_code}</div>
    </body>
    </html>
    """


@app.post('/teapot', status_code=418)
def teapot():
    return {'message': 'The requested entity body is short and stout. Tip me over and pour me out.'}


if __name__ == '__main__':
    uvicorn.run(app)