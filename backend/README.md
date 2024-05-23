# Backend

## Running the project
```bash
cd backend
litestar run -r
```

## Setup Environment Variables
```bash
cp .env.example .env
```

## Setup Database
```bash
./setup_docker_psql.sh
```

## Piccolo Migrations
```bash
# Auto-generate the migration (Auto is preferred for development)
piccolo migrations new my_app --auto # or piccolo migrations new my_app
# Apply or reverse the migration
piccolo migrations forwards my_app # or piccolo migrations forwards my_app --preview
piccolo migrations backwards my_app # or piccolo migrations backwards my_app --preview
# Apply all migrations
piccolo migrations forwards all
# Check migrations
piccolo migrations check
```

## Piccolo Admin
```bash
# Session Table, User Table
piccolo migrations forwards session_auth && piccolo migrations forwards user
# Create the tables
piccolo migrations new my_app --auto && piccolo migrations forwards my_app
piccolo migrations new media_storage --auto && piccolo migrations forwards media_storage
# Create a new user
piccolo user create
# Change the password of a user
piccolo user change_password
```

## Runbook
```bash
cp .env.example .env
./setup_docker_psql.sh
piccolo migrations forwards all
piccolo user create
```

easy docker compose setup
```bash
docker compose up
```