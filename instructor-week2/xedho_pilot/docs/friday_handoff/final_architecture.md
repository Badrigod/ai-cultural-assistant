
# KHAYRHEYE LIVING HERITAGE
## Final Pilot Architecture and Implementation Summary

**Project:** Khayrheye Somali Cultural Museum Digitization
**Document Version:** 1.0
**Reporting Milestone:** Friday, October 2, 2026
**Prepared by:** Waberi Waberi
**Status:** Technical Pilot Completed – Museum Approval Pending

---

## 1. Executive Summary

The Khayrheye Living Heritage pilot aims to digitize Somali cultural artifacts through structured inventory records, photographs, bilingual cultural storytelling, and interactive digital experiences.

During the first project milestone, five museum artifacts were successfully converted into structured JSON records and integrated into a local Streamlit application.

The pilot supports individual artifact pages, English and Somali storytelling, photograph display, source-backed information, and private QR code navigation testing.

All five records passed JSON validation, and the three existing automated Python tests passed.

Public release remains subject to museum authorization and confirmation of image permissions.

---

## 2. Pilot Artifacts

| Artifact ID | Artifact Name | Source ID | Status |
|---|---|---|---|
| KHH-001 | Dhiil | INV-001 | Draft validated |
| KHH-002 | Dambiil | INV-002 | Draft validated |
| KHH-003 | Kabad | INV-003 | Draft validated |
| KHH-004 | Jalxaad | INV-004 | Draft validated |
| KHH-005 | Xedho | INV-005 | Draft validated |

Every artifact includes:

- A unique digital identifier.
- Original inventory information.
- A linked photograph.
- Draft English and Somali storytelling.
- Source references.
- Review and approval metadata.
- Searchable source-backed passages.

---

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application and data processing |
| Streamlit | Interactive museum interface |
| JSON | Artifact data storage |
| Markdown | Technical documentation |
| QRCode (Python) | QR image generation |
| OpenCV | QR decoding verification |
| Pytest | Automated testing |
| VS Code | Development environment |
| macOS | Local development platform |

The current pilot uses JSON-based storage.

A normalized relational database is proposed for future development but has not yet been implemented.

---

## 4. System Architecture

The current pilot follows this data flow:

Museum Inventory
       |
       v
Artifact JSON Records
       |
       v
Python Core Logic
       |
       v
Streamlit Application
       |
       +---- Artifact Photograph
       |
       +---- English Storytelling
       |
       +---- Somali Storytelling
       |
       +---- Source-backed Questions
       |
       +---- Draft/Approval Status
       |
       v
Private Artifact Page
       ^
       |
Development QR Code

Each artifact is accessed through a unique identifier in the application URL.

---

## 5. Application Components

| Component | Function |
|---|---|
| app.py | Streamlit interface and artifact routing |
| core.py | Shared artifact processing functions |
| validate.py | Artifact validation and release-readiness checks |
| make_qr.py | Original Xedho QR generator |
| data/ | Individual artifact JSON records |
| assets/ | Photographs and other local media |
| docs/ | Technical documentation |
| tests/ | Automated tests |
| evidence/ | Screenshots and testing evidence |

---

## 6. Artifact Routing

The application supports five individual development routes.

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

All five routes were manually tested in Streamlit.

These addresses are intended for private local development only.

---

## 7. Data Model v0.1

The conceptual data model consists of seven primary entities:

1. Artifact
2. Media
3. Cultural Content
4. Source
5. Passage
6. Approval
7. Visitor Event

An Artifact-Source junction entity is also proposed for a future relational implementation.

The initial pilot maintains these relationships primarily through embedded JSON structures.

Supporting documentation:

- docs/data_dictionary.md
- docs/data_model_v0.1.md
- docs/xedho_mapping.md
- docs/data_relationship_diagram.md

---

## 8. Technical Testing Results

The following results were achieved during the first development milestone:

| Test | Result |
|---|---|
| JSON syntax validation | 5/5 passed |
| Artifact photograph availability | 5/5 found |
| Streamlit artifact routing | 5/5 tested |
| QR code generation | 5/5 successful |
| QR destination decoding | 5/5 passed |
| Automated Python tests | 3/3 passed |
| Screenshot evidence | 5/5 saved |

QR verification was performed using OpenCV QRCodeDetector.

Cross-device QR scanning remains pending because the development QR codes currently use localhost URLs.

---

## 9. Testing Evidence

The following documentation has been prepared:

- docs/validation_report.txt
- docs/integration_test_report.md
- docs/integration_issue_log.md
- docs/qr_test_report.md

Five artifact screenshots are stored in:

evidence/screenshots/

The development QR test images are stored in:

evidence/qr_tests/

---

## 10. Publication and Approval Requirements

All artifact records currently remain in draft status.

Before public release, the following requirements must be completed:

1. Confirm artifact photograph ownership.
2. Obtain permission to publish photographs.
3. Review Somali cultural storytelling.
4. Review English cultural storytelling.
5. Confirm artifact descriptions and materials.
6. Obtain final museum approval.

The Jalxaad inventory classification also requires review because its recorded category is Clothing & Textiles, while the inventory describes a clay vessel.

---

## 11. Future Development

Potential next-stage improvements include:

- Permanent museum-hosted artifact URLs.
- Production QR code integration.
- Approved Somali and English audio narration.
- Extended cultural storytelling.
- Visitor interaction analytics.
- Relational database implementation.
- Augmented reality experiences.
- Additional artifact digitization.

These features are proposed future enhancements and should not be presented as completed pilot functionality.

---

## 12. Conclusion

The first five-artifact technical pilot has completed its data preparation, local application integration, QR encoding verification, and documentation milestones.

The project now provides a functional local foundation for presenting Somali cultural artifacts through structured digital records and bilingual storytelling.

The pilot is ready for internal demonstration and supervisor feedback.

Museum content approval, photograph permissions, and additional integration testing remain outstanding.

**Document Status: Ready for Internal Handoff Review.**
