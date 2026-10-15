---
title: Studiare (con l'IA)
summary: Metodo di studio, ieri e oggi, tra internet e intelligenza artificiale
authors: [Diego Fantinelli]
tags: [organizzazione, metodo-di-studio, AI]
categories: [lesson]
date: "2026-09-06T00:00:00Z"
draft: false
unlisted: true
slides:
  theme: mathofthings
  transition: convex
  particles: true
  particlesColorLight: "#2f8fbf"
  particlesColorDark: "#63c2e8"
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
  <p class="mot-kicker">metodo di studio</p>
  <h1>Studiare con<br>L'intelligenza<br><em>artificiale</em></h1>
  <p class="mot-tagline">breve storia di come si studia la matematica &mdash; da prima di internet a <em>oggi</em></p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
  <aside class="notes">
    <ul>
      <li>Presentarsi in una frase e dichiarare il tema: come si studia la matematica, e non solo, da prima di internet a oggi.</li>
      <li>Tono leggero, ma con dati veri: ogni affermazione importante ha una fonte.</li>
      <li>Anticipare il filo conduttore: non conta se usare l'IA, conta cosa se ne fa.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">in una frase</p>
  <h2 class="mot-bigline">L'IA non studia <em>al posto tuo</em>.</h2>
  <ul>
    <li class="fragment">ti fa guadagnare <em>tempo</em>, in una società che ha riempito di social ogni spiraglio libero della giornata</li>
    <li class="fragment">ma quel tempo vale zero se non lo <em>reinvesti nello studio</em></li>
  </ul>
  <p class="mot-joke fragment">gli strumenti te li dà lei; il lavoro, quello, resta tuo &mdash; ed è qui che si decide tutto</p>
  <aside class="notes">
    <ul>
      <li>Slide per catturare l'attenzione: è la sintesi di tutta la lezione, detta subito.</li>
      <li>L'IA non studia al posto tuo: questa è la frase da ricordare.</li>
      <li>Il vantaggio vero è il tempo guadagnato, in una società che ha riempito di social ogni spiraglio libero.</li>
      <li>Ma il tempo guadagnato non vale nulla se non lo reinvesti nello studio.</li>
      <li>Gli strumenti li fornisce l'IA, il lavoro resta tuo: è la discriminante di tutto.</li>
      <li>Il resto della lezione serve a mostrare come, con dati ed esempi.</li>
    </ul>
  </aside>
</section>


---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">PRIMA DI INTERNET</h1>
  <p class="mot-joke fragment">quando "cercare su Google" si chiamava "andare in biblioteca"</p>
  <aside class="notes">
    <ul>
      <li>Battuta: cercare su Google si chiamava andare in biblioteca.</li>
      <li>Chiedere chi ha mai preso un libro in prestito in biblioteca per studiare.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">il metodo di una volta</p>
  <h2>Come si studiava <em>prima</em></h2>
  <ul>
    <li class="fragment">sui libri di testo: la risposta era in quel libro, oppure da nessuna parte</li>
    <li class="fragment">in biblioteca: cercare voleva dire alzarsi, camminare, sfogliare, e a volte tornare il giorno dopo</li>
    <li class="fragment">con gli appunti: presi a mano durante la lezione, poi riletti e riordinati a casa</li>
    <li class="fragment">con gli appunti del compagno: si confrontavano i quaderni per colmare i buchi di quello che ci si era perso</li>
  </ul>
  <p class="mot-joke fragment" style="font-size:0.6em;"><strong style="font-family:var(--mot-mono);">l'effetto fatica:</strong> se non capivi, rileggevi, riprovavi, e prima o poi ci arrivavi</p>
  <aside class="notes">
    <ul>
      <li>Libri di testo, biblioteca, appunti a mano.</li>
      <li>Il confronto dei quaderni con un compagno: serviva a colmare i buchi.</li>
      <li>Fatica come parte del metodo: se non capivi, riprovavi.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">il lato nascosto</p>
  <h2>Lo sforzo faceva parte <em>del metodo</em></h2>
  <p class="fragment">Non era un metodo efficiente, e nessuno rimpiange davvero il libro in prestito che scade lunedì. Ma la fatica di cercare, riscrivere e confrontare non era solo tempo perso: era già, senza saperlo, allenamento.</p>
  <p class="mot-source fragment">Lo psicologo Robert Bjork le chiama "difficoltà desiderabili": ostacoli che rallentano l'apprendimento sul momento ma ne migliorano la tenuta nel tempo. E Slamecka &amp; Graf (1978) hanno mostrato il "generation effect": ciò che produci tu, anche solo ricostruendolo, lo ricordi meglio di ciò che ti viene dato già pronto.</p>
  <p class="mot-joke fragment">il punto non è tornare alle biblioteche, ma non buttare via lo sforzo insieme alla fatica</p>
  <aside class="notes">
    <ul>
      <li>Non rimpiangere il passato: nessuno rivuole il libro in prestito che scade lunedì.</li>
      <li>Bjork: difficoltà desiderabili, rallentano ora ma fissano meglio.</li>
      <li>Slamecka e Graf: ciò che produci tu lo ricordi meglio.</li>
      <li>Messaggio: non buttare via lo sforzo insieme alla fatica.</li>
    </ul>
  </aside>
</section>

---

<section>
  <p class="mot-kicker">il filo conduttore</p>
  <h2>Delegare o <em>studiare</em>?</h2>
  <p class="mot-def fragment">Il punto di questa lezione non è se usare l'IA, ma cosa fare del tempo e della fatica che ci fa risparmiare. Gli studi disponibili dicono due cose opposte, e dipendono entrambe da come la si usa.</p>
  <dl class="mot-rows mot-rows-narrow fragment">
    <dt>se le delego lo studio</dt><dd>"riassumi", "fammi lo schema", "prepara la presentazione": nel breve e nel medio periodo i risultati a scuola peggiorano</dd>
    <dt>se la uso per studiare</dt><dd>riassunto e schema sono il punto di partenza, poi il testo lo studio davvero, con carta e penna: i risultati migliorano</dd>
  </dl>
  <aside class="notes">
    <ul>
      <li>Questo è il filo conduttore di tutta la lezione.</li>
      <li>Due usi opposti: delegare lo studio oppure studiare con il suo aiuto.</li>
      <li>Delegare: riassumi, fammi lo schema, prepara la presentazione, e basta lì.</li>
      <li>Studiare: il riassunto è l'inizio, il testo poi lo studio davvero, meglio con carta e penna.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">lo studio</p>
  <h2>Cosa dicono <em>i dati</em></h2>
  <div class="fragment" style="width:96%;">
    <svg viewBox="0 0 900 330" role="img" aria-label="Tre gruppi di studenti confrontati in due momenti. Negli esercizi con l'IA: IA che risolve +48%, IA tutor +127% rispetto a chi non usa l'IA. In verifica senza IA: IA che risolve meno 17%, IA tutor circa zero." style="width:100%; max-height:50vh; display:block; margin:0 auto; font-family:Georgia,'Times New Roman',serif; font-variant-numeric:lining-nums; fill:currentColor;">
      <g opacity="0.05">
        <rect x="0" y="95" width="900" height="62"/>
        <rect x="0" y="219" width="900" height="62"/>
      </g>
      <g font-size="19" font-weight="bold">
        <text x="12" y="132" opacity="0.75">senza IA</text>
        <text x="12" y="194" fill="#d9644a">IA che risolve</text>
        <text x="12" y="256" fill="var(--mot-primary)">IA tutor</text>
      </g>
      <g font-size="13" font-style="italic" opacity="0.65">
        <text x="12" y="150">il gruppo di confronto</text>
        <text x="12" y="212">ti dà la soluzione</text>
        <text x="12" y="274">ti dà solo suggerimenti</text>
      </g>
      <g text-anchor="middle">
        <text x="450" y="26" font-size="19" font-weight="bold">negli esercizi</text>
        <text x="450" y="46" font-size="14" font-style="italic" opacity="0.65">con l'IA a disposizione</text>
      </g>
      <line x1="340" y1="68" x2="340" y2="288" stroke="currentColor" stroke-width="1.2" opacity="0.5"/>
      <rect x="340" y="112" width="3" height="28" opacity="0.5"/>
      <rect x="340" y="174" width="72" height="28" fill="#d9644a"/>
      <rect x="340" y="236" width="190" height="28" fill="var(--mot-primary)"/>
      <g font-size="19" font-weight="bold">
        <text x="354" y="133" font-weight="normal" opacity="0.65">0</text>
        <text x="424" y="195" fill="#d9644a">+48%</text>
        <text x="542" y="257" fill="var(--mot-primary)">+127%</text>
      </g>
      <text x="450" y="312" font-size="15" font-style="italic" text-anchor="middle" opacity="0.85">sembra che funzioni...</text>
      <g class="fragment">
        <g text-anchor="middle">
          <text x="770" y="26" font-size="19" font-weight="bold">in verifica</text>
          <text x="770" y="46" font-size="14" font-style="italic" opacity="0.65">senza l'IA</text>
        </g>
        <line x1="770" y1="68" x2="770" y2="288" stroke="currentColor" stroke-width="1.2" opacity="0.5"/>
        <rect x="768" y="112" width="3" height="28" opacity="0.5"/>
        <rect x="744" y="174" width="26" height="28" fill="#d9644a"/>
        <rect x="768" y="236" width="3" height="28" fill="var(--mot-primary)"/>
        <g font-size="19" font-weight="bold">
          <text x="784" y="133" font-weight="normal" opacity="0.65">0</text>
          <text x="734" y="195" fill="#d9644a" text-anchor="end">&#8722;17%</text>
          <text x="784" y="257" fill="var(--mot-primary)">&#8776; 0</text>
        </g>
        <text x="770" y="312" font-size="15" font-style="italic" text-anchor="middle" opacity="0.85">...ma da soli, alla prova, no</text>
      </g>
    </svg>
    <p style="font-size:0.4em; margin:0.2em 0 0; opacity:0.7; text-align:center; font-family:Georgia,serif;">variazione del punteggio rispetto a chi non usa l'IA (0 = stesso risultato)</p>
  </div>
  <p class="mot-source fragment">Bastani et al. (2024, pubblicato su PNAS): circa 1000 studenti di liceo, matematica. Con l'IA risolvono molti più esercizi, ma senza IA chi si è fatto risolvere i problemi va peggio di chi non l'ha mai usata. Gli studenti non se ne accorgono: credono di aver imparato quanto gli altri.</p>
  <aside class="notes">
    <ul>
      <li>Studio di Bastani et al., PNAS 2024: circa 1000 studenti di liceo, matematica.</li>
      <li>Negli esercizi con l'IA vanno molto meglio: +48% con chatbot che risolve, +127% con tutor.</li>
      <li>In verifica, senza IA: chi si è fatto risolvere i problemi va peggio (-17%), il tutor annulla il danno.</li>
      <li>Gli studenti non se ne accorgono: credono di aver imparato quanto gli altri.</li>
      <li>Il tutor non fa meglio del controllo in verifica, ma evita il danno.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">un'ipotesi, non un dato</p>
  <h2>Il contesto <em>è cambiato</em></h2>
  <p class="mot-def fragment">I numeri del grafico dicono che l'IA non migliora il risultato in verifica. Ma non dicono come starebbe oggi uno studente senza l'IA: il confronto è tra gruppi che studiano nelle stesse condizioni, non tra oggi e vent'anni fa.</p>
  <ul>
    <li class="fragment">molte più informazioni e notifiche da gestire ogni giorno, e più stress</li>
    <li class="fragment">meno tempo libero da dedicare allo studio</li>
    <li class="fragment">l'IA può restituire una parte di quel tempo, nel reperire e riassumere</li>
    <li class="fragment">ma il tempo guadagnato giova solo se lo dedico allo studio vero</li>
  </ul>
  <p class="mot-source fragment">Ipotesi di lavoro, non un risultato di ricerca: non abbiamo dati che misurino questo effetto. Va letta come una domanda aperta, utile a spiegare perché conta come si reinveste il tempo.</p>
  <aside class="notes">
    <ul>
      <li>Dichiarare subito che è un'ipotesi, non un dato.</li>
      <li>Più informazioni, più stress, meno tempo libero per studiare.</li>
      <li>L'IA può restituire tempo, ma il tempo giova solo se lo investo nello studio.</li>
      <li>Il grafico confronta gruppi nelle stesse condizioni, non oggi con vent'anni fa.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">come si usa bene</p>
  <h2>Il tempo risparmiato va <em>reinvestito</em></h2>
  <ol>
    <li class="fragment">chiedo all'IA di reperire, sintetizzare o riassumere: risparmio tempo e fatica</li>
    <li class="fragment">poi il testo lo studio davvero: lo rileggo, lo schematizzo, lo riscrivo con parole mie</li>
    <li class="fragment">meglio se con carta e penna, e senza l'IA davanti</li>
    <li class="fragment">infine mi verifico: rifaccio da solo, e se serve chiedo all'IA di interrogarmi</li>
  </ol>
  <p class="mot-source fragment">Lehmann, Cornelius &amp; Sting (2024): chi usa l'IA come tutor, chiedendo spiegazioni, ne trae vantaggio; chi se la fa risolvere gli esercizi impara meno, perché non investe il proprio sforzo mentale. Il copia-incolla triplica le richieste di soluzioni, senza aumentare quelle di spiegazioni.</p>
  <aside class="notes">
    <ul>
      <li>Ricetta in quattro passi: faccio riassumere, studio, scrivo a mano, mi verifico.</li>
      <li>Lehmann, Cornelius e Sting 2024: tutor giova, farsi risolvere gli esercizi danneggia.</li>
      <li>Il copia-incolla triplica le richieste di soluzioni, senza più richieste di spiegazioni.</li>
      <li>La parte su carta e penna si appoggia ai principi (generation effect), non a questi studi.</li>
    </ul>
  </aside>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">PRIMA DELL'IA</h1>
  <p class="mot-joke fragment">l'era di Wikipedia, YouTube e "fidati, l'ho letto da qualche parte"</p>
  <aside class="notes">
    <ul>
      <li>Battuta: l'era di Wikipedia, YouTube e fidati, l'ho letto da qualche parte.</li>
      <li>Passaggio intermedio, veloce: due slide.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">l'era della ricerca</p>
  <h2>Internet, ma senza <em>l'IA</em></h2>
  <ul>
    <li class="fragment">Google al posto della biblioteca: la risposta è a pochi secondi, non a pochi chilometri</li>
    <li class="fragment">Wikipedia al posto dell'enciclopedia: gratis, sempre aggiornata, a volte discutibile</li>
    <li class="fragment">YouTube e le videolezioni: la stessa spiegazione, rivista quante volte serve</li>
    <li class="fragment">forum e gruppi di studio online: "qualcuno l'ha già chiesto", e spesso qualcuno ha già risposto</li>
  </ul>
  <p class="fragment">Restava però un lavoro da fare: scegliere la fonte, leggerla, capire se era affidabile e rielaborarla con parole proprie.</p>
  <aside class="notes">
    <ul>
      <li>Google, Wikipedia, YouTube, forum: l'accesso diventa quasi gratuito.</li>
      <li>Restava un lavoro: scegliere la fonte, valutarla, rielaborarla.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">cosa cambia, e cosa no</p>
  <h2>Trovare è facile, <em>capire</em> no</h2>
  <p class="mot-def fragment">Con internet l'accesso all'informazione è diventato quasi gratuito. Ma sapere dove trovare una risposta non è la stessa cosa che averla capita, e la differenza è facile da non vedere.</p>
  <p class="mot-source fragment">Fisher, Goddu &amp; Keil (2015): chi cerca una spiegazione su internet tende a sovrastimare quanto sa da solo, come se la conoscenza trovata in rete fosse diventata propria. È la stessa "illusione di fluidità" di cui parla Bjork, con un motore di ricerca al posto di un buon insegnante.</p>
  <p class="mot-joke fragment">internet ha reso facile cercare; l'IA rende facile anche non cercare più</p>
  <aside class="notes">
    <ul>
      <li>Fisher, Goddu e Keil 2015: chi cerca online sovrastima quanto sa da solo (da verificare prima di citare).</li>
      <li>Trovare una risposta non significa averla capita.</li>
      <li>Battuta finale: internet ha reso facile cercare, l'IA rende facile non cercare più.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">spirito critico — 1</p>
  <h2>Sei frasi, <em>sei firme illustri</em></h2>
  <ol>
    <li class="fragment">«Chi può farti credere assurdità può farti commettere atrocità.» <strong>Voltaire</strong></li>
    <li class="fragment">«Più una società si allontana dalla verità, più odia chi la dice.» <strong>Orwell</strong></li>
    <li class="fragment">«Se il voto facesse la differenza, non ce lo farebbero fare.» <strong>Mark Twain</strong></li>
    <li class="fragment">«In un'epoca di inganno universale, dire la verità è un atto rivoluzionario.» <strong>Orwell</strong></li>
    <li class="fragment">«Quando l'ingiustizia diventa legge, la resistenza diventa un dovere.» <strong>Thomas Jefferson</strong></li>
    <li class="fragment">«La guerra è quando il tuo governo ti dice chi è il tuo nemico. La rivoluzione è quando lo capisci da solo.» <strong>Napoleone</strong></li>
  </ol>
  <p class="mot-source fragment">Così girano in rete, in un reel di questi giorni. Suonano bene, hanno un nome famoso sotto. Vi fidereste?</p>
  <aside class="notes">
    <ul>
      <li>Reel che sta girando ora: sei citazioni, sei nomi illustri.</li>
      <li>Leggerle una alla volta, lasciare che suonino convincenti.</li>
      <li>Chiedere alla classe: ci credereste? Chi controllerebbe?</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">spirito critico — 2</p>
  <h2>Le fonti <em>vere</em></h2>
  <dl class="mot-rows mot-rows-narrow fragment">
    <dt>1 &middot; Voltaire</dt><dd>parafrasi moderna. Nel 1765 scrisse che chi può renderti assurdo può renderti ingiusto: il senso è suo, le parole no</dd>
    <dt>2 &middot; Orwell</dt><dd>non è sua: scritta nel 2009 dal giornalista americano Selwyn Duke</dd>
    <dt>3 &middot; Twain</dt><dd>non è sua: il curatore degli archivi di Twain a Berkeley la esclude, circola dal 1976 come slogan anonimo</dd>
    <dt>4 &middot; Orwell</dt><dd>non è sua: in nessuna sua opera, compare dagli anni Ottanta come epigrafe senza fonte</dd>
    <dt>5 &middot; Jefferson</dt><dd>mai scritta, lo dice la fondazione di Monticello: gli viene attribuita solo dal 2006</dd>
    <dt>6 &middot; Napoleone</dt><dd>non risulta in nessuno dei suoi scritti</dd>
  </dl>
  <p class="mot-def fragment">Una frase giusta firmata da un nome sbagliato non diventa falsa, ma dovremmo saperlo. Prima di credere a sei righe con sei firme illustri, cerca la fonte.</p>
  <aside class="notes">
    <ul>
      <li>Una sola è una parafrasi di qualcosa di vero (Voltaire), le altre cinque non sono dei loro presunti autori.</li>
      <li>Ci fidiamo perché c'è un nome famoso sotto, e raramente controlliamo.</li>
      <li>Frase giusta con firma sbagliata: non è falsa, ma dobbiamo saperlo.</li>
      <li>Ponte con l'IA: stessa trappola, l'IA risponde con sicurezza e a volte inventa le fonti.</li>
      <li>Da verificare le singole attribuzioni prima di citarle in classe (dati dal reel).</li>
    </ul>
  </aside>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">OGGI</h1>
  <p class="mot-joke fragment">studiare con l'IA, senza farsi studiare dall'IA</p>
  <aside class="notes">
    <ul>
      <li>Battuta: studiare con l'IA senza farsi studiare dall'IA.</li>
      <li>Da qui entriamo nel cuore della lezione.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">contenuto da definire</p>
  <h2>Studiare oggi con <em>l'IA</em></h2>
  <p class="fragment">Un approfondimento:<br><a href="/post/chi-ha-paura-ia/" target="_blank" class="mono" style="display:inline-flex; align-items:center; gap:0.4em;">
    <svg width="0.9em" height="0.9em" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
    Chi ha paura dell'Intelligenza Artificiale?
  </a></p>
  <p class="mot-def fragment">L'intelligenza artificiale ha cambiato, e non poco, l'approccio allo studio: porta con sé dei benefici innegabili, ma anche qualche controindicazione precisa. Quello che segue non è il solito discorso da "ai miei tempi si studiava meglio" &mdash; pesiamo pro e contro appoggiandoci a quello che la psicologia cognitiva sa già da tempo su come si impara davvero.</p>
  <aside class="notes">
    <ul>
      <li>Non è il discorso "ai miei tempi si studiava meglio".</li>
      <li>Link al post "Chi ha paura dell'Intelligenza Artificiale?" per approfondire.</li>
      <li>Pesiamo pro e contro con ciò che la psicologia cognitiva sa già.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">i contro</p>
  <h2>Gli <em>svantaggi</em></h2>
  <dl class="mot-rows mot-rows-narrow fragment">
    <dt>illusione di comprensione</dt><dd>capire una spiegazione non significa saperla rifare da soli</dd>
    <dt>dipendenza dal procedimento altrui</dt><dd>se risolve l'IA, non sviluppi un tuo metodo</dd>
    <dt>errori detti con sicurezza</dt><dd>senza basi solide, non riconosci un passaggio sbagliato</dd>
    <dt>nessun controllo in tempo reale</dt><dd>in verifica, all'orale, alla lavagna, l'IA non c'è</dd>
    <dt>il tempo risparmiato si paga altrove</dt><dd>meno fatica ora, meno allenamento dopo</dd>
  </dl>
  <p class="mot-source fragment">Non è impressione: lo psicologo Robert Bjork (UCLA) la chiama "illusione di fluidità" &mdash; capire sembra facile solo perché qualcun altro l'ha spiegato bene. E Roediger &amp; Karpicke (2006) hanno mostrato che è il tentativo di ricordare, non la rilettura, a fissare davvero la conoscenza.</p>
  <aside class="notes">
    <ul>
      <li>Illusione di comprensione: capire una spiegazione non significa saperla rifare.</li>
      <li>Bjork: illusione di fluidità. Roediger e Karpicke 2006: ricordare attivamente batte rileggere.</li>
      <li>In verifica e all'orale l'IA non c'è.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">i pro</p>
  <h2>I <em>vantaggi</em></h2>
  <dl class="mot-rows mot-rows-narrow fragment">
    <dt>disponibilità immediata</dt><dd>il dubbio si risolve subito, non il giorno dopo</dd>
    <dt>spiegazioni su misura</dt><dd>puoi farti spiegare la stessa cosa in modi diversi finché non "clicca"</dd>
    <dt>esercizi illimitati</dt><dd>ne generi quanti ne vuoi, sul tuo livello esatto</dd>
    <dt>verifica dei propri passaggi</dt><dd>fai controllare un tuo ragionamento senza aspettare la correzione</dd>
    <dt>nessun giudizio sulla domanda "stupida"</dt><dd>puoi chiedere la cosa più elementare senza il filtro della classe</dd>
  </dl>
  <p class="mot-source fragment">Non è solo comodità: è quella che lo psicologo Lev Vygotskij chiamava "zona di sviluppo prossimale" &mdash; il ruolo di un buon aiuto è farti fare un passo che da solo non faresti ancora, ma che presto farai senza aiuto.</p>
  <aside class="notes">
    <ul>
      <li>Disponibilità immediata e spiegazioni su misura.</li>
      <li>Esercizi illimitati sul proprio livello.</li>
      <li>Nessun giudizio sulla domanda stupida.</li>
      <li>Vygotskij: zona di sviluppo prossimale, l'aiuto serve a fare un passo in più.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">il bilancio</p>
  <h2>Come cambia <em>(in meglio)</em> il metodo di studio</h2>
  <dl class="mot-rows mot-rows-narrow fragment">
    <dt>da cercare a dialogare</dt><dd>dalla ricerca passiva della risposta a una conversazione che guidi tu</dd>
    <dt>da leggere a verificare</dt><dd>il centro si sposta dal "leggere e ricordare" al "chiedere, verificare, rifare da solo"</dd>
    <dt>un allenatore, non un sostituto</dt><dd>allena quello che sai già fare, non ti regala quello che non sai fare</dd>
    <dt>il controllo tocca a te</dt><dd>un libro di testo non ti mente, un'IA a volte sì</dd>
    <dt>il tempo va reinvestito</dt><dd>meno tempo perso a cercare, più tempo vero a esercitarsi</dd>
  </dl>
  <aside class="notes">
    <ul>
      <li>Dal cercare al dialogare, dal leggere al verificare.</li>
      <li>L'IA è un allenatore, non un sostituto.</li>
      <li>Il controllo tocca a te: un libro non mente, un'IA a volte sì.</li>
    </ul>
  </aside>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text">L'ARTE DEL PROMPTING</h1>
  <p class="mot-joke fragment">perché "fammi il compito" non è un prompt, è una resa</p>
  <aside class="notes">
    <ul>
      <li>Battuta: fammi il compito non è un prompt, è una resa.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">il principio base</p>
  <h2>Garbage in, <em>garbage out</em></h2>
  <p class="mot-def fragment">Il risultato che ottieni dipende, quasi interamente, da come formuli la domanda: un prompt vago produce nella migliore delle ipotesi una risposta generica, nella peggiore una risposta sbagliata detta con sicurezza.</p>
  <p class="fragment">Studiare con l'IA è anche imparare a farle le domande giuste — non è un dettaglio tecnico, è la competenza vera.</p>
  <p class="mot-source fragment">Lo psicologo Michelene Chi ha chiamato "self-explanation effect" il fatto che spiegare a parole proprie un ragionamento &mdash; anche solo a un'IA &mdash; produce più apprendimento che limitarsi a leggere una spiegazione già pronta.</p>
  <aside class="notes">
    <ul>
      <li>Il risultato dipende da come formuli la domanda.</li>
      <li>Saper fare le domande giuste è la competenza vera.</li>
      <li>Chi: spiegare con parole proprie fa imparare più che leggere.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">come si scrive un buon prompt</p>
  <h2>Contesto e <em>specificità</em></h2>
  <dl class="mot-rows fragment">
    <dt>cosa</dt><dd>l'argomento esatto, non "aiutami con la matematica" — quale argomento, quale esercizio, quale passaggio</dd>
    <dt>livello</dt><dd>dì che classe fai e cosa hai già studiato: una spiegazione da terza superiore non serve in quinta, e viceversa</dd>
    <dt>formato</dt><dd>chiedi passaggi, non solo il risultato finale — è quello che dovrai saper rifare da solo</dd>
  </dl>
  <aside class="notes">
    <ul>
      <li>Tre ingredienti: cosa (argomento esatto), livello (che classe, cosa ho studiato), formato (passaggi, non solo risultato).</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">la trappola più comune</p>
  <h2>Il procedimento, non <em>la soluzione</em></h2>
  <p class="fragment">Chiedere direttamente "qual è il risultato" produce uno studente che sa copiare, non uno studente che sa risolvere.</p>
  <ul class="fragment">
    <li class="fragment">"spiegami perché si fa così, non solo come"</li>
    <li class="fragment">"fammi una domanda per verificare se ho capito"</li>
    <li class="fragment">"correggimi solo se sbaglio un passaggio, non anticipare la soluzione"</li>
  </ul>
  <p class="mot-source fragment">Non è una mia opinione: uno studio del 2024 su studenti liceali (Bastani et al., Università della Pennsylvania) ha misurato esattamente questa differenza &mdash; un chatbot che dà la soluzione pronta peggiora i risultati alle verifiche (&minus;17%), uno vincolato a fare da tutor, con suggerimenti invece di soluzioni, annulla il danno.</p>
  <aside class="notes">
    <ul>
      <li>Chiedere il risultato produce uno studente che sa copiare.</li>
      <li>Tre frasi utili: spiegami perché, fammi una domanda, correggimi solo se sbaglio.</li>
      <li>Bastani 2024: il tutor annulla il danno.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">esempio pratico — 1</p>
  <h2>Un'equazione, e non <em>solo</em></h2>
  <dl class="mot-rows fragment">
    <dt>prompt debole</dt><dd>"risolvimi questa equazione di secondo grado"</dd>
    <dt>prompt efficace</dt><dd>"sono in terza superiore e sto studiando le equazioni di secondo grado con la formula risolutiva: risolvi con me questo esercizio passo passo, spiegando ogni passaggio senza saltarne nessuno; poi proponimi altri due esercizi simili, e guidami passo passo nella soluzione di ciascuno, uno alla volta"</dd>
  </dl>
  <p class="mot-joke fragment">così, quando servono esercizi in più per fare pratica, non serve andarli a cercare: te li costruisci da solo</p>
  <aside class="notes">
    <ul>
      <li>Confrontare prompt debole e prompt efficace.</li>
      <li>Con il prompt efficace gli esercizi extra si generano da soli.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">esempio pratico — 2</p>
  <h2>Prima di <em>iniziare</em></h2>
  <p class="fragment">Un buon prompt non serve solo a risolvere un esercizio: può servire anche a organizzare il lavoro, prima ancora di iniziarlo.</p>
  <dl class="mot-rows fragment">
    <dt>prompt</dt><dd>"prima di affrontare questo problema, elencami quali conoscenze e abilità mi servono per risolverlo; poi fammi qualche domanda per verificare se le possiedo tutte"</dd>
  </dl>
  <p class="mot-joke fragment">scoprire di non avere un prerequisito prima di iniziare l'esercizio è utile — scoprirlo a metà, molto meno</p>
  <aside class="notes">
    <ul>
      <li>Usare il prompt anche per organizzare il lavoro.</li>
      <li>Scoprire un prerequisito mancante all'inizio, non a metà esercizio.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">esempio pratico &mdash; 3</p>
  <h2>NotebookLM: <em>farsi interrogare</em></h2>
  <dl class="mot-rows mot-rows-narrow fragment">
    <dt>carico le fonti</dt><dd>appunti, capitolo del libro, slide della lezione: risponde solo in base a quelle, con la citazione del passaggio</dd>
    <dt>mi faccio interrogare</dt><dd>"interrogami su questo capitolo, una domanda alla volta: aspetta la mia risposta, poi dimmi dove sbaglio citando il testo"</dd>
    <dt>mi faccio dare uno schema</dt><dd>mappa mentale, guida allo studio, flashcard e quiz generati dalle mie fonti</dd>
  </dl>
  <p class="mot-joke fragment">il riassunto che genera è il punto di partenza: lo studio vero comincia quando lo riscrivo a mano e lo rifaccio senza guardare</p>
  <aside class="notes">
    <ul>
      <li>Mostrare dal vivo, se possibile: caricare un capitolo e farsi interrogare.</li>
      <li>Risponde solo in base alle fonti caricate, con citazioni cliccabili.</li>
      <li>Funzioni utili: mappa mentale, guida allo studio, flashcard, quiz.</li>
      <li>Cautela: il riassunto audio o testuale non è studio, è materiale.</li>
    </ul>
  </aside>
</section>

<section>
  <p class="mot-kicker">esempio pratico &mdash; 4</p>
  <h2>Claude: <em>tutor di matematica</em></h2>
  <dl class="mot-rows fragment">
    <dt>prompt</dt><dd>"sono in quarta e sto studiando le disequazioni di secondo grado. Non darmi le soluzioni: proponimi un esercizio, aspetta la mia risposta e, se sbaglio, dammi solo un indizio sul passaggio. Dopo tre esercizi giusti, passa a uno più difficile"</dd>
    <dt>variante</dt><dd>"ho risolto questo esercizio (foto del mio svolgimento): dimmi in quale passaggio sbaglio, ma non correggerlo: voglio rifarlo io"</dd>
  </dl>
  <p class="mot-joke fragment">è il tutor "socratico" dello studio di Bastani: l'IA fa le domande, il lavoro lo fai tu</p>
  <aside class="notes">
    <ul>
      <li>Esempio per la matematica: tutor che non dà la soluzione.</li>
      <li>Chiedere un esercizio alla volta, indizi e non risposte.</li>
      <li>Variante: foto del proprio svolgimento, solo individuazione dell'errore.</li>
      <li>Ricollegare allo studio di Bastani: tutor socratico.</li>
    </ul>
  </aside>
</section>

---

<section class="mot-divider" data-transition="zoom" data-background-image="doubts.jpg" data-background-opacity="0.6">
  <h1 class="r-fit-text">DOMANDE?</h1>
  <p class="mot-joke fragment">le vostre domande fatele a me — quelle all'IA, scommetto, gliele avete già fatte</p>
  <aside class="notes">
    <ul>
      <li>Lasciare spazio alle domande.</li>
      <li>Chiudere con il messaggio: l'IA fa risparmiare tempo, ma il tempo va investito nello studio.</li>
    </ul>
  </aside>
</section>

---

<section class="mot-hero" data-transition="zoom">
  <p class="mot-kicker">buon anno scolastico</p>
  <h1>The <span class="math-word">Math</span> of <em>Things</em></h1>
  <p class="mot-meta"><a href="https://mathofthings.netlify.app/" target="_blank" class="mono">mathofthings.netlify.app</a></p>
</section>

<style>
body.slides-mot {
  --mot-primary: #2f8fbf;
  --r-link-color: #2f8fbf;
  --r-link-color-hover: #57abd6;
  --r-selection-background-color: rgba(47, 143, 191, 0.35);
}

body.slides-mot.dark {
  --mot-primary: #63c2e8;
  --r-link-color: #63c2e8;
  --r-link-color-hover: #8ad3ee;
}

body.slides-mot .reveal dl.mot-rows-narrow {
  grid-template-columns: 9em 1fr;
}

body.slides-mot .reveal dl.mot-rows-narrow dt {
  white-space: normal;
  line-height: 1.25;
}

.mot-bigline {
  font-size: 1.9em;
  line-height: 1.15;
  margin: 0.2em 0 0.5em;
}

body.slides-mot .reveal section > ul,
body.slides-mot .reveal section > ol {
  font-size: 0.78em;
  text-align: justify;
  hyphens: auto;
}

body.slides-mot .reveal section > ul li,
body.slides-mot .reveal section > ol li { margin-bottom: 0.15em; }

body.slides-mot .reveal section > ul li em { color: var(--mot-primary); font-weight: 700; }

body.slides-mot .reveal section h2 { font-size: 1.5em; }

body.slides-mot .reveal section:not(.mot-hero):not(.mot-divider) > p:not([class*="mot-"]):not(.mono) { font-size: 0.8em; }

body.slides-mot .reveal .mot-def { font-size: 0.7em; }

body.slides-mot .reveal dl.mot-rows { font-size: 0.64em; }

.mot-source {
  font-family: var(--mot-mono);
  font-size: 0.4em;
  color: var(--mot-muted);
  font-style: normal;
  line-height: 1.5;
  margin-top: 1em;
  max-width: 85%;
  text-align: left;
  border-left: 2px solid var(--mot-primary);
  padding-left: 0.8em;
}

</style>
