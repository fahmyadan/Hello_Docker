FROM continuumio/miniconda3

WORKDIR /talos-app
COPY . /talos-app
RUN conda create -n talos python=3.10 -y
SHELL ["conda", "run", "-n", "talos", "/bin/bash", "-c"] 
#RUN echo "conda activate ${ENV_NAME}" >> ~/.bashrc



RUN conda install conda-forge::poetry

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi -vvv

EXPOSE 8501

#CMD [ "streamlit" "run" "main_st.py" ]
CMD ["conda", "run", "-n", "talos", "streamlit", "run", "main_st.py"]