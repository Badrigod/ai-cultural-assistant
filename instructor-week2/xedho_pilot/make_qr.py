"""Generate a QR for a team-approved URL. Never publish a draft QR."""
import argparse
from pathlib import Path
import qrcode

parser = argparse.ArgumentParser()
parser.add_argument("url", help="A reachable artifact URL, e.g. http://192.168.1.12:8501")
args = parser.parse_args()
if not args.url.startswith(("http://", "https://")):
    parser.error("Provide a full http:// or https:// URL")
path = Path(__file__).resolve().parent / "assets" / "xedho_qr.png"
qrcode.make(args.url).save(path)
print("QR saved:", path)
print("Test with a second phone on the same network. localhost points at the phone itself and will not work there.")
