import os
import sys
import json
from pathlib import Path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from easy_template import process_file, side_by_side_code

root = Path(__file__).parent

with open(root.joinpath('_scripts', 'solutions', 'q2.py'), 'r') as f:
    q2_solution = f.read()


with open(root.joinpath('students.json'), 'r') as f:
    students: dict = json.loads(f.read())

for stud in students:
    folder = f'{stud["first_name"].lower()}_{stud["last_name"].lower()}'
    with open(root.joinpath('_scripts', folder, 'q2.py'), 'r') as f:
        q2_answer = f.read()
    q2 = side_by_side_code(q2_answer, q2_solution, titles=['Answer', 'Solution'], max_line_length=80)
    values = {
        **stud,
        'question2': q2,

    }
    content = process_file(
        root.joinpath('_templates', 'feedback.md'),
        lookup_dir=root.joinpath('_scripts', folder),
        values=values
    )
    with open(root.joinpath('out', f'feedback_{folder}.md'), 'w') as f:
        f.write(content)
