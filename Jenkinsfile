Properties properties = new Properties()
File propertiesFile = new File('${env.WORKSPACE}/test.properties')
propertiesFile.withInputStream {
    a = properties.load(it)
    echo"$a"
    
}
