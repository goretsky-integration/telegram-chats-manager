<h2 align="center">✈️ Telegram chats manager</h2>
<p align="center">
    <a href="https://github.com/goretsky-integration/telegram-chats-manager/actions/workflows/codecov.yaml">
        <img src="https://github.com/goretsky-integration/telegram-chats-manager/actions/workflows/codecov.yaml/badge.svg" alt="Test">
    </a>
    <a href="https://codecov.io/github/goretsky-integration/telegram-chats-manager"> 
        <img src="https://codecov.io/github/goretsky-integration/telegram-chats-manager/branch/master/graph/badge.svg?token=EPNKMXE3BH" alt="codecov"/> 
    </a>
    <img src="https://img.shields.io/badge/python-3.11-brightgreen" alt="python">
</p>

--- 

### 📝 Описание:

Проект содержит скрипт, который синхронизирует данные о Telegram чатах в
сервисе [unit's routes database](https://github.com/goretsky-integration/unit-routes-database).

---

### 🚀 Запуск проекта:

Создание виртуального окружения:

```shell
poetry env use python3.11
```

Активация виртуального окружения:

```shell
poetry shell
```

Установка зависимостей:

```shell
poetry install --without dev
```

Запуск скрипта:

```shell
python src/main.py
```

---

### 🧪 Запуск тестов:

Активация виртуального окружения:

```shell
poetry shell
```

Установка **всех** зависимостей:

```shell
poetry install
```

Запуск тестов:

```shell
pytest
```

Создание отчёта о покрытии тестами:

```shell
pytest --cov-report=html --cov=./src
```

В корне проекта будет создана директория `htmlcov`. Внутри будет файл `index.html`.
