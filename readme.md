Build:
docker build -t sonar-report . -f .docker/Dockerfile

Run:
docker run --rm -e component=project_name -e sonar_edpoint=https://sonar.example.com -e user=admin -e password=admin -v $PWD:/app/result sonar-report
