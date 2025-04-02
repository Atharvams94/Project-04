<?php 


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
