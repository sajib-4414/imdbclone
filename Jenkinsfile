pipeline{
    agent any //any agent can run this job

    stages{
        stage('Checkout Code'){
            steps{
                checkout scm

                sh "ls -ltr"
            }
            steps{
                echo 'After checkout'
            }
        }
        stage('Echo Hello World') {
            steps {
                echo 'Hello World'
            }
        }
    },
    post {
        always {
            cleanWs() //clean workspace when done
        }
    }
}