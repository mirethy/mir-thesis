<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
$surveyVar = $_POST["surveyVar"];
//Or the one below if you first need to check if it's set, but do this for each variable or in your case perhaps just for the subject id
if(isset($_POST["surveyVar"])){
$surveyVar = (int)$_POST["surveyVar"];}

$sql="INSERT INTO $table (subject, surveyVar) VALUES ('$subject', '$surveyVar')";
$result = mysqli_query($link,$sql) or die("Invalid Query : ".mysqli_error($link)); //$link->query($sql);
}

?>