@echo off
rmdir /S /Q "C:\otree_kiosk\data"
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" ^
--kiosk ^
--no-first-run ^
--disable-session-crashed-bubble ^
--start-maximized ^
--user-data-dir="C:\otree_kiosk\data" ^
"http://SERVER_IP:8000/room/lab/?participant_label=Seat01"