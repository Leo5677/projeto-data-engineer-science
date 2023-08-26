/* AO CARREGAR O DOM */
window.addEventListener("load", () => {
  /* ANIMAÇÃO DE CARREGAMENTO */
  const loadingOverlay = document.querySelector(".loading-overlay");

  setTimeout(() => {
    loadingOverlay.style.display = "none"
  }, 1500);
});

/* ANIMAÇÃO DA DESCRIÇÃO DO PROJETO */
document.addEventListener('DOMContentLoaded', () => {
  const welcomeText = document.getElementById('welcome-text');

  const messages = [
    'Leonardo Cirqueira Valensoela',
    'Thiago Neves Pedroso',
    'Rafael Onassis Nicolau',
    'Visualizar as estatísticas dos últimos 5 anos do BTC',
    'Visualizar as estatísticas dos últimos 30 dias do BTC'
  ];

  let currentMessage = 0;
  let currentChar = 0;
  let direction = 1;

  function updateWelcomeMessage() {
    // OBTÉM O TEXTO ATUAL E INSERE NO SPAN DE BOAS-VINDAS
    const currentText = messages[currentMessage];
    const displayedText = currentText.substring(0, currentChar);
    welcomeText.textContent = displayedText;

    /* CONCATENA PARA OBTER A PRÓXIMA MENSAGEM OU A ANTERIOR */
    currentChar += direction;

    /* CASO TENHA CHEGADO NO FINAL DA DIGITAÇÃO, IRÁ APAGAR */
    if (direction === 1 && currentChar > currentText.length) {
      direction = -1;
      setTimeout(updateWelcomeMessage, 500);
    } else if (direction === -1 && currentChar < 0) {
      /* CASO NÃO TENHA APAGADO TODA A MENSAGEM, IRÁ DIGITAR A PRÓXIMA */
      direction = 1;
      currentMessage = (currentMessage + 1) % messages.length;
      currentChar = 0;
      setTimeout(updateWelcomeMessage, 500); // Tempo de espera após apagar
    } else {
      /* CASO NÃO TENHA CHEGADO NO FINAL DA DIGITAÇÃO E NÃO ESTEJA APAGANDO */
      setTimeout(updateWelcomeMessage, 50); // Velocidade de digitação
    }
  }
  updateWelcomeMessage()
});