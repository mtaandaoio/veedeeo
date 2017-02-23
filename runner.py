import sys, parseIn, parseOut, program, zero, code, jb
from os import listdir

processors = {
    'default': code,
    'zero': zero,
    'mpot': pot,
    'jb': jb
}

choice = 'default'

if len(sys.argv) > 1:
    choice = sys.argv[1]

if len(sys.argv) > 2:
    files = [sys.argv[2]]
else:
    inputPath = "in/"
    files = [inputPath + str(x) for x in listdir(inputPath)]

process = processors[choice]

inputs = parseInput.getParsedInputs(files)
outputs = {}

for name, input in inputs.items():
    print('Processing ' + name + ' with processor ' + choice + '...')
    outputs[name] = process.getOutput(input)

parseOut.parseOutputs(outputs)
