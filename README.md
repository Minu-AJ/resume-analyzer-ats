# Resume Analyzer (ATS-Based Candidate Screening System)

## Overview
The Resume Analyzer is a Django-based web application that simulates an Applicant Tracking System (ATS) used by recruiters. It allows users to upload resumes and evaluates them based on required job skills, generating a match score.

## Features
- Upload resumes in PDF format  
- Extract text from resumes using PDF processing  
- Automatic skill detection  
- Match score calculation based on job role  
- Admin panel to view and rank candidates  
- Skill comparison (Required vs Detected skills)  

## Tech Stack
- Backend: Python, Django  
- Database: SQLite3  
- Frontend: HTML, CSS (Django Templates)  
- Libraries: pdfplumber  
- Version Control: Git, GitHub  

## How It Works
1. User uploads a resume (PDF)  
2. System extracts text from the resume  
3. Required skills are fetched based on selected job role  
4. Resume skills are detected dynamically  
5. Match score is calculated
6. Candidates are ranked based on score 

## Installation and Setup

Clone the repository:
git clone https://github.com/Minu-AJ/resume-analyzer-ats.git

Navigate to the project directory:
cd resume-analyzer-ats

Create a virtual environment:
python -m venv env

Activate the environment:
env\Scripts\activate (Windows)
source env/bin/activate (Mac/Linux)

Install dependencies:
pip install -r requirements.txt

Run migrations:
python manage.py migrate

Start the development server:
python manage.py runserver

## Purpose
This project is built to:
- Demonstrate real-world ATS functionality  
- Showcase Django backend development skills  
- Improve understanding of text processing and data analysis  

## Future Improvements
- Advanced NLP-based skill extraction  
- Resume ranking dashboard  
- Support for multiple file formats  
- UI enhancements  

## Author
Minu A J  
Python Django Developer  

## Acknowledgment
Inspired by real-world recruitment systems and ATS workflows.
