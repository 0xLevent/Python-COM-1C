var WshShell = new ActiveXObject("WScript.Shell");

// VBScript kullanarak InputBox fonksiyonunu çağırmak
var number = WshShell.Exec('cscript //Nologo inputbox.vbs').StdOut.ReadLine();

if (number !== null && number !== "") {
    try {
        var comObject = new ActiveXObject("Python.SaveNumber");
        comObject.SaveNumber(number);
        WshShell.Popup("Sayı kaydedildi.", 0, "Bilgi", 64);
    } catch (error) {
        WshShell.Popup("COM objesi oluşturulamadı: " + error.message, 0, "Hata", 16);
    }
}
