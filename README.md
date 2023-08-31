## API Consumer – Data Engineer & Data Science
Sistema de consumo de API em Python - Flask para extrações de índices históricos da moeda BITCOIN e persistência dos dados em banco NoSQL MongoDB com geração de gráficos. 

### Versão 
1.0.0

### Descrição
Este sistema foi desenvolvido em Python utilizando Flask para realizar as seguintes tarefas:
•	Consumir dados sobre o Bitcoin de API’s externas;
•	Persistir os dados no MongoDB, 
•	Gerar gráficos a partir dos dados armazenados com Pandas. 

### Requisitos de Instalação
•	MongoDB
•	Python
•	Biblioteca Pandas

### Configuração
•	Clone o repositório do projeto
•	Instale as dependências do Python usando: pip install  -r requirements.txt

### Bibliotecas Utilizadas
blinker==1.6.2	idna==3.4	python-dateutil==2.8.2
certifi==2023.7.22 	Jinja2==3.1.2	pytz==2023.3
charsetnormalizer==3.2.0	kiwisolver==1.4.5	requests==2.31.0
click==8.1.7	MarkupSafe==2.1.3	simplejson==3.19.1
colorama==0.4.6	matplotlib==3.7.2	six==1.16.0
contourpy==1.1.0	numpy==1.25.2	tenacity==8.2.3
cycler==0.11.0	packaging==23.1	tzdata==2023.3
DateTime==5.2	pandas==2.0.3	urllib3==2.0.4
Flask==2.3.3	Pillow==10.0.0	Werkzeug==2.3
fonttools==4.42.1	plotly==5.16.1	
forex-python==1.8	pymongo==3.11.0	
zope.interface==6.0	pyparsing==3.0.9	

### Uso
Após clonar o repositório, utilize seguinte comando: py app.py e acesse o localhost de sua máquina. Após alguns segundos o sistema será mostrado em tela. Este tempo de carregamento ocorre devido ao consumo dos dados e operações no MongoDB

### Estrutura de Diretórios
•	models - Conexão com o MongoDB
•	static - JS e CSS
•	template - HTML
•	app.py
•	README.MD
•	requirementes.txt

### API
CoinCodex (Base histórica de 5 anos)
https://coincodex.com/page/api/
![image](https://github.com/Leo5677/projeto-data-engineer-science/assets/48198740/f84feda7-9383-4bfe-84ac-34617376e56e)


### CoinAPI (Base histórica de 30 dias)
https://rest.coinapi.io/v1/ohlcv/KRAKENFTS_PERP_BTC_USD/history? period_id=1DAY&time_start=
![image](https://github.com/Leo5677/projeto-data-engineer-science/assets/48198740/dc48ecfe-56c7-4c43-9195-f1f07df3e017)

### Banco de Dados NoSQL
MongoDB

### Geração de Gráficos
Com os dados do MongoDB, realizarmos diversos list comprehension para traduzir o dado para a biblioteca pandas e para a montagem do gráfico:

Últimos Cinco Anos
![image](https://github.com/Leo5677/projeto-data-engineer-science/assets/48198740/9775b61e-b82e-48ff-857b-8cc1f963d1e8)
![image](https://github.com/Leo5677/projeto-data-engineer-science/assets/48198740/0d9152b8-d028-4888-a1a8-8a22c84de8a8)


Últimos Trinta Dias
![image](https://github.com/Leo5677/projeto-data-engineer-science/assets/48198740/afad260c-ae1f-4c50-bc3a-d31a76f70042)
![image](https://github.com/Leo5677/projeto-data-engineer-science/assets/48198740/517fcdb2-c992-457f-bd52-41486e2f1a2c)

### Autores
•	Leonardo Cirqueira Valensoela
•	Thiago Neves Pedroso
•	Rafael Onassis Nicolau

