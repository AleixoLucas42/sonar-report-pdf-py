coverage = 61.4
duplicated_lines = 30.5
bug_lines = 3.0
security_status = 1.0
code_smells = 1073
vulnerabilities = 0
bugs = 91
pie_data = 70


def generate_coverage(data):
    return """<div class="card flex-div-card bg-green">
                <span>
                    Coverage
                </span>
                <span>
                    """+str(data)+"""%
                </span>
            </div>"""

def generate_duplicated_lines(data):
    return """<div class="card flex-div-card bg-orange">
                <span>
                    Duplicated Lines
                </span>
                <span>
                    """+str(data)+"""%
                </span>
            </div>"""

def generate_security_status(data):
    return """<div class="card flex-div-card bg-blue">
                <span>
                    Security Status
                </span>
                <span>
                    """+str(data)+"""
                </span>
            </div>"""

def generate_code_smells(data):
    return """<div class="card flex-div-card bg-red">
                <span>
                    Code smells
                </span>
                <span>
                   """+str(data)+"""
                </span>
            </div>"""

def generate_vulnerabilities(data):
    return """<div class="card flex-div-card bg-purple">
                <span>
                    Vulnerabilities
                </span>
                <span>
                    """+str(data)+"""
                </span>
            </div>"""

def generate_bugs(data):
    return """<div class="card flex-div-card bg-yellow">
                <span>
                    Bugs
                </span>
                <span>
                     """+str(data)+"""
                </span>
            </div>"""

def generate_chart_pie(data):
    return """ <div id="content" class="flex-div">
            <div class="pie" style="--p:"""+str(data)+""";--b:10px;--c:purple;">"""+str(data)+"""%</div>
        </div>"""

def generate_body():
    return """<!DOCTYPE html>
        <html lang="en">

        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <style>
                .flex-div {
                    display: flex;
                    flex-flow: row nowrap;
                    justify-content: space-evenly;
                }

                .card {
                    width: 250px;
                    height: 70px;
                    border-radius: 5px;
                    margin-top: 7px;
                }

                .card span {
                    font-weight: bold;
                    margin-left: 8%;
                }

                .flex-div-card {
                    display: flex;
                    flex-flow: column wrap;
                    justify-content: space-evenly;
                }

                .bg-green {
                    background-color: chartreuse;
                }

                .bg-orange {
                    background-color: orangered;
                }

                .bg-blue {
                    background-color: darkcyan;
                }

                .bg-red {
                    background-color: tomato;
                }

                .bg-purple {
                    background-color: darkorchid;
                }

                .bg-yellow {
                    background-color: darkgoldenrod;
                }

                .pie {
                    --w: 150px;
                    width: var(--w);
                    aspect-ratio: 1;
                    position: relative;
                    display: inline-grid;
                    place-content: center;
                    margin: 5px;
                    font-size: 25px;
                    font-weight: bold;
                    font-family: sans-serif;
                }

                .pie:before {
                    content: "";
                    position: absolute;
                    border-radius: 50%;
                    inset: 0;
                    background: conic-gradient(var(--c) calc(var(--p)*1%), #0000 0);
                    -webkit-mask: radial-gradient(farthest-side, #0000 calc(99% - var(--b)), #000 calc(100% - var(--b)));
                    mask: radial-gradient(farthest-side, #0000 calc(99% - var(--b)), #000 calc(100% - var(--b)));
                }

                .wrapper {
                    width: 1042px;
                    margin: 0 auto;
                    background-color: #EDF7F6;
                }
            </style></head><body><div class="wrapper"><div id="content" class="flex-div">"""

def generate_all():
    global coverage, duplicated_lines, bug_lines, security_status, code_smells, vulnerabilities, bugs, pie_data 
    return generate_body() + generate_coverage(coverage) + generate_duplicated_lines(duplicated_lines) + generate_security_status(security_status) + """</div> <div id="content" class="flex-div">""" + generate_code_smells(code_smells) + generate_vulnerabilities(vulnerabilities) + generate_bugs(bug_lines) + """</div>""" + generate_chart_pie(pie_data) + """</div></body></html>"""

print(generate_all())