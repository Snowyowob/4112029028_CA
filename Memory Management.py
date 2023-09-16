page_table = {0: 5, 1: 9, 2: 14}
page_size = input("Please insert page size:")
page_size = int(page_size)
logical_address = input("Please insert logical address:")
logical_address = int(logical_address)
def memory_addressing(page_table, page_size, logical_address):
    page_number, offset = divmod(logical_address, page_size)
    if page_number in page_table:
        frame_number = page_table[page_number]
        physical_address = frame_number * page_size + offset
        print(f"The physical address is {physical_address}")
    else:
        print("Invalid page number, address translation failed.")
memory_addressing(page_table, page_size, logical_address)