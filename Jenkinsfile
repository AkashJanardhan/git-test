pipeline {
    agent any
    stages {
        stage('One') {
                steps {
                       sh'echo “google.com\nfacebook.com” | python ssl_expiry.py'
			
			
                }
        }
	    stage('Two'){
		    
		steps {
			input('Do you want to proceed?')
        }
	    }
        stage('Three') {
                when {
                        not {
                                branch "master"
                        }
                }
                steps {
			echo "Hello"
                        }
        }
        stage('Four') {
                parallel {
                        stage('Unit Test') {
                                steps{
                                        echo "Running the unit test...akshit"
                                }
                        }
                        stage('Integration test') {
                        
				steps {
					echo 'Running the integration test..'
				}
                               
			}  
        }
    }
}
}
