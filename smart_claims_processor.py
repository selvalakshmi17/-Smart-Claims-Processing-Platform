
---

## ✅ 2. `smart_claims_processor.py`

```python
import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def classify_claim(text):
    if "hospital" in text or "medical" in text:
        return "Health", "High", "Health Claims Team"
    elif "car" in text or "accident" in text:
        return "Vehicle", "Medium", "Vehicle Claims Team"
    elif "fire" in text or "property" in text:
        return "Fire", "High", "Property Claims Team"
    else:
        return "General", "Low", "General Processing Team"

def main():
    sample_pdf = "sample_claim.pdf"  # Put your sample PDF here
    extracted_text = extract_text_from_pdf(sample_pdf)
    claim_type, priority, team = classify_claim(extracted_text)
    
    print("📄 Extracted Claim Details:")
    print(f"Claim Type: {claim_type}")
    print(f"Priority: {priority}")
    print(f"Routed To: {team}")
    print("Status: Awaiting Review")

if __name__ == "__main__":
    main()
