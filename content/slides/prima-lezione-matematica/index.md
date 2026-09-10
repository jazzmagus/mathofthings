---
title: La prima lezione di matematica
summary: Presentazione, regole del gioco e organizzazione dell'anno
authors: [Diego Fantinelli]
tags: [organizzazione, prima-lezione]
categories: [lesson]
date: "2026-07-09T00:00:00Z"
draft: false
unlisted: true
slides:
  theme: mathofthings
  transition: convex
  particles: true
  particlesColorLight: "#45a3d1"
  particlesColorDark: "#7ecbef"
---

<section class="mot-hero" data-transition="zoom">
  <div class="hero-icon hero-icon-anim" style="margin: 0 auto 16px; width: 140px;">
    <svg width="140" height="50" viewBox="0 0 140 50" aria-hidden="true">
      <defs>
        <filter id="hero-goo" x="-30" y="-30" width="200" height="110" filterUnits="userSpaceOnUse">
          <feGaussianBlur in="SourceGraphic" stdDeviation="4" result="blur" />
          <feColorMatrix in="blur" mode="matrix"
            values="1 0 0 0 0
                    0 1 0 0 0
                    0 0 1 0 0
                    0 0 0 20 -9" result="goo" />
          <feComposite in="SourceGraphic" in2="goo" operator="atop" />
        </filter>
      </defs>
      <g filter="url(#hero-goo)" fill="currentColor">
        <circle cx="70" cy="25" r="16" />
        <circle id="hero-icon-ball" cx="70" cy="25" r="6.5" />
      </g>
    </svg>
  </div>
  <script>
    (function () {
      var ball = document.getElementById('hero-icon-ball');
      if (!ball) return;
      var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      if (reduceMotion) return;
      var centerX = 70, amplitude = 40, duration = 1600, start = null;
      function frame(ts) {
        if (start === null) start = ts;
        var elapsed = (ts - start) % (duration * 2);
        var t = elapsed / duration;
        var x = t < 1 ? -amplitude + amplitude * 2 * t : amplitude - amplitude * 2 * (t - 1);
        ball.setAttribute('cx', centerX + x);
        requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    })();
  </script>
  <p class="mot-kicker">inizio anno scolastico</p>
  <h1>La <em>prima</em> <span class="math-word">lezione</span> di matematica</h1>
  <p class="mot-tagline">la matematica non è imparare formule a memoria, ma collegare <em>concetti</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section id="menu" class="mot-divider" data-transition="zoom">
  <p class="mot-kicker">prima lezione dell'anno</p>
  <h1 class="r-fit-text">SCEGLI LA CLASSE</h1>
  <div class="mot-menu-cards">
    <a class="mot-menu-card" href="#/terze">
      <span class="mot-menu-card-num">3&ordf;</span>
      <span class="mot-menu-card-label">Terze</span>
    </a>
    <a class="mot-menu-card" href="#/quarte">
      <span class="mot-menu-card-num">4&ordf;</span>
      <span class="mot-menu-card-label">Quarte</span>
    </a>
    <a class="mot-menu-card" href="#/quinte">
      <span class="mot-menu-card-num">5&ordf;</span>
      <span class="mot-menu-card-label">Quinte</span>
    </a>
  </div>
</section>

---

<section id="terze" class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">BENVENUTI</h1>
  <p class="mot-joke fragment">saluti, presentazioni, e qualche regola del gioco</p>
</section>

<section>
  <p class="mot-kicker">chi sono</p>
  <h2>Saluti e presentazioni</h2>
  <p class="fragment">Un primo giro di conoscenza: chi sono io, chi siete voi, da dove arrivate e cosa vi aspettate da quest'anno di matematica.</p>
  <p class="mot-joke fragment">niente paura, non c'è un'interrogazione nascosta in questa slide</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">COMUNICAZIONI</h1>
</section>

<section>
  <p class="mot-kicker">comunicazioni ufficiali</p>
  <h2>Il test d'<em>ingresso</em></h2>
  <p class="mot-def fragment">Si terrà nella mia ora, nelle prime settimane di lezione: verificheremo insieme il livello di partenza, senza ansie e senza voti che pesano.</p>
  <dl class="mot-rows fragment">
    <dt>argomenti</dt><dd>il programma dello scorso anno scolastico</dd>
    <dt>calcolo</dt><dd>operazioni, espressioni, proprietà delle potenze</dd>
    <dt>frazioni</dt><dd>operazioni con le frazioni</dd>
    <dt>geometria</dt><dd>nozioni di base</dd>
    <dt>proporzioni</dt><dd>proporzioni, percentuali</dd>
    <dt>problemi</dt><dd>semplici problemi applicativi</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">perché ci tengo al test d'ingresso</p>
  <h2>Statistiche sulle competenze <em>in ingresso</em></h2>
  <div class="mot-barchart">
    <div class="fragment mot-bar" style="--bar-color:#b3503f; --target:5%;">
      <div class="mot-bar-value">5%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">sotto le<br>minime</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#d9a441; --target:20%;">
      <div class="mot-bar-value">20%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">competenze<br>minime</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#ed6f5c; --target:50%;">
      <div class="mot-bar-value">50%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">sufficienti /<br>discrete</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#6f9e74; --target:20%;">
      <div class="mot-bar-value">20%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">buone</div>
    </div>
    <div class="fragment mot-bar" style="--bar-color:#c9a227; --target:5%;">
      <div class="mot-bar-value">5%</div>
      <div class="mot-bar-col"><div class="mot-bar-fill"></div></div>
      <div class="mot-bar-label">ottime /<br>eccellenti</div>
    </div>
  </div>
  <p class="mot-joke fragment" style="margin-top: 1.5rem;">un quarto della classe parte già sotto soglia — è per questo che il test non è una formalità</p>
</section>

<section>
  <p class="mot-kicker">test d'ingresso</p>
  <h2>Come userò <em>i risultati</em></h2>
  <dl class="mot-rows fragment">
    <dt>1. modalità</dt><dd>tipicamente un test a risposta multipla: una domanda, quattro possibilità, una sola corretta</dd>
    <dt>2. voto</dt><dd>verrà inserito in <b>blu</b>: non farà media, ma servirà come riferimento del punto di partenza — con la speranza che la media finale sia più alta di quel voto</dd>
    <dt>3. serietà</dt><dd>lo svolgimento va preso sul serio: non è una formalità, anche se non fa media</dd>
  </dl>
  <p class="mot-joke fragment">niente calcolatrice — per il semplice motivo che non vi serve, e non vi servirà per tutto l'anno</p>
</section>

<!--
<section>
  <p class="mot-kicker">supporto</p>
  <h2>Sportello e recupero</h2>
  <ul class="fragment">
    <li class="fragment">incontri pomeridiani settimanali, circa 1,5 ore ciascuno</li>
    <li class="fragment">attivi fino a dicembre</li>
    <li class="fragment">proposti sulla base dei risultati del test d'ingresso</li>
    <li class="fragment">aperti a chiunque ne senta il bisogno, non solo a chi viene "convocato"</li>
    <li class="fragment">tenuti da un collega diverso da me: è normale, ci scambiamo le classi</li>
  </ul>
  <p class="mot-joke fragment">i dettagli precisi arriveranno più avanti, appena il quadro sarà completo</p>
</section>
-->

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">MATERIALI</h1>
</section>

<section>
  <p class="mot-kicker">strumenti didattici</p>
  <h2>Dove trovare <em>tutto</em></h2>
  <dl class="mot-rows mot-rows-compact">
    <dt class="fragment">The Math of Things</dt><dd class="fragment"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a> — il mio sito web, con lezioni, dispense e materiali di approfondimento sempre disponibili</dd>
    <dt class="fragment">Google Classroom</dt><dd class="fragment">comunicazioni, compiti, materiale didattico (dispense, video, esercizi), post e suggerimenti — <a href="#/classroom-codes" class="mono">codice della classe</a></dd>
    <dt class="fragment">Registro elettronico</dt><dd class="fragment">Classeviva Spaggiari — comunicazioni ufficiali, verifiche, interrogazioni, note, voti</dd>
    <dt class="fragment">Libro di testo</dt><dd class="fragment">non strettamente indispensabile in classe; valutiamo insieme una versione digitale</dd>
    <dt class="fragment">Appunti</dt><dd class="fragment">in caso di necessità condividerò direttamente i miei appunti: non c'è bisogno di fare esercizio di pura copiatura</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA LEZIONE</h1>
</section>

<section>
  <p class="mot-kicker">come lavoriamo</p>
  <h2>Le regole del <em>gioco</em></h2>
  <blockquote class="mot-quote">
    <em>Questi sono i miei principi. Se non vi piacciono, ne ho altri.</em>
    <span class="quote-attr">&mdash; Groucho Marx</span>
  </blockquote>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Come si svolge una lezione tipo</li>
    <li class="fragment" style="margin-bottom:0.5em;">Quali sono gli strumenti didattici che useremo insieme durante l'anno</li>
    <li class="fragment" style="margin-bottom:0;">Cosa mi aspetto da voi in classe</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">a casa</p>
  <h2>Attività in <em>autonomia</em></h2>
  <ul class="fragment">
    <li class="fragment">revisione degli appunti</li>
    <li class="fragment">approfondimenti: sul testo, sul web o altre fonti digitali, con l'aiuto dell'AI</li>
    <li class="fragment">esercizi (pochi, ma buoni)</li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> quanto tempo è bene dedicare allo studio della matematica per rimanere al passo, senza fare troppa fatica?</p>
  <p class="mot-def fragment"><b>R:</b> la risposta è piuttosto soggettiva — ma qualche consiglio per voi ce l'ho.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA VERIFICA</h1>
  <p class="mot-joke fragment">delle competenze, non solo delle formule</p>
</section>

<section>
  <p class="mot-kicker">definizioni</p>
  <h2>Abilità, conoscenze, <em>competenze</em></h2>
  <p class="mot-def fragment">Le <em>abilità</em> sono la capacità di applicare le <em>conoscenze</em> apprese, con lo scopo di risolvere problemi e portare a termine compiti.</p>
  <p class="mot-def fragment">Le <em>competenze</em> sono la capacità di unire <em>conoscenze</em>, <em>abilità</em> e capacità personali, sociali e metodologiche, e di utilizzarle nello studio e nello sviluppo personale.</p>
  <p class="mot-statement fragment">Io valuterò le vostre <em>competenze</em>.</p>
</section>

<section>
  <p class="mot-kicker">valutazione — 1</p>
  <h2>La verifica <em>scritta</em></h2>
  <ul class="fragment">
    <li class="fragment">una verifica per ogni modulo/argomento</li>
    <li class="fragment"><a href="/uploads/verifiche/LB01-insiemi.pdf" target="_blank" class="mono">esempio di verifica</a></li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> come viene calcolato il punteggio e come si trasforma nel voto finale?</p>
  <p class="mot-def fragment"><b>R:</b> è un algoritmo che tiene conto di diverse variabili.</p>
  <dl class="mot-rows fragment">
    <dt>1</dt><dd>livello di assimilazione dell'argomento</dd>
    <dt>2</dt><dd>capacità di ragionamento</dd>
    <dt>3</dt><dd>capacità di calcolo</dd>
    <dt>4</dt><dd>ordine</dd>
    <dt>5</dt><dd>etc.</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">valutazione — 2</p>
  <h2>La verifica <em>orale</em></h2>
  <p class="fragment">Potrà avvenire con modalità diverse, a seconda dei livelli e dei ritmi espressi dalla classe.</p>
  <ul class="fragment" style="font-size:0.92em;">
    <li class="fragment">interrogazione classica: volontaria e concordata
      <ul style="font-size:0.76em; margin-top:0.3em;">
        <li class="fragment">per migliorare la media</li>
        <li class="fragment">per recuperare, eccezionalmente</li>
      </ul>
    </li>
    <li class="fragment">correzione di esercizi alla lavagna, non concordata, con valutazione discrezionale da parte del docente</li>
    <li class="fragment">eventuali test proposti dall'insegnante</li>
    <li class="fragment">utilizzo dei voti in blu, per avere ulteriori informazioni in fase di scrutinio di fine periodo</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">valutazione — 3</p>
  <h2>Quaderni e prove <em>pratiche</em></h2>
  <dl class="mot-rows mot-rows-compact">
    <dt class="fragment">quaderni</dt><dd class="fragment">non effettuerò alcun controllo: il lavoro va svolto in autonomia, e dato che non posso assegnare compiti per casa, non ha senso correggerli, richiederli o controllarli</dd>
    <dt class="fragment">prove pratiche</dt><dd class="fragment">Flipped-Classroom o altre attività in coppie/piccoli gruppi, solo a determinate condizioni</dd>
    <dt class="fragment">lavoro in autonomia</dt><dd class="fragment">non potendo assegnare compiti per casa, proporrò delle esercitazioni che, chi vorrà, potrà consegnarmi su Classroom in formato PDF — ne terrò conto per correggere le medie in fase di scrutinio di fine periodo</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">CREDITI</h1>
  <p class="mot-joke fragment">richiesta di esonero dalle mie meravigliose lezioni</p>
  <img src="sad-cutout.png" alt="" class="fragment mot-esonero-img" style="width:240px;">
</section>

<section>
  <p class="mot-kicker">due percorsi possibili</p>
  <h2>Tipologie di <em>crediti</em></h2>
  <dl class="mot-rows fragment">
    <dt>crediti informali</dt><dd>assegnati d'ufficio, ad esempio in caso di cambio di scuola: attestano competenze già acquisite (es. una pagella con 8 in matematica da un istituto tecnico) e comportano l'esonero automatico dalle lezioni</dd>
    <dt>crediti formali</dt><dd>concessi dal docente della disciplina sulla base di una valutazione concordata — nel mio caso, una prova scritta nella prima settimana di ottobre</dd>
  </dl>
  <p class="mot-def fragment">La prova riguarda tutto il programma dell'anno scolastico in corso — il programma è consultabile nella sezione Corsi del sito.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LEZIONI PRIVATE</h1>
</section>

<section>
  <p class="mot-def">Non posso impartire lezioni private a nessuno studente dell'istituto in cui insegno: è un impegno che ho sottoscritto ancora prima della firma del contratto.</p>
  <h2 class="fragment" style="margin-top:0.4em">I <em>privé</em> di matematica</h2>
  <p class="mot-def fragment">Ci saranno delle ore che metterò a disposizione ogni mese per degli incontri.</p>
  <dl class="mot-rows mot-rows-center fragment">
    <dt>4 studenti</dt><dd>15 minuti a testa</dd>
    <dt>3 studenti</dt><dd>20 minuti a testa</dd>
    <dt>2 studenti</dt><dd>mezz'ora a testa</dd>
    <dt>1 studente</dt><dd>un'ora</dd>
  </dl>
  <p class="mot-def fragment">Non farò ripetizioni, ma potrò dare supporto di diverso tipo: spiegare un passaggio che non si è compreso, ascoltare se avete problemi di qualsiasi tipo (principalmente, ma non solo, di matematica), o aiutarvi a organizzare il metodo di studio — non sarà un falò di Temptation Island.</p>
</section>

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <img src="quest-cutout.png" alt="" class="mot-quest-img">
</section>



---

<section id="quarte" class="mot-divider" data-transition="zoom" data-background-image="bentornati.jpg" data-background-opacity="0.65">
  <h1 class="r-fit-text">BENTORNATI</h1>
  <p class="mot-joke fragment">saluti, presentazioni, e qualche regola del gioco</p>
</section>

<section>
  <p class="mot-kicker">chi sono</p>
  <h2>Saluti e presentazioni</h2>
  <p class="mot-joke fragment">ci si rivede — vi conosco già, quindi ci risparmiamo il giro di presentazioni</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">COMUNICAZIONI</h1>
</section>

<section>
  <p class="mot-kicker">comunicazioni ufficiali</p>
  <h2>Le conferenze del <em>serale</em></h2>
  <p class="fragment">Quest'anno il ciclo di conferenze che si teneva al serale non è stato formalizzato in un progetto: di conseguenza, non è stato deliberato né accettato dal collegio docenti.</p>
  <p class="mot-def fragment">Il risultato pratico: niente conferenze, salvo che qualche docente del serale non organizzi, di sua spontanea volontà, una mini conferenza — non aperta all'esterno.</p>
  <p class="mot-joke fragment">io mi sono già attivato, e ne ho una pronta per alleggerirvi un paio d'ore — sono certo che ce ne sia almeno un'altra in arrivo, probabilmente due</p>
</section>

<section>
  <p class="mot-kicker">comunicazioni ufficiali</p>
  <h2><em>Super Power</em> dei docenti del <em>serale</em></h2>
  <p class="fragment">Rispetto al diurno, i docenti del serale hanno un vantaggio in più: gli studenti sono maggiorenni.</p>
  <p class="mot-def fragment">Il "superpotere" consiste nella possibilità di allontanare dalla classe uno studente, per motivi disciplinari o per altri motivi.</p>
  <p class="fragment">Oltre alle linee guida della scuola, il dipartimento di indirizzo ha deciso di adottarlo, per garantire lezioni più serene — e quindi più efficaci.</p>
</section>

<!--
<section>
  <p class="mot-kicker">supporto</p>
  <h2>Sportello e recupero</h2>
  <ul class="fragment">
    <li class="fragment">incontri pomeridiani settimanali, circa 1,5 ore ciascuno</li>
    <li class="fragment">attivi fino a dicembre</li>
    <li class="fragment">proposti sulla base dei risultati del test d'ingresso</li>
    <li class="fragment">aperti a chiunque ne senta il bisogno, non solo a chi viene "convocato"</li>
    <li class="fragment">tenuti da un collega diverso da me: è normale, ci scambiamo le classi</li>
  </ul>
  <p class="mot-joke fragment">i dettagli precisi arriveranno più avanti, appena il quadro sarà completo</p>
</section>
-->

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">MATERIALI</h1>
</section>

<section>
  <p class="mot-kicker">strumenti didattici</p>
  <h2>Dove trovare <em>tutto</em></h2>
  <dl class="mot-rows mot-rows-compact">
    <dt class="fragment">The Math of Things</dt><dd class="fragment"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a> — il mio sito web, con lezioni, dispense e materiali di approfondimento sempre disponibili</dd>
    <dt class="fragment">Google Classroom</dt><dd class="fragment">comunicazioni, compiti, materiale didattico (dispense, video, esercizi), post e suggerimenti — <a href="#/classroom-codes" class="mono">codice della classe</a></dd>
    <dt class="fragment">Registro elettronico</dt><dd class="fragment">Classeviva Spaggiari — comunicazioni ufficiali, verifiche, interrogazioni, note, voti</dd>
    <dt class="fragment">Libro di testo</dt><dd class="fragment">non strettamente indispensabile in classe; valutiamo insieme una versione digitale</dd>
    <dt class="fragment">Appunti</dt><dd class="fragment">in caso di necessità condividerò direttamente i miei appunti: non c'è bisogno di fare esercizio di pura copiatura</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA LEZIONE</h1>
</section>

<section>
  <p class="mot-kicker">come lavoriamo</p>
  <h2>Le regole del <em>gioco</em></h2>
  <blockquote class="mot-quote">
    <em>Questi sono i miei principi. Se non vi piacciono, ne ho altri.</em>
    <span class="quote-attr">&mdash; Groucho Marx</span>
  </blockquote>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Come si svolge una lezione tipo</li>
    <li class="fragment" style="margin-bottom:0.5em;">Quali sono gli strumenti didattici che useremo insieme durante l'anno</li>
    <li class="fragment" style="margin-bottom:0;">Cosa mi aspetto da voi in classe</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">a casa</p>
  <h2>Attività in <em>autonomia</em></h2>
  <ul class="fragment">
    <li class="fragment">revisione degli appunti</li>
    <li class="fragment">approfondimenti: sul testo, sul web o altre fonti digitali, con l'aiuto dell'AI</li>
    <li class="fragment">esercizi (pochi, ma buoni)</li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> quanto tempo è bene dedicare allo studio della matematica per rimanere al passo, senza fare troppa fatica?</p>
  <p class="mot-def fragment"><b>R:</b> la risposta è piuttosto soggettiva — ma qualche consiglio per voi ce l'ho.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA VERIFICA</h1>
  <p class="mot-joke fragment">delle competenze, non solo delle formule</p>
</section>

<section>
  <p class="mot-kicker">definizioni</p>
  <h2>Abilità, conoscenze, <em>competenze</em></h2>
  <p class="mot-def fragment">Le <em>abilità</em> sono la capacità di applicare le <em>conoscenze</em> apprese, con lo scopo di risolvere problemi e portare a termine compiti.</p>
  <p class="mot-def fragment">Le <em>competenze</em> sono la capacità di unire <em>conoscenze</em>, <em>abilità</em> e capacità personali, sociali e metodologiche, e di utilizzarle nello studio e nello sviluppo personale.</p>
  <p class="mot-statement fragment">Io valuterò le vostre <em>competenze</em>.</p>
</section>

<section>
  <p class="mot-kicker">valutazione — 1</p>
  <h2>Verifiche e <em>recuperi</em></h2>
  <ul class="fragment">
    <li class="fragment">sosterrete delle verifiche scritte e orali durante l'anno</li>
    <li class="fragment">3 valutazioni nel primo periodo, 4 nel secondo</li>
  </ul>
  <dl class="mot-rows fragment">
    <dt>primo periodo</dt><dd>2 verifiche scritte + 1 orale (test)</dd>
    <dt>secondo periodo</dt><dd>3 verifiche scritte + 1 orale (eventualmente test)</dd>
  </dl>
  <p class="mot-def fragment">I <em>recuperi</em> avverranno in modo cumulativo, a fine periodo: una verifica aggiuntiva conterrà tutti i moduli, e ognuno recupererà solo ciò che non è riuscito a fare o è risultato insufficiente.</p>
  <p class="mot-joke fragment">dato che le verifiche sono concordate, il giorno della verifica non può essere assente metà classe</p>
</section>

<section>
  <p class="mot-kicker">valutazione — 2</p>
  <h2>La verifica <em>orale</em></h2>
  <p class="fragment">Potrà avvenire con modalità diverse, a seconda dei livelli e dei ritmi espressi dalla classe.</p>
  <ul class="fragment" style="font-size:0.92em;">
    <li class="fragment">interrogazione classica: volontaria e concordata
      <ul style="font-size:0.76em; margin-top:0.3em;">
        <li class="fragment">per migliorare la media</li>
        <li class="fragment">per recuperare, eccezionalmente</li>
      </ul>
    </li>
    <li class="fragment">correzione di esercizi alla lavagna, non concordata, con valutazione discrezionale da parte del docente</li>
    <li class="fragment">eventuali test proposti dall'insegnante</li>
    <li class="fragment">utilizzo dei voti in blu, per avere ulteriori informazioni in fase di scrutinio di fine periodo</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">valutazione — 3</p>
  <h2>Quaderni e prove <em>pratiche</em></h2>
  <dl class="mot-rows mot-rows-compact">
    <dt class="fragment">quaderni</dt><dd class="fragment">non effettuerò alcun controllo: il lavoro va svolto in autonomia, e dato che non posso assegnare compiti per casa, non ha senso correggerli, richiederli o controllarli</dd>
    <dt class="fragment">prove pratiche</dt><dd class="fragment">Flipped-Classroom o altre attività in coppie/piccoli gruppi, solo a determinate condizioni</dd>
    <dt class="fragment">lavoro in autonomia</dt><dd class="fragment">non potendo assegnare compiti per casa, proporrò delle esercitazioni che, chi vorrà, potrà consegnarmi su Classroom in formato PDF — ne terrò conto per correggere le medie in fase di scrutinio di fine periodo</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">CREDITI</h1>
  <p class="mot-joke fragment">richiesta di esonero dalle mie meravigliose lezioni</p>
  <img src="sad-cutout.png" alt="" class="fragment mot-esonero-img" style="width:240px;">
</section>

<section>
  <p class="mot-kicker">due percorsi possibili</p>
  <h2>Tipologie di <em>crediti</em></h2>
  <dl class="mot-rows fragment">
    <dt>crediti informali</dt><dd>assegnati d'ufficio, ad esempio in caso di cambio di scuola: attestano competenze già acquisite (es. una pagella con 8 in matematica da un istituto tecnico) e comportano l'esonero automatico dalle lezioni</dd>
    <dt>crediti formali</dt><dd>concessi dal docente della disciplina sulla base di una valutazione concordata — nel mio caso, una prova scritta nella prima settimana di ottobre</dd>
  </dl>
  <p class="mot-def fragment">La prova riguarda tutto il programma dell'anno scolastico in corso — il programma è consultabile nella sezione Corsi del sito.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LEZIONI PRIVATE</h1>
</section>

<section>
  <p class="mot-def">Non posso impartire lezioni private a nessuno studente dell'istituto in cui insegno: è un impegno che ho sottoscritto ancora prima della firma del contratto.</p>
  <h2 class="fragment" style="margin-top:0.4em">I <em>privé</em> di matematica</h2>
  <p class="mot-def fragment">Ci saranno delle ore che metterò a disposizione ogni mese per degli incontri.</p>
  <dl class="mot-rows mot-rows-center fragment">
    <dt>4 studenti</dt><dd>15 minuti a testa</dd>
    <dt>3 studenti</dt><dd>20 minuti a testa</dd>
    <dt>2 studenti</dt><dd>mezz'ora a testa</dd>
    <dt>1 studente</dt><dd>un'ora</dd>
  </dl>
  <p class="mot-def fragment">Non farò ripetizioni, ma potrò dare supporto di diverso tipo: spiegare un passaggio che non si è compreso, ascoltare se avete problemi di qualsiasi tipo (principalmente, ma non solo, di matematica), o aiutarvi a organizzare il metodo di studio — non sarà un falò di Temptation Island.</p>
</section>

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <img src="quest-cutout.png" alt="" class="mot-quest-img">
</section>



---

<section id="quinte" class="mot-divider" data-transition="zoom" data-background-image="bentornati.jpg" data-background-opacity="0.65">
  <h1 class="r-fit-text">BENTORNATI</h1>
  <p class="mot-joke fragment">saluti, presentazioni, e qualche regola del gioco</p>
</section>

<section>
  <p class="mot-kicker">chi sono</p>
  <h2>Saluti e presentazioni</h2>
  <p class="mot-joke fragment">ci si rivede — vi conosco già, quindi ci risparmiamo il giro di presentazioni</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">COMUNICAZIONI</h1>
</section>

<section>
  <p class="mot-kicker">comunicazioni ufficiali</p>
  <h2>Le conferenze del <em>serale</em></h2>
  <p class="fragment">Quest'anno il ciclo di conferenze che si teneva al serale non è stato formalizzato in un progetto: di conseguenza, non è stato deliberato né accettato dal collegio docenti.</p>
  <p class="mot-def fragment">Il risultato pratico: niente conferenze, salvo che qualche docente del serale non organizzi, di sua spontanea volontà, una mini conferenza — non aperta all'esterno.</p>
  <p class="mot-joke fragment">io mi sono già attivato, e ne ho una pronta per alleggerirvi un paio d'ore — sono certo che ce ne sia almeno un'altra in arrivo, probabilmente due</p>
</section>

<section>
  <p class="mot-kicker">comunicazioni ufficiali</p>
  <h2><em>Super Power</em> dei docenti del <em>serale</em></h2>
  <p class="fragment">Rispetto al diurno, i docenti del serale hanno un vantaggio in più: gli studenti sono maggiorenni.</p>
  <p class="mot-def fragment">Il "superpotere" consiste nella possibilità di allontanare dalla classe uno studente, per motivi disciplinari o per altri motivi.</p>
  <p class="fragment">Oltre alle linee guida della scuola, il dipartimento di indirizzo ha deciso di adottarlo, per garantire lezioni più serene — e quindi più efficaci.</p>
</section>

<!--
<section>
  <p class="mot-kicker">supporto</p>
  <h2>Sportello e recupero</h2>
  <ul class="fragment">
    <li class="fragment">incontri pomeridiani settimanali, circa 1,5 ore ciascuno</li>
    <li class="fragment">attivi fino a dicembre</li>
    <li class="fragment">proposti sulla base dei risultati del test d'ingresso</li>
    <li class="fragment">aperti a chiunque ne senta il bisogno, non solo a chi viene "convocato"</li>
    <li class="fragment">tenuti da un collega diverso da me: è normale, ci scambiamo le classi</li>
  </ul>
  <p class="mot-joke fragment">i dettagli precisi arriveranno più avanti, appena il quadro sarà completo</p>
</section>
-->

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">MATERIALI</h1>
</section>

<section>
  <p class="mot-kicker">strumenti didattici</p>
  <h2>Dove trovare <em>tutto</em></h2>
  <dl class="mot-rows mot-rows-compact">
    <dt class="fragment">The Math of Things</dt><dd class="fragment"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a> — il mio sito web, con lezioni, dispense e materiali di approfondimento sempre disponibili</dd>
    <dt class="fragment">Google Classroom</dt><dd class="fragment">comunicazioni, compiti, materiale didattico (dispense, video, esercizi), post e suggerimenti — <a href="#/classroom-codes" class="mono">codice della classe</a></dd>
    <dt class="fragment">Registro elettronico</dt><dd class="fragment">Classeviva Spaggiari — comunicazioni ufficiali, verifiche, interrogazioni, note, voti</dd>
    <dt class="fragment">Libro di testo</dt><dd class="fragment">non strettamente indispensabile in classe; valutiamo insieme una versione digitale</dd>
    <dt class="fragment">Appunti</dt><dd class="fragment">in caso di necessità condividerò direttamente i miei appunti: non c'è bisogno di fare esercizio di pura copiatura</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA LEZIONE</h1>
</section>

<section>
  <p class="mot-kicker">come lavoriamo</p>
  <h2>Le regole del <em>gioco</em></h2>
  <blockquote class="mot-quote">
    <em>Questi sono i miei principi. Se non vi piacciono, ne ho altri.</em>
    <span class="quote-attr">&mdash; Groucho Marx</span>
  </blockquote>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Come si svolge una lezione tipo</li>
    <li class="fragment" style="margin-bottom:0.5em;">Quali sono gli strumenti didattici che useremo insieme durante l'anno</li>
    <li class="fragment" style="margin-bottom:0;">Cosa mi aspetto da voi in classe</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">a casa</p>
  <h2>Attività in <em>autonomia</em></h2>
  <ul class="fragment">
    <li class="fragment">revisione degli appunti</li>
    <li class="fragment">approfondimenti: sul testo, sul web o altre fonti digitali, con l'aiuto dell'AI</li>
    <li class="fragment">esercizi (pochi, ma buoni)</li>
  </ul>
  <p class="mot-def fragment"><b>D:</b> quanto tempo è bene dedicare allo studio della matematica per rimanere al passo, senza fare troppa fatica?</p>
  <p class="mot-def fragment"><b>R:</b> la risposta è piuttosto soggettiva — ma qualche consiglio per voi ce l'ho.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LA VERIFICA</h1>
  <p class="mot-joke fragment">delle competenze, non solo delle formule</p>
</section>

<section>
  <p class="mot-kicker">definizioni</p>
  <h2>Abilità, conoscenze, <em>competenze</em></h2>
  <p class="mot-def fragment">Le <em>abilità</em> sono la capacità di applicare le <em>conoscenze</em> apprese, con lo scopo di risolvere problemi e portare a termine compiti.</p>
  <p class="mot-def fragment">Le <em>competenze</em> sono la capacità di unire <em>conoscenze</em>, <em>abilità</em> e capacità personali, sociali e metodologiche, e di utilizzarle nello studio e nello sviluppo personale.</p>
  <p class="mot-statement fragment">Io valuterò le vostre <em>competenze</em>.</p>
</section>

<section>
  <p class="mot-kicker">valutazione — 1</p>
  <h2>Verifiche e <em>recuperi</em></h2>
  <ul class="fragment">
    <li class="fragment">sosterrete delle verifiche scritte e orali durante l'anno</li>
    <li class="fragment">3 valutazioni nel primo periodo, 4 nel secondo</li>
  </ul>
  <dl class="mot-rows fragment">
    <dt>primo periodo</dt><dd>2 verifiche scritte + 1 orale (test)</dd>
    <dt>secondo periodo</dt><dd>3 verifiche scritte + 1 orale (eventualmente test)</dd>
  </dl>
  <p class="mot-def fragment">I <em>recuperi</em> avverranno in modo cumulativo, a fine periodo: una verifica aggiuntiva conterrà tutti i moduli, e ognuno recupererà solo ciò che non è riuscito a fare o è risultato insufficiente.</p>
  <p class="mot-joke fragment">dato che le verifiche sono concordate, il giorno della verifica non può essere assente metà classe</p>
</section>

<section>
  <p class="mot-kicker">valutazione — 2</p>
  <h2>La verifica <em>orale</em></h2>
  <p class="fragment">Potrà avvenire con modalità diverse, a seconda dei livelli e dei ritmi espressi dalla classe.</p>
  <ul class="fragment" style="font-size:0.92em;">
    <li class="fragment">interrogazione classica: volontaria e concordata
      <ul style="font-size:0.76em; margin-top:0.3em;">
        <li class="fragment">per migliorare la media</li>
        <li class="fragment">per recuperare, eccezionalmente</li>
      </ul>
    </li>
    <li class="fragment">correzione di esercizi alla lavagna, non concordata, con valutazione discrezionale da parte del docente</li>
    <li class="fragment">eventuali test proposti dall'insegnante</li>
    <li class="fragment">utilizzo dei voti in blu, per avere ulteriori informazioni in fase di scrutinio di fine periodo</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">valutazione — 3</p>
  <h2>Quaderni e prove <em>pratiche</em></h2>
  <dl class="mot-rows mot-rows-compact">
    <dt class="fragment">quaderni</dt><dd class="fragment">non effettuerò alcun controllo: il lavoro va svolto in autonomia, e dato che non posso assegnare compiti per casa, non ha senso correggerli, richiederli o controllarli</dd>
    <dt class="fragment">prove pratiche</dt><dd class="fragment">Flipped-Classroom o altre attività in coppie/piccoli gruppi, solo a determinate condizioni</dd>
    <dt class="fragment">lavoro in autonomia</dt><dd class="fragment">non potendo assegnare compiti per casa, proporrò delle esercitazioni che, chi vorrà, potrà consegnarmi su Classroom in formato PDF — ne terrò conto per correggere le medie in fase di scrutinio di fine periodo</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">CREDITI</h1>
  <p class="mot-joke fragment">richiesta di esonero dalle mie meravigliose lezioni</p>
  <img src="sad-cutout.png" alt="" class="fragment mot-esonero-img" style="width:240px;">
</section>

<section>
  <p class="mot-kicker">due percorsi possibili</p>
  <h2>Tipologie di <em>crediti</em></h2>
  <dl class="mot-rows fragment">
    <dt>crediti informali</dt><dd>assegnati d'ufficio, ad esempio in caso di cambio di scuola: attestano competenze già acquisite (es. una pagella con 8 in matematica da un istituto tecnico) e comportano l'esonero automatico dalle lezioni</dd>
    <dt>crediti formali</dt><dd>concessi dal docente della disciplina sulla base di una valutazione concordata — nel mio caso, una prova scritta nella prima settimana di ottobre</dd>
  </dl>
  <p class="mot-def fragment">La prova riguarda tutto il programma dell'anno scolastico in corso — il programma è consultabile nella sezione Corsi del sito.</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">ESAME DI MATURITÀ</h1>
</section>

<section>
  <p class="mot-kicker">quinto anno</p>
  <h2>Due scuole di <em>pensiero</em></h2>
  <p class="fragment">Sull'esame di Stato, tra gli insegnanti convivono due approcci opposti.</p>
  <ul class="fragment">
    <li class="fragment">c'è chi, fin dal primo giorno, vi ricorda che quest'anno avrete l'esame di Stato</li>
    <li class="fragment">e c'è chi, come me, è convinto che aggiungere stress a stress non porti ad altro che stress</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">l'obiettivo vero</p>
  <h2>Non è <em>l'esame</em></h2>
  <p class="mot-def fragment">Sembra un paradosso, ma l'obiettivo dell'esame di Stato non è l'esame di Stato: passare l'anno concentrati sull'esame vi farà deragliare. Spesso.</p>
</section>

<section>
  <p class="mot-kicker">come funziona</p>
  <h2>La <em>commissione</em></h2>
  <p class="fragment">L'esame sarà impostato come quello dello scorso anno: un presidente e quattro commissari, due interni e due esterni. Le dinamiche, ormai, si conoscono già.</p>
</section>

<section>
  <p class="mot-kicker">il punto di domanda</p>
  <h2>Le materie d'<em>esame</em></h2>
  <p class="fragment">L'unica incognita è l'uscita delle materie d'esame, di solito a fine gennaio.</p>
  <dl class="mot-rows fragment">
    <dt>se matematica è materia d'esame</dt><dd>proseguiremo con il nostro programma: nessun problema, arriverete sani e salvi</dd>
    <dt>se non lo è</dt><dd>proseguiremo comunque con il programma fino a maggio, poi vi lascerò abbastanza liberi</dd>
  </dl>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LEZIONI PRIVATE</h1>
</section>

<section>
  <p class="mot-def">Non posso impartire lezioni private a nessuno studente dell'istituto in cui insegno: è un impegno che ho sottoscritto ancora prima della firma del contratto.</p>
  <h2 class="fragment" style="margin-top:0.4em">I <em>privé</em> di matematica</h2>
  <p class="mot-def fragment">Ci saranno delle ore che metterò a disposizione ogni mese per degli incontri.</p>
  <dl class="mot-rows mot-rows-center fragment">
    <dt>4 studenti</dt><dd>15 minuti a testa</dd>
    <dt>3 studenti</dt><dd>20 minuti a testa</dd>
    <dt>2 studenti</dt><dd>mezz'ora a testa</dd>
    <dt>1 studente</dt><dd>un'ora</dd>
  </dl>
  <p class="mot-def fragment">Non farò ripetizioni, ma potrò dare supporto di diverso tipo: spiegare un passaggio che non si è compreso, ascoltare se avete problemi di qualsiasi tipo (principalmente, ma non solo, di matematica), o aiutarvi a organizzare il metodo di studio — non sarà un falò di Temptation Island.</p>
</section>

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <img src="quest-cutout.png" alt="" class="mot-quest-img">
</section>

---

<section id="classroom-codes">
  <p class="mot-kicker">accesso rapido</p>
  <h2>Codice <em>Classroom</em></h2>
  <p class="mot-joke">scegli la tua classe — comparirà solo il codice giusto</p>
  <div class="mot-classroom-grid" id="classroom-grid">
    <button type="button" class="mot-classroom-card" data-class="3&ordf;QA" data-code="drohekpg">3&ordf;QA</button>
    <button type="button" class="mot-classroom-card" data-class="3&ordf;QES" data-code="odjovnsp">3&ordf;QES</button>
    <button type="button" class="mot-classroom-card" data-class="4&ordf;QA" data-code="f5bjswtk">4&ordf;QA</button>
    <button type="button" class="mot-classroom-card" data-class="4&ordf;QES" data-code="me3tl7di">4&ordf;QES</button>
    <button type="button" class="mot-classroom-card" data-class="5&ordf;QA" data-code="lremru63">5&ordf;QA</button>
    <button type="button" class="mot-classroom-card" data-class="5&ordf;QES" data-code="ba3jow7w">5&ordf;QES</button>
  </div>
  <div class="mot-classroom-result" id="classroom-result">
    <p class="mot-classroom-result-code" id="classroom-result-code"></p>
  </div>
  <script>
    (function () {
      var grid = document.getElementById('classroom-grid');
      var result = document.getElementById('classroom-result');
      var code = document.getElementById('classroom-result-code');
      if (!grid) return;
      Array.prototype.forEach.call(grid.querySelectorAll('.mot-classroom-card'), function (btn) {
        btn.addEventListener('click', function () {
          Array.prototype.forEach.call(grid.querySelectorAll('.mot-classroom-card'), function (b) {
            b.classList.remove('active');
          });
          btn.classList.add('active');
          code.textContent = btn.getAttribute('data-code');
          result.classList.add('visible');
        });
      });
    })();
  </script>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">buon anno scolastico</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

<style>
body.slides-mot {
  --mot-primary: #45a3d1;
  --r-link-color: #45a3d1;
  --r-link-color-hover: #6cb8dd;
  --r-selection-background-color: rgba(69, 163, 209, 0.35);
}

body.slides-mot.dark {
  --mot-primary: #7ecbef;
  --r-link-color: #7ecbef;
  --r-link-color-hover: #9ed8f2;
}

.mot-theme-toggle {
  border: none;
  background: none;
}

.mot-theme-toggle:hover {
  border: none;
}

body.slides-mot .reveal dl.mot-rows.mot-rows-center {
  grid-template-columns: auto auto;
  justify-content: center;
  width: fit-content;
  margin-left: auto;
  margin-right: auto;
  gap: 0 1.2em;
  line-height: 1;
}

.mot-menu-cards {
  display: flex;
  justify-content: center;
  gap: 1.6em;
  margin-top: 2rem;
  flex-wrap: wrap;
}

.mot-menu-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 0.4em;
  width: 190px;
  height: 190px;
  border: 2px solid var(--mot-border);
  border-radius: 14px;
  text-decoration: none;
  transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease;
}

