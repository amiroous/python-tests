pipeline {

    agent any

    stages {
        stage('Orchestration') {
            steps {
                echo 'Docker Compose'
                sh '/usr/local/bin/docker-compose up -d selenium-hub'
                sh '/usr/local/bin/docker-compose up -d chrome'
                sh '/usr/local/bin/docker-compose up hotels-tests'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying'
                echo 'TODO: Deploy if All Tests Are Being Passed'
            }
        }
    }
}
