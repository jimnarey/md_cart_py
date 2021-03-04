import os
import rom

ROM_PATH = '../md_cart_fixt'

ROM_FILES = [
            'Sonic Compilation (REV 00) (A) [!].bin',
            'Sonic the Hedgehog (JUE) [R-Jap][!].bin',
            'Sonic The Hedgehog (USA, Europe).md',
            'Sonic The Hedgehog (W) (REV00) [!].gen',
            'Sonic The Hedgehog (W) (REV01) [!].gen'
            ]

filepaths = [os.path.join(ROM_PATH, rom_file) for rom_file in ROM_FILES]

# rom = rom.Rom(filepaths[0])

for filepath in filepaths:
    r = rom.Rom(filepath)
    print(r.sys_text())
