def tenet(input_file_path: str, output_file_path: str):
    file = open(input_file_path,'r')
    output = open(output_file_path, "w")
    for line in file.readlines():
        output.write(line[::-1])
    output.close()
    pass