#!/usr/bin/python3
import os
import sys
import subprocess

arguments = sys.argv
if len(arguments) > 1:
    if str(sys.argv[1]) == "template":
        template = []
        output = []

        # Read template
        with open("reqs-template.txt", "r", encoding="utf-8") as file:
            for line in file:
                template.append(line.strip().lower())

        # Read actual requirements
        requirements = subprocess.Popen(
            ["pip", "freeze"], stdout=subprocess.PIPE
        ).communicate()[0]

        # Convert requirements bytes to list of strings
        requirements = str(requirements)[2:-5].split("\\r\\n")

        # Save new requirements to file
        with open("requirements.txt", "w") as file:
            for line in requirements:
                if line[: line.find("=")].strip().lower() in template:
                    file.write(line + "\n")
else:
    requirements = os.system('cmd /c "pip freeze > requirements.txt"')
