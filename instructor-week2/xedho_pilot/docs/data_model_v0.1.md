
# KHAYRHAYE LIVING HERITAGE
## Data Model v0.1

Document Type: Technical Design
Status: Draft
Pilot Scope: Artifacts KHH-001 to KHH-005
Reference Artifact: KHH-005 (Xedho)

---

## 1. Purpose

The purpose of this document is to define a consistent
data structure for the Khayrhaye Living Heritage
digital museum pilot.

The model supports:

- Artifact identification and inventory tracking.
- Somali and English cultural storytelling.
- Photograph and multimedia references.
- Source traceability.
- Museum review and approval.
- Source-backed information retrieval.
- Future QR and visitor interaction features.

The current implementation uses JSON files.
The relational structure described below is a
conceptual design for future database development.

## 2. Core Data Entities

### Entity 1: Artifact

Represents an individual museum object.

Primary Key: artifact_id

Fields:
- artifact_id
- inventory_id
- inventory_row
- name_so
- name_en
- category
- brief_description
- materials
- traditional_use
- observed_visual_features
- origin
- cultural_significance
- status

Example:

artifact_id: KHH-005
inventory_id: 5
name_so: Xedho
status: draft

### Entity 2: Media

Stores information about photographs and other
digital media associated with artifacts.

Proposed Primary Key: media_id
Foreign Key: artifact_id

Fields:
- media_id
- artifact_id
- path
- caption
- owner
- permission

Current implementation:
The image information is embedded inside each
artifact JSON record.

### Entity 3: Cultural Content

Stores cultural narratives and available transcripts.

Proposed Primary Key: content_id
Foreign Key: artifact_id

Fields:
- content_id
- artifact_id
- language
- story
- transcript
- review_status

Supported languages:
- so: Somali
- en: English

Current implementation:
story_so, story_en, transcript_so and transcript_en
are stored directly in each artifact JSON record.

### Entity 4: Source

Maintains traceability between artifact information
and supporting references.

Primary Key: source_id
Relationship: Artifact to Source

Fields:
- id
- title
- location
- approved
- note

Example:

Source ID: INV-005
Artifact: KHH-005
Source Type: Original inventory spreadsheet

### Entity 5: Passage

Stores individual source-backed information units
that may support search and cultural information
retrieval.

Proposed Primary Key: passage_id
Foreign Key: source_id

Fields:
- passage_id
- source_id
- language
- text
- keywords
- intent
- preview_only
- approved

Example passage intents:
- description
- material
- use

The current Xedho pilot contains six passages.

### Entity 6: Approval

Records authorization and editorial review.

Proposed Primary Key: approval_id
Foreign Key: artifact_id

Fields:
- approval_id
- artifact_id
- reviewer
- date
- notes
- status

Publication must remain blocked until the required
review and permission conditions are satisfied.

### Entity 7: Visitor Event

Supports future interaction analytics.

Proposed Primary Key: event_id
Foreign Key: artifact_id

Fields:
- event_id
- artifact_id
- event_type
- timestamp
- language

Examples:
- page_view
- language_selected
- audio_play

This entity represents planned or existing pilot
interaction functionality, not proof of a deployed
public analytics system.

---

## 3. Entity Relationships

Proposed cardinalities:

- One Artifact can have many Media records.
- One Artifact can have multiple Cultural Content records.
- One Artifact can reference multiple Sources.
- One Source can support multiple Passages.
- One Artifact can have multiple Approval records.
- One Artifact can have multiple Visitor Events.

For the current pilot, each source is embedded within
its artifact JSON record.

A future relational implementation should introduce
an Artifact-Source junction table if a single source
can support several artifacts.

---

## 4. Artifact Identifier Mapping

| Artifact ID | Inventory ID | Source ID |
|---|---:|---|
| KHH-001 | 1 | INV-001 |
| KHH-002 | 2 | INV-002 |
| KHH-003 | 3 | INV-003 |
| KHH-004 | 4 | INV-004 |
| KHH-005 | 5 | INV-005 |

All identifiers must remain unique and traceable
to the original museum inventory.

---

## 5. Data Quality Rules

1. Every artifact must have a unique artifact_id.
2. Inventory identifiers must be preserved.
3. Sources must be traceable.
4. Missing cultural information must not be invented.
5. Unverified narratives must remain draft.
6. Images require confirmed publication permission.
7. Museum approval must be recorded before release.
8. Somali and English content require editorial review.
9. JSON records must pass syntax validation.
10. Public content must use approved source-backed text.

---

## 6. Implementation Status

Current implementation:
- Five draft JSON artifact records.
- Five linked photographs.
- Source references INV-001 through INV-005.
- Somali and English draft narratives.
- Source-backed passages.
- Approval and image-permission fields.
- JSON validation and automated tests.

Future design:
- Normalized relational database.
- Independent media and cultural-content records.
- Expanded approval history.
- QR route integration.
- Visitor interaction reporting.

## 7. Outstanding Design Decisions

- Confirm final category for Jalxaad.
- Confirm final artifact naming conventions.
- Confirm authorized cultural-content reviewer.
- Confirm image ownership and permissions.
- Decide whether future data storage will remain
  JSON-based or migrate to a relational database.

Document Version: 0.1
