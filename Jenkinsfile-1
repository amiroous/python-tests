pipeline {

    agent {
        docker { image 'python:3.7.2-alpine3.9' }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building'
                sh 'python --version'
                sh 'pip --version'
                sh 'pip install --upgrade pip'
                sh 'pip install pipenv'
                sh 'pip install pytest'
                sh 'pip install selenium'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing'
                sh 'cd functional'
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

    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'Deploy Completed Successfully'
        }
        failure {
            echo 'Deploy Failed!'
        }
        unstable {
            echo 'WARNING: Unstable Build'
        }
        changed {
            echo 'Pipeline State Has Been Changed.'
        }
    }
}
