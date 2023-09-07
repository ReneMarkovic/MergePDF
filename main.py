import streamlit as st
import zipfile
import os
from PyPDF2 import PdfReader, PdfWriter

# Function to merge PDFs
def merge_pdfs(file_paths, output_path):
    pdf_writer = PdfWriter()
    for file_path in file_paths:
        pdf_reader = PdfReader(file_path)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
    with open(output_path, 'wb') as out_pdf_file:
        pdf_writer.write(out_pdf_file)

# Streamlit App
st.title("PDF Merger App")

# Upload Zip file
uploaded_file = st.file_uploader("Upload a ZIP file containing PDFs", type=["zip"])

if uploaded_file is not None:
    # Create a temporary directory to store the unzipped files
    os.makedirs("temp_dir", exist_ok=True)

    # Unzip the uploaded file
    with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
        zip_ref.extractall("temp_dir")

    # Check if a folder exists inside the ZIP file
    folder_found = False
    folder_name = ""
    for item in os.listdir("temp_dir"):
        if os.path.isdir(os.path.join("temp_dir", item)):
            folder_found = True
            folder_name = item
            break

    if not folder_found:
        st.error("No folder found in the ZIP archive.")
    else:
        # Get list of PDF files in the unzipped folder
        pdf_files = [f for f in os.listdir(os.path.join("temp_dir", folder_name)) if f.endswith('.pdf')]
        pdf_files.sort()

        if len(pdf_files) == 0:
            st.error("No PDF files found in the folder inside the ZIP archive.")
        else:
            st.write(f"Found {len(pdf_files)} PDF files.")

            # Merge PDFs
            merge_button = st.button("Merge PDFs")
            if merge_button:
                output_pdf_path = "merged_output.pdf"
                pdf_file_paths = [os.path.join("temp_dir", folder_name, pdf_file) for pdf_file in pdf_files]
                merge_pdfs(pdf_file_paths, output_pdf_path)
                st.success(f"PDFs merged successfully! [Download Merged PDF]({output_pdf_path})")
