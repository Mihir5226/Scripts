function getIP{(Get-NetIPAddress).IPv4Address | Select-String "192*"}

function pinggoogle
{
ping google.com
}