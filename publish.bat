@echo off
rem ============================================================
rem  Double-click this file to publish the latest changes.
rem  It rebuilds the map data, saves everything, and uploads it.
rem  Your website (Netlify) refreshes by itself about a minute later.
rem ============================================================

cd /d "%~dp0"

echo.
echo  [1/3] Rebuilding the map data...
"C:\Users\rolan\AppData\Local\Programs\Python\Python312\python.exe" site\build.py
if errorlevel 1 (
    echo.
    echo  ------------------------------------------------------------
    echo   Something went wrong while rebuilding. Nothing was uploaded.
    echo   Copy this window and send it to Claude.
    echo  ------------------------------------------------------------
    echo.
    pause
    exit /b 1
)

echo.
echo  [2/3] Saving changes...
git add -A
git commit -m "Update site (%DATE% %TIME%)"

echo.
echo  [3/3] Uploading...
git push

echo.
echo  ============================================================
echo   Done.
echo   - If you see "main -^> main", the upload worked; the website
echo     updates in about a minute.
echo   - If you see "nothing to commit" or "Everything up-to-date",
echo     there was simply nothing new to send. That is fine.
echo  ============================================================
echo.
pause
