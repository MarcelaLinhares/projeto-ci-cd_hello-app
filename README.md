># Projeto CI/CD com GitHub Actions - PB Compass UOL - ABR 2025 | DevSecOps

## 📝 Descrição do Projeto


O projeto foi desenvolvido como parte da trilha de CI/CD no Programa de Bolsas da Compass UOL – Abril 2025 | DevSecOps.

O objetivo principal foi implementar um pipeline completo de integração e entrega contínua (CI/CD), utilizando o GitHub Actions para build e push de uma imagem Docker de uma aplicação FastAPI, além da integração com o ArgoCD para entrega contínua em um cluster Kubernetes local via Rancher Desktop.

Durante o processo, configurei dois repositórios Git (aplicação e manifestos), desenvolvi o workflow automatizado com GitHub Actions, realizei a publicação da imagem no Docker Hub e implementei a atualização automática do manifesto Kubernetes via Pull Request no repositório monitorado pelo ArgoCD.

Com este projeto, aprendi na prática os fundamentos da automação de pipelines CI/CD, o uso de GitHub Actions com Docker Hub e a abordagem GitOps com ArgoCD para deploys Kubernetes.


## 🛠️ Tecnologias Utilizadas

![Rancher Desktop](https://img.shields.io/badge/Rancher%20Desktop-0075A8?style=for-the-badge&logo=rancher)
![WSL2 Ubuntu](https://img.shields.io/badge/WSL2-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white)
![Docker Hub](https://img.shields.io/badge/Docker%20Hub-003f8c?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes)
![ArgoCD](https://img.shields.io/badge/ArgoCD-F08705?style=for-the-badge&logo=argo)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-4A4A4A?style=for-the-badge&logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Python 3](https://img.shields.io/badge/Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white)
![VS Code](https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=visualstudiocode)


## 🔗 Repositório de Manifestos Kubernetes

Este projeto utiliza um segundo repositório exclusivo para os manifestos de deployment e service utilizados pelo ArgoCD.

👉 Acesse aqui: [projeto-ci-cd_manifests](https://github.com/MarcelaLinhares/projeto-ci-cd_manifests)


## ✅ Pré-requisitos

- **Conta no GitHub** (repo público)  
- **Conta no Docker Hub** com token de acesso  
- **Rancher Desktop com Kubernetes habilitado**  
- **kubectl configurado corretamente** (kubectl get nodes)  
- **ArgoCD instalado no cluster local**  
- **Git instalado**  
- **Python 3 e Docker instalados**  


## 🔽 Etapas do Projeto 

>O projeto foi dividido em **5 etapas sequenciais**, sendo fundamental que o usuário siga **exatamente na ordem**, começando pela **Etapa 01** e prosseguindo até a **Etapa 05**, para garantir o funcionamento correto de toda a integração.

>Cada etapa possui um README específico com o **passo a passo detalhado**, os **prints de cada configuração** e as **instruções necessárias**.

>👉 **Clique no link de cada etapa abaixo para acessar o seu respectivo README:**  

### ➤ Etapa 01 – Aplicação FastAPI e Dockerfile  
Criação da aplicação Python com FastAPI e Dockerfile para empacotamento.  
**[🔗 ACESSE O PASSO A PASSO COMPLETO DA ETAPA 01](etapas-readmes/etapa-01-fastapi-dockerfile.md)**<br><br>

### ➤ Etapa 02 – Configuração do GitHub Actions (CI/CD)  
Implementação da pipeline para build, push no Docker Hub e alteração automática do manifesto.  
**[🔗 ACESSE O PASSO A PASSO COMPLETO DA ETAPA 02](etapas-readmes/etapa-02-github-actions.md)**<br><br>

### ➤ Etapa 03 – Repositório com Manifestos Kubernetes  
Criação dos arquivos `deployment.yaml` e `service.yaml` utilizados pelo ArgoCD.  
**[🔗 ACESSE O PASSO A PASSO COMPLETO DA ETAPA 03](etapas-readmes/etapa-03-manifests.md)**<br><br>

### ➤ Etapa 04 – Integração com ArgoCD  
Criação do App no ArgoCD e vinculação com o repositório de manifestos.  
**[🔗 ACESSE O PASSO A PASSO COMPLETO DA ETAPA 04](etapas-readmes/etapa-04-argocd.md)**<br><br>

### ➤ Etapa 05 – Testes de Deploy e Atualização  
Acesso via port-forward, modificação da aplicação e verificação do redeploy automático.  
**[🔗 ACESSE O PASSO A PASSO COMPLETO DA ETAPA 05](etapas-readmes/etapa-05-teste-final.md)**<br><br>


## 👩‍💻 Desenvolvido por:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/MarcelaLinhares">
        <img src="https://avatars.githubusercontent.com/u/141354578?v=4" width="80px;" alt="Foto de perfil GitHub da Marcela Linhares"/><br />
        <sub><b>Marcela Linhares</b></sub>
      </a>
    </td>
  </tr>
</table>

---
