# 1. Importa a função que cria o Flask (ajustado para o padrão comum de pacotes)
try:
    from app import create_app
except ModuleNotFoundError:
    # Caso seu arquivo se chame app.py na raiz, usamos o import direto
    from app.app import create_app 

# 2. Importa a inicialização do banco de dados que criamos
from app.repositories.user_repository import init_db

# 3. Inicializa a variável 'app' chamando a função de fábrica (Application Factory)
app = create_app()

import os

if __name__ == '__main__':
    # O Render fornece a porta na variável de ambiente PORT, se não achar, usa a 5000
    port = int(os.environ.get("PORT", 5000))
    # O host '0.0.0.0' torna o servidor acessível externamente
    app.run(host='0.0.0.0', port=port, debug=True)