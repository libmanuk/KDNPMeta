import os
from lxml import etree

# Path to the XSD schema file
XSD_PATH = r"C:\PaperVault\MetadataDictionary\kdnp_meta_dictionary.xsd"

# Directory to search for XML files
XML_DIR = r"C:\PaperVault\IssueMetadata"

# Log file to write validation errors
LOG_FILE = r"C:\PaperVault\MetadataDictionary\validation_errors.log"

def validate_xml_files(xsd_path, xml_dir, log_file):
    # Load XSD schema
    try:
        with open(xsd_path, 'rb') as f:
            schema_doc = etree.parse(f)
        schema = etree.XMLSchema(schema_doc)
    except (etree.XMLSchemaParseError, etree.XMLSyntaxError) as e:
        print(f"Error loading XSD schema: {e}")
        return

    errors = []

    # Walk through xml_dir and validate each .xml file
    for root, _, files in os.walk(xml_dir):
        for file in files:
            if file.lower().endswith('.xml'):
                xml_path = os.path.join(root, file)
                try:
                    doc = etree.parse(xml_path)
                    schema.validate(doc)
                    if not schema.validate(doc):
                        for error in schema.error_log:
                            errors.append(f"File: {xml_path}\n  Line {error.line}: {error.message}\n")
                except (etree.XMLSyntaxError, etree.DocumentInvalid) as e:
                    errors.append(f"File: {xml_path}\n  Parsing/Validation error: {str(e)}\n")
                except Exception as e:
                    errors.append(f"File: {xml_path}\n  Unexpected error: {str(e)}\n")

    # Write errors to log file
    with open(log_file, 'w', encoding='utf-8') as logf:
        if errors:
            logf.write("XML Validation Errors:\n\n")
            logf.writelines(errors)
        else:
            logf.write("All XML files validated successfully.\n")

    print(f"Validation complete. Log file saved at: {log_file}")


if __name__ == "__main__":
    validate_xml_files(XSD_PATH, XML_DIR, LOG_FILE)

