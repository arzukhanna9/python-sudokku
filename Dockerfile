# syntax=docker/dockerfile:1

FROM python:3.9.6-slim

WORKDIR app

RUN pip3 install numpy==1.21.1

ADD  lib lib
COPY log.properties .
COPY solve_sudoku.py .

ENTRYPOINT ["./solve_sudoku.py"]

CMD ["--help"]
