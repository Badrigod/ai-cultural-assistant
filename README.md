# AI Cultural Assistant

## Project Overview

The AI Cultural Assistant is a cultural information prototype designed to answer visitor questions about artifacts, dances and performances, regions, and traditions.

The project focuses on designing a structured cultural knowledge system that can organize information from multiple cultural sources and make it accessible through a simple Streamlit interface.

## Project Objective

The main objective of this practicum project is to design the information structure for an AI cultural assistant that can answer visitor questions about:

- Artifacts
- Dances and performances
- Regions
- Traditions

The system also maintains source information and validation status to support responsible cultural documentation.

## Information Structure

The cultural knowledge base is organized into five main datasets:

| Dataset | Purpose | Current Records |
|---|---|---:|
| Artifacts | Stores information about cultural objects | 39 |
| Dances | Stores dance, ritual, and performance information | 20 |
| Regions | Organizes geographic and cultural areas | 8 |
| Traditions | Stores cultural traditions and practices | 2 |
| Sources | Records the origin of cultural information | 4 |

## Main Data Relationships

The datasets are connected using identifiers such as:

- `artifact_id`
- `dance_id`
- `region_id`
- `tradition_id`
- `source_id`

These relationships allow the assistant to connect cultural information instead of treating every record as an isolated entry.

Example:

```text
Istunka (D017)
    |
    +-- Region ID: R006
    |       |
    |       +-- Afgooye / Lower Shabelle
    |
    +-- Source ID: S004
    |
    +-- Validation Status: Pending validation
```

The dance dataset preserves the original geographic description while also allowing a normalized `region_id` relationship when an appropriate region has been identified.

## Cultural Validation

Cultural information can require confirmation from knowledgeable community members, elders, practitioners, or other appropriate sources.

For this reason, the dance and performance information includes a `validation_status` field.

Example:

```text
validation_status = Pending validation
```

This helps distinguish working cultural information from information that has received further cultural validation.

## Data Sources

The project currently contains four source records.

Sources include UNESCO cultural information and the practicum-provided Khayrhaye Living Heritage Project Somali Dance Database working template.

Source information is stored separately in `sources.csv` and connected to cultural records using `source_id`.

## AI Cultural Assistant

The assistant can search across the cultural collection and answer questions about multiple information categories.

Example visitor questions:

```text
What is Dhiil?
Tell me about Dhaanto
Tell me about Istunka
Tell me about Afgooye
What is Xeer Ciise?
```

## Streamlit Interface

A Streamlit application provides a simple visitor-facing interface where visitors can enter cultural questions and receive information from the structured collection.

## Current Dataset

The current prototype contains:

- 39 artifact records
- 20 dance and performance records
- 8 region records
- 2 tradition records
- 4 source records

## Technologies Used

- Python
- Pandas
- Streamlit
- CSV structured data
- Git
- Git Bash

## Running the Project

Activate the virtual environment:

```bash
source venv/Scripts/activate
```

Start the Streamlit application:

```bash
streamlit run app.py
```

The command-line assistant can also be tested with:

```bash
python src/cultural_assistant.py
```

## Current Prototype Status

The prototype can successfully answer questions about artifacts, dances and performances, regions, and traditions.

The project also supports source tracking, cultural validation status, and relationships between cultural records.

## Future Improvements

- Additional culturally validated records
- Elder and practitioner oral-history references
- Images and museum media
- Video references
- Improved relationship mapping
- More advanced natural-language question handling
- QR-code integration for museum exhibits
- Future augmented-reality interpretation

## Conclusion

The AI Cultural Assistant demonstrates how structured cultural information can support an interactive visitor experience. By separating artifacts, dances, regions, traditions, and sources while connecting them through identifiers, the project provides a foundation that can be expanded as additional validated information becomes available.
