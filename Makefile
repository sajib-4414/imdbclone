# Makefile
# .PHONY: up This PHONY ensures that even if there is a file named up in your directory,
# running make up will execute the specified command (docker compose up) instead of trying 
# to treat up as a file target.
.PHONY: up

# Get current user and group information for jenkins, we need to set explicit permission on host copy of jenkins volume
USER_ID := $(shell id -u)
GROUP_ID := $(shell id -g)

prepare:
  # Set ownership of jenkins_volume on host machine
  sudo chown -R $(USER_ID):$(GROUP_ID) jenkins_volume

# make prepare will run before make up is exectued as a dependency
up: prepare
	docker compose up


down:
	docker compose down
restart-movie:
	docker compose restart movie-service
