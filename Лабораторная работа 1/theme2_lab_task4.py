pages = 100  # TODO ввести количество страниц
lines = 50   # TODO ввести количество строк
chars = 25   # TODO ввести количество символов в строке
BYTES_ONE_CHAR = 1  # размер одного символа в байтах
BYTES_IN_KYLOBITE = 1024
KYLOBITES_IN_MEGABITE = 1024
DISK_CAPACITY_IN_MEGABYTES = 1.44

total_chars = chars * lines * pages          # TODO общее количество символов в книге
total_bytes = total_chars * BYTES_ONE_CHAR   # TODO размер одной книги в байтах

disk_size = DISK_CAPACITY_IN_MEGABYTES * BYTES_IN_KYLOBITE * KYLOBITES_IN_MEGABITE  # TODO размер дискеты в байтах

BOOKS_IN_DISK = disk_size // total_bytes

print(BOOKS_IN_DISK)  # TODO найти количество книг, которое поместится на дискете
