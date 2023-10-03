# English

# Update Notifier

## Description

This Python script checks for available system updates on a Linux machine and sends a KDE notification.

## Requirements

- Python 3.x
- KDE Plasma Desktop
- `kdialog` installed

## Usage

Run the script manually:

```bash
python3 script.py
```

## Autostart Configuration

### Using Cron

1. Open your crontab for editing:

    ```bash
    crontab -e
    ```

2. Add the following line to run the script every day at noon:

    ```bash
    0 12 * * * /usr/bin/python3 /path/to/your/script.py
    ```

### Using Systemd

1. Create a service file, e.g., `/etc/systemd/system/update-notifier.service`:

    ```ini
    [Unit]
    Description=Update Notifier

    [Service]
    ExecStart=/usr/bin/python3 /path/to/your/script.py
    ```

2. Create a timer file, e.g., `/etc/systemd/system/update-notifier.timer`:

    ```ini
    [Unit]
    Description=Runs update-notifier every day

    [Timer]
    OnCalendar=daily
    Persistent=true

    [Install]
    WantedBy=timers.target
    ```

3. Reload systemd and activate the timer:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable --now update-notifier.timer
    ```

---
# Русский

# Уведомитель об Обновлениях

## Описание

Этот скрипт на Python проверяет доступные системные обновления на Linux-машинах и отправляет уведомление KDE.

## Требования

- Python 3.x
- Рабочий стол KDE Plasma
- Установленный `kdialog`

## Использование

Запустите скрипт вручную:

```bash
python3 script.py
```

## Настройка Автозапуска

### Использование Cron

1. Откройте ваш crontab для редактирования:

    ```bash
    crontab -e
    ```

2. Добавьте следующую строку для запуска скрипта каждый день в полдень:

    ```bash
    0 12 * * * /usr/bin/python3 /путь/к/вашему/скрипту.py
    ```

### Использование Systemd

1. Создайте файл службы, например, `/etc/systemd/system/update-notifier.service`:

    ```ini
    [Unit]
    Description=Update Notifier

    [Service]
    ExecStart=/usr/bin/python3 /путь/к/вашему/скрипту.py
    ```

2. Создайте файл таймера, например, `/etc/systemd/system/update-notifier.timer`:

    ```ini
    [Unit]
    Description=Запускает уведомитель об обновлениях каждый день

    [Timer]
    OnCalendar=daily
    Persistent=true

    [Install]
    WantedBy=timers.target
    ```

3. Перезагрузите systemd и активируйте таймер:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable --now update-notifier.timer
    ```
