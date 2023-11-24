import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_directory(directory_path, output_file):
    # Initialize PdfMerger object
    merger = PdfMerger()

    # Loop through all files in the directory
    for file in os.listdir(directory_path):
        if file.endswith('.pdf'):
            # Append the PDF file to the merger
            merger.append(os.path.join(directory_path, file))

    # Write out the merged PDF to the specified output file
    merger.write(output_file)
    merger.close()
    return output_file

# Example usage
directory_path = 'downloaded_files'
output_file = 'inmates.pdf'
merged_file = merge_pdfs_in_directory(directory_path, output_file)
print(f"Merged PDF saved as: {merged_file}")
