from warnings import catch_warnings
import pdfkit
import requests
import json
import pdfkit
import base64
import os
from datetime import date

## Variables
manager = os.environ['manager']
email = os.environ['email']
component = os.environ['component']
sonar_endpoint = os.environ['sonar_endpoint']
user = os.environ['user']
password = os.environ['password']

metrics = "coverage,code_smells,reliability_rating,security_rating,bugs,vulnerabilities,duplicated_lines_density"
nota = "ABCDE"
auth = f"{user}:{password}"
data = base64.b64encode(auth.encode())
token = data.decode("utf-8")

url = f"{sonar_endpoint}/api/measures/search_history?component={component}&metrics={metrics}"
payload={}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {token}'
}
try:
    meansures = requests.request("GET", url, headers=headers, data=payload)
    url = f"{sonar_endpoint}/api/qualitygates/project_status?projectKey={component}"
    project_status = requests.request("GET", url, headers=headers, data=payload)
except Exception as err:
    print(f"Não foi possivel concluir a request, error code {err}")

data = json.loads(json.dumps(meansures.json()))
status = json.loads(json.dumps(project_status.json()))

project_status = status["projectStatus"]["status"]

print(f"Project: {component}")
coverage = data["measures"][0]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print(f"Cobertura: {coverage}")

duplicated_lines_density = data["measures"][1]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print(f"duplicated_lines_density: {duplicated_lines_density}")

reliability_rating = data["measures"][2]["history"][len(data["measures"][0]["history"]) - 1]["value"]
r = "%.0f" % float(reliability_rating)
print(f"Reliability rating: {nota[int(r) - 1]}")
reliability_rating = nota[int(r) - 1]

security_rating = data["measures"][3]["history"][len(data["measures"][0]["history"]) - 1]["value"]
i = "%.0f" % float(security_rating)
print(f"Security Rating: {nota[int(i) - 1]}")
security_rating = nota[int(i) - 1]

code_smells = data["measures"][4]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print(f"Code Smell: {code_smells}")

bugs = data["measures"][5]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print(f"Bugs: {bugs}")

vulnerabilities = data["measures"][6]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print(f"Vulnerabilities: {vulnerabilities}")

total_scan = data["paging"]["total"]
print(f"total_scan: {total_scan}")

with open("static/logo-sonarqube.svg", "r") as logo_sonar:
    sonarqube_logo = logo_sonar.read()

with open("static/logo-company.svg", "r") as logo_company:
    company_logo = logo_company.read()

page = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Sonarqube report</title>
</head>

<body style="background-color: #f2f2f2;">
    <div class="content-card">
        <div class="div-flex">
        {sonarqube_logo}
            <h1>DevSecOps Report</h1>
        </div>
        <hr style="margin-top: -15px">
        <div class="wrap-card">
            <div class="div-flex">
                <div class="card-flex">
                    <span>Project name</span>
                    <label>{component}</label>
                </div>
                <div class="card-flex">
                    <span>Quality gate status</span>
                    <label>{project_status}</label>
                </div>
                <div class="card-flex">
                    <span>Report date</span>
                    <label>{date.today()}</label>
                </div>
            </div>
        </div>
    </div>
    <div class="report-content">
        <div class="div-flex">
            <div class="report-card">
                <h2>Coverage</h2>
                <h3>{coverage}%</h3>
            </div>
            <div class="report-card">
                <h2>Duplicated lines</h2>
                <h3>{duplicated_lines_density}%</h3>
            </div>
            <div class="report-card">
                <h2>Reliability rating</h2>
                <div class="letter-circle bg-circle-{reliability_rating}">{reliability_rating}</div>
            </div>
        </div>
    </div>
    <div class="report-content">
        <div class="div-flex">
            <div class="report-card">
                <h2>Bugs</h2>
                <h3>{bugs}</h3>
            </div>
            <div class="report-card">
                <h2>Code Smell</h2>
                <h3>{code_smells}</h3>
            </div>
            <div class="report-card">
                <h2>Security Rating</h2>
                <div class="letter-circle bg-circle-{security_rating}">{security_rating}</div>
            </div>
        </div>
    </div>
    <div class="report-content">
        <div class="div-flex">
            <div class="report-card">
                <h2>Vulnerabilities</h2>
                <h3>{vulnerabilities}</h3>
            </div>
            <div class="report-card">
                <h2>Total scan</h2>
                <h3>{total_scan}</h3>
            </div>
            <div class="report-card">
                <h2>Branch</h2>
                <h3>Master</h3>
            </div>
        </div>
    </div>
    <div class="report-content">
        <div id="data-info">
        <ul>
            <li>E-mail: {email}</li>
            <li>Project Owner: {manager}</li>
            <li><a href="https://docs.sonarqube.org/latest/user-guide/metric-definitions/">SonarQube</a></li>
        </ul>
    </div>
    </div>
    <div style="height: 212px;">.</div>
    <div class="report-content">
        <div class="footer">
            {company_logo}
        </div>
    </div>
</body>

</html>
"""

options = {
    'page-size': 'A4'
}

config = pdfkit.configuration(wkhtmltopdf='/bin/wkhtmltopdf')
pdfkit.from_string(page, f"result/{component}.pdf", css="static/style.css", configuration=config, options=options)
