import os
import argparse
import csv
import codecs

# Traverses a data_dir and returns a list of paths to all .txt files found
def find_text_file_paths(data_dir_path):
    text_file_paths = []
    for root, dirs, files in os.walk(data_dir_path):
        for file in files:
            # check if file extension is .txt
            if os.path.splitext(file)[1] == '.txt':
                text_file_paths.append(os.path.join(root, file))
    return text_file_paths



def main(data_dir_path, output_path):
    file_paths = find_text_file_paths(data_dir_path)

    # Open the output file. newline argument avoids newline spaces in the final output-file. 
    with open(output_path, 'w', encoding = 'utf8', newline = '') as output:
        writer = csv.writer(output)
        writer.writerow(['filename', 'total_words', 'unique_words'])

        for path in file_paths:
            # codecs is used to deal with problematic characters within the textfiles. 
            with codecs.open(path, 'r', encoding = 'utf8', errors = 'ignore') as file:
                file_content = file.read()
                words = file_content.split()
                
                # The three components are extracted. 
                basename = os.path.basename(path)
                num_words = len(words)
                num_unique_words = len(set(words))

                writer.writerow([basename, num_words, num_unique_words])
            


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'searches the datafolder for text-files and calculates total amount of words and amount of unique words. ')
    parser.add_argument('-d', '--data_dir_path', default = './data/', help = 'A path to a text-corpus or filstructure containing text-files.')
    parser.add_argument('-o', '--output_path', default = './output/output.csv', help = 'A path to a csv-file that the results will be saved into')
    args = parser.parse_args()

    main(data_dir_path = args.data_dir_path, output_path = args.output_path)