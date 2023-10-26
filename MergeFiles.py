def merge_files(output_file, *input_file):
    with open(output_file, 'w') as output:
        for input_file in input_file:
            with open(input_file, 'r') as input:
                output.write(input.read())
                output.write('\n')

if __name__ == "__main__":
    file1 = str(input("Type the first file name: "))
    file2 = str(input("Type the second file name: "))
    final_file = str(input("Type the final file name: "))

    merge_files(final_file, file1, file2)

    print("Files Merged with Success!")
