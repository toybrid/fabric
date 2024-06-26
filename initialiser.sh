
# TOYBRID SETTINGS
export TB_BASE_DIR=/Users/arjunthekkumadathil/toybrid
export TB_SOFTWARE_BASE_DIR=$TB_BASE_DIR/software
export TB_REPOSITORY_BASE_DIR=$TB_BASE_DIR/repository
export TB_PROJECTS_BASE_DIR=$TB_BASE_DIR/projects
export TB_SITE=lon
export TB_FARM=0
export TB_LOG_BASE_DIR=$TB_BASE_DIR/logs
export TB_LOG_LEVEL=INFO

# MINIMAL PATHS FOR TOYBRID FRAMEWORK
# Rez executable path
export PATH=$PATH:$TB_SOFTWARE_BASE_DIR/rez/bin/rez
# CMake executable path
export PATH=$PATH:/Applications/CMake.app/Contents/bin


# REZ SETTINGS
source $TB_SOFTWARE_BASE_DIR/rez/completion/complete.zsh
export REZ_DISABLE_HOME_CONFIG=1

# KONFIG SETTINGS
export TB_KONFIG_RELEASE_PATH=$TB_BASE_DIR/fabric/konfig

# REZ TOYBRID SETTINGS
export TB_INTERNAL_RELEASE_PATH=$TB_REPOSITORY_BASE_DIR/internal
export TB_EXTERNAL_RELEASE_PATH=$TB_REPOSITORY_BASE_DIR/external
export TB_USER_LOCAL_PATH=~/packages