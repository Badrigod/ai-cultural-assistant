
# Khayrhaye Living Heritage
## Data Dictionary — Pilot Artifacts 001–005

Document status: Draft  
Work-plan date: Tuesday, September 29, 2026  
Scope: KHH-001 to KHH-005

### 1. Purpose

This document establishes a consistent data structure for the museum's digital artifact records, supporting inventory management, cultural storytelling, source traceability, and bilingual presentation.

### 2. Core Artifact Fields

| Field Name | Data Type | Description | Example |
|---|---|---|---|
| artifact_id | String | Unique digital artifact identifier | KHH-001 |
| inventory_id | Integer | Original spreadsheet inventory number | 1 |
| inventory_row | Integer | Original spreadsheet row | 2 |
| name_so | String | Somali artifact name | Dhiil |
| name_en | String | English/display name | Dhiil |
| category | String | Artifact classification | Containers & Storage |
| brief_description | String | Physical inventory description | Tall, narrow woven vessel |
| materials | String | Recorded construction materials | Woven plant fibers |
| traditional_use | String | Recorded historical/traditional purpose | Used to collect and store milk |
| origin | String | Recorded geographical/cultural origin, if known | Empty until verified |
| cultural_significance | String | Reviewed cultural interpretation | Empty until reviewed |
| observed_visual_features | String | Features visible in the supplied photograph | Empty until inspected |
| story_so | String | Draft Somali cultural narrative | Somali text |
| story_en | String | Draft English cultural narrative | English text |
| transcript_so | String | Somali audio transcript | Empty if unavailable |
| transcript_en | String | English audio transcript | Empty if unavailable |
| status | String | Editorial approval state | draft |
| approval | Object | Museum reviewer, date and notes | See approval fields |
| image | Object | Photograph and permission details | See image fields |
| sources | Array | Supporting references and review state | INV-001 |
| passages | Array | Searchable source-backed content | Description, materials, use |
| inventory_review | Object | Inventory matching information | Draft match |

### 3. Source Convention

Each artifact must maintain a traceable connection to its original inventory record.

| Artifact ID | Inventory ID | Source ID |
|---|---:|---|
| KHH-001 | 1 | INV-001 |
| KHH-002 | 2 | INV-002 |
| KHH-003 | 3 | INV-003 |
| KHH-004 | 4 | INV-004 |
| KHH-005 | 5 | INV-005 |

### 4. Approval Fields

- reviewer: Name of the authorized reviewer.
- date: Date of approval.
- notes: Additional review comments.

### 5. Image Fields

- path: Relative location of the photograph.
- caption: Description of the image.
- owner: Copyright holder or image owner.
- permission: Permission status, initially unconfirmed.

### 6. Source and Passage Fields

Source records use:

- id
- title
- location
- approved
- note

Passage records use:

- source_id
- language
- preview_only
- approved
- text
- keywords
- intent

### 7. Quality and Publication Rules

1. Every artifact requires a unique KHH identifier.
2. The original inventory ID must be preserved.
3. Inventory facts must not be confused with cultural interpretation.
4. Unverified information must remain explicitly unconfirmed.
5. Somali and English narratives require review.
6. Photograph permissions must be recorded.
7. Draft records must not be automatically published.
8. Source references must remain traceable.
