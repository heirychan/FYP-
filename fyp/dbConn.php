<?php

$db = mysqli_connect("localhost","root","123","fyp");

if(!$db)
{
    die("Connection failed: " . mysqli_connect_error());
}

?>