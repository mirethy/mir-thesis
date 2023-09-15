<?php

ini_set('display_errors', '1');
ini_set('display_startup_errors', '1');
error_reporting(E_ALL);


include('mlwebdb.inc.php');
session_start();

// overrule session variable with form output

if (!isset($_SESSION['subject'])) {$subject="anonymous";};
if (isset($_GET['condnum'])) {$condnum=$_GET['condnum'];}
 else {
	 if (isset($_SESSION['condnum'])) {$condnum=$_SESSION['condnum'];$_SESSION['condnum']=$condnum;}
		else {$condnum=-1;};
	}

if (isset($_SESSION['subjectzz'])) {
    $subject=$_SESSION['subjectzz'];
}


//$subject = $_SESSION['subjectzz'];
$table = 'Mate_ASRS';
	
$ipstr = $_SERVER['REMOTE_ADDR'];

// $sqlquery = "select MAX(id) from $table";
// $result = mysqli_query($link, $sqlquery);

// $id = mysqli_fetch_array($result)[0];
// if (is_null($id)) $id=0; else $id++; 

// print_r($_POST);die;
foreach($_POST as $question => $answer) {
    if(strpos($question,'q') === 0) {
        $sqlquery = "INSERT INTO $table (subject_a,question,answer) VALUES ('$subject','$question','$answer')";
        $result = mysqli_query($link, $sqlquery);
    }
}
mysqli_close($link);

/* Redirect to a different page in the current directory that was requested */
$host  = $_SERVER['HTTP_HOST'];
$uri   = rtrim(dirname($_SERVER['PHP_SELF']), '/\\');

$trial = $_SESSION['trialzz'];
$trial = ($trial + 1);
$_SESSION['trialzz']=$trial;

header("Location: http://$host$uri/gamble.php");


exit;
?>