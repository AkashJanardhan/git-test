

pipeline {
    agent any
    stages {
	    
stage ('Prepare') {
   steps {
      script {
         properties = readProperties file: 'test.properties'
         echo "${properties.a}"
       }
     }
   }
	    
        stage('One') {
                steps {
                       echo "hello"
			
			
                }
        }
	    
}
}
