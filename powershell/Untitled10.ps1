$filepath = "C:\Users\Administrator\Desktop\testing112.txt"
$event = get-eventlog -LogName System -EntryType Error | Out-File -FilePath $filepath
$fromaddress = Read-Host -Prompt 'Enter email address'
$toaddress = Read-Host -Prompt 'Enter email address of the Receiver'
$Subject = "Test message" 
$body = "Please find attached - test"
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

