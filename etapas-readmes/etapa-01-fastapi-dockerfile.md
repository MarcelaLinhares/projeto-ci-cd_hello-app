# Etapa 01 – Criar a Aplicação FastAPI e o Dockerfile

Nesta etapa foi desenvolvida a aplicação base do projeto CI/CD, utilizando **FastAPI**, uma das bibliotecas mais modernas para criação de APIs em Python.

Também foi criado o **Dockerfile**, responsável por empacotar essa aplicação em uma imagem Docker que será utilizada nas próximas etapas do pipeline de CI/CD.

👉 Para organizar o projeto, foram criados dois repositórios Git distintos:

- **projeto-ci-cd_hello-app**: repositório principal da aplicação, contendo os arquivos `main.py` e `Dockerfile`.
- **projeto-ci-cd_manifests**: repositório contendo os manifests Kubernetes utilizados pelo ArgoCD.

🔗 **Repositório dos manifests: [projeto-ci-cd_manifests](https://github.com/MarcelaLinhares/projeto-ci-cd_manifests)**

---

## 1. Criação da Aplicação FastAPI

Foi criado o arquivo `main.py` com o seguinte conteúdo:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

🔗 **Link direto para o arquivo: [main.py](https://github.com/MarcelaLinhares/projeto-ci-cd_hello-app/blob/main/main.py)**

## 2. Criação do Dockerfile

Foi criado o arquivo Dockerfile com as instruções para empacotar e executar a aplicação FastAPI em um container:

```dockerfile
FROM python:alpine3.22
WORKDIR /app
RUN pip install fastapi uvicorn
COPY main.py .
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

`FROM python:alpine3.22` - Usa uma imagem leve do Python com Alpine Linux

`WORKDIR /app` - Define o diretório de trabalho dentro do container

`RUN pip install fastapi uvicorn` - Instala as dependências da aplicação

`COPY main.py .` - Copia o arquivo da aplicação para dentro da imagem

`EXPOSE 8080` - Expõe a porta que será usada pela aplicação

`CMD [...]` - Define o comando que inicia o servidor FastAPI com Uvicorn

🔗 **Link direto para o arquivo: [Dockerfile](https://github.com/MarcelaLinhares/projeto-ci-cd_hello-app/blob/main/Dockerfile)**

---

## ✅ Conclusão da Etapa

A aplicação FastAPI foi implementada e empacotada com Docker, estando pronta para ser utilizada no pipeline de CI/CD com GitHub Actions e deploy via ArgoCD.

---

### **[🔙 Voltar - README Principal](https://github.com/MarcelaLinhares/projeto-ci-cd_hello-app) | [➡️ Avançar - Etapa 02](etapas-readmes/etapa-02-github-actions.md)**