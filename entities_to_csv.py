from documentcloud import DocumentCloud
from local_settings import *
import csv

def connect_client():
    '''Connect your machine to DocumentCloud's API'''
    if PASSWORD and USERNAME:
        print('Getting DocumentCloud credentials from local_settings.py')
        client = DocumentCloud(USERNAME, PASSWORD)
        return client
    else:
        print("You must add your credentials to local_settings.py")
        exit()

def get_project():
    '''Retreive your project information from DocumentCloud'''
    if PROJECT_ID:
        print('Connecting to DocumentCloud')
        client = connect_client()
        project = client.projects.get(id=PROJECT_ID)
        return project
    else: 
        print("You must add your project ID to local_settings.py")
        exit()

def fix_breaks(my_string):
    '''Change line returns inside strings to spaces'''
    my_string = my_string.replace('\n', ' ')
    return my_string

def make_csv(project):
    '''Get all the entities from your project's documents and put them in a csv'''
    entities_list = []
    doc_list = project.get_document_list()
    for doc in doc_list:
        print("Writing entities from {0}".format(doc.title))
        for entity in doc.entities:
            row = {}
            row['doc_id'] = doc.id
            row['doc_source'] = doc.source
            row['doc_name'] = doc.title
            row['entity_name'] = fix_breaks(entity.value)
            row['entity_type'] = entity.type
            row['entity_score'] = entity.relevance
            entities_list.append(row)
    fieldnames = entities_list[0].keys()
    csvfile = open("entities.csv","w", newline="")
    output = csv.DictWriter(csvfile, fieldnames = fieldnames, delimiter=',',quotechar='"',quoting=csv.QUOTE_NONNUMERIC)
    output.writeheader()
    for entity in entities_list:
        output.writerow(entity)
    print('Writing all entities to a csv')
    csvfile.close()
    return

if __name__== '__main__':
    project = get_project()
    make_csv(project)