import nsetools
import os
import smtplib
import schedule
import fastapi 

app=fastapi.FastAPI()
nse=nsetools.Nse()

@app.get("/")
def daily_data():
    data=nse.get_quote("SBIN")
    return data





# command to run the script
# uvicorn daily_data:app --reload