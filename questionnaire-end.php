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


<FORM id="mlwebform" name="mlwebform" onSubmit="return checkForm(this)" method="POST" action="saveEnd.php">
 
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
            <h1>Master Thesis - Questionnaire Part 2 </h1>
        </header>
        <div class="w3-white w3-container">

            <h1>Survey</h1>
            <p>The experiment is finished and you are almost done. However, we still need some demographic information, which you can find below. Please, answer all of them. </p>
			<h2>Demographic Questions</h2>
			<div class="w3-container">

			<p>
			<label class="w3-text-grey"><b>What is your age?</b></label>
			<input class="w3-input w3-border " name="_age" type="text" required></p>
			
            <p class="w3-text-grey">What is your gender?</p>			 
			
            <p><input class="w3-radio" type="radio" name="_gender" value="Male" required>
			<label>Male</label>

            <p><input class="w3-radio" type="radio" name="_gender" value="Female" >
			<label>Female</label>
           
            <p><input class="w3-radio" type="radio" name="_gender" value="Non_binary" >
			<label>Non-binary</label>
            
            <p><input class="w3-radio" type="radio" name="_gender" value="Prefer_not_to_say" >
			<label>Prefer not to say</label>

<H2>Education</h2>		
			<p class="w3-text-grey">What is the highest degree or level of education you have completed?</p>			 
			 <p><input class="w3-radio" type="radio" name="_education" value="High School" required>
			<label>High School</label>

            <p><input class="w3-radio" type="radio" name="_education" value="Bachelor's Degree" >
			<label>Bachelor's Degree</label>

            <p><input class="w3-radio" type="radio" name="_education" value="Master's Degree" >
			<label>Master's Degree</label>
			
            <p><input class="w3-radio" type="radio" name="_education" value="Ph.D. or higher" >
			<label>Ph.D. or higher</label>

<H2>Would you like to be eligible to win one of your choices?</h2>		
			<p class="w3-text-grey">Lottery: Five participants will be randomly selected to receive 1/4th (25%) of one of their chosen amounts from the main experiment at the given time point. If your answer is yes please fill in your preferred email address in the provided space!</p>			 
			 <p><input class="w3-radio" type="radio" name="_lottery" value="yes" >
			<label>Yes</label>
            <input class="w3-input w3-border" name="_email" type="text" ></p>
            
            <p><input class="w3-radio" type="radio" name="_lottery" value="no" required>
			<label>No</label>
	

	
            <div id="container"  class="w3-white w3-container w3-col" style="width:90%">
            </div>
			
        </div>
		<div class="w3-white w3-container w3-center w3-padding">
			<button class="confirm w3-button w3-center w3-round-xlarge" name="submit" value="confirm">Confirm</button>
		</div>
        <footer class="w3-container w3-sand">
		<h4>Thank you!</h4>
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
