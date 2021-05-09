import json

import ndjson
from pydantic_models import models
from pydantic import ValidationError
import logging
from datetime import datetime


def validate_schema(data_input_file):
    """
    Checks validity of event schema and stores detected error logs
    :param error_logs_file: (str) Where to write error log messages to
    :param data_input_file: (str) Where the file with event data is stored
    :return:
    """

    with open(data_input_file) as file:
        ndjson_reader = ndjson.reader(file)
        for row in ndjson_reader:
            try:
                models.EventStreamX.parse_obj(row)  # validate the event
            except ValidationError as e:
                logging.error(f"Event: {row} \n {e} \n")


def generate_event_report(data_input_file, report_file):
    """
    Generates a report that counts the number of events per event name and sent_at date
    :param data_input_file: (str) Path to input data containing the events
    :return: (Dict) Example: {'submission_success': {'2018-01-30': 2}, 'registration_initiated': {'2018-02-03': 1}}
    """
    report = {"unknown": 0}

    with open(data_input_file) as file:
        ndjson_reader = ndjson.reader(file)

        for row in ndjson_reader:

            if "event" in row.keys() and "sent_at" in row.keys():
                event_value = row["event"]
                sent_at_value = datetime.strptime(
                    row["sent_at"], "%Y-%m-%d %H:%M:%S.%f"
                ).strftime("%Y-%m-%d")

                if event_value in report.keys():  # event exists already
                    if (
                        sent_at_value in report[event_value].keys()
                    ):  # date exists already
                        report[event_value][sent_at_value] += 1
                    else:
                        report[event_value][sent_at_value] = 1
                else:
                    report[event_value] = {f"{sent_at_value}": 1}
            else:
                report["unknown"] += 1

    with open(report_file, "w") as file:
        json.dump(report, file)

    return report


if __name__ == "__main__":

    # data_input_file = "./input_data/input_test.json"
    # error_logs_file = "/logs/error_logs.txt"
    # report_file = "/logs/event_report.txt"

    # locally:
    data_input_file = "./input_data/input.json"
    error_logs_file = "./error_logs.txt"
    report_file = "./event_report.txt"

    logging.basicConfig(
        filename=error_logs_file,
        filemode="a",
        format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
        level=logging.ERROR,
    )

    # clean up from previous runs:
    with open(error_logs_file, "w") as file:
        file.truncate(0)
        file.close()

    # Objective 1:
    validate_schema(data_input_file)
    # Objective 2:
    generate_event_report(data_input_file, report_file)
