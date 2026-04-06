bash
#!/bin/bash
pip install -r requirements.txt
uvicorn course_recommender_apis:app --host 0.0.0.0 --port 8000