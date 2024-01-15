import speedtest 
import subprocess

speed = speedtest.Speedtest()

subprocess.run(["speedtest-cli", "--share"])
print("\n Click and OPEN the above link ↑ to view graphical representation of internet speed")

download_speed = speed.download()
upload_speed = speed.upload()
print("The download speed is:", download_speed)
print("The upload speed is:", upload_speed)
