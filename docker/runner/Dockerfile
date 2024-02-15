# This dockerfile is to build on project-root (../../)
ARG python_version=3.12
FROM python:${python_version}

COPY docker/runner/entrypoint.sh /entrypoint.sh
COPY requirements.lock /requirements.lock
RUN <<EOF
  chmod +x /entrypoint.sh
  pip install -r /requirements.lock
EOF
ENTRYPOINT ["/entrypoint.sh"]
