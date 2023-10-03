import subprocess


def get_updates():
    # Получаем список пакетов для обновления
    process = subprocess.Popen(
        ['dnf', 'check-update', '--refresh'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    return parse_updates(stdout.decode('utf-8'))


def parse_updates(output):
    lines = output.strip().split("\n")
    update_lines = []

    # Найти пустую строку и начать собирать обновления после неё
    found_empty_line = False
    for line in lines:
        if line.strip() == "":
            found_empty_line = True
        elif found_empty_line:
            update_lines.append(line.split()[0])

    return "\n".join(update_lines)


def send_kde_notification(message):
    result = subprocess.run([
        'kdialog', '--icon', 'utilities-terminal', '--yesno',
        f"Доступны обновления:\n{message}\n\nХотите обновить сейчас?",
        '--title', 'Обновления'
    ])

    if result.returncode == 0:
        subprocess.run(['konsole', '-e', 'sudo dnf update -y'])


if __name__ == '__main__':
    updates = get_updates()
    if updates:
        send_kde_notification(updates)
