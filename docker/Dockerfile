# Need to define if we want to fix this
FROM jupyter/tensorflow-notebook:latest

ARG api_version

RUN pip install -Iv srgssr-publication-data-api==${api_version}

COPY pdp /tmp/pdp