FROM continuumio/miniconda3

WORKDIR /talos-api
COPY . /talos-api
RUN conda create -n talos python=3.10 -y
SHELL ["conda", "run", "-n", "talos", "/bin/bash", "-c"] 
RUN conda install conda-forge::poetry
RUN pip install uvicorn

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi -vvv
EXPOSE 8000

CMD ["conda", "run", "-n", "talos","uvicorn", "some_api:app", "--host", "0.0.0.0", "--port", "8000"]