import os
import subprocess
import shutil
import sys

def check_pyinstaller():
    """Проверяет, установлен ли PyInstaller, и устанавливает его при необходимости."""
    print("Checking PyInstaller installation...")
    result = subprocess.run([sys.executable, "-m", "pip", "show", "pyinstaller"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode != 0:
        print("PyInstaller is not installed. Installing it now...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)

def clean_previous_builds(output_dir, build_dir):
    """Удаляет предыдущие сборки, если они существуют."""
    if os.path.exists(output_dir):
        print("Removing previous build...")
        shutil.rmtree(output_dir)
    if os.path.exists(build_dir):
        print("Removing previous build...")
        shutil.rmtree(build_dir)

def copy_extra_files(output_dir, files):
    """Копирует дополнительные файлы в папку сборки."""
    for file in files:
        if os.path.exists(file):
            shutil.copy(file, output_dir)
            print(f"Copied {file} to {output_dir}")
        else:
            print(f"File {file} not found, skipping.")

def build_executable(script_name, exe_name, output_dir = "dist", build_dir = "build", icon_path = None):
    """Собирает исполняемый файл с помощью PyInstaller."""
    print(f"Building {script_name}...")
    command = [
        "pyinstaller",
        "--onefile",
        f"--hidden-import=sqlalchemy",
        f"--distpath={output_dir}",
        f"--workpath={build_dir}",
        "-s",
        f"-n={exe_name}",
        "--noconsole",
        "--log-level=ERROR",
        script_name
    ]
    if icon_path and os.path.exists(icon_path):
        command.insert(5, f"--icon={icon_path}")

    subprocess.run(command, check=True)

    exe_path = os.path.join(output_dir, f"{exe_name}.exe" if os.name == "nt" else exe_name)
    if os.path.exists(exe_path):
        print(f"Build successful! The executable is located in the {output_dir} folder.")
    else:
        print("Build failed. Please check the PyInstaller logs for details.")

def main():
    os.chdir(os.path.dirname(os.getcwd()))
    script_name = "main.py"
    exe_name = "SportProductsShopPy"
    output_dir = "bin"
    build_dir = "build"
    icon_path = os.path.join("img", "database.ico")
    # icon_path = ""

    check_pyinstaller()
    clean_previous_builds(output_dir, build_dir)
    build_executable(script_name, exe_name, output_dir, build_dir, icon_path)

    # Копируем дополнительные файлы
    extra_files = ["Pril.db"]
    copy_extra_files(output_dir, extra_files)

    # Удаление временных файлов
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    for file in os.listdir():
        if file.endswith(".spec"):
            os.remove(file)

if __name__ == "__main__":
    main()