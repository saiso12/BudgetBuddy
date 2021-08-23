# BudgetBuddy

This project intends to help you keep track of your spending habits and budget automation


# Bill reader using Tesseract OCR engine

- This project deals with the problem of recognizing all the different handrwritten or printed characters and convert them to a machine-readable, digital data format.
- OCR consists of several sub-process to perform this op

  - Image preprocessing
  - Text localization
  - Character segmentation
  - Character recognition
  - Post Processing

We use `Pytesseract` a python wrapper class for Tesseract OCR.

** NOTE : Pytesseract cannot be used directly to perform OCR. We need to have the Tesseract software installed on our systems to perform the OCR on digital data. **

