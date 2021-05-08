import ndjson
import pydantic_models.models

data_input_file = "./input_data/input.json"


with open(data_input_file) as file:
    ndjson_reader = ndjson.reader(file)
    for row in ndjson_reader:
        print(row)
        pydantic_models.models.EventStreamX.parse_obj(row)
# TODO: add timestamp validation