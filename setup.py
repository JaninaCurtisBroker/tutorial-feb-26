# If PATH has not been set (system does not know where git is), use full path.
# No remote has been configured yet:
"C:\Program Files\Git\cmd\git.exe" remote add origin https://github.com/YOURNAME/REPONAME.git
# Change branch name - from master for example (if needed)
"C:\Program Files\Git\cmd\git.exe" branch -M main
# push local repo to remote
"C:\Program Files\Git\cmd\git.exe" push -u origin main

# Add path - so you can skip ("C:\ etc not needed") adding user variables (not environment variables, since these require admin and )
