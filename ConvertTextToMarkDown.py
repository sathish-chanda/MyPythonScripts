''' 
This file helps to convert a text with a heading and description.
This text can be copied from the online learning platforms to make a notes of the course and save the notes into TechNotes repo as a markdown file.

INPUT:
Llamafile - Framework bundling LLMs into standalone binaries
Cosmopolitan Libc - Enables single file portable executables
Large language models - Foundation AI models handling text tasks
Inference server - Serves predictions from trained ML models
System metrics - Performance indicators like GPU usage
Model governance - Policies and controls around model access
Confidential computing - Secure protected execution environments
Telemetry - Real-time collection of system metrics

OUTPUT:
**Llamafile** - Framework bundling LLMs into standalone binaries

**Cosmopolitan Libc** - Enables single file portable executables

**Large language models** - Foundation AI models handling text tasks

**Inference server** - Serves predictions from trained ML models

**System metrics** - Performance indicators like GPU usage

**Model governance** - Policies and controls around model access

**Confidential computing** - Secure protected execution environments

**Telemetry** - Real

INSTRUCTION:
Just update the string in the text variable and run the code. It will generate the markdown format of the string.

'''

text = '''
Llamafile - Framework bundling LLMs into standalone binaries
Cosmopolitan Libc - Enables single file portable executables
Large language models - Foundation AI models handling text tasks
Inference server - Serves predictions from trained ML models
System metrics - Performance indicators like GPU usage
Model governance - Policies and controls around model access
Confidential computing - Secure protected execution environments
Telemetry - Real-time collection of system metrics
'''

print(text)
text = text.strip()
print(text.split('\n'))
for line in text.split('\n'):
    info = line.split('-')
    heading = info[0].strip()
    description = info[1].strip()
    print('**'+heading+'**' + ' - ' + description)
    print()
