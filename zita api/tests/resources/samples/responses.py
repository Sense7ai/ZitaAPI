import json
from pathlib import Path

FILE_DIR = Path(__file__).resolve().parent
with open(f"{FILE_DIR}/analytes_response_with_patient_note.json", "r") as json_file:
    analytes_response_with_patient_note = json.load(json_file)
with open(f"{FILE_DIR}/analytes_response.json", "r") as json_file:
    analytes_response = json.load(json_file)
with open(f"{FILE_DIR}/analytes_response_no_value.json", "r") as json_file:
    analytes_response_no_value = json.load(json_file)
