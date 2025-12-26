# Казанский храм - Официальный сайт

![Казанский храм](static/images/temple.jpg)

Официальный сайт Казанского храма Калужской епархии Московского Патриархата.

## 🏛️ О проекте

Веб-сайт для Казанского храма в пос. Октябрьский Ферзиковского района с информацией о храме, расписанием богослужений, контактами, фотогалереей и возможностью пожертвований.

## ✨ Возможности

- **Информация о храме** - история и описание
- **Духовенство** - информация о настоятеле и контакты
- **Расписание богослужений** - актуальное расписание
- **Контакты** - адрес, телефоны, навигация
- **Фотогалерея** - фотографии храма с модальным просмотром
- **Святыни храма** - информация о чудотворных иконах и мощах
- **Помощь храму** - реквизиты для пожертвований

## 🚀 Технологии

- **Backend**: Flask 3.1.2 (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Сервер**: Gunicorn + Nginx
- **Автоматизация**: GitHub Actions CI/CD
- **Хостинг**: Ubuntu Server на reg.ru

## 🌐 Деплой

Сайт автоматически деплоится при пуше в ветку `main` через GitHub Actions.

### Структура проекта:
temple_site/
├── app.py # Основное Flask приложение
├── requirements.txt # Зависимости Python
├── templates/
│ ├── index.html # Главная страница
│ └── about.html # Страница информации
├── static/
│ ├── css/
│ │ └── style.css # Стили
│ └── images/ # Изображения храма
└── .github/workflows/
└── deploy.yml # GitHub Actions workflow
## 🛠️ Установка и запуск локально

### 1. Клонирование репозитория
```bash
git clone https://github.com/Mikhail15011976/temple_site.git
cd temple_site
### 2. Создание виртуального окружения
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows
### 3. Установка зависимостей
pip install -r requirements.txt
### 4. Запуск приложения
python app.py

### Продакшн-развертывание
Требования на сервере:
Ubuntu/Debian
Python 3.11+
Nginx
Systemd

### Настройка сервера:
#### 1. Установка зависимостей:
sudo apt update
sudo apt install python3-venv nginx -y
#### 2. Настройка проекта:
sudo mkdir -p /opt/temple_site
sudo chown $USER:$USER /opt/temple_site
cd /opt/temple_site
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
#### 3. Systemd сервис:
sudo nano /etc/systemd/system/temple-site.service
Добавить:
[Unit]
Description=Temple Site Flask Application
After=network.target

[Service]
Type=simple
User=mikhail
Group=mikhail
WorkingDirectory=/opt/temple_site
Environment="PATH=/opt/temple_site/venv/bin"
ExecStart=/opt/temple_site/venv/bin/gunicorn --workers 2 --bind 127.0.0.1:5001 --timeout 120 app:app
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
#### 4. Nginx конфигурация:
sudo nano /etc/nginx/sites-available/temple-site
Добавить:
server {
    listen 80;
    server_name 194.67.124.178;
    
    location / {
        proxy_pass http://127.0.0.1:5001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    location /static/ {
        alias /opt/temple_site/static/;
    }
}
