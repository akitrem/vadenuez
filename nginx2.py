import os
import yaml

def create_namespace(namespace):
    namespace_yaml = {
        'apiVersion': 'v1',
        'kind': 'Namespace',
        'metadata': {
            'name': namespace
        }
    }

    with open('namespace.yaml', 'w') as f:
        yaml.dump(namespace_yaml, f)

    os.system('kubectl apply -f namespace.yaml')

def create_deployment(namespace, deployment_name, replicas, image_name, service_name):
    deployment_yaml = {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {
            'name': deployment_name,
            'namespace': namespace
        },
        'spec': {
            'replicas': replicas,
            'selector': {
                'matchLabels': {
                    'app': 'nginx'
                }
            },
            'template': {
                'metadata': {
                    'labels': {
                        'app': 'nginx'
                    }
                },
                'spec': {
                    'containers': [{
                        'name': 'nginx',
                        'image': image_name
                    }]
                }
            }
        }
    }

    service_yaml = {
        'apiVersion': 'v1',
        'kind': 'Service',
        'metadata': {
            'name': service_name,
            'namespace': namespace
        },
        'spec': {
            'type': 'NodePort',
            'selector': {
                'app': 'nginx'
            },
            'ports': [{
                'protocol': 'TCP',
                'port': 80,
                'targetPort': 80,
                'nodePort': 30000
            }]
        }
    }

    with open('deployment.yaml', 'w') as f:
        yaml.dump(deployment_yaml, f)

    with open('service.yaml', 'w') as f:
        yaml.dump(service_yaml, f)

    os.system('kubectl apply -f deployment.yaml')
    os.system('kubectl apply -f service.yaml')

    
namespace = input("Ingrese el nombre del namespace: ")
deployment_name = input("Ingrese el nombre del deployment: ")
replicas = int(input("Ingrese la cantidad de réplicas: "))
image_name = input("Ingrese el nombre de la imagen para el contenedor: ")
service_name = input("Ingrese el nombre del servicio: ")

create_namespace(namespace)
create_deployment(namespace, deployment_name, replicas, image_name, service_name)
