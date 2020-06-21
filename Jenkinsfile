

pipeline {
    agent any
    stages {
	    
stage('Read Config') {
            steps {
                script {
                    arrayURL = readFile "${env.WORKSPACE}/config.txt"
                    abc = arrayURL.split('\n')
		    echo"$abc[0]"	
		
       }
     }
   }
	    
       
	    
}
}
