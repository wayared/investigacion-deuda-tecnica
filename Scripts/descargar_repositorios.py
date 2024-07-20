import os
import shutil
import openpyxl



def clone_git(repo_link):
  if "tree" in repo_link.lower():
    data = repo_link.split('/')
    tree_index = data.index('tree')

    branch = data[-1]
    repo_link = '/'.join(data[:tree_index])
    repo_name = repo_link.split('/')[-1]
    print(f"El repositorio {repo_link} no es un repositorio git. Es un branch de un repositorio.")
    print(f"URL: {repo_link}. Clonando branch...")
    os.system(f"git clone --branch {branch} {repo_link}")
  else:
    print(f"Clonando {repo_link}...")
    os.system(f"git clone {repo_link}")
    repo_name = repo_link.split('/')[-1]
  return repo_name

def remove_git_safely(path):
  if not os.path.exists(path):
    print(f"Directory '{path}' no encontrado. Saltando.")
    return

  try:
    if os.path.isdir(path):
      shutil.rmtree(path)
      print(f"Successfully removed directory '{path}'.")
  except OSError as e:
    print(f"Error removing '{path}': {e}")
  try:
    os.remove(".gitignore")
    print("Successfully removed '.gitignore'.")
  except FileNotFoundError:
    print(".gitignore no encontrado. Saltando.")




def clone_repo(repo_id, repo_url):
      if os.path.exists(repo_id):
        print(f"El repositorio {repo_id} ya fue clonado.")
        return
      os.mkdir(repo_id)
      os.chdir(repo_id)
      repo_name = clone_git(repo_url)
      # Copy the template report file
      with open('../plantilla_informe.md', 'r') as f:
        template_report = f.read()
      with open(f'Informe Deuda Técnica - {repo_id}.md', 'w') as f:
        f.write(template_report + '\n\n\n')
        f.write(f"Este repositorio fue obtenido de: {repo_url}")
      # Delete the .git folder and .gitignore file
      try:
        os.chdir(repo_name)
        remove_git_safely(".git")
        os.chdir('..\\..')
      except OSError as e:
        print(f"Error: {e}")
        os.chdir('..')

# Load the workbook
def get_names(file):
  wb = openpyxl.load_workbook(file)
  repositorios = wb['Repositorios']
  names = []
  for i in range(2, 63):
    repo_id = repositorios[f'H{i}'].value
    if not repo_id:
      continue
    names.append(repo_id) if repo_id not in names else None
  return names
nombres = get_names('RepositoriosAnalizados.xlsx')
def get_repos(name,file):
  wb = openpyxl.load_workbook(file)
  repositorios = wb['Repositorios']
  for i in range(2, 63):
    repo_id = repositorios[f'A{i}'].value
    repo_url = repositorios[f'D{i}'].value
    asignado = repositorios[f'H{i}'].value
    if not repo_id:
      continue
    if asignado == name or name == "all":
      clone_repo(repo_id, repo_url)    
  print("Repositorios clonados.")
menu_text = "Bienvenido, desea conseguir los repositorios asignados a:\n"
for i, name in enumerate(nombres):
  menu_text += f"{i + 1}. {name}\n"
menu_text += f"{len(nombres) + 1}. Todos\n"
menu_text += "0. Salir\n"
while True:
  file = "RepositoriosAnalizados.xlsx"
  option = input(menu_text)
  if option == '0':
    break
  elif option == str(len(nombres) + 1):
    get_repos("all",file)
  elif option.isdigit() and int(option) <= len(nombres)+1:
    get_repos(nombres[int(option) - 1],file)
  else:
    print("Opción inválida. Intente de nuevo.")
    continue
print("Gracias por usar el script.")