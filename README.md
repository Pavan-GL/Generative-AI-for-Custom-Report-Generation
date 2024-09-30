# Generative AI Document Summarization

This project allows users to upload documents in PDF, DOCX, or TXT format and automatically summarizes them using a Generative AI model (T5) from Hugging Face.

## Features
- Handles multiple document formats (PDF, DOCX, TXT)
- Summarizes text using the T5 transformer model from Hugging Face
- Simple and interactive Streamlit UI

## Business Outcomes
1. **Enhanced Efficiency**: Automating document summarization reduces the time spent by professionals in reviewing lengthy documents.
2. **Improved Accuracy**: Leveraging AI reduces human errors that may occur during manual summarization.
3. **Cost Savings**: Streamlining document review processes leads to overall cost efficiency.
4. **Better Compliance**: Ensures critical information is highlighted, facilitating compliance checks.
5. **Scalability**: Can handle a high volume of documents, allowing firms to scale operations.
6. **Faster Decision-Making**: Provides quick access to key information for stakeholders and clients.

## Tech Stack

Python: The primary programming language used for developing the application.
Streamlit: A web framework used to create the interactive user interface, allowing users to upload documents and view summaries.
Hugging Face Transformers: A library that provides pre-trained models for natural language processing tasks, specifically the T5 or BART model for text summarization.
PyPDF2: A Python library for extracting text from PDF files, enabling the application to read and process PDF documents.
python-docx: A Python library used for reading and extracting text from Microsoft Word (DOCX) documents.
Pandas: Although not directly utilized in the current version, it can be incorporated for handling tabular data if needed in future enhancements.
Streamlit: For building the user interface and presenting the summarized output to users.

## Setup
1. Clone this repository:
   ```bash
   git clone <repo_url>
   cd generative_ai_document_summarization

pip install -r requirements.txt
streamlit run app.py

Usage
Upload a document (PDF, DOCX, or TXT)
View the original text and its summarized version