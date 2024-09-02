import os

# Definindo as tags válidas para os nomes de pastas.
VALID_TAGS = [
    "lettuce", "rice", "banana", "potato", "meat", "onion", "beans",
    "chicken", "orange", "milk", "apple", "watermelon", "strawberry",
    "egg", "tomato",
]

# Definindo os modos válidos para as pastas (test, train, validation).
VALID_MODES = ["test", "train", "validation"]

# Solicitando ao usuário que insira o nome da pasta desejada.
selected_tag = input("Enter desired folder name to be used:")

# Verifica se o nome da pasta inserido pelo usuário é válido.
if selected_tag not in VALID_TAGS:
    print(
        f"\nThe selected folder name '{selected_tag}' is not valid!! Valid choices are:"
    )
    print(", ".join(VALID_TAGS))
    exit()

# Solicita ao usuário que insira o modo da pasta (test, train, validation).
selected_mode = input("Enter the folder training mode to be renamed:")

# Verifica se o modo inserido pelo usuário é válido.
if selected_mode not in VALID_MODES:
    print(f"\nThe selected mode '{selected_mode}' is not valid!! Valid choices are:")
    print(", ".join(VALID_MODES))
    exit()

# Define o caminho para a pasta de destino baseada nas entradas do usuário.
destination_path = f"/data/images/{selected_mode}/{selected_tag}"
current_dir = os.getcwd()  # Obtém o diretório de trabalho atual.

# Tenta mudar o diretório para o caminho de destino.
try:
    os.chdir(current_dir + destination_path)
except Exception:
    # Se o caminho não for válido, exibe uma mensagem de erro e encerra o script.
    print(f'\nThe current directory path "{destination_path}" is not valid!!\n')
    print(
        f"Make sure this script is inserted where the following folders for the mode {selected_mode}, would be. For example: /data/images/{selected_mode}/{selected_tag}"
    )
    exit()

# Definindo as extensões de arquivos aceitas.
accepted_extensions = ["jpg", "jpeg", "png"]

# Solicita ao usuário o valor inicial para ser usado na renomeação dos arquivos.
count = int(
    input("Enter the starting value to be used while renaming the image files:")
)

# Exibe o diretório atual.
print(os.getcwd())

# Percorre todos os arquivos no diretório atual.
for filename in os.listdir(os.getcwd()):
    name, _, extension = filename.rpartition(".")  # Separa o nome e a extensão do arquivo.

    # Se a extensão do arquivo não estiver na lista de extensões aceitas, pula para o próximo arquivo.
    if extension.lower() not in accepted_extensions:
        continue

    # Renomeia o arquivo com o novo nome seguindo o padrão "img_<count>.<extensão>".
    new_filename = f"img_{count}.{extension}"
    os.rename(filename, new_filename)  # Renomeia o arquivo.
    count += 1  # Incrementa o contador para o próximo arquivo.
