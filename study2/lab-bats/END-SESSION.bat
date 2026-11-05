@echo off
setlocal

set SCRIPT_DIR=%~dp0
for %%I in ("%SCRIPT_DIR%..") do set OTREE_ROOT=%%~fI

call "%SCRIPT_DIR%lab-config.bat"

echo Stopping oTree server...
set SHELL_PID=
for /f "usebackq delims=" %%P in (`powershell -NoProfile -Command "Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'cmd.exe' -and $_.CommandLine -like '*otree prodserver*' } | Select-Object -First 1 -ExpandProperty ProcessId"`) do set SHELL_PID=%%P

if not defined SHELL_PID (
    echo No oTree server shell found. Already stopped?
    echo.
) else (
    taskkill /PID %SHELL_PID% /T /F >nul 2>&1
)

powershell -NoProfile -Command "if (Get-NetTCPConnection -LocalPort %OTREE_PORT% -State Listen -ErrorAction SilentlyContinue) { exit 1 } else { exit 0 }"
if errorlevel 1 (
    echo WARNING: oTree server still appears to be running on port %OTREE_PORT%.
    echo Close it manually, then re-run END-SESSION.bat.
    echo.
    pause
    exit /b 1
)

call "%SCRIPT_DIR%_backup-db.bat"
if errorlevel 1 (
    echo ERROR: Backup failed.
    echo.
    pause
    exit /b 1
)

for %%I in ("%OTREE_ROOT%\..") do set PROJECT=%%~nxI

if not exist "%BACKUP_ROOT%\%PROJECT%" (
    echo ERROR: Backup folder not found:
    echo %BACKUP_ROOT%\%PROJECT%
    echo.
    pause
    exit /b 1
)

echo Opening backup folder...
explorer "%BACKUP_ROOT%\%PROJECT%"
