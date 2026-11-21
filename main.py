import subprocess #Da pra utilizar comandos do terminal do windows

data = (subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']) #utiliza o comando e guarda numa variavel
        .decode('utf-8') #Transforma a saida de bytes para texto
        .split('\n') #Faz a separação em cada quebra de linha
        )

profiles = []
for name in data:
    if 'Todos os Perfis de Usuários' in name: #Pega o nome de todos os perfis com o comando do netsh do windows
        profiles.append(name.split(':')[1].strip()) #Adiciona os nomes no profiles

for name in profiles:
    results = (
        subprocess
        .check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear'])
        .decode('utf-8')
        .split('\n')
    )
    password = []
    for key in results:
        if 'Conteúdo da Chave' in key:
            password.append(key.split(':')[1].strip()) #Separa a senha e adiciona no password tirando espaços desnecessários

    try:
        print(f'{name:<20}| {password[0]:<}') #Mostra os dois resultados
    except IndexError:
        print(f'{name:<20}| {'':<}') #Se der errado mostra só o nome da rede
        