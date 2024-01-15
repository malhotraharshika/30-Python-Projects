import speedtest 
import subprocess

speed = speedtest.Speedtest()

subprocess.run(["speedtest-cli", "--share"])

print("The download speed is:", speed.download()) 
print("The upload speed is:", speed.upload()) 
