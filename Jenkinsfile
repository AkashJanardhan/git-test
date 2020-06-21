Properties properties = new Properties()
File propertiesFile = new File('test.properties')
propertiesFile.withInputStream {
    properties.load(it)
}

def runtimeString = 'a'

pipeline {
    agent any
    stages {
        stage('One') {
                steps {
                       echo "$runtimeString"
			
			
                }
        }
	    
}
}
