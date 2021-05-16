### Trader - Arquivando as velas, API-Cache em redis

[ ] Autenticar Uso da API 
[x] Autenticar API no Redis
[x] Get - Velas/id
[x] Get - Categorias
[x] Delete-key


### Usando Anaconda3 em caso de Windows
```zsh
# Usando anaconda3
conda init powershell
conda activate py38mt4
```

### Dependencias do python 3.8
```zsh
pip install redis
pip install faker
pip install faker_vehicle

pip install python-binance
pip install flask
    # Setar a variavel de embinte
        # powershell: set FLASK_APP=app.py
        # bash: $env:FLASK_APP=app.py

#### https://vscode.readthedocs.io/en/latest/editor/integrated-terminal/
```

### Iniciando docker compose
```zsh
# Redis - Docker
docker-compose up -d

# Utilitario Client (Redis Desctop Manager) gerenciamento de Redis
    # https://www.electronjs.org/apps/anotherredisdesktopmanager
```


### Usando a API
```zsh
http://127.0.0.1:5000
http://127.0.0.1:5000/delete-key

http://127.0.0.1:5000/velas/1
http://127.0.0.1:5000/categorias
```