import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        with open(path) as report:
            if ".csv" in path:
                report_results = csv.DictReader(report)
            elif ".json" in path:
                report_results = json.load(report)
            elif ".xml" in path:
                report_results = xmltodict.parse(report.read())["dataset"][
                    "record"
                ]
            results = list(report_results)
            if report_type == "simples":
                return SimpleReport.generate(results)
            else:
                return CompleteReport.generate(results)
