Set WshShell = Wscript.CreateObject("Wscript.Shell")
strRegKey = "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\Domains\"
WshShell.RegWrite strRegKey & "sberbank.ru\", "", "REG_SZ"
WshShell.RegWrite strRegKey & "\sberbank.ru\cert\", "", "REG_SZ"
WshShell.RegWrite strRegKey & "\sberbank.ru\cert\" & "https", "1", "REG_DWORD"
x=msgbox("Адрес https://cert.sberbank.ru добавлен в зону Local Intranet" ,64, "Добавлено!")
