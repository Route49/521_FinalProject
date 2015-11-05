#NOTES

10/29/15
- The microscope was installed using "sudo apt-get install guvcview" and "sudo apt-get install cheese"
- guvcview doesn't work on it's own "can't detect device"

- Setup permissions and enable driver
  "sudo usermod -a -G video pi"
  "sudo modprobe uvcvideo"
- Then reboot pi
- Open up cam using
  "guvcview --size=544x288 --format=yuyv"
- Didn't work

- Needed to install luvcview to enable microscope
 "sudo apt-get install luvcview uvccapture"
 use luvcview to just view what is under the microscope
 use uvccapture to capture microscope image, need to figure out how to use command to capture image

  