.mot-menu-card:hover {
  transform: translateY(-4px);
  border-color: var(--mot-primary);
  background: rgba(237, 111, 92, 0.06);
}

.mot-menu-card-num {
  font-family: var(--mot-display);
  font-size: 2.6em;
  color: var(--mot-primary);
  line-height: 1;
}

.mot-menu-card-label {
  font-family: var(--mot-mono);
  font-size: 0.55em;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--mot-text);
}

.mot-barchart {
  display: grid;
  grid-template-rows: auto 1fr auto;
  grid-auto-flow: column;
  grid-auto-columns: 1fr;
  column-gap: 1.4em;
  justify-content: center;
  height: 260px;
  margin: 2rem auto 0;
  max-width: 900px;
}

.mot-bar {
  display: contents;
}

.mot-bar-value {
  justify-self: center;
  align-self: end;
  font-family: var(--mot-mono);
  font-size: 0.55em;
  font-weight: 700;
  color: var(--bar-color);
  margin-bottom: 0.4em;
}

.mot-bar-col {
  justify-self: center;
  align-self: stretch;
  width: 100%;
  max-width: 130px;
  display: flex;
  align-items: flex-end;
  border-radius: 6px 6px 0 0;
  background: rgba(128, 128, 128, 0.1);
  overflow: hidden;
}

