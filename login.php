<?php 
session_start(); 
include('configall.php');

if (isset($_POST['uname']) && isset($_POST['password'])) {

	function validate($data){
       $data = trim($data);
	   $data = stripslashes($data);
	   $data = htmlspecialchars($data);
	   return $data;
	}

	$uname = validate($_POST['uname']);
	$pass = validate($_POST['password']);

    //echo $role;


	if (empty($uname)) {
		echo "<script type='text/javascript'>alert('Enter username');
        window.location='home.php';
        </script>";
	}else if(empty($pass)){
		echo "<script type='text/javascript'>alert('Enter password');
        window.location='home.php';
        </script>";
	}else{
		$sql = "SELECT * FROM admin WHERE username='$uname' AND password='$pass'";

		$result = mysqli_query($connection, $sql);

		if (mysqli_num_rows($result) == 1) {
			$row = mysqli_fetch_assoc($result);
            if ($row['username'] === $uname && $row['password'] === $pass) {
            	$_SESSION['user_name'] = $row['username'];
            	#$_SESSION['name'] = $row['name'];
				$_SESSION['id'] = $row['id'];			
            	header("Location: admin_home_page.php?user exists");
		        exit();
            }else{
				echo "<script type='text/javascript'>alert('Incorrect username or password');
				window.location='home.php';
				</script>";
			}
		}else{
			echo "<script type='text/javascript'>alert('Incorrect username or password');
				window.location='home.php';
				</script>";
		}
	}
	
}else{
	header("Location: index.php?bruh");
	exit();
}