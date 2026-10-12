from core import ROOT, load_artifact, approved_passages, release_ready
import sys

artifact_name = sys.argv[1] if len(sys.argv) > 1 else "xedho"
artifact_path = ROOT / "data" / f"{artifact_name}.json"
r = load_artifact(artifact_path)
issues = []
ALLOWED_SOURCE_CATEGORIES = {
    "Museum verified",
    "Published source",
    "UNESCO / official source",
    "Elder or community interview",
    "Draft / unverified",
}

sources = r.get("sources", [])
if not sources:
    issues.append("No source is recorded")

for source in sources:
    source_id = source.get("id", "<missing ID>")
    category = source.get("source_category")
    if category not in ALLOWED_SOURCE_CATEGORIES:
        issues.append(f"{source_id}: missing or invalid source category")
    if category == "Museum verified" and source.get("approved") is not True:
        issues.append(f"{source_id}: museum-verified source is not approved")
if not (ROOT / r["image"]["path"]).is_file():
    issues.append("Photograph is missing")
if r["image"]["permission"] != "confirmed":
    issues.append("Image permission is unconfirmed")
if r["inventory_row"] is None:
    issues.append("Inventory match is unconfirmed")
if r["status"] != "approved":
    issues.append("Museum approval is pending")
else:
    for field in ("name_so", "traditional_use", "story_en", "story_so"):
        if not r.get(field, "").strip():
            issues.append("Missing approved field: " + field)
    if not r["approval"].get("reviewer") or not r["approval"].get("date"):
        issues.append("Reviewer name or date missing")
    for lang in ("en", "so"):
        if not approved_passages(r, lang):
            issues.append("No approved source-backed passage for " + lang)
print("Artifact:", r["artifact_id"], r["name_so"])
print("Release readiness:", "READY FOR TEAM REVIEW" if release_ready(r) and not issues else "BLOCKED")
for issue in issues:
    print(" -", issue)
