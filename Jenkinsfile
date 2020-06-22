

pipeline {
    agent any
    stages {
	    
stage('Read Config') {
            steps {
                script {
                    fileContents = readFile "${env.WORKSPACE}/config.txt"
                    fileContentsArray = fileContents.split('\n')
		    filesToVerify = fileContentsArray[0].split('"')[1].split(' ')
		    echo "$filesToVerify"
		    secretServerURL = fileContentsArray[1].split('"')[1]
		    echo "$secretServerURL"
		    cdnBaseURL = fileContentsArray[2].split('"')[1]
		    echo "$cdnBaseURL"
		    sftpUser = fileContentsArray[3].split('"')[1]
		    echo "$sftpUser"
		    credentialsId = fileContentsArray[4].split('"')[1]
		    echo "$credentialsId"
		
       }
     }
   }
	      
       
	    
}
}
