<?php 
session_start();
$condnum=-1;
//     }
// }

    // if (isset($_GET['trial'])) {
    //     $trial = $_GET['trial'];
    // }
    // else {
    
    include('mlwebdb.inc.php');
    //$currTrial= $row_col[$trial]; // swap this for $trial in the $sql query above
    //print_r($_SESSION);
    //print_r($trial);
    
    //$sql="SELECT Small_Amount,Large_Amount,Soon_Time,Late_Time FROM data_input WHERE row_col=2";
    //$result = mysqli_query($link,$sql) or die("Invalid Query : ".mysqli_error($link));  //Query the database for the value;
    //$row=mysqli_fetch_array($result); //Get the value as an array;
    $box1="10 Euro"; //Assign a variable to your value of interest
    $box2="12 Euro"; //Assign a variable to your value of interest
    $box3="Today"; //Assign a variable to your value of interest
    $box4="2 Weeks"; //Assign a variable to your value of interest

    $jsonName='mir.thesis.json'; //define json file
    $data = file_get_contents($jsonName); //decode json to array
    $json_arr = json_decode($data, true);
    $json_arr["cell"][0]["A"]["txt"]=$box1;//replace value
    $json_arr["cell"][0]["B"]["txt"]=$box2;//replace value
    $json_arr["cell"][1]["A"]["txt"]=$box3;//replace value
    $json_arr["cell"][1]["B"]["txt"]=$box4;//replace value

file_put_contents($jsonName, json_encode($json_arr));



?>
<html>
<head>
        <title>Gamble</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script type="text/javascript" src="main.js"></script>
        <script type="text/javascript" src="jquery-3.1.1.min.js"></script>
        <script src="jquery.foggy.min.js"></script>
        <script language=javascript src="mlweb20.js"></script>
        <link rel="stylesheet" href="w3.css">
		
	</head>

    <body class="w3-light-grey w3-content" style="max-width:1600px" onLoad="timefunction('onload', 'body', 'body')">
        <!--BEGIN set vars-->
        <script language="javascript">

            //override defaults
            mlweb_outtype = "CSV";
            mlweb_fname = "mlwebform";
            chkFrm = true;
            warningTxt = "U heeft nog niet alle vragen beantwoord!";
			choice = "";
        </script>


<FORM id="mlwebform" name="mlwebform" onSubmit="return checkForm(this)" method="POST">
 
			<INPUT type=hidden id='processData' name="procdata" value="">
            <!-- set all variables here -->
            <input id="expName" type=hidden name="expname" value="<?php echo($currTrial)?>">
            <input type=hidden name="nextURL" value="<?php echo($nextPage)?>">
            <input type=hidden name="to_email" value="">
            <!--in the above written lines, you can link what will be written next-->
            <!--these will be set by the script -->
			<input type=hidden name="subject" value="<?php echo($subject)?>">
			<input type=hidden id="condnum" name="condnum" value="<?php echo($condnum)?>">
            <input id="choice" type=hidden name="choice" value="">


        <header class="w3-container w3-grey">
            <h1>Decision Task</h1>
        </header>
        <div class="w3-white w3-container">

            <h1>Test-Trial</h1>
            <p>In this experimental task, you will have to decide between two options (Option A and Option B). Each of them consist of an amount of money to get in a specific time frame. You can see the amount and timeframe when hovering over the box with the mouse. Make a decision by selecting "Option A" or "Option B" and continue by clicking on the button "Cornfim".</p>
            <div id="container"  class="w3-white w3-container w3-col" style="width:90%">
            </div>
			
        </div>
		<div class="w3-white w3-container w3-center w3-padding">
        <a class="confirm w3-button w3-center w3-round-xlarge" name="submit" href="Start-Ex.php">Confirm</a>
		</div>
        <footer class="w3-container w3-grey">
		<h4></h4>
        </footer>
</div>
<script type="text/javascript">

// here the json file to generate the trial, for a particular set in the json file is generated. If the third attribute is set to random, it will select an order at random.
// if you enter a number, it will choose one of the orders using modulo of that number
o=$("#condnum").val();
if (o<0) {o="random"};

generateTrial("mir.thesis.json", "dynSet", o);

            
 //function that starts the page :)
$(document).ready(function () { 
$(".confirm").click(function (event) {
if (choice=="" && $(".choiceButton").length>0) {event.preventDefault();return false;}           
});
});	


</script>
    </body>
</html>