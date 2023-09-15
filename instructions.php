<?php 
session_start();

if (isset($_GET['subject'])) {$subject=$_GET['subject'];$_SESSION['subject']=$subject;}
 else {
	 if (isset($_SESSION['subject'])) {$subject=$_SESSION['subject'];}
	 else {$subject="anonymous";};
		}
if (isset($_GET['condnum'])) {$condnum=$_GET['condnum'];}
 else {
	 if (isset($_SESSION['condnum'])) {$condnum=$_SESSION['condnum'];$_SESSION['condnum']=$condnum;}
		else {$condnum=-1;};
	}
	
?>
<html>
    <head>
        <title>Welcome!</title>
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


        <header class="w3-container w3-sand">
            <h1> Welcome and thank you for participating in this experiment!</h1>
        </header>
        <div class="w3-white w3-container">

            <p> Dear participant,
            
            <BR> You are about to start the study by Mate Rethy with the supervision of Dr. Jan Hausfeld. With this study we aim to find the effect of differences in information gathering on intertemporal choice. The current research plan has been evaluated by the Economics & Business Ethics Committee (EBEC) of the University of Amsterdam ( the Netherlands). In the next paragraphs you will be given further information about the study.</p>
            
            <p><ins>The experimental design</ins></p>
            
            <p>The entire experiment will take about 20 minutes and consists of three parts: (1) a decision task - 40 trials, (2) a questionnaire, and (3) some demographic questions. 
            In the decision task you are asked to choose between two options. The options are presented in 4 boxes. Each choice has a time-delivery box and an amount box, like the following picture.</p>
            
            <img src="blurred_box_ex.png" alt="box_example" width="600" height="400" display= block margin-left= auto margin-right= auto>
            
            <p>In order to unravel the information behind the box, you need to hover over the box with your mouse. Then you only need to click on your preferred choice and confirm it. An example of such a decision can be seen in the video.</p>
            
            <video width="600" height="400" display= block margin-left= auto margin-right= auto controls>
            <source src="Choice_Ex.mp4" type="video/mp4">Your browser does not support the video tag.</video>
            
            <p><ins>Lottery</p></ins>
            <p>Once you finish all parts of the experiment, you can sign up for the lottery. Five participants will be randomly picked and have 1/4th (25%) of the value of a financial choice that they have made selected for payment in the chosen time point (eg. if you chose €40, you will receive €10). You will then receive an email from me, in which you will be asked to give me your preferred banking method and your banking details.</p>
            
            <p><ins>Voluntary Participation</p></ins>
            <p>It is completely voluntary to participate in the experiment. However, your consent is needed again. Therefore, please read all the information carefully. If you do not wish to participate, you can withdraw from the experiment with no explanation needed and with no negative consequences for you.</p>
           
            <p><ins>Consequences of participation</p></ins>
            <p>No direct or indirect personal benefits or disadvantages are expected to arise from participation in this research, except for the larger theoretical contribution that the results of this research may provide.</p>

            <p><ins>Data treatment: Privacy and confidentiality</p></ins>
            <p>All your stated information will be treated confidentially and according to the General Data Protection Regulation (GDPR);  this means that no personal or medical information will be disclosed in any way. Your data will be stored anonymously and used for educational purposes only. If there are any questions regarding data storage, you can contact us via email.</p>

            <p><ins>What else do you need to know?</p></ins>
            <p>You may always ask questions about the research study: now, during the research, and after the end of the research.You can do so by sending an email to the experimenter (mate.rethy@student.uva.nl).</p>
            <BR>        
            <BR>        
            <BR>


            <p><i><ins>By clicking on the "Confirm"- button, you are agreeing to the following points:</i></p></ins>
            <p><i>-You have read and understood the information about this research.</i></p>
            <p><i>-There are no right or wrong answers, and there are no advantages or disadvantages of participation</i></p>
            <p><i>-All responses will be securely stored, and the data will only be used for scientific and educational purposes.</i></p>
            <p><i>-I understand that this project subscribes to the ethical conduct of research and to the protection of the dignity, right, interests, and safety of participants at all times.</i></p>
            <p><i>-Furthermore, I understand that in case I choose to provide my email address, my personal data will be processed, and handled according to the GDPR regulations, as explained previously.</i></p>
            <div id="container"  class="w3-white w3-container w3-col" style="width:90%">
            </div>
			
        </div>
		<div class="w3-white w3-container w3-center w3-padding">
			<a class="confirm w3-button w3-center w3-round-xlarge" name="submit" href="test-trial.php">Confirm</a>
		</div>
        <footer class="w3-container w3-sand">
		<h4>Thank you for your participation!</h4>
        </footer>
</div>

    </body>
</html>