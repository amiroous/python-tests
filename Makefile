build:
	docker-compose build

up:
	docker-compose up --build -d

down:
	docker-compose down --remove-orphans

run:
	make up && $(call pause) && make test && $(call pause) && make down

jenkins:
	docker-compose up --build -d jenkins

chrome:
	docker-compose up --build -d selenium-hub && docker-compose up --build -d chrome

test:
	docker-compose run hotels-tests

define pause
    sleep 1
endef
