from pathlib import Path
import runpy
import sys

# Locate the actual Week 2 application.
project_root = Path(__file__).resolve().parent.parent
week2_folder = project_root / "instructor-week2" / "xedho_pilot"
week2_app = week2_folder / "app.py"

if not week2_app.is_file():
    raise FileNotFoundError(f"Week 2 application not found: {week2_app}")

# Allow the Week 2 application to import core.py.
sys.path.insert(0, str(week2_folder))

# Launch the actual Week 2 application.
runpy.run_path(str(week2_app), run_name="__main__")
