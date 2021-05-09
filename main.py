import ndjson
from pydantic_models import models
from pydantic import ValidationError
import logging
from datetime import datetime


def validate_schema(error_logs_file, data_input_file):

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
                models.EventStreamX.parse_obj(row)  # validate the event
            except ValidationError as e:
                logging.error(f"Event: {row} \n {e} \n")


def generate_event_report(data_input_file):
    """
    Generates report counting nr of events per event and sent_at date
    :param data_input_file: path to input data containing the events
    :return: Dict, example: {'submission_success': {'2018-01-30': 2}, 'registration_initiated': {'2018-02-03': 1}}
    """
    report = {}

    with open(data_input_file) as file:
        ndjson_reader = ndjson.reader(file)

        for row in ndjson_reader:

            if "event" in row.keys() or "sent_at" in row.keys():
                event_value = row["event"]
                sent_at_value = datetime.strptime(row["sent_at"], "%Y-%m-%d %H:%M:%S.%f").strftime("%Y-%m-%d")

                if event_value in report.keys():   # event exists already
                    if sent_at_value in report[event_value].keys():    # date exists already
                        report[event_value][sent_at_value] += 1
                    else:
                        report[event_value][sent_at_value] = 1
                else:
                    report[event_value] = {f"{sent_at_value}": 1}
            else:
                logging.error(f"Necessary keys missing for event: {row}")

    return report

if __name__ == "__main__":

    error_logs_file = "error_logs.txt"
    data_input_file = "./input_data/input_test.json"

    # validate_schema(error_logs_file, data_input_file)
    print(generate_event_report(data_input_file))