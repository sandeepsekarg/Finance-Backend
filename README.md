# Finance Data Processing Backend

## Business problem that i worked on
1. User exist with different roles.
2. Financial data (Income/expenses) is stored.
3. Users can only perform actions based on their role.

## Would like to add on in Future
1. the System will provide useful summaries.

## Overview
Backend system to manage financial records with role based access control and dashboard analytics.

## Features
- User and Role Management
- Financial Records CRUD
- Record Filtering
- Dashboard Summary APIs
- Role Based Access Control (RBAC)
- Input Validation and Error Handling

## Tech Stack
- FastAPI
- Python
- SQLite
- SQLAlchemy

## How to Run
pip install -r requirements.txt
uvicorn app.main:app --reload

## API Docs
http://127.0.0.1:8000/docs
