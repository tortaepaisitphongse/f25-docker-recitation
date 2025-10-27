from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#TODO Fix recitation hours to be correct for this semester.
RECITATION_HOURS = {"a": "09:00~09:50", "b": "10:00~10:50",
                    "c": "11:00~11:50", "d": "12:00~12:50"}
MICROSERVICE_LINK = "http://17313-teachers2.s3d.cmu.edu:8080/section_info/"


@app.get("/section_info/{section_id}")
def get_section_info(section_id: str):

    if section_id is None:
        raise HTTPException(status_code=404, detail="Missing section id")

    section_id = section_id.lower()

    # Check if section exists
    if section_id not in RECITATION_HOURS:
        raise HTTPException(status_code=404, detail="Invalid section id")

    # Get TA information from microservice
    response = requests.get(MICROSERVICE_LINK + section_id)
    
    # You can check out what the response body looks like in terminal using the print statement
    data = response.json()
    print(data)
    ta_name_list = data["ta"]
    
    # Parse start and end times from RECITATION_HOURS
    time_range = RECITATION_HOURS[section_id]
    start_time, end_time = time_range.split("~")
    
    return {
        "section": section_id,
        "start_time": start_time,
        "end_time": end_time,
        "ta": ta_name_list
    }
