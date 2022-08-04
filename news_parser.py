#!/usr/bin/env python3
import click
import json
import os 

@click.command()
@click.option(
    '--directory',
    '-d',
    type=str, 
    help='Directory where the json files are'
)
@click.option(
    '--filename',
    '-f' ,
    type=str,
    help='JSON file.'
)
@click.option(
    '--debug',
    is_flag=True,
    help='Enable Debug mode'
)
def parse_news(directory, filename, debug):

    if directory:
        print('directory found: ' + directory)
        files = os.listdir(directory)
        
        for file in files:
            parse_file(directory+'/'+file, debug)

    else:
        if filename:
            parse_file(filename, debug)
            
        else:
            click.secho("There are no directory or files to read", fg='red')


def parse_file(filename, debug):
    if debug:
        click.secho(f'Filename to read: {filename}', fg='green')

    with open(filename, 'r') as myfile:
        data = myfile.read()
        
    object_list = json.loads(data)
    root_directory = 'news_data'
    directory_name = object_list[0]["source"]
    repeated_files = []

    os.makedirs(root_directory+'/'+directory_name)

    if debug:
        click.secho(f'directory created: {directory_name}', fg='green')

    for obj in object_list:
        file_path = root_directory + '/' + directory_name + "/" + str(obj["id"]).replace('/','-')
        if debug:
            click.secho(f'file created: {file_path}.txt', fg='green')
        # Save File and remove "@ " pattern
        try:
            with open(f"{file_path}.txt", "x") as output:
                output.write(str(obj["content"]).replace('@ ', ''))
        except FileExistsError:
            repeated_files.append(file_path)
            click.secho(f'file already created: {file_path}.txt... Skipping', fg='red')

    if len(repeated_files) > 0:
        click.secho(f'\n The following files were found repeated: \n {repeated_files}', fg='red')

def main():
    """Parse files"""
    parse_news()

if __name__ == "__main__":
    main()