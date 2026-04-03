FROM python:3
 
WORKDIR /app
 
# Install dependencies first (cache layer)
COPY .venv/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
 
# The actual source is mounted at runtime via volume,
# so no COPY . . needed — keeps local changes live.
 
EXPOSE 8000
 
# Run as root to avoid any permissions issues with manage.py / db.sqlite3
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]