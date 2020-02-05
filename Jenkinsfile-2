pipeline {

    agent {
        dockerfile true
    }

    stages {
        stage('Test') {
            steps {
                echo 'Testing'
                sh 'python -m pytest -m health_test'
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
