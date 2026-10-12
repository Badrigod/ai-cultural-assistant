
# KHAYRHEYE LIVING HERITAGE
## Week 1 — Project Demonstration

Prepared by: Waberi Waberi
Status: Internal Practicum Demonstration

---

## 1. Introduction 

Good morning Omar,

Today, I would like to present the work completed
during the first week of our Khayrheye Living
Heritage practicum.

Our objective was to establish a digital foundation
for documenting Somali cultural artifacts, preserving
their information, and creating an accessible
bilingual museum experience.

For the initial pilot, I worked on five artifacts:

- KHH-001 — Dhiil
- KHH-002 — Dambiil
- KHH-003 — Kabad
- KHH-004 — Jalxaad
- KHH-005 — Xedho

---

## 2. Data Preparation 

Each artifact now has a structured JSON record
containing:

- Unique artifact identifier.
- Inventory information.
- Materials and traditional use.
- Linked photograph.
- English and Somali draft stories.
- Inventory source references.
- Publication and review status.

We also prepared a Data Dictionary, Data Model v0.1,
Xedho Mapping, and an Entity Relationship Diagram.

These documents provide a foundation for future
database development.

---

## 3. Live Streamlit Demonstration

Open the local Streamlit application.

Demonstrate the Dhiil page:

http://localhost:8501/?artifact=KHH-001

Show:

1. Artifact name and photograph.
2. English cultural story.
3. Somali language selection.
4. Draft publication warning.
5. Artifact question interface.

Next, demonstrate navigation to another artifact:

http://localhost:8501/?artifact=KHH-005

Explain that all five artifacts have individual
development URLs.

---

## 4. QR Code and Testing Results

Five private development QR codes were generated.

Each code was automatically decoded using OpenCV
and compared against its intended artifact URL.

Results:

- JSON validation: 5/5 passed.
- Artifact page testing: 5/5 reported working.
- QR decoding: 5/5 passed.
- Automated Python tests: 3/3 passed.
- Screenshot evidence: 5 files saved.

Cross-device QR scanning remains pending.

---

## 5. Outstanding Issues

Although the technical pilot is working locally,
the artifacts are not yet approved for publication.

We still require:

- Photograph publication permissions.
- Museum approval.
- Cultural-content verification.
- English and Somali narrative review.
- Confirmation of the Jalxaad classification.
- Additional end-to-end integration testing.

We would appreciate the museum team's guidance
on these matters.

---

## 6. Closing Statement

This first milestone provides a working technical
foundation for the digital museum.

Our proposed next steps are to validate the cultural
information, obtain the required permissions,
complete the remaining integration tests, and
continue developing the visitor experience.

Thank you, Omar. We welcome your feedback and
guidance on the next project priorities.
