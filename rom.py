

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

    def sys_text(self):
        return [
            self.data[0x100:0x100 + 16],
            self.data[0x80000:0x80000 + 0x100 + 16]
        ]