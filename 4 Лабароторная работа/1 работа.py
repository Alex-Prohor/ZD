class Printer3D:
    """Базовый класс для 3D-принтеров."""

    def __init__(self, model: str, manufacturer: str, print_volume: tuple[float, float, float]):
        """
        :param model: Модель принтера.
        :param manufacturer: Производитель принтера.
        :param print_volume: Объем печати (X, Y, Z) в мм.
        """
        self._model = model  # Инкапсуляция, так как модель не должна изменяться после создания объекта
        self._manufacturer = manufacturer  # Аналогично с производителем
        self.print_volume = print_volume  # Использует setter

    @property
    def model(self) -> str:
        return self._model

    @property
    def manufacturer(self) -> str:
        return self._manufacturer

    @property
    def print_volume(self) -> tuple[float, float, float]:
        return self._print_volume

    @print_volume.setter
    def print_volume(self, value: tuple[float, float, float]):
        if not (isinstance(value, tuple) and len(value) == 3 and all(
                isinstance(i, (int, float)) and i > 0 for i in value)):
            raise ValueError("Объем печати должен быть кортежем из трех положительных чисел (X, Y, Z).")
        self._print_volume = value

    def __str__(self) -> str:
        return f"3D-принтер {self.model} от {self.manufacturer}, объем печати: {self.print_volume} мм"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model={self.model!r}, manufacturer={self.manufacturer!r}, print_volume={self.print_volume})"


class FDMPrinter(Printer3D):
    """Класс для FDM 3D-принтеров."""

    def __init__(self, model: str, manufacturer: str, print_volume: tuple[float, float, float], nozzle_diameter: float):
        """
        :param nozzle_diameter: Диаметр сопла (мм).
        """
        super().__init__(model, manufacturer, print_volume)
        self.nozzle_diameter = nozzle_diameter  # Использует setter

    @property
    def nozzle_diameter(self) -> float:
        return self._nozzle_diameter

    @nozzle_diameter.setter
    def nozzle_diameter(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Диаметр сопла должен быть положительным числом.")
        self._nozzle_diameter = value

    def calibrate(self) -> str:
        """Метод калибровки принтера."""
        return f"Калибровка сопла {self.nozzle_diameter} мм на {self.model} завершена."

    def __str__(self) -> str:
        return f"FDM 3D-принтер {self.model} от {self.manufacturer}, объем печати: {self.print_volume} мм, сопло {self.nozzle_diameter} мм"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model={self.model!r}, manufacturer={self.manufacturer!r}, print_volume={self.print_volume}, nozzle_diameter={self.nozzle_diameter})"


# Тестовый запуск
if __name__ == "__main__":
    fdm_printer = FDMPrinter("Crealiti 1", "Creality", (220, 220, 250), 0.4)

    print(fdm_printer)
    print(repr(fdm_printer))
    print(fdm_printer.calibrate())
