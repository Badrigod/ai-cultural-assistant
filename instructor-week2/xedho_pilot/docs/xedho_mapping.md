
# KHAYRHAYE LIVING HERITAGE
## Xedho Data Mapping — KHH-005

Document Version: 0.1
Status: Draft
Reference Artifact: Xedho

---

## 1. Purpose

This document maps the existing Xedho JSON record
to the conceptual Data Model v0.1.

It demonstrates how inventory information,
cultural content, photographs, sources and
approval information relate to one another.

Source file: data/xedho.json

## 2. Artifact Identification

| Field | Existing Value | Conceptual Entity |
|---|---|---|
| artifact_id | KHH-005 | Artifact |
| inventory_id | 5 | Artifact |
| inventory_row | 6 | Artifact |
| name_so | Xedho | Artifact |
| name_en | Xedho | Artifact |
| status | draft | Artifact |
| category | Clothing & Textiles | Artifact |

## 3. Inventory Mapping

Inventory Source ID: INV-005

Description:
Vessel protected and decorated with leatherwork,
straps and cowrie shells.

Recorded Materials:
Gourd or wooden vessel, leather/hide and cowrie shells.

Traditional Use:
Used for collecting, carrying and storing.

The inventory does not confirm which alternative
base material was used in this specific example.

## 4. Media Mapping

Conceptual Entity: Media

Existing JSON structure:

image.path:
assets/xedho.png

image.permission:
unconfirmed

The photograph is present in the pilot project.
Publication permission remains unconfirmed.

## 5. Cultural Content Mapping

Conceptual Entity: Cultural Content

| Existing JSON Field | Target Language |
|---|---|
| story_so | Somali |
| story_en | English |
| transcript_so | Somali |
| transcript_en | English |

The narratives are draft content derived from
the supplied inventory and require review.

## 6. Source and Passage Mapping

Conceptual Entities: Source and Passage

Source:
INV-005

Number of recorded sources: 1
Number of recorded passages: 6

Passage structure:
- source_id
- language
- preview_only
- approved
- text
- keywords
- intent

Passage categories:
- Description
- Material
- Traditional Use

Languages:
- English (en)
- Somali (so)

## 7. Approval Mapping

Conceptual Entity: Approval

Current artifact status:
draft

Required before publication:
- Confirmation of photograph ownership.
- Confirmation of publication permission.
- Cultural-content review.
- Translation review.
- Museum approval.

No approval should be assumed.

## 8. Relationship Summary

Artifact KHH-005
    |
    |-- Inventory record 5
    |
    |-- Media: xedho.png
    |
    |-- Source: INV-005
    |       |
    |       |-- Six source-backed passages
    |
    |-- Cultural Content
    |       |-- Somali story
    |       |-- English story
    |
    |-- Approval Record
            |-- Pending

## 9. Data Quality Notes

1. Artifact ID matches the inventory mapping.
2. The photograph exists in the project.
3. Inventory provenance is recorded.
4. Six passages support draft information retrieval.
5. Materials must retain the recorded uncertainty.
6. Publication remains blocked until review.
7. No historical interpretation should be
   presented as verified without evidence.

## 10. Implementation Status

The mapping is based on the current JSON pilot.

The proposed normalized database entities have
not yet been implemented as separate tables.

Document Status: Ready for internal review.
