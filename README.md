# Sveltekit-Litestar-Fullstack Web Application
This project integrates sveltekit, litestar, and piccolo to create a fullstack web application.

[backend](backend/README.md)
[frontend](frontend/README.md)

## Testing API
Visit [API documentation](http://localhost:8000/schema/swagger) to test the API

## Running the application
sveltekit
```bash
cd frontend/app
# set .env variables
cp .env.example .env
pnpm install
pnpm run dev
```

backend
```bash
docker compose up
```

## Dependencies
Node v20.10.0
- sveltekit
- skeletonui

Python 3.11
- litestar
- piccolo
- piccolo_admin
- ruff

External
- docker
- or postgres if no docker