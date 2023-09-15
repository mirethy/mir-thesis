<?php
session_start();
//unset($_SESSION);
if(!empty($_SESSION['trialzz']) && $_SESSION['trialzz'] > 17) {
    if($_SESSION['trialzz'] == 18) {
        include('asrs.php');
    }
    elseif($_SESSION['trialzz'] == 19) {
        include('questionnaire-end.php');
    }
    else {
        include('thank_you.php');
        $_SESSION['trialzz'] = 0;
    }
    die;
}


if (isset($_GET['subject'])) {
    $subject=$_GET['subject'];
    $_SESSION['subjectzz']=$subject;
}
else {
	if (isset($_SESSION['subjectzz'])) {
        $subject=$_SESSION['subjectzz'];
    }
	else {
        $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        $charactersLength = strlen($characters);
        $randomString = '';
        for ($i = 0; $i < 14; $i++) {
            $randomString .= $characters[rand(0, $charactersLength - 1)];
        }
        $subject = $randomString; // random id generator
        $_SESSION['subjectzz']=$subject;
    }
}
// if (isset($_GET['condnum'])) {
//     $condnum=$_GET['condnum'];
// }
// else {
// 	if (isset($_SESSION['condnum'])) {
//         $condnum=$_SESSION['condnum'];$_SESSION['condnum']=$condnum;
//     }
//     else {
        $condnum=-1;
//     }
// }

$_SESSION['roundnum']=$roundnum; //update session roundnum

    // if (isset($_GET['trial'])) {
    //     $trial = $_GET['trial'];
    // }
    // else {
        if(!empty($_SESSION['trialzz']) ) {
            $trial = $_SESSION['trialzz'];
        } else {
            $trial=0;
            $_SESSION['trialzz'] = 0;
        }
        //print_r($_SESSION);
    // }

    // print_r($_SESSION);

    if(empty($_SESSION['row_col'])) {
        $row_col = range(1, 18); // 18 trials 
        shuffle($row_col);
        $_SESSION['row_col'] = $row_col;
    } else {
        $row_col = $_SESSION['row_col'];
    }

    include('mlwebdb.inc.php');
    $currTrial= $row_col[$trial]; // swap this for $trial in the $sql query above
    
    $currentPage="expt_page";
    if ($trial>16)// for 18 trials
    {$nextPage="before_asrs.php";}
    else {$nextPage="cont-ex.php";}
    
    $sql="SELECT Small_Amount,Large_Amount,Soon_Time,Late_Time FROM data_input WHERE row_col=$currTrial";
    $result = mysqli_query($link,$sql) or die("Invalid Query : ".mysqli_error($link));  //Query the database for the value;
    $row=mysqli_fetch_array($result); //Get the value as an array;
    $box1=$row[0]; //Assign a variable to your value of interest
    $box2=$row[1]; //Assign a variable to your value of interest
    $box3=$row[2]; //Assign a variable to your value of interest
    $box4=$row[3]; //Assign a variable to your value of interest

    $jsonName='json_files/mir.thesis.json'; //define json file
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
        <title>Experiment</title>
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
            warningTxt = "You did not answer all the questions!";
			choice = "";
        </script>


<FORM id="mlwebform" name="mlwebform" onSubmit="return checkForm(this)" method="POST" action="save.php">
 
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
            <h1>Decision Task - Trial <?php echo($trial)?>  </h1>
        </header>
        <div class="w3-white w3-container">

            <h1></h1>
           
            <div id="container"  class="w3-white w3-container w3-col" style="width:90%">
            </div>
			
        </div>
		<div class="w3-white w3-container w3-center w3-padding">
			<button class="confirm w3-button w3-center w3-round-xlarge" name="submit" value="confirm">Confirm</button>
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
            
			generateTrial("json_files/mir.thesis.json", "dynSet", o);

            			
     		//function that starts the page
        $(document).ready(function () { 
		$(".confirm").click(function (event) {
			if (choice=="" && $(".choiceButton").length>0) {event.preventDefault();return false;}           
			});
		});	
	

        </script>
    </body>
</html>

<?