import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.core.artifacts import (
    artifacts,
)

from app.services.resume_service import (
    analyze_resume,
)

artifacts.load()

result = analyze_resume(
    "sample_resume.pdf"
)

# print("\n")
# print("=" * 60)
# print("FINAL RESULT")
# print("=" * 60)
print(result)