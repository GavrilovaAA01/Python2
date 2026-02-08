import doctest


class GameDisk:
    def __init__(self, title: str, platform: str, capacity_gb: float):
        """
        Создание и подготовка к работе объекта "Диск с игрой".

        :param title: Название игры (непустая строка)
        :param platform: Платформа (непустая строка), например "PS5", "Xbox", "Switch"
        :param capacity_gb: Объем диска в ГБ (число > 0)

        Примеры:
        >>> disk = GameDisk("Gran Turismo 7", "PS5", 100.0)
        """
        if not isinstance(title, str):
            raise TypeError("title должен быть типа str")
        if not title.strip():
            raise ValueError("title не должен быть пустой строкой")
        self.title = title.strip()

        if not isinstance(platform, str):
            raise TypeError("platform должен быть типа str")
        if not platform.strip():
            raise ValueError("platform не должен быть пустой строкой")
        self.platform = platform.strip()

        if not isinstance(capacity_gb, (int, float)):
            raise TypeError("capacity_gb должен быть типа int или float")
        if capacity_gb <= 0:
            raise ValueError("capacity_gb должен быть положительным числом")
        self.capacity_gb = float(capacity_gb)

    def is_compatible(self, console_platform: str) -> bool:
        """
        Проверить совместимость диска с платформой приставки.

        :param console_platform: Платформа приставки (непустая строка)
        :return: True если совместим, иначе False

        Примеры:
        >>> disk = GameDisk("Halo", "Xbox", 50)
        >>> disk.is_compatible("Xbox")
        """
        if not isinstance(console_platform, str):
            raise TypeError("console_platform должен быть типа str")
        if not console_platform.strip():
            raise ValueError("console_platform не должен быть пустой строкой")
        ...

    def install(self, free_space_gb: float) -> None:
        """
        Установить игру при заданном свободном месте (упрощенно).

        :param free_space_gb: Свободное место в ГБ (число >= 0)
        :raise ValueError: Если free_space_gb меньше требуемого места (логика внутри метода)
        :return: None

        Примеры:
        >>> disk = GameDisk("Forza Horizon", "Xbox", 80)
        >>> disk.install(120)
        """
        if not isinstance(free_space_gb, (int, float)):
            raise TypeError("free_space_gb должен быть типа int или float")
        if free_space_gb < 0:
            raise ValueError("free_space_gb не может быть отрицательным")
        ...

    def mark_scratched(self, severity: int) -> None:
        """
        Отметить, что диск поцарапан.

        :param severity: Уровень повреждения (int от 0 до 10)
        :return: None

        Примеры:
        >>> disk = GameDisk("The Legend of Zelda", "Switch", 16)
        >>> disk.mark_scratched(3)
        """
        if not isinstance(severity, int):
            raise TypeError("severity должен быть типа int")
        if severity < 0 or severity > 10:
            raise ValueError("severity должен быть в диапазоне 0..10")
        ...


