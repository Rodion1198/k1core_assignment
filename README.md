## Local Setup

### Pre-requirements

1. docker
2. docker-compose
3. make (CLI)

---

### Setup

1. (only once) Create .env file with environment variables from the template.
   Edit the created `.env` file with your parameters:

```bash
cp .env.example .env
# edit .env file as you need
```

2. (only once or by request) Apply migrations

```bash
make mm
```

3. (only once) Setup Static Files

```bash
make bash
python manage.py collectstatic --noinput
exit
```

4. (only once or by request) Fill the database by default currencies and providers

```bash
make bash
python manage.py populate_db
exit
```

5. (only once or by request) Create a superuser for the Admin panel. Specify your own credentials

```bash
make bash
python manage.py create_default_superuser --username admin --password admin123 --email admin@admin.com
exit
```

6. (every time) Launch the project

```bash
make run  # common mode
# or
make run-d  # daemon mode
```
