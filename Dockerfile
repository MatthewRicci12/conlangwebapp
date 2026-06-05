FROM python:3
 
WORKDIR /app
 
# Install dependencies first (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#RUN npm install

EXPOSE 8000
 
# Run as root to avoid any permissions issues with manage.py / db.sqlite3
ENTRYPOINT ["./entrypoint.sh"]