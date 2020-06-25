Properties properties = new Properties()
File propertiesFile = new File('${env.WORKSPACE}/test.properties')
propertiesFile.withInputStream {
    properties.load(it)
}
