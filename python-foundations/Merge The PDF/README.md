# 📄 PDF Merger Tool

A simple Python script to merge multiple PDF files from a folder into a single PDF.  
It also allows you to **preview available PDFs**, **select specific ones**, and **confirm the merge order** before creating the final file.

---

## 🚀 Features
- Lists all `.pdf` files in the chosen folder.
- Lets you select which files to merge (instead of merging everything).
- Maintains the order you specify when selecting files.
- Asks for confirmation before merging.
- Saves the merged file in the same folder (default name: `merged.pdf`).

---

Install dependency:
```bash
pip install pypdf
python -m pip install pypdf
```

---

## 📝 Example Run
```bash
Enter your folder path: 
📂 PDFs found:
1. report.pdf
2. notes.pdf
3. invoice.pdf
Enter file numbers to merge (comma-separated): 3,1
👉 You selected these files in this order:
- invoice.pdf
- report.pdf
Proceed with merging? (y/n): y

✅ PDFs merged successfully into: C:/Users/xyz/abc/merged.pdf
```

