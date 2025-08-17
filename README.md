# Newspaper Issue XML Schema (XSD)

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

Validate your XML files describing newspaper issues against this schema to ensure data consistency and integrity.

## Schema Details

- Developed with XML Schema 1.0 standards.
- Custom simple types and enumerations enforce format and controlled vocabularies.
- Extensible for additional fields as needed.

---


