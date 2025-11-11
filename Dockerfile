FROM python
WORKDIR /web1

RUN pip install cloudipsp  && \
     pip install flask && \
     pip install pysqlite3
COPY . .

CMD ["python", "app.py"]