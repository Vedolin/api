# [Atados API](http://www.atados.com.br)
[![Codeship](https://www.codeship.io/projects/139f1dd0-a88e-0131-806c-1a66b7fb6c8b/status)](https://codeship.io/projects/19157)
[![Dependency Status](https://gemnasium.com/atados/api.svg)](https://gemnasium.com/atados/api)


A ideia é simples: uma rede social na qual pessoas predispostas a praticar o bem
encontram oportunidades de voluntariado.

Nosso principal objetivo é ampliar o senso de comunidade na sociedade, levando
cada vez mais pessoas a entrar nessa corrente de gente boa. Afinal, tudo o que
você faz bem, pode fazer bem a alguém.


## Por que colaborar com o projeto?

Porque você quer viver em uma sociedade melhor!

Porque colaborando com o Atados você estará ajudando todas as causas! Sejam
elas lutar pelo direito dos animais, pelo meio ambiente, por educação de
qualidade, por mais respeito aos direitos humanos entre outras. Isso mesmo!
Você vai contribuir com o trabalho de diversas ONGs que juntas apoiam todas as
causas!

Já que você está aqui, provavelmente você é alguém envolvido com tecnologia.
Suas habilidades são muito valiosas para a sociedade. Colaborar com o Atados é
uma forma de contribuir para o desenvolvimento coletivo fazendo algo que você
faz muito bem!


## Apps que precisam estar instalados

- pip
- elasticsearch rodando no port 9200
- [postgresql](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-14-04)

## Como rodar o projeto

    git clone https://github.com/atados/api.git
    cd api
    apt-get install libmysqlclient-dev python-dev # Ubuntu
    sudo apt-get install python-psycopg2 # Ubuntu
    sudo apt-get install libpq-dev # Ubuntu
    make install && make run

## License

MIT License (See LICENSE file).


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/atados/api/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

