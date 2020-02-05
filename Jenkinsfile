pipeline {

    agent any

    stages {
        stage('Orchestration') {
            steps {
                echo 'Docker Compose'
                sh 'docker-compose up -d selenium-hub'
                sh 'docker-compose up -d chrome'
                sh 'docker-compose up hotels-tests'
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
