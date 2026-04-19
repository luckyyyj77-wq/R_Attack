import re

# Read the HTML file
with open('R_Attack.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Process each line
fixed_lines = []
for line in lines:
    # Fix lines with corrupted stage names
    # Pattern: name: "Stage N"<garbage>, marbles:
    line = re.sub(r'(name: "Stage \d+")[^",]+,\s*marbles:', r'\1, marbles:', line)
    fixed_lines.append(line)

# Write back
with open('R_Attack.html', 'w', encoding='utf-8') as f:
    f.writelines(fixed_lines)

print("Fixed all corrupted stage names!")
