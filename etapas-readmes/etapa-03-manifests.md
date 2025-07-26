# Etapa 03 – Criação dos Manifests Kubernetes

Nesta etapa foram criados os **manifests do Kubernetes** que serão utilizados pelo ArgoCD para realizar o deploy automático da aplicação FastAPI.

O repositório de manifests é monitorado pelo ArgoCD e atualizado automaticamente via GitHub Actions com a nova tag da imagem Docker sempre que houver alterações no repositório da aplicação.

---

## 1. Repositório de Manifests

Todos os arquivos desta etapa foram adicionados no repositório:

🔗 **[projeto-ci-cd_manifests](https://github.com/MarcelaLinhares/projeto-ci-cd_manifests)**


## 2. Arquivo `deployment.yaml`

Define o objeto `Deployment` que descreve como o container da aplicação deve ser criado e gerenciado no cluster Kubernetes.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-app-deployment
  labels:
    app: hello-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: hello-app
  template:
    metadata:
      labels:
        app: hello-app
    spec:
      containers:
        - name: hello-app
          image: marcelalinhares/hello-app:latest
          ports:
            - containerPort: 8080
```

## 3. Arquivo `service.yaml`

Define o serviço responsável por expor a aplicação dentro do cluster Kubernetes.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-app-service
spec:
  selector:
    app: hello-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
  type: ClusterIP
```

---

## ✅ Conclusão da Etapa

Com os arquivos deployment.yaml e service.yaml configurados no repositório projeto-ci-cd_manifests, o ArgoCD poderá sincronizar automaticamente os deploys conforme as atualizações de imagem feitas via GitHub Actions.

---

### **[🔙 Voltar - Etapa 02](etapa-02-github-actions.md) | [➡️ Avançar - Etapa 04](etapa-04-argocd.md)**