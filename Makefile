# Makefile
# .PHONY: up This PHONY ensures that even if there is a file named up in your directory,
# running make up will execute the specified command (docker compose up) instead of trying 
# to treat up as a file target.
.PHONY: up
up:
	docker compose up
down:
	docker compose down
restart-movie:
	docker compose restart movie-service
