# AI Recruitment System (Streamlit) - GitHub Ready
This repository is prepared for deployment on Streamlit Community Cloud.

## Features
- Candidate & HR registration/login
- Resume upload & parsing (PDF, DOCX, TXT) with spaCy NER support
- Semantic matching using SBERT (sentence-transformers)
- Interview scheduler with email notifications (SMTP)
- HR Dashboard with shortlist & export

## Setup (Local testing)
1. Clone the repo
2. Create venv and install requirements:
   python -m venv venv
   source venv/bin/activate     # Windows: venv\Scripts\activate
   pip install -r requirements.txt
3. Download spaCy model:
   python -m spacy download en_core_web_sm
4. (Optional) Set SMTP env vars (for sending emails):
   export SMTP_USER='you@example.com'
   export SMTP_PASS='app_password'
5. Run locally:
   streamlit run app.py

## Deploy to Streamlit Cloud
1. Create a new GitHub repository and push this project.
2. Go to https://streamlit.io/cloud and link your GitHub account.
3. Create a new app -> select the repository and branch.
4. Set Secrets (in Streamlit Cloud dashboard): SMTP_USER, SMTP_PASS, SMTP_HOST (optional), SMTP_PORT (optional).
5. Deploy.

Notes:
- The first time SBERT runs it will download model weights; ensure internet access.
- For production, secure credentials and consider a managed DB.
