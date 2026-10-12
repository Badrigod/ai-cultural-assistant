
# KHAYRHAYE LIVING HERITAGE
## QR Integration Test Report

Version: 0.1
Date: October 2, 2026
Status: Private Development Testing

### 1. Objective

Verify that each pilot artifact has a separate QR image
containing the correct Streamlit development URL.

### 2. Test Environment

- Python virtual environment (.venv)
- qrcode library
- OpenCV QRCodeDetector
- Local Streamlit server: localhost:8501
- Platform: macOS

### 3. QR Verification Results

| Artifact ID | QR Filename | Result |
|---|---|---|
| KHH-001 | dhiil_qr_TEST.png | PASS |
| KHH-002 | dambiil_qr_TEST.png | PASS |
| KHH-003 | kabad_qr_TEST.png | PASS |
| KHH-004 | jalxaad_qr_TEST.png | PASS |
| KHH-005 | xedho_qr_TEST.png | PASS |

Total: 5/5 passed.

### 4. Verification Method

1. Generated five separate QR images.
2. Encoded a distinct localhost development URL in each.
3. Decoded each image using OpenCV.
4. Compared the decoded URL against the expected artifact ID.
5. Confirmed that all five comparisons matched.

### 5. Evidence

QR images are stored in:

evidence/qr_tests/

Artifact development pages were previously tested
successfully in the local Streamlit browser.

### 6. Limitations

Localhost URLs are valid only on the host computer.

Cross-device scanning has not yet been verified.

These test QR images must not be publicly distributed
or treated as permanent museum QR codes.

Image permissions and museum approval remain pending.

### 7. Conclusion

All five QR code images passed automated
destination verification.

The QR generation and encoding milestone is complete.
Network accessibility and public deployment remain
outside the scope of this test.
