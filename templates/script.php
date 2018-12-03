<?php
$text = ( isset( $_GET['text'] ) AND !empty( $_GET['text'] ) ) ? $_GET['text'] : '' ;
$myfile = fopen("MonCorpus.txt", "a") or die("Unable to open file!");
fwrite($myfile, "\n".$text);
fclose($myfile);
?>
