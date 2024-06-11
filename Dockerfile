# This dockerfile is to build on project-root (../../)
ARG python_version=3.12.3
FROM python:${python_version}

RUN <<EOF
  mkdir /app /data
  cat <<'EOL' > /entrypoint.sh
#!/bin/sh

$@
EOL
  chmod +x /entrypoint.sh
  pip install uv
EOF

COPY packages/main /app/packages/main
COPY requirements.lock /app/requirements.lock
RUN <<EOF
  cd /app
  uv venv
  uv pip install -r requirements.lock
EOF

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT ["/entrypoint.sh"]
