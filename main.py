from warnings import catch_warnings
import requests
import json
import pdfkit
import base64
import os
import shutil

metrics = "coverage,code_smells,reliability_rating,security_rating,bugs,vulnerabilities,duplicated_lines_density"
nota = "ABCDE"

############################CHANGE VARS##########################################
component = os.environ['component']
sonar_edpoint = os.environ['sonar_edpoint']
user = os.environ['user']
password = os.environ['password']
############################/CHANGE VARS#########################################

auth = "{}:{}".format(user,password)
data = base64.b64encode(auth.encode())
token = data.decode("utf-8")

url = "{}/api/measures/search_history?component={}&metrics={}".format(sonar_edpoint, component, metrics)
payload={}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic {}'.format(token)
}
try:
  meansures = requests.request("GET", url, headers=headers, data=payload)
  url = "{}/api/qualitygates/project_status?projectKey={}".format(sonar_edpoint, component)
  project_status = requests.request("GET", url, headers=headers, data=payload)
except Exception as err:
  print("Não foi possivel concluir a request, error code {}".format(err))

data = json.loads(json.dumps(meansures.json()))
status = json.loads(json.dumps(project_status.json()))

project_status = status["projectStatus"]["status"]

print("Project: {}".format(component))
coverage = data["measures"][0]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print("Cobertura: {}".format(coverage))

duplicated_lines_density = data["measures"][1]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print("duplicated_lines_density: {}".format(duplicated_lines_density))

reliability_rating = data["measures"][2]["history"][len(data["measures"][0]["history"]) - 1]["value"]
r = "%.0f" % float(reliability_rating)
print("Reliability rating: {}".format(nota[int(r) - 1]))
reliability_rating = nota[int(r) - 1]

security_rating = data["measures"][3]["history"][len(data["measures"][0]["history"]) - 1]["value"]
i = "%.0f" % float(security_rating)
print("Security Rating: {}".format(nota[int(i) - 1]))
security_rating = nota[int(i) - 1]

code_smells = data["measures"][4]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print("Code Smell: {}".format(code_smells))

bugs = data["measures"][5]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print("Bugs: {}".format(bugs))

vulnerabilities = data["measures"][6]["history"][len(data["measures"][0]["history"]) - 1]["value"]
print("Vulnerabilities: {}".format(vulnerabilities))

total_scan = data["paging"]["total"]
print("total_scan: {}".format(total_scan))

html_style = """
<style>
table, th, td {
  border: 1px solid black;
}
 
table {
  width: 100%;
}
</style>
"""
page = """
<!DOCTYPE html>
<html>
<head>
""" + html_style + """
</head>
<body>
 
<h3>Sonar Report for {}</h3>
<h3>Last result {}, Total Scan {}</h3>
 
<table>
  <tr>
    <th>MEASURES</th>
    <th>RESULT</th>
  </tr>
  <tr>
    <td>Coverage</td>
    <td>{}%</td>
  </tr>
  <tr>
    <td>Duplicated Lines</td>
    <td>{}%</td>
  </tr>
  <tr>
    <td>Bugs status</td>
    <td>{}</td>
  </tr>
  <tr>
    <td>Security status</td>
    <td>{}</td>
  </tr>
  <tr>
    <td>Code smells</td>
    <td>{}</td>
  </tr>
  <tr>
    <td>Vulnerabilities</td>
    <td>{}</td>
  </tr>
  <tr>
    <td>Bugs</td>
    <td>{}</td>
  </tr>
</table>
 
</body>
</html>
""".format(component, project_status, total_scan, coverage, duplicated_lines_density, reliability_rating, security_rating, code_smells, vulnerabilities, bugs)


config = pdfkit.configuration(wkhtmltopdf = r"wkhtmltopdf")
pdfkit.from_string(page, "result/{}.pdf".format(component), configuration = config)
