import ndjson
import pydantic_models.models
from pydantic import ValidationError
import logging

error_logs_file = "error_logs.txt"
data_input_file = "./input_data/input.json"

logging.basicConfig(
    filename=error_logs_file,
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.ERROR,
)

with open(data_input_file) as file:
    ndjson_reader = ndjson.reader(file)
    for row in ndjson_reader:
        try:
            pydantic_models.models.EventStreamX.parse_obj(row)
        except ValidationError as e:
            logging.error(f"Event: {row} \n {e} \n")
