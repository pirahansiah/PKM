@echo off

setlocal
cd /d "%~dp0"

REM Reuse the existing conda env per workspace policy (never create a new one).
call conda activate py314 2>nul

set "MODEL=qwen3.5:4b-mlx"
set "HOST=http://127.0.0.1:11434"

python "%~dp0main.py" --model "%MODEL%" --host "%HOST%" %*
if errorlevel 1 (
  echo [ERROR] Graph build failed.
  exit /b 1
)

echo [OK] knowledge_graph.html updated
start "" "%~dp0knowledge_graph.html"
endlocal
