from pathlib import Path
import yaml

TEMPLATE = r"""# Course Name

---

## Quick Information

| Item | Value |
| ------------ | ----- |
| Course Code | |
| ECTS | |
| Semester | |
| Programme(s) | |
| Professor(s) | |
| Assessment | |

---

## Course Overview

Provide a short description of the course and its role within the curriculum.

---

## Course Structure

### Part 1

Description.

### Part 2

Description.

### Part 3

Description.

---

## How to Study

### During the Semester

* Attend lectures?
* Read course notes?
* Focus on exercises?
* Make summaries?
* Use external resources?

### Before the Exam

* Recommended preparation method
* Time required
* Important chapters
* Chapters that can be deprioritized

---

## Exam Intelligence

### Exam Format

* Written
* Oral
* Multiple choice
* Open questions
* Exercises

### Typical Question Types

* Question type 1
* Question type 2
* Question type 3

### Topics Frequently Appearing

* Topic A
* Topic B
* Topic C

### Common Mistakes

* Mistake 1
* Mistake 2
* Mistake 3

### Difficulty Assessment

| Category | Rating |
| -------- | ------ |
| Difficulty | ⭐⭐⭐☆☆ |
| Workload | ⭐⭐⭐☆☆ |
| Exam Difficulty | ⭐⭐⭐☆☆ |
| Usefulness | ⭐⭐⭐⭐⭐ |

---

## Resources

### Official Material

* Lecture slides
* Course notes
* Textbook

### Additional Resources

* YouTube videos
* Websites
* External notes

### Useful Software

* MATLAB
* Python
* LTspice
* SolidWorks
* Other

---

## Files and Downloads

Store files in:

docs/files/{slug}/

---

## Past Exams

| Academic Year | Available | Notes |
| ------------- | --------- | ----- |
| 2025-2026 | | |
| 2024-2025 | | |
| 2023-2024 | | |

---

## Lab Information

### Lab Description

Description.

### Useful Advice

Advice from previous students.

---

## Student Reviews

### Review 1

**Academic Year:**
**Final Grade:**

Comments.

---

## Frequently Asked Questions

### Is attendance important?

Answer.

### Which chapters matter most?

Answer.

### Is the textbook necessary?

Answer.

### How difficult is the exam?

Answer.

---

## Contributors

* Contributor 1

Last updated: YYYY-MM-DD
"""

from pathlib import Path
import re

with open("mkdocs.yml", "r", encoding="utf-8") as f:
    content = f.read()

course_files = sorted(set(
    re.findall(r'courses/[A-Za-z0-9\-]+\.md', content)
))

print(f"Found {len(course_files)} course pages")

ok_to_run = True;

for course_path in course_files:

    print(course_path)

    if ok_to_run:

        md_path = Path("docs") / course_path

        slug = md_path.stem

        title = slug.replace("-", " ").title()

        md_path.parent.mkdir(parents=True, exist_ok=True)

        if not md_path.exists():
            md_path.write_text(
                TEMPLATE.format(slug=slug).replace(
                    "# Course Name",
                    f"# {title}"
                ),
                encoding="utf-8"
            )

        files_root = Path("docs/files") / slug

        (files_root / "past-exams").mkdir(parents=True, exist_ok=True)
        (files_root / "labs").mkdir(parents=True, exist_ok=True)
        (files_root / "exercise-sessions").mkdir(parents=True, exist_ok=True)

print("Done")