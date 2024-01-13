# Reading data from the input file
input_file_path = "product_descriptions.txt"
output_file_path = "formatted_descriptions.txt"

try:
    with open(input_file_path, 'r') as input_file:
        # Reading lines from the input file
        lines = input_file.readlines()

        # Capitalizing the first letter of each word in the descriptions
        capitalized_lines = [line.strip().title() for line in lines]

    # Save the capitalized data to the output file
    with open(output_file_path, 'w') as output_file:
        output_file.write("\n".join(capitalized_lines))

    print(f"Formatted descriptions saved to {output_file_path}")

except FileNotFoundError:
    print(f"Error: The file {input_file_path} was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
