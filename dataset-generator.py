#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: lara (with some help from ChatGPT)
"""

import re, csv

# Define function to read corpus text file and return array of song lyrics
def get_songs():
    # Read from corpus file
    corpus = open('./corpus.txt')
    lyrics = corpus.read()
    
    # Divide the input string into songs based on two or more consecutive line breaks
    untrimmed_songs = re.split(r'\n{2,}', lyrics)

    # Trim leading or trailing whitespace
    songs = list(map(str.strip, untrimmed_songs))

    return songs

# Define function to generate csv files with required format from array of song lyrics
def generate_datasets(songs):
    # Prepare the CSV outputs for training, validation, and test data
    with open('training-data.csv', mode='w', newline='', encoding='utf-8') as train_file, \
         open('validation-data.csv', mode='w', newline='', encoding='utf-8') as val_file, \
         open('test-data.csv', mode='w', newline='', encoding='utf-8') as test_file:
        
        # Create CSV writers
        train_writer = csv.writer(train_file)
        val_writer = csv.writer(val_file)
        test_writer = csv.writer(test_file)
        
        # Write header rows for each CSV file
        header = ['input_text', 'target_text']
        train_writer.writerow(header)
        val_writer.writerow(header)
        test_writer.writerow(header)
        
        # Separate the songs into training, validation, and test sets
        num_songs = len(songs)
        print(f'Number of songs is: {num_songs}')
        
        # Last 8 songs will be divided into validation and test
        validation_songs = songs[-8:-4]  # Last 8 songs, first 4 are validation
        test_songs = songs[-4:]  # Last 4 songs are for testing
        training_songs = songs[:-8]  # All songs except the last 8
        
        # Function to process and write songs to the appropriate CSV
        def write_songs_to_csv(songs, writer):
            for song in songs:
                # Split the song into lines
                lines = song.strip().splitlines()

                # Skip empty songs (in case there are any)
                if not lines:
                    continue

                # Separate the song into input_text (everything except the last 4 lines)
                input_text = "\n".join(lines[:-4])

                # Target text is the last 4 lines
                target_text = "\n".join(lines[-4:])

                # Write the row to the CSV file
                writer.writerow([input_text, target_text])

        # Write data to each CSV file
        write_songs_to_csv(validation_songs, val_writer)
        write_songs_to_csv(test_songs, test_writer)
        write_songs_to_csv(training_songs, train_writer)

    print("CSV files 'training-data.csv', 'validation-data.csv', and 'test-data.csv' have been created successfully.")


songs = get_songs()
generate_datasets(songs)
