

# You need git.exe on your PATH to VS Code can find it. 
# If PATH has not been set (system does not know where git is), use full path.
# 1. Link to a remote, or equivalently, connect my github to my local repo - in this case no remote has been configured yet:
"C:\Program Files\Git\cmd\git.exe" remote add origin https://github.com/YOURNAME/REPONAME.git
# 2. Change branch name - from master to main for example (if needed)
"C:\Program Files\Git\cmd\git.exe" branch -M main
# push local repo to remote
"C:\Program Files\Git\cmd\git.exe" push -u origin main

# Or start by adding it to your PATH - so you can skip ("C:\ etc not needed") adding user variables (not environment variables, since these require admin and )
# Open command prompt and set a new user variable. type: 
setx PATH "%PATH%;C:\ProgramFiles\Git\mingw64\libexec\git-core"
# If you're an admin, you can set a new environmental variable instead -  looks like this (example only):
# setx JAVA_HOME "C:\Program Files\Java\jdk" /m