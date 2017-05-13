Moms phone no : 9818651662

just to check it works or not
	gammu getallsms

to config the modem
	gammu-config
 		get port: /dev/ttyUSB0
 		connection: at115200 //for more connection check this link: https://wammu.eu/phones/huawei/?page=4
		every thing just default!



Important notice!!!: Network manager has tendency to lock your GSM device once you start your GSM Internet connection. The device stays locked even after you disconnect so you must make sure that right click on Network manager -> Enable mobile broadband option is unchecked before you use Gammu. If this option is enabled you will get permission denied errors from Gammu.

Sending messages
       NOTE:
          All messages below are sent to number 123456, replace it with proper destination.

       Send text message up to standard 160 chars:

          echo "All your base are belong to us" | gammu sendsms TEXT 123456

       or

          gammu sendsms TEXT 123456 -text "All your base are belong to us"

       Send long text message:

          echo "All your base are belong to us" | gammu sendsms TEXT 123456 -len 400

       or

          gammu sendsms TEXT 123456 -len 400 -text "All your base are belong to us"

       or

          gammu sendsms EMS 123456 -text "All your base are belong to us"

       Send some funky message with predefined sound and animation from 2 bitmaps:

          gammu sendsms EMS 123456 -text "Greetings" -defsound 1 -text "from Gammu -tone10 axelf.txt -animation 2 file1.bmp file2.bmp

       Send protected message with ringtone:

          gammu sendsms EMS 123456 -protected 2 -variablebitmaplong ala.bmp -toneSElong axelf.txt -toneSE ring.txt


