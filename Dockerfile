# This dockerfile is to build on project-root (../../)
ARG python_version=3.12.3
FROM python:${python_version}

RUN <<EOF
  cat <<'EOL' > /entrypoint.sh
#!/bin/sh

$@
EOL
  chmod +x /entrypoint.sh
EOF
ENTRYPOINT ["/entrypoint.sh"]
