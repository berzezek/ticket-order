class DataMixins:

    def set_shared_data(self, key, value):
        """Сохраняет данные в словарь shared_data"""
        self.shared_data[key] = value

    def get_shared_data(self, key):
        """Получает данные из словаря shared_data"""
        return self.shared_data.get(key)