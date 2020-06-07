<?php

$uploads_dir = '../static';
$allowed_ext = array('jpg','jpeg','png','gif');

$error = $_FILES['myfile']['error'];
$name = $_FILES['myfile']['name'];
$ext = array_pop(explode('.', $name));

move_uploaded_file( $_FILES['myfile']['tmp_name'], "$uploads_dir/$name");
