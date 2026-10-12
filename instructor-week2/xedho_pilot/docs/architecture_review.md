
# KHAYRHAYE LIVING HERITAGE
## Architecture Review and Issue Log

Version: 0.1
Status: Draft for Supervisor Review
Scope: Pilot Artifacts KHH-001 to KHH-005

---

## 1. Architecture Overview

The pilot uses a local Python application with
JSON-based artifact records.

The current structure supports:

- Individual digital artifact identification.
- Original inventory mapping.
- Somali and English draft narratives.
- Local artifact photographs.
- Source-backed information passages.
- Editorial and publication status fields.
- JSON validation and automated testing.

The architecture separates inventory information,
cultural interpretation, source evidence and
publication approval.

## 2. Current Project Components

| Component | Implementation | Status |
|---|---|---|
| Artifact records | JSON files | Implemented |
| Photographs | Local assets folder | Available |
| Data validation | validate.py | Working |
| Core logic | core.py | Working |
| Automated tests | pytest | 3 passed |
| Data dictionary | Markdown | Prepared |
| Data Model v0.1 | Markdown | Prepared |
| Xedho mapping | Markdown | Prepared |
| ERD | Mermaid | Created |
| Approval workflow | Draft fields and release checks | Awaiting authorization |
| QR integration | make_qr.py | End-to-end testing pending |
| Visitor interaction data | SQLite pilot file | Detailed review pending |

## 3. Known Issues and Dependencies

| ID | Issue | Priority | Proposed Action |
|---|---|---|---|
| ISS-001 | Image permissions unconfirmed | High | Request written authorization. |
| ISS-002 | Museum approval pending | High | Arrange content review with Omar. |
| ISS-003 | Somali narratives require review | Medium | Assign language/cultural reviewer. |
| ISS-004 | Jalxaad category discrepancy | Medium | Confirm classification with museum. |
| ISS-005 | Artifact naming conventions | Medium | Confirm preferred Somali spellings. |
| ISS-006 | QR end-to-end testing pending | Medium | Test artifact page and QR destination. |
| ISS-007 | Future database architecture undecided | Low | Review conceptual ERD with supervisor. |
| ISS-008 | Visitor analytics requirements | Medium | Confirm required events and privacy rules. |

## 4. Technical Verification

Current validation evidence:

- Five valid artifact JSON records.
- Five local artifact photographs found.
- Five records checked by the project validator.
- Three automated tests passed.
- Combined validation report generated.

All records remain blocked from publication
pending permission and museum approval.

Evidence file:
docs/validation_report.txt

## 5. Recommendations for Supervisor Review

Questions for Omar:

1. Who will authorize publication of photographs?
2. Who will review Somali and English narratives?
3. Should Jalxaad remain classified under Clothing
   & Textiles or be reclassified?
4. Are the proposed data entities sufficient?
5. Which visitor interaction metrics are required?
6. What should be included in Friday's pilot demonstration?

## 6. Next Activities

- Review the data model and relationship diagram.
- Test artifact pages and QR code destinations.
- Record test screenshots.
- Prepare the final handoff checklist.
- Prepare the pilot demonstration.
- Record outstanding dependencies.

## 7. Current Project Status

The data preparation and conceptual architecture
milestones are complete as draft deliverables.

The remaining work concerns end-to-end integration,
testing, editorial review and authorization.

Document Status: Ready for internal supervisor review.
