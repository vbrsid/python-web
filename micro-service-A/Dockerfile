FROM python:3.9.5
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python3" ]
CMD [ "a-pod-1.py" ]

