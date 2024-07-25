import os
import pythoncom
import win32com.server.util
import win32com.server.register

class SaveNumber:
    _public_methods_ = ['SaveNumber']
    _reg_progid_ = "Python.SaveNumber"
    _reg_clsid_ = pythoncom.CreateGuid()

    def SaveNumber(self, number):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "numbers.txt")
        try:
            with open(file_path, "a") as file:
                file.write(f"{number}\n")
            return True
        except Exception as e:
            print(f"Hata oluştu: {e}")
            return False

if __name__ == "__main__":
    from win32com.server.register import UseCommandLine
    UseCommandLine(SaveNumber)