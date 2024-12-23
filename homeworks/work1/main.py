import time
import csv
import argparse
from commands import CommandDispatcher

class ShellEmulator:
    def __init__(self, username, fs_path, log_path):
        self.log_file = open(log_path, 'w', newline='')
        self.logger = csv.writer(self.log_file)
        self.logger.writerow(['Timestamp', 'Command'])
        self.username = username
        self.hostname = "NVpc"
        self.fs_path = fs_path
        self.dispatcher = CommandDispatcher(self.fs_path, self.username)

    def execute_command(self, command):
        """Выполнение команды"""
        result = self.dispatcher.execute(command)
        self.log_command(command)
        return result

    def log_command(self, command):
        """Логирование команды"""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.logger.writerow([timestamp, command])

    def start_console(self):
        """Запуск консольного интерфейса для ввода команд"""
        print(f"Welcome to {self.dispatcher.uname} shell emulator, {self.username}!. Type 'exit' to exit.")
        while True:
            try:
                command = input(f"\033[0;32m{self.username}@{self.hostname}\033[0m:{self.dispatcher.inputPrompt_path}$ ").strip()
                result = self.execute_command(command)
                print(result) if result else 0
            except Exception as e:
                print(f"Error: {e}")


# Запуск эмулятора 
if __name__ == "__main__":     
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", required=True, help="Имя компьютера для показа в приглашении к вводу.")
    parser.add_argument("-p", "--path", required=True, help="Путь к архиву виртуальной файловой системы.")
    parser.add_argument("-l", "--log", required=True, help="Путь к лог-файлу.")
    args = parser.parse_args()
    emulator = ShellEmulator(
                            username=args.name, 
                            fs_path=args.path, 
                            log_path=args.log)
    emulator.start_console()