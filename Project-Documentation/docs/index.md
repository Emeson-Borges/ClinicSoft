# DOCUMENTAÇÃO CLINICSOFT

Software especializado em Gestão Clínica

## **O que é a ClinicSoft**
<div style="text-align: justify;">
A ClinicSoft é uma solução inovadora que visa aprimorar a eficiência e a gestão em ambientes de saúde. Seja como um software abrangente para a administração de clínicas médicas ou como o nome de uma clínica específica, a ClinicSoft destaca-se por oferecer funcionalidades avançadas, como agendamento de consultas, prontuários eletrônicos, faturamento integrado e outros recursos essenciais. Com um compromisso com a excelência, a ClinicSoft busca proporcionar uma experiência otimizada tanto para profissionais de saúde quanto para pacientes, promovendo assim uma abordagem moderna e eficaz na prestação de serviços de saúde.
</div><br>

---------------------------

## **Tecnologias**
* `Python   (API - BackEnd)`
* `React    (FrontEnd)`
* `MKDocs   (Documentação)`
* `Postgres (Banco de Dados)`
* `pgAdmin  (SGBD)`

---------------------------

### **Dependências do BackEnd**
* `pip install django`          - Framework para construção do BacEnd.
* `django-cors-headers==4.3.1`  - Cors para conexão com FrontEnd.
* `djangorestframework==3.14.0` - Biblioteca para construção da API.
* `Pillow==10.0.1`              - Biblioteca de processamento de imagens
* `python manage.py createsuperuser` - Para criar um Super Usuário (Adm).
* `pip install psycopg2` - Conexão com o banco de dados Postgres   
---------------------------

### **Depedências do FrontEnd**
* `npx create-next-app` - Framework para frontend - NextJS.
* `npx create-expo-app` - Cria o App React Native.

---------------------------

### **Dependências do MKDocs**
* `pip install mkdocs`  - Documentação do Projeto.

---------------------------

### **Rodar o Projeto Django**
* `python manage.py runserver 8000` - 

---------------------------

### **Rodar o Projeto MKDocs**
* `mkdocs serve -a localhost:8001` - 
* `mkdocs serve --dev-addr 127.0.0.1:8001` - 

---------------------------

## **Arquitetura do Sistema**
**Diagramas Arquiteturais**


* **Diagrama de Componentes:**
Representação visual dos principais componentes do sistema e suas interações.


* **Diagrama de Implantação:**
Se o sistema é distribuído, um diagrama que mostra como os componentes são distribuídos em hardware físico ou ambientes de nuvem.


* **Diagrama de Fluxo de Dados:**
Ilustração dos principais fluxos de dados entre os componentes do sistema


**Camadas e Componentes**

* **Camadas de Arquitetura:**
Identificação e explicação de cada camada da arquitetura (por exemplo, frontend, backend, banco de dados).

* **Componentes Principais:**
Descrição detalhada dos principais componentes, como servidores web, bancos de dados, serviços externos, etc.

**Padrões de Design e Princípios**

* **Padrões Utilizados:**
Documentação sobre padrões arquiteturais específicos utilizados no sistema, como MVC, Microservices, SOA, entre outros.

* **Princípios de Design:**
Enumeração dos princípios de design adotados, como SOLID, DRY, KISS, etc.

**Decisões Arquiteturais**

* **Registros de Decisões (ADR):**
Documentação de decisões arquiteturais importantes, incluindo o contexto, a decisão tomada e as consequências.

* **Razão por Trás das Escolhas:**
Explicação do raciocínio por trás das decisões arquiteturais, considerando requisitos não funcionais, escalabilidade, manutenibilidade, etc.

**Comunicação entre Componentes**

* **Interfaces e Contratos:**
Detalhes sobre como os diferentes componentes se comunicam, incluindo APIs, contratos, formatos de dados e protocolos utilizados.

* **Protocolos de Comunicação:**
Documentação sobre os protocolos utilizados para comunicação, como HTTP, gRPC, WebSocket, etc.

**Segurança**

* **Considerações de Segurança:**
Informações sobre práticas de segurança adotadas, autenticação, autorização, criptografia, e medidas para proteger contra ameaças conhecidas.

* **Políticas de Segurança:**
Descrição das políticas de segurança aplicadas, incluindo gestão de identidades, controle de acesso e auditorias.

**Escalabilidade e Desempenho**

* **Estratégias de Escalabilidade:**
Informações sobre como o sistema escala horizontal e verticalmente para lidar com maior carga.

* **Otimizações de Desempenho:**
Técnicas e estratégias utilizadas para otimizar o desempenho do sistema.

**Gestão de Dados**

* **Modelos de Dados:**
Descrição dos modelos de dados utilizados no sistema, incluindo esquemas de banco de dados, relacionamentos e indexação.

* **Estratégias de Armazenamento:**
Informações sobre como os dados são armazenados, recuperados e gerenciados.

**Manutenção e Evolução**

* **Procedimentos de Atualização:**
Documentação sobre como atualizar o sistema, incluindo procedimentos e práticas recomendadas.

* **Estratégias de Evolução:**
Informações sobre como o sistema pode evoluir ao longo do tempo, incluindo estratégias para adoção de novas tecnologias e práticas.
---------------------------
## **Componentes Principais**

- **Frontend:**
  Descrição do frontend do sistema.

- **Backend:**
  Descrição do backend do sistema.
---------------------------
## **Padrões de Design**

- Utilizamos o padrão de design MVT (Model View Template) para organizar nosso código.

---------------------------
## **Fluxo de Dados**
- Descrição do fluxo de dados no sistema.

---------------------------

## **APIs**

- **API REST:**
  Descrição da API REST utilizada pelo sistema.
---------------------------
## **Segurança**

Discussão sobre práticas de segurança implementadas no sistema. 

---------------------------

First Header | Second Header | Third Header
------------ | ------------- | ------------
Content Cell | Content Cell  | Content Cell
Content Cell | Content Cell  | Content Cell

---------------------------

```python
def fn():
    pass
```

---------------------------

### Versão
* `0.0.1`

---------------------------

### Lincença
* MIT