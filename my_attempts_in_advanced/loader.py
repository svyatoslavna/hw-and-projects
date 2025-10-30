import os
import numpy
import pandas


class DataLoader:

    def __init__(self, file_path=None):
        self.file_path = file_path
        self.data = None

    def _validate_file_path(self, file_path):
        """Проверяет, существует ли файл и то, что это не директория"""
        if not os.path.exists(file_path):
            raise FileNotFoundError("Ошибка: файл не найден")
        if not os.path.isfile(file_path):
            raise FileNotFoundError("Ошибка: путь ведёт к директории, а не к файлу")
        return True

    def load_data(self, file_path):
        """Загружает данные"""
        self._validate_file_path(file_path)
        try:
            self.data = pandas.read_csv(file_path)
            self.file_path = file_path
            return self.data
        except Exception as e:
            raise Exception(f"Ошибка загрузки CSV-файла: {e}")

    def get_basic_info(self):
        """Вовзращает в виде строки базовую информацию о датасете:
        форму, имена колонок и количество пропущенных значений в каждой колонке."""
        if self.data is None:
            return "Данные не загружены. Сначала вызовите load_data()."
        try:
            data_array = self.data.values
            num_rows, num_columns = data_array.shape
            columns_info = self.data.columns.tolist()
            missing_info = self.data.isnull().sum()
            info_text = "=== БАЗОВАЯ ИНФОРМАЦИЯ ===\n"
            info_text += f"Форма: {data_array.shape}\n"
            info_text += f"Количество строк: {num_rows}\n"
            info_text += f"Количество колонок: {num_columns}\n"
            info_text += "Колонки:\n"
            for i, column in enumerate(columns_info, 1):
                info_text += f"  {i}. {column}\n"

            info_text += "Пропущенные значения по колонкам:\n"
            for column, missing_count in missing_info.items():
                info_text += f"  {column}: {missing_count} пропусков\n"

            return info_text

        except Exception as e:
            return f"Ошибка при анализе данных CSV-файла: {e}"
