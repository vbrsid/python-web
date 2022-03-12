FROM python:3.9.5
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5002
ENTRYPOINT [ "python3" ]
CMD [ "a-pod-2.py" ]

