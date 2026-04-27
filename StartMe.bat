@echo off
setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul
cd /d "%~dp0"

set "LUVA_ROOT=%~dp0"
if "%LUVA_ROOT:~-1%"=="\" set "LUVA_ROOT=%LUVA_ROOT:~0,-1%"
set "LUVA_VENV=%LUVA_ROOT%\.venv"
set "LUVA_REPORTS=%LUVA_ROOT%\reports"
set "LUVA_UPLOADS=%LUVA_ROOT%\uploads"
set "LUVA_LOG_DIR=%LUVA_ROOT%\artifacts\logs"
set "LUVA_LOG_FILE=%LUVA_LOG_DIR%\StartMe.log"
set "LUVA_SERVER_LOG=%LUVA_LOG_DIR%\gui-server.log"
set "USER_PY_SCRIPTS=%USERPROFILE%\AppData\Roaming\Python\Python312\Scripts"
set "PATH=%USER_PY_SCRIPTS%;%PATH%"
set "PYTHONUTF8=1"
set "PYTHONIOENCODING=utf-8"
set "PYTHONLEGACYWINDOWSSTDIO=utf-8"
set "GUI_URL="
set "GUI_HOST=127.0.0.1"
set "GUI_BASE_PORT=8765"
set "LUVA_SERVER_META=%LUVA_LOG_DIR%\gui-server.json"

if not exist "%LUVA_REPORTS%" mkdir "%LUVA_REPORTS%"
if not exist "%LUVA_UPLOADS%" mkdir "%LUVA_UPLOADS%"
if not exist "%LUVA_LOG_DIR%" mkdir "%LUVA_LOG_DIR%"
echo ==== Luva StartMe.bat run at %date% %time% ==== > "%LUVA_LOG_FILE%"
echo Root: %LUVA_ROOT%>> "%LUVA_LOG_FILE%"

for /f %%P in ('powershell -NoProfile -Command "$tcp = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Loopback, 0); $tcp.Start(); $port = $tcp.LocalEndpoint.Port; $tcp.Stop(); $port"') do set "GUI_BASE_PORT=%%P"

call :log [1/5] Checking Python...
python --version >> "%LUVA_LOG_FILE%" 2>&1
if errorlevel 1 goto :python_missing

call :log [2/5] Ensuring virtual environment exists...
if not exist "%LUVA_VENV%\Scripts\python.exe" (
  call :log Creating local virtual environment...
  python -m venv "%LUVA_VENV%" >> "%LUVA_LOG_FILE%" 2>&1
  if errorlevel 1 goto :venv_failed
) else (
  call :log Existing virtual environment found.
)

call :log [3/5] Installing/repairing Luva dependencies...
call "%LUVA_VENV%\Scripts\python.exe" -m pip install --upgrade pip setuptools wheel >> "%LUVA_LOG_FILE%" 2>&1
if errorlevel 1 goto :install_failed
call "%LUVA_VENV%\Scripts\python.exe" -m pip install -e "%LUVA_ROOT%" >> "%LUVA_LOG_FILE%" 2>&1
if errorlevel 1 goto :install_failed
call :log Dependency repair step completed.

call :log [4/5] Preparing dynamic GUI port selection...
if exist "%LUVA_SERVER_META%" del /q "%LUVA_SERVER_META%" >nul 2>&1

call :log Selected base port: %GUI_BASE_PORT%
set "GUI_URL=http://%GUI_HOST%:%GUI_BASE_PORT%"

call :show_summary

call :log [5/5] Starting Luva HTML GUI...
start "Luva Control Center Server" /D "%LUVA_ROOT%" cmd /c "set LUVA_PORT=%GUI_BASE_PORT% && "%LUVA_VENV%\Scripts\python.exe" "%LUVA_ROOT%\LuvaGuiServer.py" >> "%LUVA_SERVER_LOG%" 2>&1"
start "" "%GUI_URL%"

echo Luva GUI started.
echo Open in browser: %GUI_URL%
echo Upload or choose a capture inside the GUI.
goto :done

:show_summary
echo.>> "%LUVA_LOG_FILE%"
echo ==================== LUVA READYNESS SUMMARY ====================>> "%LUVA_LOG_FILE%"
echo Luva root      : %LUVA_ROOT%>> "%LUVA_LOG_FILE%"
echo Reports dir    : %LUVA_REPORTS%>> "%LUVA_LOG_FILE%"
echo Uploads dir    : %LUVA_UPLOADS%>> "%LUVA_LOG_FILE%"
echo Venv python    : %LUVA_VENV%\Scripts\python.exe>> "%LUVA_LOG_FILE%"
echo GUI URL        : %GUI_URL%>> "%LUVA_LOG_FILE%"
echo Server meta    : %LUVA_SERVER_META%>> "%LUVA_LOG_FILE%"
echo Log file       : %LUVA_LOG_FILE%>> "%LUVA_LOG_FILE%"
echo Server log     : %LUVA_SERVER_LOG%>> "%LUVA_LOG_FILE%"
echo ===============================================================>> "%LUVA_LOG_FILE%"

echo.
echo ==================== LUVA READYNESS SUMMARY ====================
echo Luva root      : %LUVA_ROOT%
echo Reports dir    : %LUVA_REPORTS%
echo Uploads dir    : %LUVA_UPLOADS%
echo Venv python    : %LUVA_VENV%\Scripts\python.exe
echo GUI URL        : %GUI_URL%
echo Server meta    : %LUVA_SERVER_META%
echo Log file       : %LUVA_LOG_FILE%
echo Server log     : %LUVA_SERVER_LOG%
echo ===============================================================
echo.
exit /b 0

:python_missing
call :log Python was not found. Install Python 3.10+ and re-run this launcher.
echo Python was not found. Install Python 3.10+ and re-run this launcher.
goto :hold_open

:venv_failed
call :log Failed to create virtual environment.
echo Failed to create the local virtual environment.
goto :hold_open

:install_failed
call :log Dependency installation or repair failed.
echo Failed to install or repair Luva dependencies.
echo Check the log: %LUVA_LOG_FILE%
goto :hold_open

:hold_open
echo.
echo Press any key to close this window...
pause >nul
endlocal
exit /b 0

:done
echo.
echo Press any key to close this window...
pause >nul
endlocal
exit /b 0

:log
echo %*
echo %*>> "%LUVA_LOG_FILE%"
exit /b 0
