# Xedho: private first-artifact pilot

This is a working local prototype for the Khayrhaye Living Heritage practicum. The supplied photograph and user-confirmed name **Xedho** are included. Its inventory match, cultural history, materials, use, image permission and museum approval are **unconfirmed**. Do not distribute the photo or publish a visitor page/QR until the authorized museum reviewer clears them.

## Four student handoffs

| Owner | Deliverable | Handoff |
| --- | --- | --- |
| BIA 1 | Match Xedho to the inventory; identify sources and image owner; fill the reviewed record and data dictionary | Versioned `data/xedho.json` with an approval trail |
| BIA 2 | Define event names, review counts, and build the museum dashboard | Counts from `data/events.sqlite3`; never collect questions or visitor IDs |
| DAAI 1 | Source-grounded question answering and evaluation | `core.py`, approved passages, Q&A results |
| DAAI 2 | Somali/English scripts, transcript/narration review, mobile page and QR integration | `app.py`, approved language/media and phone test |

Museum representative: review cultural claims and approve the public version. The four students should demonstrate one Xedho flow before making another artifact.

## Run it yourself on a Mac

1. Download and unzip the package into your practicum folder, then open Terminal. Navigate into the `xedho_pilot` folder. On macOS, type `cd `, drag the unzipped folder into Terminal, and press Return.
2. Create a private Python environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   ```

3. Check draft readiness and run the tests:

   ```bash
   python validate.py
   python -m unittest discover -s tests -v
   ```

   `BLOCKED` is the correct readiness result until approval. The tests should pass.

4. Start the local preview:

   ```bash
   streamlit run app.py
   ```

   Visit `http://localhost:8501` on your Mac. Confirm the Xedho photo appears, the draft warning is visible, and the question "What is its traditional use?" returns an unavailable answer. Stop the app with Control-C.

## Complete the artifact record manually

1. **Preserve the original `Artifacts.xlsm`.** In a working copy, have BIA 1 match the supplied photo to the correct inventory row. The workbook has names that are blank or formula-derived; do not assume a match from appearance alone. Enter the verified row number in `inventory_row`.
2. Ask the museum representative to confirm `name_so`, alternative names, materials, origin, use and cultural context. For each factual claim record the speaker/document, date and relevant consent or publication rights. If unknown, leave it empty.
3. In `data/xedho.json`, replace the empty `story_en` and `story_so` with reviewed stories. Add one or more **approved** sources and short approved passages in this form (illustrative placeholders, not Xedho facts):

   ```json
   "sources": [{"id": "S1", "title": "[Source name]", "location": "[Private source reference]", "approved": true}],
   "passages": [
     {"source_id": "S1", "language": "en", "approved": true, "text": "[Reviewed English sentence about this artifact.]"},
     {"source_id": "S1", "language": "so", "approved": true, "text": "[Weedh Soomaali ah oo dib loo eegay.]"}
   ]
   ```

   Each answer is copied verbatim from one approved passage and displays its source ID. This is intentionally a small retrieval prototype, **not yet an LLM or production RAG system**. Text matching can return a passage that is related but does not fully answer the question; test every release question with a reviewer.
4. Add approved `transcript_en` and `transcript_so` as needed. If audio is approved, place `assets/xedho_en.mp3` and `assets/xedho_so.mp3`. The page will show only files present when the record is approved. Review pronunciation with a Somali speaker.
5. Set `image.permission` to `confirmed` only after the rights holder permits this use. Set `approval.reviewer` to the reviewer's real name, `approval.date` to the actual review date, and `status` to `approved` only after review. Never mark approval just to remove the warning.
6. Run `python validate.py` again. Resolve every blocker. Have a second team member inspect the page, sources, spelling and mobile layout.

## Evaluate Q&A

Start with `data/qa_tests.json`, then add at least 10 reviewed questions per language: direct, paraphrased, unknown, and potentially disputed. Record the expected source ID and whether the response is correct, incomplete or unsupported. For unknown questions, require the unavailable response. The simple word-overlap retrieval will need improvement before public release; keep all published answers constrained to approved source passages.

## Test a QR privately

For a second phone on the same private Wi-Fi, first run `streamlit run app.py --server.address 0.0.0.0`. Find your Mac's local network address in **System Settings → Wi-Fi → Details → TCP/IP**. Generate a QR, substituting your actual address:

```bash
python make_qr.py http://192.168.1.12:8501
```

Scan `assets/xedho_qr.png` on the phone while the app is running. A `localhost` URL will not work from the phone. Use a private network; this prototype has **no authentication**, and its dashboard must be protected before any public deployment. The page URL and the hosting location for a permanent museum QR must be decided with the project lead.

## Dashboard and handover

The sidebar "Private team dashboard" shows event counts: page view, language selection, audio play and question asked. It stores only timestamp, artifact ID and event type in a local SQLite file. It does not store question text, IP address, identity or language choice. BIA 2 can export aggregate counts for a private dashboard after the team agrees on access. A Streamlit page view is **not automatically proof of a physical QR scan**; count scans separately only if the final QR redirect can reliably record them.

Keep `data/events.sqlite3`, draft records, images, audio and source documents out of any public repository. Before handover, document installation, owner, approved sources, review date, test results, unresolved issues and how to onboard artifact number two.
