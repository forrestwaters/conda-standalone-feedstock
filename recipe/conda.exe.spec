# -*- mode: python ; coding: utf-8 -*-
import os
import sys

block_cipher = None

datas = []
if sys.platform == "win-32":
    datas = [(os.path.join(os.getcwd(), 'constructor', 'constructor', 'nsis', '_nsis.py'), 'Lib')]

a = Analysis(['entry_point.py', 'imports.py'],
             pathex=['.'],
             binaries=[],
             datas=datas,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='conda.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=True,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )