# reader.py
import boto3

class Reader(object):
    def __init__(self, type, days):
        self.type = type
        self.days = days
        self.iam = boto3.client('iam')

    def get_roles(self):
        response = self.iam.list_roles()
        return response['Roles']

    def get_unused_role_permissions(self, role):
        unused = []
        
        job_id = self.iam.generate_service_last_accessed_details(
            Arn = role['Arn'],
            Granularity = 'SERVICE_LEVEL'
        )

        response = self.iam.get_service_last_accessed_details(
            JobId = job_id['JobId']
        )

        for service in response['ServicesLastAccessed']:
            if service['LastAuthenticated'] is not None:
                unused.append(service['ServiceName'])
        
        return unused

    def __exit__(self):
        self.iam.close()