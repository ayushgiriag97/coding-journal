#imports
import os
from pypdf import PdfWriter

#helper functions

def list_pdfs(folder_path):
    """Finds the '.pdf' files, sorts them, and shows them."""
    files = sorted(f for f in os.listdir(folder_path) if f.lower().endswith(".pdf"))
    if not files:
        print("❌ No PDF files found.")
    else:
        print("📂 PDFs found:")
        for i, file in enumerate(files, 1):
            print(f"{i}. {file}")
    return files

def select_pdfs(folder_path):
    """Allow user to select specific PDFs to merge."""
    files = list_pdfs(folder_path)
    if not files:
        return []

    choices = input("Enter file numbers to merge (comma-separated): ")
    indices = [int(x.strip()) - 1 for x in choices.split(",") if x.strip().isdigit()]
    selected = [files[i] for i in indices if 0 <= i < len(files)]

    if selected:
        print("\n👉 You selected these files in this order:")
        for file in selected:
            print(f"- {file}")
        confirm = input("Proceed with merging? (y/n): ").strip().lower()
        if confirm != "y":
            print("❌ Merge cancelled.")
            return []
    return selected

def merge_pdfs(folder_path, output_name="merged.pdf"):
    """Main block to do the merging"""
    try:
        if not os.path.isdir(folder_path):
            raise FileNotFoundError(f"Folder not found: {folder_path}")

        # Let user choose PDFs
        selected_files = select_pdfs(folder_path)
        if not selected_files:
            raise ValueError("No valid PDFs selected.")

        pdf_merger = PdfWriter()

        for file in selected_files:
            full_path = os.path.join(folder_path, file)
            pdf_merger.append(full_path)

        output_path = os.path.join(folder_path, output_name)
        with open(output_path, "wb") as f_out:
            pdf_merger.write(f_out)

        print(f"\n✅ PDFs merged successfully into: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")


# Main Execution Block
if __name__ == "__main__":
    folder_path = input("Enter your folder path: ").strip()
    merge_pdfs(folder_path)