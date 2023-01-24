import nsetools
import os
import smtplib
import schedule
import fastapi

app=fastapi.FastAPI()


@app.get("/")
def get_data():
    nse=nsetools.Nse()
    data=nse.get_quote("INFY")
    return data




# command to run the script
# uvicorn daily_data:app --reload