import sys, parseIn, parseOut, program, pot

inputs = parseIn.getParsedInputs()
outputs = {}

for name, input in inputs.items():
    processors = {
        'default': program,
        'pot': pot,
    }

    choice = 'default'

    if len(sys.argv) > 1:
        choice = sys.argv[1]

    process = processors[choice]

    print('Processing ' + name + ' with processor ' + choice + '...')
    outputs[name] = process.getOutput(input)

parseOutput.parseOutputs(outputs)