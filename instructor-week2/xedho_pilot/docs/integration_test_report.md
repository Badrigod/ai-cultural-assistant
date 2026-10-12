
# KHAYRHAYE LIVING HERITAGE
## Thursday — Integration Test Report

Project: Museum Artifact Digitization Pilot
Report Date: October 2, 2026
Version: 0.1
Status: Internal Development Testing

---

## 1. Objective

Verify that the Streamlit application correctly loads
the first five museum artifacts through their unique
identifiers and displays their corresponding digital
content.

Test Environment:

- Operating System: macOS
- Programming Language: Python
- Web Framework: Streamlit
- Data Format: JSON
- Application: app.py
- Test Address: http://localhost:8501

Testing was conducted locally. No public deployment
or publication approval is claimed.

## 2. Artifact Page Testing

| Artifact ID | Artifact Name | Route Test |
|---|---|---|
| KHH-001 | Dhiil | Passed |
| KHH-002 | Dambiil | Passed |
| KHH-003 | Kabad | Passed |
| KHH-004 | Jalxaad | Passed |
| KHH-005 | Xedho | Passed |

All five artifact pages were reported working
during local browser testing.

## 3. Individual Artifact URLs

KHH-001:
http://localhost:8501/?artifact=KHH-001

KHH-002:
http://localhost:8501/?artifact=KHH-002

KHH-003:
http://localhost:8501/?artifact=KHH-003

KHH-004:
http://localhost:8501/?artifact=KHH-004

KHH-005:
http://localhost:8501/?artifact=KHH-005

These addresses are private development routes.
They are not public museum URLs.

## 4. Functional Test Results

| Test Case | Status |
|---|---|
| Load individual artifact by ID | Passed |
| Display corresponding artifact record | Passed |
| Display artifact photograph | Passed |
| Display draft publication warning | Passed |
| Display Somali cultural narrative | Passed |
| Display English cultural narrative | Passed (manual test reported) |
| Display language selector | Passed |
| Display artifact question interface | Visible |
| QR scanning and destination testing | Pending |
| Audio narration playback | Not yet verified |
| Visitor analytics accuracy | Not yet verified |

Note: Visibility of the question interface does not
constitute verification of every chatbot response.

## 5. Screenshot Evidence

Evidence directory:

evidence/screenshots/

Recommended evidence files:

- khh001_dhiil.png
- khh002_dambiil.png
- khh003_kabad.png
- khh004_jalxaad.png
- khh005_xedho.png

Dhiil's Streamlit screenshot has already been captured.

Screenshots for the remaining pages should be saved
to the evidence directory for final handoff.

## 6. Existing Technical Validation

Previous validation confirmed:

- Five valid JSON records.
- Five artifact photographs available.
- Source references INV-001 to INV-005.
- Three existing automated tests passed.

Evidence:
docs/validation_report.txt

## 7. Publication Restrictions

Although local page routing works, all records
remain drafts.

Publication is blocked because:

1. Image permissions are unconfirmed.
2. Museum approval is pending.
3. Cultural storytelling requires editorial review.

Development functionality must not be interpreted
as authorization for public deployment.

## 8. Overall Test Conclusion

The five-artifact Streamlit page-routing milestone
has been completed successfully based on the
reported local browser tests.

QR integration, visitor-event verification and
final publication approval remain outstanding.

Report Status: Ready for internal technical review.
