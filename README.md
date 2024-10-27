# MergePDF

 ## PDF Merger App

A Streamlit web application that merges multiple PDF files contained within a ZIP archive into a single PDF document. The application automatically processes PDF files in alphabetical order, making it perfect for combining sequential documents.

## Features

- Upload ZIP files containing multiple PDFs
- Automatically extracts PDFs from a folder within the ZIP file
- Merges PDFs in alphabetical order
- Simple and intuitive web interface
- Instant download of the merged PDF

## Requirements

```
streamlit
PyPDF2
zipfile (built-in)
os (built-in)
```

To install the required packages, run:

```bash
pip install streamlit PyPDF2
```

## Installation

1. Clone this repository or download the source code
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run main.py
   ```
2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)
3. Prepare your PDFs:
   - Place all PDF files you want to merge in a single folder
   - Create a ZIP archive containing this folder
4. Use the app:
   - Click the "Upload a ZIP file containing PDFs" button
   - Select your ZIP file
   - Click "Merge PDFs"
   - Download the merged PDF file

## File Structure Requirements

Your ZIP file should have the following structure:
```
archive.zip
└── folder_name/
    ├── file1.pdf
    ├── file2.pdf
    └── file3.pdf
```

Note: The application expects a folder inside the ZIP file containing the PDFs. PDFs placed directly in the ZIP archive root will not be processed.

## How It Works

1. The application accepts a ZIP file upload
2. Extracts the contents to a temporary directory
3. Looks for a folder within the extracted contents
4. Identifies all PDF files within that folder
5. Merges the PDFs in alphabetical order
6. Provides the merged PDF for download

## Error Handling

The app includes error messages for common issues:
- No folder found in the ZIP archive
- No PDF files found in the folder
- Invalid file formats

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

[Add your chosen license here]