.mot-bar-fill {
  width: 100%;
  height: 0;
  background: var(--bar-color);
  border-radius: 6px 6px 0 0;
  transition: height 1s cubic-bezier(0.22, 0.9, 0.35, 1);
}

.mot-bar.visible .mot-bar-fill {
  height: var(--target);
}

.mot-bar-label {
  justify-self: center;
  align-self: start;
  font-family: var(--mot-mono);
  font-size: 0.4em;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--mot-muted);
  text-align: center;
  margin-top: 0.6em;
  max-width: 140px;
  line-height: 1.3;
}

.mot-statement {
  font-size: 1.1em;
  font-weight: 700;
  color: var(--mot-text);
  text-align: center;
  margin-top: 1.5rem;
}

.mot-statement em {
  font-style: italic;
  color: var(--mot-primary);
}

.mot-classroom-grid {
  display: flex;
  flex-wrap: nowrap;
  justify-content: center;
  gap: 0.5em;
  margin-top: 2rem;
}

.mot-classroom-card {
  font-family: var(--r-heading-font, Georgia, serif);
  text-transform: uppercase;
  letter-spacing: 0.03em;
  font-size: 0.55em;
  font-weight: 700;
  padding: 0.5em 0.7em;
  border: 2px solid var(--mot-border);
  border-radius: 8px;
  background: transparent;
  color: var(--mot-text);
  cursor: pointer;
  transition: transform 0.2s ease, border-color 0.2s ease, background 0.2s ease;
}

.mot-classroom-card:hover {
  border-color: var(--mot-primary);
  transform: translateY(-2px);
}

.mot-classroom-card.active {
  border-color: var(--mot-primary);
  background: rgba(237, 111, 92, 0.1);
  color: var(--mot-primary);
}

.mot-classroom-result {
  margin-top: 2.5rem;
  min-height: 4em;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.mot-classroom-result.visible {
  opacity: 1;
  transform: translateY(0);
}

.mot-classroom-result-code {
  font-family: var(--mot-mono);
  font-size: 3em;
  font-weight: 700;
  color: var(--mot-primary);
  letter-spacing: 0.05em;
  margin: 0;
}

body.slides-mot .reveal section img.mot-esonero-img {
  display: block;
  margin: 1.2rem auto 0;
  background: none;
  border: none;
  box-shadow: none;
}

body.slides-mot .reveal section img.mot-quest-img {
  position: fixed;
  bottom: 0;
  right: 2%;
  width: 300px;
  max-width: 28%;
  margin: 0;
  background: none;
  border: none;
  box-shadow: none;
  pointer-events: none;
}
</style>
