buildscripts:
	go build -o bin/addshorts ./scripts/addshorts
	go build -o bin/rmshorts ./scripts/rmshorts
	go build -o bin/linkcheck ./scripts/linkcheck

windowsbuildscripts:
	go build -o bin\addshorts.exe .\scripts\addshorts
	go build -o bin\rmshorts.exe .\scripts\rmshorts
	go build -o bin\linkcheck.exe .\scripts\linkcheck
