### Trader - Arquivando as velas, API-Cache em redis

### Funções a fazer...
```doc
[ ] Autenticar Uso da API
[x] Autenticar API no Redis
[x] Get - Velas/id
[x] Get - Categorias
[x] Delete-key

[x] Tratando API Binance estraindo dados
    [x] todos os ultimos preços
    [x] Livro de Ordens
    [x] Preço medio
    [x] Pegando preços dointervalo de 1 dia
    [x] Transformando e tratando o json

[x] Pegar dados publicos abertos CMV
    [x] Direto da extenção csv
    [x] De dentro do arquivo zip
```

### Usando Anaconda3 em caso de Windows
```zsh
# Usando anaconda3
conda create -n py38mt4 python=3.8
conda init powershell
conda activate py38mt4
```

### Dependencias do python 3.8
```zsh
# Executar dependencias listada
pip freeze > requirements.txt
pip install -r requirements.txt

# Instalar
pip install redis
pip install faker
pip install faker_vehicle

pip install python-binance
pip install nltk
pip install twisted
pip install bta-lib
pip install pandas
pip install flask

pip install binance-api
pip install asyncio
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
flask run

http://127.0.0.1:5000
http://127.0.0.1:5000/delete-key

http://127.0.0.1:5000/velas/1
http://127.0.0.1:5000/categorias
```