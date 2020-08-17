import os
import shutil
import yaml
import csv

"""
Quick and dirty way of auditing pre emptive gcp permissions
Requires glcoud to be install and authicanted because it will use it 
to generate yaml files and parse through them. 

This also can be improved by using google's python api instead of gcloud 

ONLY TESTED ON MACOS, and will only work there because I'm using bash commands
"""
company = ''

# write output of gcloud to projects.txt
def get_project_list(all=False):
    """
    run gcloud command to get a list of all projects in GCP which start with Company-format
    it will create projects.txt file
    To run for all projects pass True
    :param all:
    :return:
    """
    if all:
        print('Using gcloud to get all projects names....')
        os.system('''
         > projects.txt
          gcloud projects list | while $project read a b c; do; echo $a >> projects.txt; done''')
    else:
        print('using gcloud to get all Company-format projects name...')
        os.system(f'''
         > projects.txt
         gcloud projects list | while $project read a b c; do
         if [[ $a == {company}* ]]; then
            echo $a >> projects.txt
        fi
        done''')


def parseYamlFile(directory, csv_file="google_audit.csv", permission='roles/owner'):
    """ Parse yaml file for members which have
    the permisisosn roles/editor assign to them and
    output into a csv file based on yaml file name in the
    directory passed to the function
    """
    print('Creating CSV Files.....')
    with open(csv_file, 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(['Project', 'Role', 'Members'])

    print('Parsing Yaml File...')
    for yaml_file in os.listdir(directory):
        with open(os.path.join(directory, yaml_file)) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            for item in data['bindings']:
                if item['role'] == permission:
                    with open(csv_file, 'a') as csvFile:
                        writer = csv.writer(csvFile)
                        writer.writerow([f'{yaml_file[:-4]}', f'{permission}', f'{item["members"]}'])


def make_yaml_directory(directory="yaml"):
    try:
        shutil.rmtree(os.path.join(os.getcwd(), directory))
    except:
        pass

    try:
        os.mkdir(directory)
        return os.path.join(os.getcwd(), directory)
    except:
        pass


def move_yaml_files(dest, source=os.getcwd()):
    """
    moves yaml file in current directory to another directory
    :param dst:
    :param src:
    :return:
    """
    print("Moving Yaml Files....")
    for file in os.listdir(source):
        if file.endswith('.yaml'):
            shutil.move(file, dest)


def main():
    get_project_list()
    directory = make_yaml_directory()

    with open('projects.txt') as f:
        contents = f.readlines()

    contents = list(map(lambda x: x.strip(), contents))

    print('Creating YAML IAM policy files......')
    for project in contents:
        os.system(f"gcloud projects get-iam-policy {project} > {project}.yaml")

    move_yaml_files(directory)

    parseYamlFile(directory)


if __name__ == "__main__":
    main()
