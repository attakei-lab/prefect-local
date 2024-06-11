# Prefect local environmnent

This is small environmnent for Prefect using Docker Compose.

## Usage

### Pre-settings

- Detect python version
- Detect prefect version

### 1. Configure env

Detect version of Python and Prefect on your env,
and write these into `.env`.

```
cp .env.example .env
vi .env
```

Select container components that you want to run on machine,
and copy Docker-Compose file from server package.

```
cp packages/server/compose.YOUR_CHOICE.yml ./compose.yml
```

### 1. Create workspace

You must manage scripts on Prefect's flow by yourself.

On default docker components, it must be on `./scripts` directory.

* If you want to try fast, copy `scripts-example` to `script`.
* If you manage scripts already other repository, add as submodule.

### 2. Run compose

```
docker compose build
docker compose up -d
open http://localhost:4200
```
