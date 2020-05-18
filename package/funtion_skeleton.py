#input memory
memory = input("\nHow many memory you want?")

#input cpu
cpu = input("\nHom many CPU you want?")

#input file name
filename = input("\nWhat is the name of inputfile?")

#input coordinate
print("\nInput the coordinate of your molecule, hit enter to finish")
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
coordinate = '\n'.join(lines)

#create inputfile
with open("{}.com".format(filename), 'w') as f:
    print("$RunGauss\n%NprocLinda=1\n%Mem={}gb\n%NProcshared={}\n# b3lyp/gen EmpiricalDispersion=GD3 Freq Opt\n\nTest\n\n0,1\n{}".format(memory,cpu,coordinate), file=f)