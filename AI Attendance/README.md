
# Face Attendance (browser embeddings)

Components:
- frontend/checkin.html  -- HTML + JS using face-api.js to compute descriptors and call backend
- backend/app.py         -- FastAPI server to store descriptors, match, and record attendance
- backend/requirements.txt

## Setup 


1. Create & activate venv:
   cd backend
   python -m venv venv
   venv\Scripts\Activate

2. Install Python packages:
   pip install --upgrade pip
   pip install -r requirements.txt

3. Run the backend:
   uvicorn app:app --reload --host 0.0.0.0 --port 8000

4. Serve the frontend:
   cd frontend
   python -m http.server 5500

   Then open: http://localhost:5500/checkin.html

5. How to use:
   - Allow camera access in browser.
   - Register: enter name + student id and click "Capture & Register".
   - Check-in: click "Capture & Check-in".
   - Refresh Attendance to see records.

