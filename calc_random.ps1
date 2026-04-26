Start-Process calc.exe
Start-Sleep 2
Add-Type -AssemblyName System.Windows.Forms
$a = Get-Random -Minimum 1 -Maximum 100
$b = Get-Random -Minimum 1 -Maximum 100
$op = Get-Random -InputObject @('+', '-', '*', '/')
if ($op -eq '/' -and $b -eq 0) { $b = 1 }
$keys = "$a$op$b="
[System.Windows.Forms.SendKeys]::SendWait($keys)
Start-Sleep 1
[System.Windows.Forms.SendKeys]::SendWait("%{F4}")