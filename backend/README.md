# Deploying to Render

The repository includes a Render Blueprint in `render.yaml`. In Render, choose **New → Blueprint Instance**, connect this repository, and deploy. The Blueprint creates a Python web service and a PostgreSQL database, generates `DJANGO_SECRET_KEY`, and supplies the database URL.

The Django service is rooted at `backend`. Its build command installs `requirements.txt`, collects static files, and runs Django's deployment checks. Its start command applies database migrations and launches Gunicorn. The free PostgreSQL plan is suitable for a demo; choose a supported paid plan for persistent production data and backups.

## Local run

From `backend`, install dependencies with `pip install -r requirements.txt`, then run `python auqa/manage.py runserver`. Without `DATABASE_URL`, Django uses the checked-in SQLite configuration for local development. Set `DJANGO_SECRET_KEY` and `DATABASE_URL` in the environment when running outside local development.

## Game records database

The leaderboard reads the game's separate SQLite file. Set `GEOMETRY_GAME_DATABASE` to a persistent mounted disk path and provide a populated database if the deployed site should show game records. Render's default filesystem is ephemeral, so this external game database is not persisted by the web service automatically.