class GameConsole:
    def __init__(self, model: str, platform: str, storage_gb: float):
        """
        Создание и подготовка к работе объекта "Игровая приставка".

        :param model: Модель приставки (непустая строка), например "PlayStation 5"
        :param platform: Платформа/семейство (непустая строка), например "PS5"
        :param storage_gb: Объем накопителя в ГБ (число > 0)

        Примеры:
        >>> console = GameConsole("PlayStation 5", "PS5", 825)
        """
        if not isinstance(model, str):
            raise TypeError("model должен быть типа str")
        if not model.strip():
            raise ValueError("model не должен быть пустой строкой")
        self.model = model.strip()

        if not isinstance(platform, str):
            raise TypeError("platform должен быть типа str")
        if not platform.strip():
            raise ValueError("platform не должен быть пустой строкой")
        self.platform = platform.strip()

        if not isinstance(storage_gb, (int, float)):
            raise TypeError("storage_gb должен быть типа int или float")
        if storage_gb <= 0:
            raise ValueError("storage_gb должен быть положительным числом")
        self.storage_gb = float(storage_gb)

    def power_on(self) -> None:
        """
        Включить приставку.

        :return: None

        Примеры:
        >>> console = GameConsole("Xbox Series X", "Xbox", 1000)
        >>> console.power_on()
        """
        ...

    def insert_disk(self, disk: GameDisk) -> None:
        """
        Вставить диск в приставку.

        :param disk: Экземпляр GameDisk
        :raise ValueError: Если платформа диска не совпадает с платформой приставки
        :return: None

        Примеры:
        >>> console = GameConsole("PlayStation 5", "PS5", 825)
        >>> disk = GameDisk("Gran Turismo 7", "PS5", 100)
        >>> console.insert_disk(disk)
        """
        if not isinstance(disk, GameDisk):
            raise TypeError("disk должен быть экземпляром GameDisk")
        if disk.platform != self.platform:
            raise ValueError("Диск не совместим с данной приставкой (platform не совпадает)")
        ...

    def free_space_after_install(self, game_size_gb: float) -> float:
        """
        Оценить свободное место после установки игры (упрощенно).

        :param game_size_gb: Размер игры в ГБ (число >= 0)
        :raise ValueError: Если game_size_gb больше объема storage_gb
        :return: Оценка свободного места в ГБ

        Примеры:
        >>> console = GameConsole("Nintendo Switch", "Switch", 64)
        >>> console.free_space_after_install(10)
        """
        if not isinstance(game_size_gb, (int, float)):
            raise TypeError("game_size_gb должен быть типа int или float")
        if game_size_gb < 0:
            raise ValueError("game_size_gb не может быть отрицательным")
        if game_size_gb > self.storage_gb:
            raise ValueError("game_size_gb не может превышать storage_gb")
        ...


class Keyboard:
    def __init__(self, layout: str, keys_count: int, has_backlight: bool):
        """
        Создание и подготовка к работе объекта "Клавиатура".

        :param layout: Раскладка (непустая строка), например "RU", "US"
        :param keys_count: Количество клавиш (int > 0)
        :param has_backlight: Наличие подсветки (bool)

        Примеры:
        >>> keyboard = Keyboard("US", 104, True)
        """
        if not isinstance(layout, str):
            raise TypeError("layout должен быть типа str")
        if not layout.strip():
            raise ValueError("layout не должен быть пустой строкой")
        self.layout = layout.strip()

        if not isinstance(keys_count, int):
            raise TypeError("keys_count должен быть типа int")
        if keys_count <= 0:
            raise ValueError("keys_count должен быть больше 0")
        self.keys_count = keys_count

        if not isinstance(has_backlight, bool):
            raise TypeError("has_backlight должен быть типа bool")
        self.has_backlight = has_backlight

    def press_key(self, key: str) -> None:
        """
        Нажать клавишу.

        :param key: Название/символ клавиши (непустая строка)
        :return: None

        Примеры:
        >>> keyboard = Keyboard("RU", 104, False)
        >>> keyboard.press_key("A")
        """
        if not isinstance(key, str):
            raise TypeError("key должен быть типа str")
        if not key.strip():
            raise ValueError("key не должен быть пустой строкой")
        ...

    def set_backlight_brightness(self, brightness: int) -> None:
        """
        Установить яркость подсветки.

        :param brightness: Яркость (int от 0 до 100)
        :raise ValueError: Если у клавиатуры нет подсветки
        :return: None

        Примеры:
        >>> keyboard = Keyboard("US", 87, True)
        >>> keyboard.set_backlight_brightness(50)
        """
        if not isinstance(brightness, int):
            raise TypeError("brightness должен быть типа int")
        if brightness < 0 or brightness > 100:
            raise ValueError("brightness должен быть в диапазоне 0..100")
        if not self.has_backlight:
            raise ValueError("Нельзя менять яркость: у клавиатуры нет подсветки")
        ...

    def connect(self, device_name: str) -> bool:
        """
        Подключить клавиатуру к устройству (условная операция).

        :param device_name: Имя устройства (непустая строка)
        :return: True, если подключение возможно/успешно (логика не реализуется)

        Примеры:
        >>> keyboard = Keyboard("US", 104, True)
        >>> keyboard.connect("PlayStation 5")
        """
        if not isinstance(device_name, str):
            raise TypeError("device_name должен быть типа str")
        if not device_name.strip():
            raise ValueError("device_name не должен быть пустой строкой")
        ...


if __name__ == "__main__":
    doctest.testmod()

