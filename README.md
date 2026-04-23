<img width="1436" height="852" alt="Screenshot 2026-04-22 at 9 19 04 PM" src="https://github.com/user-attachments/assets/e72365d7-cc88-44bd-81d0-f5dfd68cef56" />
# Interest-Based Recommendation System

A live demonstration project for college based on the **cloud computing domain**.

## Features
- Interest-based recommendation logic
- Streamlit web interface for live demo
- Sample cloud-computing resource dataset
- Easy local execution

## Project Structure
- `app.py` - Streamlit frontend and app controller
- `src/recommender.py` - recommendation logic
- `src/data_loader.py` - CSV dataset loader
- `data/resources.csv` - sample resource dataset
- `requirements.txt` - dependencies

## How It Works
The system uses **content-based filtering**:
1. The user selects interests such as AWS, Docker, Kubernetes, Security, DevOps, etc.
2. Each learning resource contains tags.
3. The recommendation engine computes similarity using tag overlap.
4. The system ranks and returns the top matching resources.

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Demo Use Case
For live demonstration, select multiple interests like:
- AWS + Docker + Kubernetes
- Security + Networking
- Azure + Terraform + Automation

Then click **Generate Recommendations**.

## Possible Future Enhancements
- User login and profile storage
- Database integration (MySQL / MongoDB)
- Deployment on AWS / Azure / GCP
- Hybrid recommendation using user behavior data
