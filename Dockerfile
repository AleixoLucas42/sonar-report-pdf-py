FROM surnet/alpine-python-wkhtmltopdf:3.12.1-0.12.6-full
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "-u"]
CMD ["main.py"]