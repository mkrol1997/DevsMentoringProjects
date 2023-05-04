class EmptyFilePathError(Exception):
    def __str__(self):
        return "Specified file path can not be empty"


class InvalidFilePathError(Exception):
    def __str__(self):
        return 'Invalid File Path specified.'


class NoConnectorRangeError(Exception):
    def __str__(self):
        return "NoConnector value must be less or equal to 10"


class NoConnectorTypeError(Exception):
    def __str__(self):
        return "NoConnector value must be class <int>"


class FileSizeRangeError(Exception):
    def __str__(self):
        return "Maximum file size must be in range 1000 - 9999"


class FileSizeTypeError(Exception):
    def __str__(self):
        return "Maximum file size must be class <int>"


class FileHandler:
    def __init__(self, file_path: str, no_connectors: int, max_file_size: int):
        FileHandler._validate_path(file_path)
        FileHandler._validate_noconnectors(no_connectors)
        FileHandler._validate_file_size(max_file_size)

        self._file_path = file_path
        self._no_connectors = no_connectors
        self._max_file_size = max_file_size

    @staticmethod
    def _validate_path(file_path: str) -> None:
        if isinstance(file_path, str):
            if len(file_path) == 0:
                raise EmptyFilePathError
        else:
            raise InvalidFilePathError

    @staticmethod
    def _validate_noconnectors(no_connectors: int) -> None:
        if isinstance(no_connectors, int):
            if no_connectors not in range(0, 11):
                raise NoConnectorRangeError
        else:
            raise NoConnectorTypeError

    @staticmethod
    def _validate_file_size(max_file_size: int) -> None:
        if isinstance(max_file_size, int):
            if max_file_size not in range(1000, 10000):
                raise FileSizeRangeError
        else:
            raise FileSizeTypeError

    @staticmethod
    def save_to_file(file_path: str) -> None:
        FileHandler._validate_path(file_path)
        print(f'Saved to file: {file_path}')

    @staticmethod
    def read_content(text: str) -> None:
        if isinstance(text, str):
            if len(text) == 0:
                raise ValueError("Empty string provided")
        else:
            raise TypeError('Invalid type. Expected class <str>')
        print(text)

    def file_path(self):
        return self._file_path

    def change_file_path(self, new_path: str) -> None:
        FileHandler._validate_path(new_path)
        self._file_path = new_path

    def no_connectors(self):
        return self._no_connectors

    def change_no_connectors(self, value: int) -> None:
        FileHandler._validate_noconnectors(value)
        self._no_connectors = value

    def max_file_size(self):
        return self._max_file_size

    def change_max_file_size(self, new_file_size: int) -> None:
        FileHandler._validate_file_size(new_file_size)
        self._max_file_size = new_file_size
