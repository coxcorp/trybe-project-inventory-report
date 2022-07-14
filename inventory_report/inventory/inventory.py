import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, report_type):
        if "csv" in path:
            with open(path) as report:
                report_results = csv.DictReader(report)
                results = list(report_results)
            if report_type == "simples":
                return SimpleReport.generate(results)
            else:
                return CompleteReport.generate(results)
