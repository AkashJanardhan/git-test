

pipeline {
    agent any
    stages {
	    
stage('Read Config') {
            steps {
                script {
                    fileContents = readFile "${env.WORKSPACE}/config.txt"
                    fileContentsArray = fileContents.split('\n')
		    filesToVerify = fileContentsArray[0].split(' ')
		    secretServerURL = fileContentsArray[1]
		    cdnBaseURL = fileContentsArray[2]
		    sftpUser = fileContentsArray[3]
		    credentialsId = fileContentsArray[4]
		
       }
     }
   }
	      
       
	    
}
}
