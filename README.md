# fabric
Core studio framework for VFX and Animation companies

## Pre-requisites
- Rez
- Python 3
- cmake (3+)

## Initialization

set TB_BASE_DIR, PATH vairables in `initialiser.sh` once the base values are setup can be deployed to setup default studio setup

## Code Structure
```shell
konfig
|-------KonfigAPI
infra
|-------get_site()
|-------get_user()
|-------get_hostname()
|-------get_ipv4_address()
studio
|-------get_software_base()
|-------get_projects_base()
|-------get_repository_base()
|-------get_log_base()
logger
|-------FabricLogger
utils
|-------get_rez_package_root()
```

##### Credits
- [Tabnine (AI based documentation)](http://tabnine.com/)