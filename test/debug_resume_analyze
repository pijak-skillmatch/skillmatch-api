import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.artifacts import (
    artifacts,
)

from app.services.resume_analysis_service import (
    analyze_resume_profile,
)

artifacts.load()

result = analyze_resume_profile(
    pdf_path="sample_resume.pdf",
    experience="Entry Level",
)

print(result)