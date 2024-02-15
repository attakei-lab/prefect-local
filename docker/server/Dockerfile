ARG python_version=3.12
FROM python:${python_version}

ARG prefect_version=2.14.21
RUN <<EOF
  pip install "prefect==${prefect_version}"
EOF
