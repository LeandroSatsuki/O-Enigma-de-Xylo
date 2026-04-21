import sys

def check_balance(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract script content
    start_tag = '<script id="game-state-machine">'
    end_tag = '</script>'
    
    start_idx = content.find(start_tag)
    if start_idx == -1:
        print("Script tag not found")
        return
    
    start_idx += len(start_tag)
    end_idx = content.find(end_tag, start_idx)
    if end_idx == -1:
        print("End script tag not found")
        return
    
    script = content[start_idx:end_idx]
    
    stack = []
    lines = script.split('\n')
    for i, line in enumerate(lines):
        for char in line:
            if char == '{':
                stack.append(('{', i + 1))
            elif char == '}':
                if not stack:
                    print(f"Extra '}}' found on line {i + 1}")
                else:
                    stack.pop()
    
    if stack:
        for char, line in stack:
            print(f"Unclosed '{char}' from line {line}")
    else:
        print("Braces are balanced")

if __name__ == "__main__":
    check_balance(sys.argv[1])
