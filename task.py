import json


class Dataset:
    def __init__(self, filename):
        self.filename = filename
        self.data = self._read_file()

    def _read_file(self):
        """Считывает файл"""
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("Error: The file was not found.")
        except json.JSONDecodeError:
            print("Error: JSON decoding error.")
        except Exception as e:
            print(f"Error: {e}")

    def get_song(self, song_id):
        """Возвращает название песни по её id"""
        return self.data[song_id - 1].get("title")

    def find_similar(self, song_id):
        """Возвращает названия похожих песен через запятую"""
        similar_title = ""
        similar_title_list = []
        similar_id_list = self.data[song_id - 1].get("similar_ids") # Находит id похожих песен и сохраняет их в виде списка
        for similar_id in similar_id_list: # Перебирает каждую похожую песню из списка по id
            similar_title = self.data[similar_id - 1].get("title")  # Находит название похожей песни из списка
            similar_title_list.append(similar_title) # Добавляет в список название похожей песни
        return ", ".join(similar_title_list) # Возвращает строку с названиями похожих песен через запятую


if __name__ == "__main__":
    dataset = Dataset("api.json")
    print(f"Here you see all the data:\n{dataset.data}\n") # Выводит всю информацию в виде словаря
    print(f"Song #1: {dataset.get_song(1)}\n") # Выводит название первой песни
    print(f"Songs that are similar to song #1: {dataset.find_similar(1)}") # Выводит названия похожих на первую песен