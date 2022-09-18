# dashboard
É um aplicativo de loja simples. 
Que gerar dados de amostra usando um comando de gerenciamento do Django 
depois visualizá-los com Chart.js, em um graficos assincróno.

## Instalação && Execução
Executar a migrações:
	- py manage.py makemigrations
	- py manage.py migrate

Crie um superusuario:
	- py manage.py createsuperuser

Execute o comando personalizado para gerar dados aleatórios na Base de dados:
	- py manage.py populate_db --montante 

Inici o servidor de execução, navegue até:
	-> http://127.0.0.1:8000/shop/


## Meta
Samuel K. Africano  – kandumboafricano@gmail.com


## Contribuir

1. Faça o _fork_ do projeto (https://github.com/SamuelAfricano/dashboard.git)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_

