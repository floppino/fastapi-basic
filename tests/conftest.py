import pytest
from py.xml import html


def pytest_html_report_title(report):
    report.title = "Rat Tests"


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(0, html.th("Method"))
    cells.insert(1, html.th("Route"))
    cells.insert(2, html.th("Title"))
    cells.insert(3, html.th("Description"))
    cells.insert(4, html.th("Expected status code"))
    cells.insert(5, html.th("Effective status code"))
    cells.insert(7, html.th("Full response"))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(0, html.td(report.method))
    cells.insert(1, html.td(report.route))
    cells.insert(2, html.td(report.title))
    cells.insert(3, html.td(report.description))
    cells.insert(4, html.td(report.expected_status_code))
    cells.insert(5, html.td(report.effective_status_code))
    cells.insert(7, html.td(report.full_response))


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.method = getattr(item, "_method", "Missing method")
    report.route = getattr(item, "_route", "Missing route")
    report.title = getattr(item, "_title", "Missing title")
    report.description = getattr(item, "_description", "Missing description")
    report.expected_status_code = getattr(item, "_expected_status_code", "Missing expected status code")
    report.effective_status_code = getattr(item, "_effective_status_code", "Missing effective status code")
    report.full_response = getattr(item, "_full_response", "Missing full response")
