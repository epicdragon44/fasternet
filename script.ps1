if (!([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process PowerShell -Verb RunAs "-NoProfile -ExecutionPolicy Bypass -Command `"cd '$pwd'; & '$PSCommandPath';`"";
    exit;
}
Set-DNSClientServerAddress "Ethernet" –ServerAddresses ("192.168.1.1", "74.82.42.42")
Set-DNSClientServerAddress "Wi-Fi" –ServerAddresses ("192.168.1.1", "74.82.42.42")