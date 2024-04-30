
    var questions = {{ questions|safe }};
    var currentQuestionIndex = 0;
    var correctAnswers = 0;
    var timerInterval;
    var timeLimit = 60; // Tiempo límite de respuesta en segundos
    // Seleccionar el formulario y el campo de entrada
    var form = document.getElementById('integer-form');
    var input = document.getElementById('integer-input');
    var questionContainer = document.getElementById('question-container');
    var answersContainer = document.getElementById('answers-container');
    

    function displayQuestion(question) {
        var questionHTML = `
            <div class="question">
                <h4>${question.index}</h4>
                <h3 class="mb-3">${question.ask}</h3>
                
            </div>
            
        `;
        var answersHTML = `
            <div class="answers">
                <div class="form-check mb-3">
                    <ul class='answer_list'>
                        <li><button class='button-28' onclick="checkAnswer('${question.option_one}', '${question.correct_answer}')">${question.option_one}</button></li>
                        <li><button class='button-28' onclick="checkAnswer('${question.option_two}', '${question.correct_answer}')">${question.option_two}</button></li>
                        <li><button class='button-28' onclick="checkAnswer('${question.option_three}', '${question.correct_answer}')">${question.option_three}</button></li>
                    </ul>
                </div>
                <br>
                <p id="timer"></p>
                
            </div>
            
            
        `;
        questionContainer.innerHTML = questionHTML;
        answersContainer.innerHTML = answersHTML;
        startTimer();
    }

    function startTimer() {
        var timeLeft = timeLimit;
        updateTimerDisplay(timeLeft);
        timerInterval = setInterval(function() {
            timeLeft--;
            updateTimerDisplay(timeLeft);
            if (timeLeft === 0) {
                clearInterval(timerInterval);
                nextQuestion();
            }
        }, 1000);
    }

    function updateTimerDisplay(timeLeft) {
        document.getElementById('timer').innerText = `Tiempo restante: ${timeLeft} segundos`;
    }

    function checkAnswer(selectedAnswer, correctAnswer) {
        clearInterval(timerInterval); // Detener el temporizador
        if (selectedAnswer === correctAnswer) {
            correctAnswers++;
            alert("¡Respuesta correcta!");
        } else {
            alert("Respuesta incorrecta. La respuesta correcta es: " + correctAnswer);
        }
        nextQuestion();
    }

    function nextQuestion() {
        clearInterval(timerInterval); // Asegurarse de que el temporizador se detenga
        currentQuestionIndex++;
        if (currentQuestionIndex < questions.length) {
            displayQuestion(questions[currentQuestionIndex]);
        } else {
            // Establecer el valor del campo de entrada a los asiertos del jugador
            input.value = correctAnswers;

            // Enviar el formulario programáticamente
            form.submit();
            //alert(`Has respondido ${correctAnswers} preguntas correctamente.`);
        }
    }

    // Comenzar mostrando la primera pregunta
    displayQuestion(questions[currentQuestionIndex]);

