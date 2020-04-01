file(REMOVE_RECURSE
  "lib/libkhaiii.pdb"
  "lib/libkhaiii.so"
  "lib/libkhaiii.so.0"
  "lib/libkhaiii.so.0.4"
)

# Per-language clean rules from dependency scanning.
foreach(lang CXX)
  include(CMakeFiles/khaiii.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
