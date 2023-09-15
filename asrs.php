<?php 
session_start();


if (!isset($_SESSION['subject'])) {$subject="anonymous";};
if (isset($_GET['condnum'])) {$condnum=$_GET['condnum'];}
 else {
	 if (isset($_SESSION['condnum'])) {$condnum=$_SESSION['condnum'];$_SESSION['condnum']=$condnum;}
		else {$condnum=-1;};
	}

if (isset($_SESSION['subjectzz'])) {
    $subject=$_SESSION['subjectzz'];
}

?>
<html>
    <head>
        <title>Survey</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script type="text/javascript" src="main.js"></script>
        <script type="text/javascript" src="jquery-3.1.1.min.js"></script>
        <script src="jquery.foggy.min.js"></script>
        <script language=javascript src="mlweb20.js"></script>
        <link rel="stylesheet" href="w3.css">
		<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.0/css/all.css" integrity="sha384-lZN37f5QGtY3VHgisS14W3ExzMWZxybE1SJSEsQp9S+oqd12jhcu+A56Ebc1zFSJ" crossorigin="anonymous">
		
		
	</head>

    <body class="w3-sand w3-content" style="max-width:1600px" onLoad="timefunction('onload', 'body', 'body')">
        <!--BEGIN set vars-->
        <script language="javascript">

            //override defaults
            mlweb_outtype = "CSV";
            mlweb_fname = "mlwebform";
            chkFrm = false;
            warningTxt = "Please answer all questions.";
			choice = "";
        </script>


<FORM id="mlwebform" name="mlwebform" onSubmit="return checkForm(this)" method="POST" action="saveASRS.php">
 
			<INPUT type=hidden id='processData' name="procdata" value="">
            <!-- set all variables here -->
            <input id="expName" type=hidden name="expname" value="survey">
            <input type=hidden name="nextURL" value="gamble.php">
            <input type=hidden name="to_email" value="">
            <!--these will be set by the script -->
			<input type=hidden name="subject" value="<?php echo($subject)?>">
			<input type=hidden id="condnum" name="condnum" value="<?php echo($condnum)?>">
           <input id="choice" type=hidden name="choice" value="">


        <header class="w3-container w3-sand">
            <h1>Master Thesis - Questionnaire Part 1 </h1>
        </header>
        <div class="w3-white w3-container">

            <p>DIRECTIONS: Please answer the questions below, rating yourself on each of the criteria shown. As you answer each question, select the box that best describes how you have felt and conducted yourself over the past 6 months. Do not spend too much time on any statement. Answer quickly and honestly.</p>
	
		<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-white w3-left-align w3-large " style="width: 50%;">Please answer the statements below </div>
  <div class="w3-container w3-col w3-grey w3-center" style="width: 10%;height: 50px" ><b>Never</b></div>
  <div class="w3-container w3-col white w3-center" style="width: 10%;height: 50" ><b>Rarely</b></div>
  <div class="w3-container w3-col w3-grey w3-center " style="width: 10%;height: 50" ><b>Sometimes</b></div>
  <div class="w3-container w3-col w3-white w3-center" style="width: 10%;height: 50" ><b>Often</b></div>
  <div class="w3-container w3-col w3-grey w3-center" style="width: 10%;height: 50" ><b>Very often</b></div>

</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align " style="width: 50%;height: 60px" >1. How often do you have trouble wrapping up the final details of a project, once the challenging parts have been done?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q1" value="1" required>&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q1" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q1" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q1" value="4" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q1" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >2. How often do you have difficulty getting things in order when you have to do a task that requires organization?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q2" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q2" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q2" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q2" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q2" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >3. How often do you have problems remembering appointments or obligations?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q3" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q3" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q3" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q3" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q3" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align w3-" style="width: 50%;height: 60px" >4. When you have a task that requires a lot of thought, how often do you avoid or delay getting started?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q4" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q4" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q4" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q4" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q4" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align " style="width: 50%;height: 60px" >5. How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q5" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q5" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q5" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q5" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q5" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >6. How often do you feel overly active and compelled to do things, like you were driven by a motor?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q6" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q6" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q6" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q6" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q6" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >7. How often do you make careless mistakes when you have to work on a boring or difficult project?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q7" value="1" required>&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q7" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q7" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q7" value="4" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q7" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >8. How often do you have difficulty keeping your attention when you are doing boring or repetitive work?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q8" value="1" required>&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q8" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q8" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q8" value="4" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q8" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >9. How often do you have difficulty concentrating on what people say to you, even when they are speaking to you directly?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q9" value="1" required>&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q9" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q9" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q9" value="4" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q9" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >10. How often do you misplace or have difficulty finding things at home or at work?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q10" value="1" required>&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q10" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q10" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q10" value="4" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q10" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >11. How often are you distracted by activity or noise around you?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q11" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q11" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q11" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q11" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q11" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >12. How often do you leave your seat in meetings or other situations in which you are expected to remain seated?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q12" value="1" required>&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q12" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q12" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q12" value="4" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q12" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >13. How often do you feel restless or fidgety?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q13" value="1" required>&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q13" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q13" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q13" value="4" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q13" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >14. How often do you have difficulty unwinding and relaxing when you have time to yourself?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q14" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q14" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q14" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q14" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q14" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >15. How often do you find yourself talking too much when you are in social situations?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q15" value="1" required>&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q15" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q15" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q15" value="4" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q15" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >16. When you are in a conversation, how often do you find yourself finishing the sentences of the people you are talking to, before they can finish them themselves?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q16" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q16" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q16" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q16" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q16" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >17. How often do you have difficulty waiting your turn in situations when turn taking is required?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q17" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q17" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q17" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q17" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q17" value="5" >&nbsp;</div>
</div>
<div class="w3-row w3-border">
  <div class="w3-container w3-col w3-light-grey w3-left-align" style="width: 50%;height: 60px" >18. How often do you interrupt others when they are busy?</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q18" value="1" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q18" value="2" >&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q18" value="3" >&nbsp;</div>
  <div class="w3-container w3-col w3-white w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q18" value="4" required>&nbsp;</div>
  <div class="w3-container w3-col w3-gray w3-center w3-hover-sand" style="width: 10%;height: 60px" ><input class="w3-radio" type="radio" name="q18" value="5" >&nbsp;</div>
</div>


	
            <div id="container"  class="w3-white w3-container w3-col" style="width:90%">
            </div>
			
        </div>
		<div class="w3-white w3-container w3-center w3-padding">
			<button class="confirm w3-button w3-center w3-round-xlarge" name="submit" value="confirm">Confirm</button>
		</div>
        <footer class="w3-container w3-sand">
		<h4>Thank you for your participation!</h4>
        </footer>
</div>

        <script type="text/javascript">

			// here the json file to generate the trial, for a particular set in the json file is generated. If the third attribute is set to random, it will select an order at random.
			// if you enter a number, it will choose one of the orders using modulo of that number
			// now taking the number from the condnum variable to set the order of the options
            o=$("#condnum").val();
			if (o<0) {o="random"};
            
			//generateTrial("json_files/tv.json", "dynSet", o);

            			
     		//function that starts the page
	$(document).ready(function () { 
		$(".confirm").click(function (event) {
			if (choice=="" && $(".choiceButton").length>0) {event.preventDefault();return false;}           
			});
		});	
	
			

        </script>
    </body>
</html>
