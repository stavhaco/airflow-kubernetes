FROM continuumio/miniconda3

WORKDIR /app

# Create the environment:
COPY environment.yml .

RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]
RUN conda install -c conda-forge fbprophet && \
    pip install google-cloud-bigquery-storage==1.0.0 && \
    pip install google-cloud-bigquery==1.26.1 && \
    pip install google-cloud==0.34.0 && \
    pip install google.cloud.bigquery && \
    pip install google-cloud-storage && \
    pip install pyarrow 

COPY app.py /app

ENTRYPOINT ["conda", "run", "-n", "myenv", "python", "app.py", "test_model"]