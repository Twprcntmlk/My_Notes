# If port 80:80 is Occupied with system

## In PowerShell
```bash
net stop W3SVC
start docker container
net start W3SVC
```
NET stop HTTP
NET start HTTP

## Diagnostic Tools

```bash
netsh http show urlacl
netstat -ano | findstr LISTENING | findstr :80
```

##
docker run --detach --publish 81:80 --name webserver nginx
