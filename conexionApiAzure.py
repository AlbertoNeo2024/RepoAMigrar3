from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint

# Fill in with your personal access token and org URL
personal_access_token = 'x32tdxvxq4g2ponmdjlqkzoohgt2vdloirvunokz5yyzzjboos7q'
# organization_url = 'https://dev.azure.com/neorisddc'
organization_url = 'https://neorisddc.visualstudio.com/'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client = connection.clients.get_core_client()





#numero de proyectos que deseo desplegar
top= 100
#parametro skip para saltar proyectos que ya se han procesado
skip=0

get_projects_response = core_client.get_projects(top=top, skip=skip)
index = 0
while get_projects_response and skip!=top:
    for project in get_projects_response:
        pprint.pprint("[" + str(index) + "] " + project.name)
        index += 1
    skip += top
    get_projects_response = core_client.get_projects(top=top, skip=skip)






# Get the first page of projects
# get_projects_response = core_client.get_projects()
# index = 0

# while get_projects_response is not None:
#     for project in get_projects_response:
#         pprint.pprint("[" + str(index) + "] " + project.name)
#         index += 1
#     if get_projects_response.continuation_token is not None and get_projects_response.continuation_token != "":
#         # Get the next page of projects
#         get_projects_response = core_client.get_projects(continuation_token=get_projects_response.continuation_token)
#     else:
#         # All projects have been retrieved
#         get_projects_response = None