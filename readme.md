# GENERATE REPORT PDF FOR SONARQUBE

### .env file variables:
| Variable      | Info |
| ------------- | ------- |
| manager       | The name it will appear on pdf as manager |
| email         | The email it will appear on pdf           |
| component     | Sonarqube project key                     |
| sonar_edpoint | Sonar address                             |
| user          | Sonar user                                |
| password      | Sonar password                            |

Ex: sonarqube_endpoint=http://localhost:3000

## Run without docker:
- Make venv
> python -m venv .venv
- Activate venv
> source .venv/bin/activate
- Install dependency
> pip install -r requirements.txt
- Create a .env and reference all the variables above; then export
> export $(cat .env | xargs)
- Now execute
> python3 main.py
- If you get an error, try to create a result folder
> mkdir ./result

## Run with docker
- Create a .env and reference all the variables above; then run:
> docker run --rm --env-file=.env -v $PWD:/app/result aleixolucas/sonar-pdf-report

## FAQ
- If you are using docker, if you want to make any changes on source, you have to re-build the docker image and use it to run instead my dockerhub image.
- You can change the report images just by changing the svg in the static folder.
- To generate a report your user have to have access in the project on sonarqube.
- This application only make a single report per project, if you want to generate more reports, you have to run another time.
- You can edit the css on static/style.css
- to change the page layout, you have to change the html on main.py, the page.html is only for development purpose.

### Extras
- [Dockerhub](https://hub.docker.com/r/aleixolucas/sonar-pdf-report)
- [Github](https://github.com/AleixoLucas42/sonar-report-pdf-py)
- [SVG image viewer](https://codebeautify.org/svg-viewer)
- [SVG image converter](https://picsvg.com/)