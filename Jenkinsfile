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
