<?php
$link = mysqli_connect("localhost", "satisht1_notes", "Kmrsatish@12", "satisht1_onlinenotes");
if(mysqli_connect_error()){
    die('ERROR: Unable to connect:' . mysqli_connect_error()); 
    echo "<script>window.alert('Hi!')</script>";
}
    ?>