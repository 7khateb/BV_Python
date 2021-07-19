FROM python:3
ADD tutorial/helloWorld.py/
RUN pip install pystrich
CMD ["python" , "./helloWorld.py"]
