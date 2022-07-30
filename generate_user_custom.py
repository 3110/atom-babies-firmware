Import("env")
import os

firmware_name = env.GetProjectOption("custom_firmware_name")
firmware_version = env.GetProjectOption('custom_firmware_version')
firmware_suffix = env.GetProjectOption('custom_firmware_suffix')
firmware_dir = env.GetProjectOption('custom_firmware_dir')
firmware_bin = os.path.join(firmware_dir, '%s_%s%s' % (firmware_name, firmware_version, firmware_suffix))

app_bin = os.path.join('$BUILD_DIR','${PROGNAME}%s' % firmware_suffix)

env.AddCustomTarget(
    name="firmware",
    dependencies=['buildfs'],
    actions=[
        '"$PYTHONEXE" "$UPLOADER" --chip esp32 merge_bin -o %s %s $ESP32_APP_OFFSET %s' % (firmware_bin, ' '.join([addr + " " + name for addr, name in env['FLASH_EXTRA_IMAGES']]), app_bin)
    ],
    title="Generate User Custom")