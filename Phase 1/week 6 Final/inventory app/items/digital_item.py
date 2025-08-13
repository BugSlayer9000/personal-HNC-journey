from item import Item
from datetime import datetime

class DigitalItem(Item):
    def __init__(self, _id: str, _name: str, _price: float, _quantity: int, _category: str, _created_at: datetime, _file_size: float, _download_link: str) -> None:
        self._file_size = _file_size
        self._download_link = _download_link
        super().__init__(_id, _name, _price, _quantity, _category, _created_at)
        

    @property
    def file_size(self):
        return self._file_size

    @property
    def download_link(self):
        return self._download_link

    def _attribute_check(self):
        if not isinstance(self._file_size, (int, float)):
            raise ValueError("File size must be a number")
        
        if self._file_size <= 0:
            raise ValueError("File size must be positive")

        if not isinstance(self._download_link, str):
            raise ValueError("Download link must be a string")
        return super()._attribute_check()

