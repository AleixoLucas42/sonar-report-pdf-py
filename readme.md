Build:
docker build -t sonar-report . -f .docker/Dockerfile

Run:
docker run --rm -e component=project_name -e sonar_edpoint=https://sonar.example.com -e user=admin -e password=admin -v $PWD:/app/result sonar-report

docker run --rm -e component=bitbucket_pernamlabs_cms-home-api -e sonar_edpoint=https://sonar.pefisa.com.br -e user=admin -e password=123abc. -v $PWD:/app/result sonar-report

docker run -v $pwd:/app/result --rm --entrypoint cp image:version /app/result/*.pdf /app/result
