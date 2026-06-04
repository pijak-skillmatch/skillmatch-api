import re
import fitz

from app.core.artifacts import (
    artifacts,
)


def clean_text(
    text: str,
) -> str:

    text = text.lower()

    text = text.replace(
        "\xa0",
        " "
    )

    text = text.replace(
        "\n",
        " "
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


def extract_text_from_pdf(
    pdf_path: str,
) -> str:

    document = fitz.open(
        pdf_path
    )

    text = ""

    for page in document:

        page_text = page.get_text(
            "text"
        )

        if isinstance(
            page_text,
            str,
        ):
            text += page_text
        else:
            text += str(
                page_text
            )

    document.close()

    return clean_text(
        text
    )


def extract_skills_from_text(
    text: str,
) -> list[str]:

    if not artifacts.skill_gap_engine:

        raise RuntimeError(
            "Artifacts not loaded"
        )

    vocabulary = (
        artifacts.skill_gap_engine.get(
            "skill_vocabulary",
            []
        )
    )

    # print("=" * 60)
    # print(
    #     "VOCAB SIZE:",
    #     len(vocabulary)
    # )
    # print(
    #     "FIRST 10 SKILLS:",
    #     vocabulary[:10]
    # )
    # print("=" * 60)

    # print(
    #     "TEXT SAMPLE:"
    # )

    # print(
    #     text[:500]
    # )

    # print("=" * 60)

    detected_skills = []

    for skill in vocabulary:

        pattern = (
            r"\b"
            + re.escape(
                skill.lower()
            )
            + r"\b"
        )

        if re.search(
            pattern,
            text,
        ):

            # print(
            #     f"MATCH FOUND: {skill}"
            # )

            detected_skills.append(
                skill
            )

    return sorted(
        list(
            set(
                detected_skills
            )
        )
    )


def analyze_resume(
    pdf_path: str,
) -> dict:

    text = extract_text_from_pdf(
        pdf_path
    )

    detected_skills = (
        extract_skills_from_text(
            text
        )
    )

    return {

        "detected_skills":
            detected_skills,

        "resume_text":
            text[:1000],

    }