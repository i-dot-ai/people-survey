define _update_requirements
	docker-compose run requirements bash -c "pip install -U pip setuptools && pip install -U -r /app/$(1).txt && pip freeze > /app/$(1).lock"
endef

.PHONY: update-api-requirements
update-api-requirements:
	$(call _update_requirements,requirements)
	$(call _update_requirements,requirements-dev)
