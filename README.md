# ATOM Babies ファームウェア for M5Burner v3

M5Burner v3 の User Custom で配布する ATOM Babies のファームウェアです。

## 事前準備

[PlatformIO](https://platformio.org/) 環境が必要です。私は Windows 11 環境で[PlatformIO IDE for VSCode](https://platformio.org/install/ide?install=vscode)を使用しています。

## 実行方法

PlatformIO のメニューから「Generate User Custom」を実行すると`firmware/atom_babies_firmware_バージョン番号.bin`が生成されます。ファームウェアが生成されるディレクトリとバージョン番号は，それぞれ`platformio.ini`の`custom_firmware_dir`と`custom_firmware_version`で指定します。

## 他のプロジェクトで利用する方法

利用するプロジェクトの`platformio.ini`があるディレクトリに`generate_user_custom.py`をコピーし，`platformio.ini`に以下を設定します。

```
[env]
...
custom_firmware_version = 0.0.1 # ファームウェアのバージョン番号
custom_firmware_name = atom_babies_firmware # ファームウェアの名前
custom_firmware_suffix = .bin # ファームウェアの拡張子
custom_firmware_dir = firmware # ファームウェアを生成するディレクトリ（相対パス）
...

[env:m5atom]
...
extra_scripts = post:generate_user_custom.py
```

## 参考

- 「[M5Burner v3 の使いかた](https://zenn.dev/saitotetsuya/articles/m5stack_m5burner_v3)」の「[10. 独自ファームウェアの公開](https://zenn.dev/saitotetsuya/articles/m5stack_m5burner_v3#10.-%E7%8B%AC%E8%87%AA%E3%83%95%E3%82%A1%E3%83%BC%E3%83%A0%E3%82%A6%E3%82%A7%E3%82%A2%E3%81%AE%E5%85%AC%E9%96%8B)」
