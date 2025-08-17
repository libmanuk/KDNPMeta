# Newspaper Issue XML Schema (XSD) & Validation Script

This repository contains the XML Schema Definition (XSD) for validating **Kentucky Digital Newspaper Program (KDNP) newspaper issue metadata**. It enforces strict formats and controlled vocabularies for various fields such as dates, identifiers, and geographic data relevant to Kentucky newspaper collections.

## Features

- **Date Fields:**
  - `IssueDate` must follow `YYYY-MM-DD` format.
  - `Year` is a 4-digit number.
  - `Month`, `Day`, and `Edition` are two-digit numbers.

- **Identifiers:**
  - `KDNPTitleCode`: exactly 3 lowercase letters (a–z).
  - `KDNPControlIdentifier`: 13 characters; first 3 are lowercase letters, followed by 10 digits.

- **Geographic Fields:**
  - `Region` must be one of six predefined Kentucky regions.
  - `County` must be a valid Kentucky county name (120 counties enumerated).

## Usage

Validate KDNP XML files describing newspaper issues against this schema to ensure data consistency and integrity.

## Schema Details

- Developed with XML Schema 1.0 standards.
- Custom simple types and enumerations enforce format and controlled vocabularies.
- Extensible for additional fields as needed.

---

📄 XML Validation Script

This Python script validates multiple XML files in a directory against a specified XSD (XML Schema Definition) file using the lxml library. It logs any validation or parsing errors into a log file.

📁 File Structure and Paths

XSD Schema File
XSD_PATH
Path to the .xsd file used to validate XML files.

XSD_PATH = r"C:\Users\eweig\PaperVault\MetadataDictionary\kdnp_meta_dictionary.xsd"


XML Files Directory
XML_DIR
Directory containing XML files to be validated.

XML_DIR = r"C:\Users\eweig\PaperVault\MetadataDictionary\testmeta"


Validation Log File
LOG_FILE
Path where validation errors (if any) are written.

LOG_FILE = r"C:\Users\eweig\PaperVault\MetadataDictionary\validation_errors.log"

🛠️ Function: validate_xml_files(xsd_path, xml_dir, log_file)
Description:

Validates each .xml file found in the provided directory (and subdirectories) against the provided XSD schema.

Steps:

Load XSD schema using lxml.etree.XMLSchema.

Traverse the XML directory using os.walk.

Parse and validate each .xml file:

If validation fails, the schema error log is captured.

If parsing fails, the exception message is recorded.

Write results to log file:

If errors are found, they are written to the specified log file.

If no errors are found, a success message is logged.

Example Output in Log File:
XML Validation Errors:

File: C:\path\to\file.xml
  Line 15: Element 'title': This element is not expected. Expected is ( name ).

File: C:\path\to\another_file.xml
  Parsing error: Premature end of data in tag book line 3

✅ Success Message

If all XML files pass validation, the log will contain:

All XML files validated successfully.

▶️ Execution

To run the script directly:

python validate_xml.py


Make sure this block is at the bottom of the file:

if __name__ == "__main__":
    validate_xml_files(XSD_PATH, XML_DIR, LOG_FILE)

🧩 Dependencies

Python 3.x

lxml package

Install with:

pip install lxml

🔐 Notes

File paths are Windows-specific (using raw strings r"...").

Ensure the XSD file is well-formed, or schema loading will fail.

XML parsing errors (e.g., malformed XML) are caught and logged.
