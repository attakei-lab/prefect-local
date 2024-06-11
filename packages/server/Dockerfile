ARG python_version=3.12.3
FROM python:${python_version}

ARG prefect_version=2.19.4
RUN <<EOF
  pip install "prefect==${prefect_version}"
EOF
