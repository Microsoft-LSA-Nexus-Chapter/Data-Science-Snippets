import logging

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a sample text file and write content to it
filename = 'sample_file.txt'

# Write some content to the file
with open(filename, 'w') as file:
    file.write("Hello, World!\nWelcome to the world of Python file handling.\n")
    logging.info(f'File {filename} created and content written successfully.')

# Read content from the file and print it
try:
    with open(filename, 'r') as file:
        content = file.read()
        logging.info(f'Content read from {filename}: \n{content}')
        print(content)
except FileNotFoundError:
    logging.error(f"File {filename} not found.")
except Exception as e:
    logging.error(f"An error occurred while reading the file: {e}")
