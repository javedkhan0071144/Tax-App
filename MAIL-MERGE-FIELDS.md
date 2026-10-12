# Mail merge field mapping
The template processor expects Word placeholders in this exact form:
- `{{Owner Name}}` — business/taxpayer name from Excel column Owner Name
- `{{Category}}` — from Cate.
- `{{Financial Period}}` — from cr Period (e.g. 2026-27)
- `{{Cr Tax}}` — from Cr Tax
- `{{TotalFormatted}}` — total formatted as a number with thousands separators
- `{{Amount in words}}` — from Amount in words; if blank, generated from Total
- `{{Last Date}}` — currently configured as 30-09-2026 in app.py; change before use if the department changes the due date.
- Any other `{{Exact Excel Header}}` — value from that field, such as `{{Circle}}` or `{{Bank}}`.

Important: insert these placeholders into the existing Word template at the correct positions. Do not assume the example text can be safely replaced without visually checking the output.
