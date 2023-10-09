# main.py
from fastapi import FastAPI
from ExcelMapper import read_excel_sheet
import pandas as pd

app = FastAPI()

location = 'Student Survey - Jan.xlsx'

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/headings")
def read_headings():
    return {"headings": None}

@app.get("/data")
def read_data(sheet_name: str = None):
    return read_excel_sheet(sheet_name,location)

@app.get("/participantData")
def read_participant_data():
    return read_excel_sheet("participants",location)

@app.get("/affiliations_Data")
def read_affiliation_data():
    return read_excel_sheet("affiliations",location)

@app.get("/participant_Responses")
def read_participant_responses():
    participant_data = read_excel_sheet("participants",location)
    participant_responses = read_excel_sheet("responses",location)
    df1 = pd.DataFrame(participant_data)
    df2 = pd.DataFrame(participant_responses)

    df1['Participant-ID'] = df1['Participant-ID'].astype(int)
    df2['Participant-ID'] = df2['Participant-ID'].astype(int)

    # Perform a merge (similar to SQL JOIN) based on the 'id' column
    merged_df = pd.merge(df1, df2, on='Participant-ID', how='inner')

    # Convert the result back to a list of dictionaries
    merged_json = merged_df.to_dict(orient='records')

    # Print the result
    return merged_json

@app.get("/data_dictionary")
def read_participant_responses():
    data_dictionary = read_excel_sheet("data_dictionary", location)
    return data_dictionary