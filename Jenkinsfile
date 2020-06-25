
properties = null     

def loadProperties() {
    node {
        checkout scm
        properties = new Properties()
        File propertiesFile = new File("${env.WORKSPACE}/test.properties")
        properties.load(propertiesFile.newDataInputStream())
        echo "Immediate one ${properties.b}"
    }
}

pipeline {
    agent none

    stages {
        stage ('prepare') {
            agent any

            steps {
                script {
                    loadProperties()
                    echo "Later one ${properties.c}"
                }
            }
        }
    }
}
