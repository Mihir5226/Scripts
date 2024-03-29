﻿$createfile = New-Item -path "C:\" -Name "logfile.txt" -ItemType "file"
$filepath = "C:\logfile.txt"
$event = get-eventlog -LogName System -EntryType Error | Out-File -FilePath $filepath
$fromaddress = "patelm7@Mail.uc.edu" 
$toaddress = "patelm7@mail.uc.edu" 
$Subject = "Test message" 
$body = "Please find attached for the logfiles"
$attachment = $filepath
$smtpserver = "smtp.office365.com" 
$emailPort = "587"

$message = new-object System.Net.Mail.MailMessage 
$message.From = $fromaddress 
$message.To.Add($toaddress)
$message.IsBodyHtml = $True 
$message.Subject = $Subject 
$attach = new-object Net.Mail.Attachment($attachment) 
$message.Attachments.Add($attach) 
$message.body = $body 
$smtp = new-object Net.Mail.SmtpClient($smtpserver)
$smtp.Port=$emailPort
$smtp.EnableSsl =$True
$smtp.Credentials=Get-Credential
$smtp.Send($message)

