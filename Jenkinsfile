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



pipeline {

    agent {
        dockerfile true
    }

    stages {
        stage('Test') {
            steps {
                echo 'Testing'
                step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: false])
            }
        }
    }
}



pipeline {
    agent none

    stages {
        stage('Prepare') {
            agent any
            steps {
                echo 'Prepare'
                step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: false])
            }
        }
        stage('Build') {
            agent {
                dockerfile true
            }
            steps {
                sh 'python -m pytest -m health_test'
            }
        }
    }
}


