# reader.py
import boto3
import time

class Reader(object):
    def __init__(self, type, days):
        self.type = type
        self.days = days
        self.iam = boto3.client('iam')

    def get_unused(self):
        roles = self.get_roles()

        for role in roles:
            self.get_unused_role_permissions(role)


    def get_roles(self):
        response = self.iam.list_roles()
        return response['Roles']

    def get_unused_role_permissions(self, role):
        unused = []

        job = self.iam.generate_service_last_accessed_details(
            Arn = role['Arn'],
            Granularity = 'SERVICE_LEVEL'
        )

        services = self.iam.get_service_last_accessed_details(
            JobId = job['JobId']
        )

        while services['JobStatus'] != 'COMPLETED':
            time.sleep(1.0)
            services = self.iam.get_service_last_accessed_details(
                JobId = job['JobId']
            )

        for service in services['ServicesLastAccessed']:
            if 'LastAuthenticated' in service:
                unused.append(service['ServiceName'])
        
        if unused:
            print(f'\"{role["RoleName"]}\": {unused}')
            return unused

    def __exit__(self):
        self.iam.close()