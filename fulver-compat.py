import re
from pathlib import Path

file_path_md = Path("changelog.md")
file_path_txt = Path("changelog.txt")
file_path_md_upper = Path("CHANGELOG.md")
file_path_txt_upper = Path("CHANGELOG.txt")
file_path = None
found = True

if file_path_md.is_file():
    print("Markdown file exists")
    file_path = file_path_md
elif file_path_txt.is_file():
    print("Text file exists")
    file_path = file_path_txt
elif file_path_md_upper.is_file():
    print("Markdown file exists")
    file_path = file_path_md_upper
elif file_path_txt_upper.is_file():
    print("Text file exists")
    file_path = file_path_txt_upper
else:
	print("No changelog file found")
	found = False
	exit(1)

regex = re.compile(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?", flags=re.MULTILINE)
match = None

with open(file_path, "r") as f:
	test_str = f.read()
	match = regex.search(test_str)

semver = ""
fulver = ""

if match:
	print("Found a match!")
	semver = f"{match.group(1)}.{match.group(2)}.{match.group(3)}"
	fulver = f"{match.group(1)}.{match.group(2)}.{match.group(3)}.{match.group(4)}"
	print("Full version:", match.group(0))
	print("Major:", match.group(1))
	print("Minor:", match.group(2))
	print("Patch:", match.group(3))
	print("Extra:", match.group(4))
	if match.group(5):
		semver += f"-{match.group(5)}"
		fulver += f"-{match.group(5)}"
		print("Pre-release:", match.group(5))
	if match.group(6):
		semver += f"+{match.group(6)}"
		fulver += f"+{match.group(6)}"
		print("Build:", match.group(6))
	print("Semver:", semver)
	print("Fulver:", fulver)
	Path(".versions").mkdir(exist_ok=True)
	with open(".versions/semver.txt", "w") as f:
		f.write(semver)
	with open(".versions/fulver.txt", "w") as f:
		f.write(fulver)
else:
	print("No match found.")
