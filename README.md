AI Powered Study Buddy (NLP Project)
 Project Overview

AI Powered Study Buddy is a Natural Language Processing (NLP) based web application that helps students automatically generate:

📄 Text Summaries

📝 Short Notes

❓ Quiz Questions

The system accepts text input or PDF files and processes the content using a pre-trained Transformer model to assist students in efficient learning and revision.

🎯 Problem Statement

  1 Students often struggle with:

  2 Reading lengthy study materials

  3 Manually preparing notes

  4 Creating revision questions

  5 Managing large PDF documents

This project aims to reduce manual effort and improve learning efficiency using AI-powered automation.

💡 Proposed Solution

The system:

1 Accepts user text input or PDF upload

2 Extracts and preprocesses text

3 Applies NLP-based summarization

4 Generates structured output (Summary / Notes / Quiz)

5 Displays results through a web interface

🏗️ System Architecture

User Input → Text Extraction → Preprocessing → NLP Model → Output Display

⚙️ Technologies Used
🔹 Frontend

HTML

CSS

🔹 Backend

Python

Flask

🔹 AI / NLP

Hugging Face Transformers

Pre-trained Transformer Model (BART)

Abstractive Summarization

🔹 Additional Libraries

PyPDF2 (PDF text extraction)

Torch

Transformers

🔄 Working Algorithm

1 User enters text or uploads a PDF file.

2 PDF text is extracted using PyPDF2.

3 Extracted content is cleaned and preprocessed.

4 User selects Summary / Notes / Quiz.

5 Text is passed to a Transformer-based NLP model.

6 Generated result is displayed on the Flask web interface.

🚀 Deployment

1 Runs locally using Flask server

2 Can be deployed using:

3 Streamlit

4 Gradio

5 Cloud platforms (Future scope)

📊 Results

The system successfully:

1 Generates meaningful summaries

2 Converts long text into short structured notes

3 Creates quiz questions for revision

4 Extracts text from PDF documents

5 Provides an interactive study experience

🔮 Future Scope

 1 Multilingual support

 2 Speech-to-Text integration

 3 Advanced MCQ quiz generation

 4 Student performance tracking

 5 Full cloud deployment

6 Mobile application version
