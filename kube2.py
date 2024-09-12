from kubernetes import client, config

config.load_kube_config()



namespace = input("Ingresa el nombre del namespace: ")
name = input("Ingresa el nombre para el deployment: ")
servicio = input("Ingresa el nombre del servicio: ")
imagen = input("ingresa el nombre de la imagen: ")


def create_namespace(name):
    api = client.CoreV1Api()
    namespace = client.V1Namespace()
    namespace.metadata = client.V1ObjectMeta(name=name)
    api.create_namespace(namespace)

def create_deployment(name, namespace, image):
    api = client.AppsV1Api()
    deployment = client.V1Deployment()
    deployment.metadata = client.V1ObjectMeta(name=name, namespace=namespace)
    deployment.spec = client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(match_labels={"app": name}),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(labels={"app": name}),
            spec=client.V1PodSpec(containers=[client.V1Container(name=name, image=imagen)])
        )
    )
    api.create_namespaced_deployment(namespace, deployment)

def create_service(name, namespace, port):
    api = client.CoreV1Api()
    service = client.V1Service()
    service.metadata = client.V1ObjectMeta(name=name, namespace=namespace)
    service.spec = client.V1ServiceSpec(
        selector={"app": name},
        ports=[client.V1ServicePort(protocol="TCP", port=port, target_port=port)],
        type="ClusterIP"
    )
    api.create_namespaced_service(namespace, service)


create_namespace(namespace)
create_deployment(name, namespace, imagen)
create_service(servicio, namespace, 9090)
