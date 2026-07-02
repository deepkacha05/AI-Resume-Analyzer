# AI Resume Analyzer

This project is developed to analyze resumes and compare them with a Job Description (JD) to check ATS compatibility. It helps users identify missing skills and improve their resumes according to job requirements.

## Features

- Upload Resume in PDF format
- Paste Job Description
- Extract skills from resume
- Compare resume with job description
- Generate ATS score
- Show matched skills
- Show missing skills
- Provide suggestions for improvement
- Interactive dashboard with charts

## Technologies Used

- Python
- Streamlit
- NLTK
- Scikit-learn
- Pandas
- Plotly
- pdfplumber
- PyPDF2

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── skills_database.csv
│
├── modules/
│   ├── pdf_extractor.py
│   ├── preprocess.py
│   ├── skill_extractor.py
│   └── ats_calculator.py
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/deepkacha05/AI-Resume-Analyzer.git
```

2. Go to project directory

```bash
cd AI-Resume-Analyzer
```

3. Install required libraries

```bash
pip install -r requirements.txt
```

4. Run the application

```bash
streamlit run app.py
```

## Output

The application provides:

- ATS compatibility score
- Matched keywords
- Missing keywords
- Resume strength analysis
- Suggestions to improve resume

## Future Improvements

- Resume PDF report generation
- Job Description PDF upload support
- Advanced NLP techniques
- More accurate ATS scoring

## Author

DeepKumar Kacha

Computer Engineering Student

GitHub: https://github.com/deepkacha05
