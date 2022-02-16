FROM python
WORKDIR /app
RUN apt update && apt install wkhtmltopdf -y
RUN pip install requests
RUN pip install pdfkit
COPY . .
ENTRYPOINT ["python"]
CMD ["main.py"]