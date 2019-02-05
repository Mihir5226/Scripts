function getIP{(Get-NetIPAddress).IPv4Address | Select-String "192*"}
$IP =getIP
$Hostname = (hostname)
$User = ($env:USERNAME)
 
$Date = Get-Date -Format f

$Version =($HOST.Version.Major)

$Body = "This machine's IP is $IP. User is $User. Hostname is $Hostname. Powershell version $Version. Today's date is $Date"


Send-MailMessage -To "botheaj@ucmail.uc.edu" -From "patelm7@mail.uc.edu" -Subject "IT3038C Windows SysInfo" -Body $Body -SmtpServer smtp.office365.com -port 587 -UseSsl -Credential(Get-Credential)



