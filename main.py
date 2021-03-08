import os
import rom

ROM_PATH = '../md_cart_fixt'


MAC_ROM_FILES = [
            'Sonic The Hedgehog (USA, Europe).md',
            'Sonic The Hedgehog (W) (REV00) [!].gen',
            'Sonic The Hedgehog 2 (W) (REV00) [!].gen',
            'Sonic The Hedgehog 2 (World).md'
            ]

LIN_ROM_FILES = [
            'Sonic Compilation (REV 00) (A) [!].bin',
            'Sonic the Hedgehog (JUE) [R-Jap][!].bin',
            'Sonic The Hedgehog (USA, Europe).md',
            'Sonic The Hedgehog (W) (REV00) [!].gen',
            'Sonic The Hedgehog (W) (REV01) [!].gen'
            ]

ROM_FILES = MAC_ROM_FILES

filepaths = [os.path.join(ROM_PATH, rom_file) for rom_file in ROM_FILES]

for filepath in filepaths:
    r = rom.Rom(filepath)
    # print(r.system_id())
    r.header()
