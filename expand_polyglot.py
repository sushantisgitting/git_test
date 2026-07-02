import os

languages = {
    "polyglot/hello.ts": "const helloTS_{i}: string = 'This is a large TypeScript block to register language presence on GitHub.'; console.log(helloTS_{i});\n",
    "polyglot/main.go": "package main\nimport \"fmt\"\nfunc main() {\n\t_ = \"This is a large Go block to register language presence on GitHub. {i}\"\n}\n",
    "polyglot/main.rs": "fn main() {\n\tlet _s = \"This is a large Rust block to register language presence on GitHub. {i}\";\n}\n",
    "polyglot/Hello.java": "public class Hello {\n\tpublic static void main(String[] args) {\n\t\tString s = \"This is a large Java block to register language presence on GitHub. {i}\";\n\t}\n}\n",
    "polyglot/main.cpp": "#include <iostream>\nint main() {\n\tstd::string s = \"This is a large C++ block to register language presence on GitHub. {i}\";\n\treturn 0;\n}\n",
    "polyglot/main.c": "#include <stdio.h>\nint main() {\n\tchar* s = \"This is a large C block to register language presence on GitHub. {i}\";\n\treturn 0;\n}\n",
    "polyglot/hello.sh": "#!/bin/bash\n# This is a large Shell block to register language presence on GitHub. {i}\necho \"Hello\"\n",
    "polyglot/index.php": "<?php\n// This is a large PHP block to register language presence on GitHub. {i}\necho \"Hello\";\n?>\n",
    "polyglot/main.rb": "# This is a large Ruby block to register language presence on GitHub. {i}\nputs \"Hello\"\n",
    "polyglot/main.kt": "fun main() {\n\tval s = \"This is a large Kotlin block to register language presence on GitHub. {i}\"\n}\n"
}

for filepath, template in languages.items():
    content = ""
    # Generate ~25KB of file content to make it stand out
    for i in range(300):
        content += template.replace("{i}", str(i))
    with open(filepath, "w") as f:
        f.write(content)

print("Expanded all polyglot files to ~25KB each!")
