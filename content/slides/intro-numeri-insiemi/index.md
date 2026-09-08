---
title: Il mondo dei numeri
summary: Aneddoti, storie e curiosità per cominciare l'anno
authors: [Diego Fantinelli]
tags: [organizzazione, prima-lezione, numeri]
categories: [lesson]
date: "2026-07-27T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: true
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
  <p class="mot-kicker">prima di cominciare</p>
  <h1>Il <em>mondo</em> dei <span class="math-word">numeri</span></h1>
  <p class="mot-tagline">storie, litigi e ossessioni di chi ha inventato ciò che diamo per scontato</p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">PERCHÉ CONTARE?</h1>
  <p class="mot-joke fragment">spoiler: c'entrano le pecore</p>
</section>

<section>
  <p class="mot-kicker">le origini</p>
  <h2>Tacche, dita e <em>pastori</em></h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">I primi numeri non erano scritti: erano ossa incise con delle tacche, una per ogni giorno, una per ogni pecora</li>
    <li class="fragment" style="margin-bottom:0;">L'osso di Ishango, in Congo, ha più di 20.000 anni ed è probabilmente il più antico "quaderno di matematica" del mondo</li>
  </ul>
  <p class="mot-joke fragment">nessuna interrogazione programmata, all'epoca: se sbagliavi il conto delle pecore, il problema se ne accorgeva da solo</p>
</section>

<section>
  <p class="mot-kicker">un indizio nel corpo</p>
  <h2>Perché contiamo a <em>dieci</em>?</h2>
  <p class="mot-def fragment">Il sistema decimale non è "naturale": è anatomico. Contiamo a dieci perché abbiamo dieci dita, non perché dieci sia un numero speciale.</p>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">I Babilonesi contavano in base 60, ed è per questo che un'ora ha 60 minuti</li>
    <li class="fragment" style="margin-bottom:0;">I Maya contavano in base 20 — probabilmente contando anche le dita dei piedi</li>
  </ul>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">LO ZERO</h1>
  <p class="mot-joke fragment">l'invenzione più pigra e più geniale della storia</p>
</section>

<section>
  <p class="mot-kicker">un numero per il "niente"</p>
  <h2>Il <em>nulla</em> che serviva a tutti</h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">I Romani non avevano uno zero: come si scrive "niente" con i numeri romani? Non si scrive, semplicemente non si scriveva nulla</li>
    <li class="fragment" style="margin-bottom:0;">Lo zero come numero vero e proprio — con cui si può anche fare calcolo — arriva dall'India, intorno al V secolo, e viaggia poi verso l'Europa passando per il mondo arabo</li>
  </ul>
  <p class="mot-joke fragment">ci sono voluti secoli per capire che "niente" meritasse un simbolo tutto suo</p>
</section>

<section>
  <p class="mot-kicker">perché ci serviva davvero</p>
  <h2>A cosa serve <em>lo zero</em></h2>
  <h3 class="fragment" style="font-size:0.65em; text-align:left;">Come <em>segnaposto</em></h3>
  <p class="fragment" style="text-align:left;">Distingue 1, 10 e 100: senza una cifra per lo zero, la posizione delle altre cifre diventa ambigua.</p>
  <h3 class="fragment" style="font-size:0.65em; text-align:left;">Come <em>numero</em></h3>
  <p class="fragment" style="text-align:left;">È l'elemento neutro dell'addizione (n + 0 = n): permette di fare calcoli, risolvere equazioni, definire i numeri negativi.</p>
  <p class="mot-joke fragment">non è solo "l'assenza di qualcosa" — è un numero che si comporta, a tutti gli effetti, come gli altri</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">NUMERI SOSPETTI</h1>
</section>

<section>
  <p class="mot-kicker">un debito è un numero?</p>
  <h2>I numeri <em>negativi</em>, rifiutati per secoli</h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Per molti matematici europei, fino al 1600 circa, i numeri negativi erano "numeri assurdi" o "falsi": come puoi avere meno di niente?</li>
    <li class="fragment" style="margin-bottom:0;">Eppure in Cina, già duemila anni fa, si usavano bastoncini di colore diverso per rappresentare i debiti: un'idea pratica, arrivata in Occidente con secoli di ritardo</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">una leggenda inquietante</p>
  <h2>Pitagora e i numeri <em>irrazionali</em></h2>
  <p class="mot-def fragment">La scuola pitagorica credeva che tutto nell'universo fosse spiegabile con rapporti di numeri interi. Poi qualcuno dimostrò che la diagonale di un quadrato non si può scrivere come frazione.</p>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">La leggenda narra che Ippaso di Metaponto, colpevole di questa scoperta scomoda, sia stato gettato in mare dai suoi stessi compagni</li>
    <li class="fragment" style="margin-bottom:0;">Vera o no, la storia racconta bene quanto un numero possa far paura</li>
  </ul>
  <p class="mot-joke fragment">morale: a volte un numero scomodo dà più fastidio di un errore</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">FIBONACCI</h1>
  <p class="mot-joke fragment">il matematico che ci ha "venduto" le cifre che usiamo ancora oggi</p>
