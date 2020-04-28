FROM jupyter/scipy-notebook
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["demp.py"]
