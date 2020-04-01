# This file will be configured to contain variables for CPack. These variables
# should be set in the CMake list file of the project before CPack module is
# included. The list of available CPACK_xxx variables and their associated
# documentation may be obtained using
#  cpack --help-variable-list
#
# Some variables are common to all generators (e.g. CPACK_PACKAGE_NAME)
# and some are specific to a generator
# (e.g. CPACK_NSIS_EXTRA_INSTALL_COMMANDS). The generator specific variables
# usually begin with CPACK_<GENNAME>_xxxx.


set(CPACK_BUILD_SOURCE_DIRS "/home/kmusw/바탕화면/capstone-2020-4/src/khaiii;/home/kmusw/바탕화면/capstone-2020-4/src/khaiii/build")
set(CPACK_CMAKE_GENERATOR "Unix Makefiles")
set(CPACK_COMPONENT_UNSPECIFIED_HIDDEN "TRUE")
set(CPACK_COMPONENT_UNSPECIFIED_REQUIRED "TRUE")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_FILE "/usr/local/share/cmake-3.17/Templates/CPack.GenericDescription.txt")
set(CPACK_DEFAULT_PACKAGE_DESCRIPTION_SUMMARY "khaiii built using CMake")
set(CPACK_GENERATOR "TGZ")
set(CPACK_INSTALL_CMAKE_PROJECTS "/home/kmusw/바탕화면/capstone-2020-4/src/khaiii/build;khaiii;ALL;/")
set(CPACK_INSTALL_PREFIX "/usr/local")
set(CPACK_MODULE_PATH "/home/kmusw/.hunter/_Base/Download/Hunter/0.23.34/70287b1/Unpacked/cmake/modules;/home/kmusw/.hunter/_Base/Download/Hunter/0.23.34/70287b1/Unpacked/cmake/find")
set(CPACK_NSIS_DISPLAY_NAME "khaiii 0.4")
set(CPACK_NSIS_INSTALLER_ICON_CODE "")
set(CPACK_NSIS_INSTALLER_MUI_ICON_CODE "")
set(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES")
set(CPACK_NSIS_PACKAGE_NAME "khaiii 0.4")
set(CPACK_NSIS_UNINSTALL_NAME "Uninstall")
set(CPACK_OUTPUT_CONFIG_FILE "/home/kmusw/바탕화면/capstone-2020-4/src/khaiii/build/CPackConfig.cmake")
set(CPACK_PACKAGE_DEFAULT_LOCATION "/")
set(CPACK_PACKAGE_DESCRIPTION_FILE "/usr/local/share/cmake-3.17/Templates/CPack.GenericDescription.txt")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Kakao Hangul Analyzer III")
set(CPACK_PACKAGE_FILE_NAME "khaiii-0.4-Linux")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "khaiii 0.4")
set(CPACK_PACKAGE_INSTALL_REGISTRY_KEY "khaiii 0.4")
set(CPACK_PACKAGE_NAME "khaiii")
set(CPACK_PACKAGE_RELOCATABLE "true")
set(CPACK_PACKAGE_VENDOR "Kakao Corp.")
set(CPACK_PACKAGE_VERSION "0.4")
set(CPACK_PACKAGE_VERSION_MAJOR "0")
set(CPACK_PACKAGE_VERSION_MINOR "4")
set(CPACK_RESOURCE_FILE_LICENSE "/home/kmusw/바탕화면/capstone-2020-4/src/khaiii/LICENSE")
set(CPACK_RESOURCE_FILE_README "/home/kmusw/바탕화면/capstone-2020-4/src/khaiii/README.md")
set(CPACK_RESOURCE_FILE_WELCOME "/usr/local/share/cmake-3.17/Templates/CPack.GenericWelcome.txt")
set(CPACK_SET_DESTDIR "OFF")
set(CPACK_SOURCE_GENERATOR "ZIP")
set(CPACK_SOURCE_IGNORE_FILES "/\\..*;/.*build.*/;/train/;__pycache__;.*\\.pyc")
set(CPACK_SOURCE_OUTPUT_CONFIG_FILE "/home/kmusw/바탕화면/capstone-2020-4/src/khaiii/build/CPackSourceConfig.cmake")
set(CPACK_SOURCE_PACKAGE_FILE_NAME "khaiii-0.4")
set(CPACK_SYSTEM_NAME "Linux")
set(CPACK_TOPLEVEL_TAG "Linux")
set(CPACK_WIX_SIZEOF_VOID_P "8")

if(NOT CPACK_PROPERTIES_FILE)
  set(CPACK_PROPERTIES_FILE "/home/kmusw/바탕화면/capstone-2020-4/src/khaiii/build/CPackProperties.cmake")
endif()

if(EXISTS ${CPACK_PROPERTIES_FILE})
  include(${CPACK_PROPERTIES_FILE})
endif()
