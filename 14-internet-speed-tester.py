import speedtest 
import subprocess

speed = speedtest.Speedtest()

subprocess.run(["speedtest-cli", "--share"])
print("Click and open the above link ↑ ")

download_speed = speed.download()
upload_speed = speed.upload()
print("The download speed is:", download_speed)
print("The upload speed is:", upload_speed)
