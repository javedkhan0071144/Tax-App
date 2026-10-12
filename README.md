# Professional Tax Challan System — Starter Project

This is a local Windows starter app built around the uploaded `Challanstax KS 26-27.xlsm` workbook and `Challans Professional tax KS 26-27.docx` Word file.

## Features included
- Dashboard and taxpayer register
- Search by serial number, business name, or category
- Add and edit records
- Import records from the included Excel workbook
- Export current database records to Excel
- Generate an editable Word challan per selected record
- Attempt automatic PDF conversion when LibreOffice is installed
- SQLite database stored in `data/challans.db`

## Run it (Windows)
1. Extract this ZIP into a folder such as `C:\ProfessionalTaxChallan`.
2. Install Python 3.11 or newer from python.org. During installation, tick **Add Python to PATH**.
3. Double-click `RUN-WINDOWS.bat`.
4. Wait until the terminal says the server is running.
5. Open `http://127.0.0.1:5000` in your browser.
6. Click **Import Excel** once.
7. Select a taxpayer and click **Generate challan**.

Keep the black terminal window open while using the app. To stop, press `Ctrl+C`. Start again by double-clicking the BAT file.

## IMPORTANT: Mail merge template setup
The uploaded Word file contains example text rather than explicit `{{Field Name}}` merge tags. The application does not guess where each field should go, because that could damage the official challan layout.

To activate reliable mail merge:
1. Open `templates/Challans Professional tax KS 26-27.docx` in Microsoft Word.
2. Save a working copy first.
3. In each of the three challan copies, replace the example taxpayer/business name with `{{Owner Name}}`.
4. Replace the displayed category with `{{Category}}` if the category is printed in that location.
5. Replace the period text with `{{Financial Period}}`.
6. Replace the tax amount text with `{{Cr Tax}}` or `{{TotalFormatted}}`, matching the correct field on your official template.
7. Replace the amount-in-words text with `{{Amount in words}}`.
8. Replace the last-date text with `{{Last Date}}`.
9. Save the file under the same template filename.
10. Generate a challan and check the Word file and PDF before official printing.

Use exactly the braces shown, including both curly braces. If a merge field is not printed in the current template, add it only where that data belongs. The merge code replaces `{{Field Name}}` placeholders in Word XML and is designed to keep the page layout.

## Workbook fields observed
The main worksheet is `Professional Challan`. The headers include:
`Sr No`, `Paid`, `dt`, `Month`, `Bank`, `Special Remarks`, `Cate.`, `Circle`, `Temp Serial No`, `Owner Name`, `Detials`, `PP`, `cr Period`, `To`, `Ar Period`, `Cr Tax`, `Ar tas`, `Surchage`, `Total`, `Day`, `Month (2)`, `Yuear`, `Amount in words`, `Remarks`, `Eti`, `Remarks -1`, `Remarks 2`.

The workbook contains duplicate `Month` headers; the importer renames duplicate headers as `Month (2)` so data is not lost.

## PDF conversion
For automatic PDF output, install LibreOffice and ensure `soffice.exe` is available in PATH. Without it, the app downloads the generated Word document instead and shows a message.

## Important limitations / before official use
- This is a local prototype, not yet a shared multi-computer system.
- It does not record or verify payments.
- Tax calculations should be reviewed and approved before production use.
- Verify every merged field and all three challan copies against the official template.
- Make a backup of the `data` folder regularly.
- Do not expose this development server to the internet.
