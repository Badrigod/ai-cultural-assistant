import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent / "src"))

from cultural_assistant import answer_question


def test_artifact_dhiil():
    response = answer_question("What is Dhiil?")
    assert "Artifact: Dhiil" in response
    assert "Traditional Use:" in response


def test_dance_dhaanto():
    response = answer_question("Tell me about Dhaanto")
    assert "Dance / Performance: Dhaanto" in response
    assert "Validation Status:" in response


def test_dance_istunka():
    response = answer_question("Tell me about Istunka")
    assert "Dance / Performance: Istunka" in response
    assert "Afgooye, Lower Shabelle" in response
    assert "Pending validation" in response


def test_region_afgooye():
    response = answer_question("Tell me about Afgooye")
    assert "Region: Afgooye / Lower Shabelle" in response


def test_tradition_xeer_ciise():
    response = answer_question("What is Xeer Ciise?")
    assert "Tradition: Xeer Ciise" in response


def test_unknown_question():
    response = answer_question("Tell me about ExampleUnknownRecord")
    assert "could not find information" in response.lower()
