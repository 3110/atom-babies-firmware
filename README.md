# ATOM Babies ファームウェア for M5Burner v3

M5Burner v3 の User Custom で配布する [ATOM Babies](https://github.com/3110/atom-babies-arduino) のファームウェアです。

## 事前準備

[PlatformIO](https://platformio.org/) 環境が必要です。私は Windows 11 環境で[PlatformIO IDE for VSCode](https://platformio.org/install/ide?install=vscode)を使用しています。

## 実行方法

PlatformIO のメニューから「Generate User Custom」を実行すると`firmware/atom_babies_firmware_バージョン番号.bin`が生成されます。ファームウェアが生成されるディレクトリとバージョン番号は，それぞれ`platformio.ini`の`custom_firmware_dir`と`custom_firmware_version`で指定します。

## 他のプロジェクトで利用する方法

[M5Burner v3で独自ファームウェアを生成する雛形](https://github.com/3110/m5burner-user-custom-platformio-template)を参照してください。

## 参考

- 「[M5Burner v3 の使いかた](https://zenn.dev/saitotetsuya/articles/m5stack_m5burner_v3)」の「[10. 独自ファームウェアの公開](https://zenn.dev/saitotetsuya/articles/m5stack_m5burner_v3#10.-%E7%8B%AC%E8%87%AA%E3%83%95%E3%82%A1%E3%83%BC%E3%83%A0%E3%82%A6%E3%82%A7%E3%82%A2%E3%81%AE%E5%85%AC%E9%96%8B)」
