GUPPI stands for General User Primarily Peripheral Interface. It is used as a hub for scripts that will help me with day to day activities on the computer. I can edit it by going to the GUPPI.py file. I can add more scripts by creating a new file in this directory and then importing it into the GUPPY.py file.

To use this for yourself, put these into a (preferably) hidden file .IntStor, and then use a
bash script in the home directory to call it. For example, the bash script could look like so:
  cd .Instor
  python3 GUPPI.py
I used Debian 12 to create this, so I know this should work on Debian-based linux distros at 
the very least.
ChatGPT helped, resulting in the code being horrific, but that should not be a problem, because
we, as the users, will not be reading the code, and it is not very data intesive.

If you have ideas to make the code better (there are many ways to make it better, but I am too
lazy to do so), please tell me in the Pull Requests.
