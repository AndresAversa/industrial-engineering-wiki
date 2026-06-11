from pathlib import Path

files_root = Path("docs/files")

count = 0

for course_dir in files_root.iterdir():

    if not course_dir.is_dir():
        continue

    course_name = course_dir.name.replace("-", " ").title()

    folders = {
        "past-exams": f"# Past Exams\n\nUpload past exams and solutions for {course_name} here.\n",
        "labs": f"# Labs\n\nUpload lab material and reports for {course_name} here.\n",
        "exercise-sessions": f"# Exercise Sessions\n\nUpload exercise sheets and solutions for {course_name} here.\n",
    }

    for folder, content in folders.items():

        target = course_dir / folder / "README.md"

        if not target.exists():
            target.write_text(content, encoding="utf-8")
            count += 1

print(f"Created {count} README files")