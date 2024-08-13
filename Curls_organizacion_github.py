import requests
import csv

# Configuración de la API de GitHub
github_api_url = "https://api.github.com"
github_token = "ghp_"  # Reemplaza con tu token de acceso a la API de GitHub (opcional)

# Parámetros de la solicitud
org_name = "Mycompany"
params = {
    "per_page": 100  # Número de repositorios por página
}

# Encabezados de la solicitud
headers = {
    "Accept": "application/json"
}

if github_token:
    headers["Authorization"] = f"Bearer {github_token}"

# Realizar la solicitud a la API de GitHub
response = requests.get(f"{github_api_url}/orgs/{org_name}/repos", params=params, headers=headers)

# Verificar si la respuesta es exitosa
if response.status_code == 200:
    # Obtener la lista de repositorios de la respuesta
    repos = response.json()
    print(repos)

    # Crear un archivo CSV para escribir los resultados
    with open('github_repos.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Escribir la cabecera del archivo CSV
        writer.writerow(["Repository", "Branch", "Has README", "README Content"])

        # Imprimir los nombres de los repositorios, si tienen archivo README y las ramas
        for repo in repos:
            repo_name = repo["name"]
            repo_id = repo["id"]

            # Realizar la solicitud para obtener las ramas del repositorio
            branches_response = requests.get(f"{github_api_url}/repos/{org_name}/{repo_name}/branches", headers=headers)

            if branches_response.status_code == 200:
                branches = branches_response.json()

                for branch in branches:
                    branch_name = branch["name"]

                    # Realizar la solicitud para obtener la información del archivo README en la rama
                    readme_response = requests.get(f"{github_api_url}/repos/{org_name}/{repo_name}/contents/README.md?ref={branch_name}", headers=headers)

                    if readme_response.status_code == 200:
                        readme_content = readme_response.text

                        has_readme_content = "yes" if readme_content else "no"
                        writer.writerow([repo_name, branch_name, "yes", has_readme_content])
                    else:
                        writer.writerow([repo_name, branch_name, "no", "no"])
            else:
                writer.writerow([repo_name, "Error", "Error", "Error"])
else:
    print(f"Error: {response.status_code}")

