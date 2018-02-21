from sys import argv

script, from_file, to_file = argv

print(f"Copied from {from_file} to {to_file}")

in_file = open(from_file)
out_file = open(to_file, 'w')
out_file.write(in_file.read())
out_file.close()
in_file.close()