
import subprocess

if __name__ == '__main__':
    x=input("enter what to prnounce: ")
    command = f'powershell -ExecutionPolicy Bypass -File "D:\\downloads\\script.ps1" -text "{x}"'
    subprocess.run(command, shell=True)
