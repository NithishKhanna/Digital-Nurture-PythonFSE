# ex3-SOLID-Principles.py
# Placeholder for SOLID Principles example

class Report:
    def __init__(self, content):
        self.content = content


class ReportPrinter:
    def print_report(self, report):
        print(report.content)


if __name__ == "__main__":
    report = Report("This is a sample report")
    printer = ReportPrinter()
    printer.print_report(report)
