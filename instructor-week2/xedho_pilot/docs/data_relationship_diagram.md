
# KHAYRHAYE LIVING HERITAGE
## Data Relationship Diagram v0.1

Status: Draft
Pilot Scope: KHH-001 to KHH-005

### Entity Relationship Diagram

```mermaid
erDiagram

    ARTIFACT ||--o{ MEDIA : has
    ARTIFACT ||--o{ CULTURAL_CONTENT : contains
    ARTIFACT ||--o{ ARTIFACT_SOURCE : references
    SOURCE ||--o{ ARTIFACT_SOURCE : supports
    SOURCE ||--o{ PASSAGE : provides
    ARTIFACT ||--o{ APPROVAL : requires
    ARTIFACT ||--o{ VISITOR_EVENT : records

    ARTIFACT {
        string artifact_id PK
        int inventory_id
        int inventory_row
        string name_so
        string name_en
        string category
        string materials
        string traditional_use
        string status
    }

    MEDIA {
        string media_id PK
        string artifact_id FK
        string path
        string caption
        string owner
        string permission
    }

    CULTURAL_CONTENT {
        string content_id PK
        string artifact_id FK
        string language
        string story
        string transcript
        string review_status
    }

    SOURCE {
        string source_id PK
        string title
        string location
        boolean approved
        string note
    }

    ARTIFACT_SOURCE {
        string artifact_id PK,FK
        string source_id PK,FK
    }

    PASSAGE {
        string passage_id PK
        string source_id FK
        string language
        string text
        string keywords
        string intent
        boolean approved
    }

    APPROVAL {
        string approval_id PK
        string artifact_id FK
        string reviewer
        string date
        string status
    }

    VISITOR_EVENT {
        string event_id PK
        string artifact_id FK
        string event_type
        string timestamp
        string language
    }
```

### Implementation Notes

1. This diagram represents the proposed conceptual
   relational database structure.

2. The current pilot uses JSON files rather than
   normalized relational database tables.

3. ARTIFACT_SOURCE is a proposed junction entity
   allowing one inventory source to support
   multiple museum artifacts.

4. The visitor-event relationship is part of the
   architecture design and does not indicate that
   a public analytics system is deployed.

5. Publication requires image permission and
   museum approval.

### Xedho Example

Artifact: KHH-005

Inventory: 5

Source: INV-005

Media: assets/xedho.png

Cultural Content:
- Somali draft story
- English draft story

Source Passages: 6

Approval Status: Pending
