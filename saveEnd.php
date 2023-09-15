<?php
// 		save.php: saves MouselabWEB data in database
//
//       v 2.00 Nov 2017 
//
//     (c) 2003-2017 Martijn C. Willemsen and Eric J. Johnson 
//
//    This program is free software; you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation; either version 2 of the License, or
//    (at your option) any later version.
//
//    This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//
//    You should have received a copy of the GNU General Public License
//    along with this program; if not, write to the Free Software
//    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

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
$table = 'Mate_Participants';
	
$ipstr = $_SERVER['REMOTE_ADDR'];

// $sqlquery = "select MAX(id) from $table";
// $result = mysqli_query($link, $sqlquery);

// $id = mysqli_fetch_array($result)[0];
// if (is_null($id)) $id=0; else $id++; 

$answers = [];
foreach($_POST as $question => $answer) {
    if(strpos($question,'_') === 0) {
        $answers[$question] = $answer;
    }
}
$answers = json_encode($answers);
$sqlquery = 'INSERT INTO '.$table.' (subject_p,answers) VALUES ("'.$subject.'","'.addslashes($answers).'")';
$result = mysqli_query($link, $sqlquery);
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