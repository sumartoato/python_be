# python_be
pip install fastapi uvicorn
py --version   
python -m uvicorn app.main:app --reload
or
py -m uvicorn app.main:app --reload
```open
http://localhost:8000/
http://localhost:8000/docs -> for swagger
http://localhost:8000/redoc ->

app/
├── main.py          # seperti app.js/server.js
├── routers/         # seperti routes/
├── controllers/     # logic controller
├── services/        # business logic
├── repositories/    # akses database
├── models/          # ORM model
├── schemas/         # request/response model (Pydantic)
├── middleware/
├── core/
│   ├── config.py
│   └── security.py
└── database.py

.\.venv\Scripts\Activate.ps1
pip install sqlalchemy psycopg2-binary python-dotenv
python -m pip install fastapi uvicorn sqlalchemy psycopg[binary] python-dotenv

terbaru

app/
├── main.py
│
├── core/
│   ├── config.py
│   ├── database.py
│   ├── security.py
│   ├── dependencies.py
│   └── logger.py
│
├── routers/
│   ├── health.py
│   ├── auth.py
│   └── users.py
│
├── controllers/
│   ├── auth_controller.py
│   └── user_controller.py
│
├── services/
│   ├── auth_service.py
│   └── user_service.py
│
├── repositories/
│   ├── auth_repository.py
│   └── user_repository.py
│
├── models/
│   ├── base.py
│   └── user.py
│
├── schemas/
│   ├── auth_schema.py
│   └── user_schema.py
│
├── middleware/
│   └── auth.py
│
└── utils/
    └── helper.py

.env
requirements.txt