import header

class Rom:

    def __init__(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.data = file.read()
        except FileNotFoundError:
            self.data = None
            print('File {0} not found'.format(filename))
    
    def size(self):
        return len(self.data)

    # Test on byte-swapped rom
    def system_id(self):
        ids = []
        for byte_slice in [ [0x100, 0x110], [0x80000, 0x80110] ]: # 0x80000 + 0x100 + 16
            try:
                ids.append(self.data[byte_slice[0]:byte_slice[1]].decode())
            except UnicodeDecodeError:
                pass
        return ids

    def header(self):
        for value in Rom.HEADER.values():
            print( '{0} : {1}'.format( value[2], self.data[ value[0]:value[0] + value[1] ] ) )


    # HEADER = {
    #     'system' : [0x100, 16, 'System'],
    #     'copy_release' : [0x110, 16, 'Copyright & Release'],
    #     'title_dom' : [0x120, 48, 'Title (Domestic)'],
    #     'title_int' : [0x150, 48, 'Title (International)'],
    #     'serial' : [0x180, 14, 'Serial Number'],
    #     'rom_check' : [0x18E, 2, 'ROM Checksum'],
    #     'dev_support' : [0x190, 16, 'Device Support'],
    #     'rom_add_range' : [0x1A0, 8, 'ROM Address Range'],
    #     'ram_add_range' : [0x1A8, 8, 'RAM Address Range'],
    #     'extra_mem' : [0x1BC, 12, 'Extra Memory'],
    #     'modem_support' : [0x1BC, 12, 'Modem Support'],
    #     'reserved_1' : [0x1C8, 40, 'Reserved Area 1'],
    #     'region' : [0x1F0, 3, 'Region Support'],
    #     'reserved_2' : [0x1F3, 13, 'Reserved Area 2']
    # }