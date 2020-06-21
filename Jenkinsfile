

pipeline {
    agent any
    stages {
	    
stage('Read Config') {
            steps {
                script {
                    arrayURL = readFile "${env.WORKSPACE}/config.txt"
                    abc = arrayURL.split('\n')
		    abcd = abc[0].split(' ')
		    echo"$abcd"	
		
       }
     }
   }
	    
       
	    
}
}
