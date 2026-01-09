# Казанский храм - Официальный сайт

[![Flask](https://img.shields.io/badge/Flask-3.1.2-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)

[![Nginx](https://img.shields.io/badge/Nginx-✓-009639?logo=nginx&logoColor=white)](https://nginx.org)

[![Gunicorn](https://img.shields.io/badge/Gunicorn-✓-499848?logo=gunicorn&logoColor=white)](https://gunicorn.org)

[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-✓-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)

[![Production](https://img.shields.io/badge/Production-Online-brightgreen)](https://hram-oktyabrsky.ru)

**Официальный информационный портал Казанского храма с полным циклом production-развертывания на VPS через CI/CD.**

## Особенности проекта

*   **Профессиональный адаптивный дизайн** — Оптимизирован для всех устройств от мобильных до десктопов    
*   **Единая архитектура страниц** — Все информационные разделы в одном шаблоне с динамической загрузкой    
*   **Интерактивные фотогалереи** — Полноэкранный просмотр с навигацией клавишами и тач-жестами  
*   **Production-ready инфраструктура** — Автоматический деплой, systemd сервис, мониторинг здоровья  
*   **Полный CI/CD цикл** — Тестирование и деплой через GitHub Actions при каждом коммите  
*   **Безопасная конфигурация** — Изолированное окружение, SSH-ключи, резервное копирование  

## Технологический стек

## Backend:  
* Python 3.11  
* Flask 3.1.2  
* Gunicorn (production) 23.0.0
* Systemd (сервисное управление)  

## Frontend:  
* HTML5 + Jinja2 шаблоны  
* CSS3 с Flexbox/Grid  
* Vanilla JavaScript (без зависимостей)  
* Адаптивный дизайн (3 брейкпоинта)  

## Инфраструктура:  
* Ubuntu Server (VPS на reg.ru)  
* GitHub Actions CI/CD  
* SSH-ключи для безопасного доступа  
* Nginx (обратный прокси)  

## Инструменты разработки  
* Git + GitHub  
* Virtual Environment  
* VS Code  
* Bash скрипты  

## Архитектура проекта

```
temple_site/
├── app.py                     # Основное Flask приложение с маршрутизацией
├── requirements.txt           # Python зависимости (Flask, gunicorn)
├── .github/workflows/        # CI/CD пайплайн GitHub Actions
│   └── deploy.yml            # Полный workflow: тестирование → деплой
├── templates/                 # HTML шаблоны
│   ├── index.html            # Главная страница с навигацией
│   └── about.html            # ЕДИНЫЙ шаблон для всех разделов (Jinja2)
├── static/                    # Статические ресурсы
│   ├── css/
│   │   └── style.css         # Полностью адаптивные стили (1600+ строк)
│   └── images/               # Медиафайлы (оптимизированные)
│       ├── temple.jpg        # Главное фото храма
│       ├── icon1-2.jpg       # Иконы для главной страницы
│       ├── photo1-10.jpg     # Фотогалерея храма
│       └── shrine1-4.jpg     # Святыни храма
├── .venv/                    # Виртуальное окружение Python
├── .gitignore               # Игнорируемые файлы Git
└── README.md                # Документация проекта
```

## Ключевые технические решения

### 1. Единый шаблон для всех разделов
```python
# app.py - единая точка входа для всех разделов
@app.route('/about')
def about():
    return render_template('about.html', section='about')

@app.route('/clergy')
def clergy():
    return render_template('about.html', section='clergy')
```
```html
<!-- about.html - динамическое отображение через Jinja2 -->
{% if section == 'about' %}
    <h2>О храме</h2>
    <p>История храма...</p>
{% elif section == 'clergy' %}
    <h2>Духовенство</h2>
    <p>Настоятель: протоиерей Михаил...</p>
{% endif %}
```
**Преимущества:**
* Единая кодовая база для всех разделов
* Простое добавление новых разделов
* Согласованный дизайн на всех страницах

### 2. Адаптивный дизайн с 3 брейкпоинтами
```css
/* Десктопы: > 1024px */
.container { display: flex; gap: 1cm; }

/* Планшеты: 769px - 1024px */
@media (max-width: 1024px) {
    .container { padding: 0.3cm; gap: 0.8cm; }
}

/* Мобильные: < 768px */
@media (max-width: 768px) {
    .container { flex-direction: column; }
    .temple-photo { max-height: 50vh; }
}
```
### 3. Интерактивные галереи на чистом JavaScript
```javascript
// Фотогалерея с навигацией и управлением клавиатурой
function openModal(img) {
    currentImageIndex = Array.from(images).indexOf(img);
    document.getElementById('imageModal').style.display = 'block';
    document.body.style.overflow = 'hidden';
}

// Управление стрелками и ESC
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeModal();
    if (e.key === 'ArrowLeft') changeImage(-1);
    if (e.key === 'ArrowRight') changeImage(1);
});
```
### 4.  Production-развертывание с нуля
```bash
# Ручная настройка сервера
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv nginx git -y

# Настройка systemd сервиса
sudo systemctl enable temple-site
sudo systemctl start temple-site

# Конфигурация Nginx
sudo nginx -t && sudo systemctl restart nginx
```
### 5. Полный CI/CD пайплайн
```yaml
# .github/workflows/deploy.yml
name: Deploy Temple Site

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Debug - Show all files
        run: |
          find . -type f -name "*.txt" -o -name "*.py" | sort
          cat -n requirements.txt
      
      - name: Install dependencies with debug
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - name: Setup SSH
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.SSH_PRIVATE_KEY }}" > ~/.ssh/id_ed25519
          chmod 600 ~/.ssh/id_ed25519
      
      - name: Deploy to server
        run: |
          # Резервное копирование
          ssh user@server "cd /opt/temple_site && mkdir -p backups/"
          
          # Копирование файлов
          scp -r . user@server:/opt/temple_site/
          
          # Перезапуск сервиса
          ssh user@server "
            cd /opt/temple_site
            source venv/bin/activate
            pip install -r requirements.txt
            sudo systemctl restart temple-site            
          "
```

## Быстрый старт для разработки

### Установка и запуск

```bash
# 1. Клонирование репозитория
git clone https://github.com/mikhailbbk/temple_site.git
cd temple_site

# 2. Создание виртуального окружения
python3 -m venv .venv

# Активация (Linux/Mac)
source .venv/bin/activate

# Активация (Windows)
# .venv\Scripts\activate

# 3. Установка зависимостей
pip install -r requirements.txt

# 4. Запуск локального сервера
python app.py
```

## Production развертывание

### 1. Подготовка VPS сервера
```bash
# Обновление системы
sudo apt update && sudo apt upgrade -y

# Установка базовых пакетов
sudo apt install python3 python3-pip python3-venv nginx git ufw -y

# Настройка брандмауэра
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw --force enable
```
### 2. Развертывание приложения
```bash
# Создание рабочей директории
sudo mkdir -p /opt/temple_site
sudo chown -R $USER:$USER /opt/temple_site
cd /opt/temple_site

# Клонирование проекта
git clone https://github.com/mikhailbbk/temple_site.git .

# Создание виртуального окружения
python3 -m venv venv
source venv/bin/activate

# Установка зависимостей
pip install --upgrade pip
pip install -r requirements.txt
```
### 3. Настройка systemd сервиса
```bash
# Создание файла сервиса
sudo nano /etc/systemd/system/temple-site.service
```
```ini
[Unit]
Description=Gunicorn instance for Казанский храм
After=network.target

[Service]
User=ваш_пользователь
Group=www-data
WorkingDirectory=/opt/temple_site
Environment="PATH=/opt/temple_site/venv/bin"
ExecStart=/opt/temple_site/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/opt/temple_site/temple-site.sock \
    -m 007 \
    app:app

[Install]
WantedBy=multi-user.target
```
```bash
# Активация сервиса
sudo systemctl daemon-reload
sudo systemctl enable temple-site
sudo systemctl start temple-site
sudo systemctl status temple-site
```
### 4. Настройка Nginx
```bash
# Создание конфигурации
sudo nano /etc/nginx/sites-available/temple-site
```
```nginx
server {
    listen 80;
    server_name hram-oktyabrsky.ru;
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/opt/temple_site/temple-site.sock;
    }
    
    location /static {
        alias /opt/temple_site/static;
        expires 30d;
        access_log off;
    }
}
```
```bash
# Активация сайта
sudo ln -s /etc/nginx/sites-available/temple-site /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## Мониторинг и управление

### Проверка статуса
```bash
# Статус приложения
sudo systemctl status temple-site

# Просмотр логов
sudo journalctl -u temple-site -f

# Перезапуск
sudo systemctl restart temple-site
```

### Резервное копирование
```bash
# Автоматическое создание бэкапов в workflow
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backups/$TIMESTAMP"
mkdir -p $BACKUP_DIR
cp -f app.py requirements.txt $BACKUP_DIR/
```

## Информационные разделы сайта

### Навигационная структура:
1. Главная — Фото храма и быстрый доступ ко всем разделам  
2. О храме — История строительства и информация о храме  
3. Духовенство — Контакты настоятеля и служителей  
4. Расписание — Время богослужений и особые службы  
5. Контакты — Адрес, телефоны, навигация (Yandex/Google Maps)  
6. Фото — Интерактивная фотогалерея (10+ фото)  
7. Святыни — Чудотворные иконы и мощи с описанием  
8. Помощь храму — Реквизиты для пожертвований, срочные проекты  

## Срочный проект храма

### Система водоотведения
**Требуется:** 6 000 000 рублей  
**Статус:** Все документы готовы, ожидается финансирование  
**Назначение платежа:** "Пожертвование на водоотведение"  

## Реквизиты для пожертвований:
```text
Полное наименование: Архиерейское Подворье - Храм в Честь Казанской Иконы 
                     Пресвятой Богородицы в П. Октябрьский Ферзиковского района
ИНН: 4020005692
КПП: 402702001
Расчетный счет: 40703810327000000178
Банк: Россельхозбанк
Корр. счет: 30101810100000000780
БИК: 042908780
```
## Контакты храма
**Адрес:** Калужская обл., Ферзиковский район, пос. Октябрьский, д. 1а  
**Настоятель:** протоиерей Михаил Бабков (+7 910 604-43-19)  
**Email:** mikhail.babkov@yandex.ru  
**Telegram:** https://t.me/c/1727599325/1  
**Навигация:** 54.357098, 36.772368  

## Разработка и поддержка
**Разработчик:** Михаил Бабков  
**Технологии:** Python, Flask, Nginx, Systemd, GitHub Actions  
**Статус:** Production, автоматическое обновление через CI/CD  

## Лицензия и использование
Проект разработан для Казанского храма Калужской епархии Московского Патриархата.
Все материалы защищены авторским правом.
Использование кода и дизайна возможно только с разрешения администрации храма.

© 2024 Казанский храм. Калужская епархия Московского Патриархата.

**Сайт доступен по адресу:** https://hram-oktyabrsky.ru  
**Исходный код:** https://github.com/mikhailbbk/temple_site  
**CI/CD:** Автоматический деплой при каждом коммите в main ветку  
