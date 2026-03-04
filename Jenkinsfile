pipeline {
    agent any

    stages {

        stage('Run Tests') {
            steps {
                bat '''
                mkdir Automation
                xcopy /E /I config Automation\\config
                xcopy /E /I pages Automation\\pages
                xcopy /E /I tests Automation\\tests
                xcopy /E /I utils Automation\\utils
                "C:\\Users\\SAHIBA\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pytest -v Automation\\tests
                '''
            }
        }

    }
}