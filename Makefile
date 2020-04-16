IMG_NAME=ntc-jv/ansible
IMG_VERSION=0.1.5

.DEFAULT_GOAL := test
.PHONY: test
test: lint unit

.PHONY: build
build:
	docker build -t $(IMG_NAME):$(IMG_VERSION) . 

.PHONY: cli
cli:
	docker run -it --env-file=.env \
		-v $(shell pwd):/local \
		-w /local \
		$(IMG_NAME):$(IMG_VERSION) bash

.PHONY: pylint
pylint:
	find ./ -name "*.py" | xargs pylint

.PHONY: lint
lint:
	@echo "Starting lint"
	docker run -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) yamllint --strict .
	docker run -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) ansible-lint .
	docker run -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) make pylint
	docker run -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) black --check
	docker run -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) bandit --recursive --config .bandit.yml ./
	
	@echo "Completed lint"
	
.PHONY: unit
unit:
	@echo "Starting  unit tests"
	docker run -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) pytest -vv
	docker run -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) ansible-playbook tests/pb.unittest.yml
	@echo "Completed unit tests"

.PHONY: unit-pytest
unit-pytest:
	@echo "Starting  unit tests"
	docker run -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) pytest -vv
	@echo "Completed unit tests"

.PHONY: unit-ansible
unit-ansible:
	@echo "Starting  unit tests"
	docker run -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) ansible-playbook tests/pb.unittest.yml
	@echo "Completed unit tests"

.PHONY: demo_show_setup
demo_show_setup:
	@echo "Starting the Setup demo"
	docker run -e "TERM=xterm-256color" -v $(shell pwd):/local $(IMG_NAME):$(IMG_VERSION) ansible-playbook setup_netbox.yml --limit rtr-1

.PHONY: demo_setup
demo_setup:
	@echo "Starting the Setup demo"
	ansible-playbook setup_netbox.yml --tags ios

.PHONY: demo_audit
demo_audit:
	@echo "Starting Audit of single device"
	ansible-playbook audit_netbox.yml --limit wanrtr01
	read
	ansible-playbook audit_netbox.yml
