<?php

   require("php_serial.class.php");

   $serial = new phpSerial;

   $serial->deviceSet("COM10");

   $serial->confBaudRate(9600);
   $serial->deviceOpen();


   $smsx = $_REQUEST['servox'];
   $serial->sendMessage("'x'+$smsx");
   sleep (1);

   $serial->deviceClose();

?>
