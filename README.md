# super-marketplace. Пример user checkout flow с использованием RabbitMQ
## Руководство по развертыванию приложения.
___

## Как развернуть в кластере кубера?
### 1) Создаем кластер `kind create cluster -n market`
### 2) Накатываем ingress/deploy/service `nginx`, `elk` через релизы `helm`:
```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm install elasticsearch bitnami/elasticsearch
helm install kibana bitnami/kibana
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm repo update
helm install nginx-ingress ingress-nginx/ingress-nginx --namespace ingress-nginx --create-namespace
```
### 3) Чекаем стэйт подов внешнего load balancer   `kubectl get pods -n ingress-nginx`
### 4) Чекаем подхватил ли он статик айпишник от провайдера `kubectl get svc -n ingress-nginx`
### 5) Накатываем манифесты кибаны/эластика/бэкенда
```
kubectl apply -f kibana-ingress.yml
kubectl apply -f dev-configmap.yml
kubectl apply -f backend.ingress.yml
kubectl apply -f elk-manifest.yml
```
____
## Как развернуть локально?
### 1) Клонируем репозиторий

```git clone https://github.com/Dr1DeX/super-marketplace.git```

### 2) Создаем виртуальное окружение, например conda (или вашим любимым пакетным менеджером) 

``` conda create -n example_env ```

### 3) Устанавливаем poetry и зависимости(руководство по установке poetry [тык](https://python-poetry.org/docs/))

### Устанавливаем зависимости:
```poetry install```
### 4) Создание локального файла для хранения переменных окружения
#### В зависимости от окружения нужно будет создать `.env` файл и добавить следующие зависимости, например:

### Локальный  `.env.local `:
```
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=market
DB_DRIVER=postgresql+asyncpg
JWT_SECRET_KEY=mega-super-secret
JWT_ENCODE_ALGORITHM=HS256
RABBITMQ_URL=amqp://guest:guest@localhost/
RABBIT_HOSTNAME=localhost
```
### 5) Локальный запуск приложения с помощью `make`
```make run ENV=.env.local```
___
## Как развернуть приложение на стенд с помощью докера?
### 1) Создаем переменную окружения, например:

### `.env.dev`:
```
DB_HOST=market
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=market
DB_DRIVER=postgresql+asyncpg
JWT_SECRET_KEY=mega-super-secret
JWT_ENCODE_ALGORITHM=HS256
RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672/
RABBITMQ_DEFAULT_USER=guest
RABBITMQ_DEFAULT_PASS=guest
RABBIT_HOSTNAME=rabbitmq
```

### 2) Запуск с помощью команды `docker-compose up -d`
___

## Пример ответ ручки:
`GET /product/all`

*Get Products*

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "product_name": "string",
    "product_count": 0,
    "category_id": 0,
    "product_price": 0
  }
]
```

<h3 id="get_products_product_all_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_products_product_all_get-responseschema">Response Schema</h3>

Status Code **200**

*Response Get Products Product All Get*

___
## by Dr1DeX