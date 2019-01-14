pipeline {
    agent any

    stages {
        stage('Building') {
            steps {
                echo 'Building'
                echo 'Unit Testing'
                echo 'Docker Build'
            }
        }
        stage('Deploy to Stage') {
            steps {
                echo 'Deploying to Stage'
            }
        }
        stage('Parallel Testing') {
            steps {
                parallel(
                    Functional: {
                        echo 'Functional Test'
                    },
                    Performance: {
                        echo 'Performance Test'
                    }
                )
            }
        }
        stage('Deliver to Live Site') {
            steps {
                echo 'Delivering'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}