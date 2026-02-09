# Backend Setup Instructions

1. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install fastapi uvicorn

3. Run server:
   uvicorn main:app --host 0.0.0.0 --port 8000

4. Access:
   http://localhost:8000

