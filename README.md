**How to run binance app**

1. Pull a branch with app
2. Run a venv
3. Go to project main folder (manage.py level)
4. Execute command: _pip install -r requirements.txt_
5. Execute command: _python manage.py makemigrations binance_
6. Execute command: _python manage.py migrate_
7. To get (update) binance data, execute command: _python manage.py refresh_
8. Run local server (_python manage.py runserver_)
9. Open _http://127.0.0.1:8000/admin/binance/market/_ page
10. Verify if new data exists in the Market table

**Python-Binance API**
- https://python-binance.readthedocs.io/en/latest/general.html