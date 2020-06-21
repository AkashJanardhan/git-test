

pipeline {
    agent any
    stages {
	    
stage('Read Config') {
            steps {
                script {
                    arrayURL = readFile "${env.WORKSPACE}/config.txt"
                    echo "$arrayURL"
       }
     }
   }
	    
       
	    
}
}