</section>

<section>
  <p class="mot-kicker">un mercante in viaggio</p>
  <h2>Leonardo da Pisa, detto <em>Fibonacci</em></h2>
  <ul style="font-size:0.8em;">
    <li class="fragment" style="margin-bottom:0.5em;">Nel 1202 pubblica il <i>Liber Abaci</i>, dove convince l'Europa mercantile ad abbandonare i numeri romani per le cifre indo-arabiche — quelle che usiamo tuttora, 0-9</li>
    <li class="fragment" style="margin-bottom:0;">Come esempio "di scuola" nel suo libro compare anche il problema dei conigli che si riproducono: nasce così, quasi per caso, la sequenza che porta il suo nome</li>
  </ul>
  <dl class="mot-rows fragment">
    <dt>la sequenza</dt><dd>$1, 1, 2, 3, 5, 8, 13, 21, 34, \dots$</dd>
    <dt>la regola</dt><dd>ogni numero è la somma dei due precedenti</dd>
  </dl>
</section>

<section>
  <p class="mot-kicker">tre video, una sola storia</p>
  <h2>Guarda, prima di <em>leggere</em></h2>
  <p class="fragment">Qui sotto trovi tre video, brevi e diversi tra loro, sulla vita di Fibonacci e sulla sua sequenza. Guardali con calma, anche solo per curiosità.</p>
  <p class="mot-joke fragment">non c'è nulla da studiare, per una volta: solo da guardare</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">UN GIOCO DI NUMERI</h1>
</section>

<section>
  <p class="mot-kicker">un trucchetto da raccontare</p>
  <h2>Pensa un <em>numero</em></h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.15em;">Pensa un numero</li>
    <li class="fragment" style="margin-bottom:0.15em;">Raddoppialo</li>
    <li class="fragment" style="margin-bottom:0.15em;">Aggiungi 10</li>
    <li class="fragment" style="margin-bottom:0.15em;">Dividi per 2</li>
    <li class="fragment" style="margin-bottom:0;">Sottrai il numero di partenza</li>
  </ul>
  <p class="mot-def fragment fragment">Il risultato è sempre 5, qualunque numero tu abbia scelto — ed è un'algebra travestita da magia: chiamando $x$ il numero, l'espressione è $\dfrac{2x+10}{2} - x = 5$.</p>
  <p class="mot-joke fragment">il "mago" non ha nessun potere: ha solo scritto un'equazione al contrario</p>
</section>

<section>
  <p class="mot-kicker">divisione mentale, senza calcoli a memoria</p>
  <h2>Dividi come un <em>bambino</em></h2>
  <p style="font-size: 2.2em; text-align: center; margin: 0.6em 0;">91 &divide; 7 = <span class="mot-result">?</span></p>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Il riflesso di molti è chiedersi "quante volte il 7 sta nel 91?" — un conto che si fa a fatica a mente</li>
    <li class="fragment" style="margin-bottom:0;">Un bambino, spesso, farebbe di meglio</li>
  </ul>
</section>

<section>
  <p class="mot-kicker">passo per passo</p>
  <h2>Conti alla <em>mano</em></h2>
  <ul>
    <li class="fragment" style="margin-bottom:0.5em;">Spezziamo 91 in due pezzi più comodi da dividere per 7</li>
    <li class="fragment" style="margin-bottom:0.5em;">Primo tentativo: $91 = 80 + 11$. Ma né 80 né 11 sono multipli di 7 — vicolo cieco</li>
    <li class="fragment" style="margin-bottom:0;">Secondo tentativo: $91 = 70 + 21$. Questa volta sì: sono entrambi multipli di 7</li>
  </ul>
  <p class="mot-def fragment">$\dfrac{91}{7} = \dfrac{70+21}{7} = \dfrac{70}{7} + \dfrac{21}{7} = 10 + 3 = \mathbf{13}$</p>
  <p class="mot-joke fragment">non è un trucco: è la proprietà distributiva della divisione, travestita da furbizia</p>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">DOVE ANDIAMO</h1>
</section>

<section>
  <p class="mot-kicker">da qui in poi</p>
  <h2>Insiemi <em>numerici</em></h2>
  <p class="fragment">Da questa curiosità partiamo per un percorso più ordinato: naturali, interi, razionali, reali — le famiglie di numeri che useremo per tutto l'anno.</p>
  <p class="mot-joke fragment">niente più conigli, promesso. O quasi.</p>
</section>

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">buon inizio</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>
