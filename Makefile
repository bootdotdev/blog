buildscripts:
	go build -o bin/addshorts ./scripts/addshorts
	go build -o bin/rmshorts ./scripts/rmshorts
	go build -o bin/linkcheck ./scripts/linkcheck
