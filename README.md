# ATOM Babies ファームウェア for M5Burner v3

M5Burner v3 の User Custom で配布する ATOM Babies のファームウェアです。

## 事前準備

[PlatformIO](https://platformio.org/) 環境が必要です。私は Windows 11 環境の [VS Code](https://code.visualstudio.com/)で使用しています。

## 実行方法

PlatformIO のメニューから「Generate User Custom」を実行すると`firmware/atom_babies_firmware_バージョン番号.bin`が生成されます。ファームウェアが生成されるディレクトリとバージョン番号は，それぞれ`platformio.ini`の`custom_firmware_dir`と`custom_firmware_version`で指定します。

## 参考

- [M5Burner v3 の使いかた](https://zenn.dev/saitotetsuya/articles/m5stack_m5burner_v3)
