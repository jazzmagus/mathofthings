---
title: "Il battito d'ali"
summary: "Storia (breve) di un'idea che ha rotto la fisica classica"
authors: [Diego Fantinelli]
tags: [caos, sistemi dinamici, storia della scienza]
categories: [conference]
date: "2026-07-27T00:00:00Z"
slides:
  theme: mathofthings
  transition: convex
  particles: false
  highlight_style: github
---

<section class="mot-hero" data-background-color="#2a2a3d" data-background-video="butterfly-home.mp4" data-background-video-loop data-background-video-muted data-background-opacity="0.32" data-transition="zoom">
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
  <div id="particles-ef-hero" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <p class="mot-kicker" style="color: white; position: relative; z-index: 10;">conferenza serale, 2027</p>
  <h1 style="color: white; position: relative; z-index: 10;">Il <span class="math-word" style="color: white; font-style: italic;">battito d'ali</span></h1>
  <p style="font-family: 'Playfair Display', serif; font-style: italic; color: rgba(255,255,255,0.95); font-size: 1.4em; position: relative; z-index: 10; margin-top: 0.5rem;">L'Effetto Farfalla e la Teoria del Caos</p>
  <p class="mot-tagline" style="font-family: 'JetBrains Mono', monospace; color: rgba(255,255,255,0.95); font-size: 1em; letter-spacing: 0.02em; position: relative; z-index: 10;">storia (breve) di un'idea che ha rotto la <em style="color: white;">fisica classica</em></p>
  <p class="mot-meta" style="color: rgba(255,255,255,0.9); position: relative; z-index: 10;">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<!-- ATTO I — Il sogno della predicibilità (~10') -->

<section class="mot-divider" data-background-color="#2a2a3d" data-transition="zoom" style="color: white;">
  <div id="particles-ef-atto1" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">ATTO I &mdash; IL SOGNO DELLA PREDICIBILITÀ</h1>
</section>

<section>
  <div id="particles-ef-content3" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <!-- SFONDO SUGGERITO: incisione d'epoca di Newton, o una cometa/orbita disegnata a mano -->
  <!-- data-background-image="newton.jpg" data-background-size="cover" data-background-position="center" data-background-opacity="0.15" -->
  <p class="mot-kicker">1687, l'universo diventa un orologio</p>
  <h2>Newton e la cometa <em>puntualissima</em></h2>
  <p class="mot-def fragment">Halley usa le leggi di Newton per calcolare l'orbita di una cometa avvistata nel 1682 e prevede: <b>tornerà a fine 1758</b>.</p>
  <p class="fragment mot-result" style="margin-top: 1.5rem;">Halley muore nel 1742. La cometa torna, puntuale, il 25 dicembre 1758. Da allora si chiama Cometa di Halley.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Un uomo prevede un appuntamento cosmico sedici anni prima, senza esserci: probabilmente il ghosting più elegante della storia della scienza.</p>
  <aside class="notes">
    <ol>
      <li>Halley applica la gravitazione di Newton ("Principia", 1687) e nota che le comete del 1531, 1607 e 1682 hanno orbite così simili da poter essere lo stesso oggetto.</li>
      <li>Ne predice il ritorno per la fine del 1758, tenendo conto delle perturbazioni di Giove e Saturno (calcolate poi con più precisione da Clairaut).</li>
      <li>Halley non vedrà la conferma: muore nel 1742.</li>
      <li>La cometa viene riavvistata il 25 dicembre 1758.</li>
    </ol>
    <ul>
      <li>È il primo trionfo pubblico della meccanica newtoniana applicata alla previsione.</li>
      <li>Da qui nasce l'idea (radicalizzata da Laplace) che conoscere le leggi fisiche equivalga a conoscere il futuro.</li>
      <li>Gancio per dopo: la logica che qui funziona benissimo, con Lorenz nell'Atto II si romperà.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content4" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <!-- SFONDO SUGGERITO: ritratto di Laplace (o incisione d'epoca), b/n, molto in trasparenza dietro il testo -->
  <!-- data-background-image="laplace.jpg" data-background-size="cover" data-background-position="center" data-background-opacity="0.15" -->
  <p class="mot-kicker">1814, un demone molto sicuro di sé</p>
  <h2>Se conosci <em>tutto</em>, prevedi tutto</h2>
  <p class="mot-def fragment">Laplace: dammi la posizione e la velocità <b>di ogni particella dell'universo</b>, e ti calcolo il futuro fino all'ultimo decimale &mdash; passato compreso.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Un'entità onnisciente e un po' pallosa: sa già come va a finire la partita di stasera.</p>
  <aside class="notes">
    <ul>
      <li>Apertura leggera: chiedere al pubblico "chi di voi ha già deciso cosa mangerà a cena domani sera? Ecco, Laplace lo sapeva anche per voi, nel 1814".</li>
      <li>Il "demone di Laplace" è un esperimento mentale, non un essere reale: un'intelligenza che conosce posizione e quantità di moto di ogni particella dell'universo in un istante.</li>
      <li>Con le leggi di Newton, per questa intelligenza "nulla sarebbe incerto, e l'avvenire, come il passato, sarebbe presente ai suoi occhi".</li>
      <li>È il manifesto del determinismo: universo = orologio, leggi = ingranaggi, tutto il resto è calcolo.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content5" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <!-- SFONDO SUGGERITO: mappa/atlante astronomico d'epoca con orbite disegnate, molto trasparente -->
  <!-- data-background-image="nettuno.jpg" data-background-size="cover" data-background-position="center" data-background-opacity="0.15" -->
  <p class="mot-kicker">1846, un pianeta trovato "a tavolino"</p>
  <h2>Il trionfo della <em>meccanica celeste</em></h2>
  <p class="mot-def fragment">Urano non si comporta come dovrebbe. Le Verrier non punta un telescopio: <b>fa i conti</b>, prevede dove deve esserci un pianeta ancora sconosciuto.</p>
  <p class="fragment mot-result" style="margin-top: 1.5rem;">Il telescopio di Berlino lo trova quella stessa notte, a meno di 1° dal punto previsto.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Nettuno scoperto con carta e penna: la fisica classica non aveva più bisogno di guardare il cielo, bastava saperlo prevedere.</p>
  <aside class="notes">
    <ul>
      <li>Apice del determinismo laplaciano: enfatizzarlo come un trionfo, prima del colpo di scena dell'Atto II.</li>
      <li>Le Verrier (e indipendentemente Adams) nota anomalie nell'orbita di Urano rispetto alle previsioni newtoniane.</li>
      <li>Ipotizza un pianeta sconosciuto la cui gravità le spiega e ne calcola posizione e massa.</li>
      <li>Galle, all'osservatorio di Berlino, punta il telescopio la sera del 23 settembre 1846 e lo trova quasi esattamente lì.</li>
      <li>Aneddoto, con orgoglio scientifico un po' guascone: "abbiamo scoperto un pianeta prima di vederlo".</li>
      <li>Prepara il contrasto con Lorenz nell'Atto II: un secolo dopo, lo stesso tipo di equazioni ci tradirà.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content6" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <!-- SFONDO SUGGERITO: ritratto di Poincaré, o una pagina di calcoli/manoscritto d'epoca -->
  <!-- data-background-image="poincare.jpg" data-background-size="cover" data-background-position="center" data-background-opacity="0.15" -->
  <p class="mot-kicker">1889, la prima crepa (e nessuno se ne accorge)</p>
  <h2>Poincaré e il <em>problema dei tre corpi</em></h2>
  <p class="mot-def fragment">Il re Oscar II di Svezia mette in palio un premio per chi risolve il moto di tre corpi celesti soggetti solo alla gravità reciproca (Sole, Terra, Luna, per dire).</p>
  <ul style="margin-top: 1.5rem;">
    <li class="fragment" style="margin-bottom:0.5em;">Poincaré vince</li>
    <li class="fragment" style="margin-bottom:0.5em;">Poi, mentre il suo saggio è già in stampa, si accorge di un errore: il sistema può essere <b>sensibilissimo</b> a variazioni minime</li>
    <li class="fragment" style="margin-bottom:0;">Deve farsi ristampare tutta la tiratura della rivista, a proprie spese</li>
  </ul>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Il caos entra ufficialmente nella storia della scienza costando a un matematico più della cifra del premio che aveva appena vinto.</p>
  <aside class="notes">
    <ol>
      <li>Il concorso per il 60° compleanno di Oscar II di Svezia (1889) chiedeva di dimostrare la stabilità del sistema solare risolvendo il problema dei tre corpi.</li>
      <li>Poincaré presenta un lavoro che vince il premio.</li>
      <li>Il revisore Phragmén nota un'incongruenza mentre il saggio è già in stampa su Acta Mathematica.</li>
      <li>Poincaré scava per correggere l'errore e scopre qualcosa di più profondo: anche con 3 sole masse e solo gravità (niente attrito, turbolenza o rumore), differenze minime nelle condizioni iniziali portano a evoluzioni completamente diverse.</li>
      <li>Paga di tasca propria la ristampa dell'intera tiratura già distribuita, con la versione corretta.</li>
    </ol>
    <ul>
      <li>Il lavoro contiene in nuce la teoria del caos, settant'anni prima di Lorenz.</li>
      <li>Resta un episodio isolato, sepolto in un trattato di meccanica celeste che quasi nessuno legge fino in fondo.</li>
      <li>Frase per creare suspense verso l'Atto II: "la crepa c'era già, semplicemente per settant'anni nessuno ci ha ripensato".</li>
    </ul>
  </aside>
</section>

---

<!-- ATTO II — Lorenz e la scoperta (~20') -->

<section class="mot-divider" data-background-color="#2a2a3d" data-transition="zoom" style="color: white;">
  <div id="particles-ef-atto2" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">ATTO II &mdash; LA SCOPERTA ACCIDENTALE</h1>
</section>

<section>
  <div id="particles-ef-content8" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <!-- SFONDO SUGGERITO: foto di Lorenz, o una vecchia stazione meteo/barometro -->
  <!-- data-background-image="lorenz-ritratto.jpg" data-background-size="cover" data-background-position="center" data-background-opacity="0.15" -->
  <p class="mot-kicker">un matematico prestato al meteo</p>
  <h2>Chi era Edward <em>Lorenz</em></h2>
  <p class="mot-def fragment">Matematico di formazione, durante la Seconda Guerra Mondiale fa il previsore meteo per l'aeronautica militare. Resta affascinato (e un po' deluso) da quanto sia difficile prevedere qualcosa di così quotidiano.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Passa il resto della carriera a costruire modelli matematici per capire perché i modelli matematici del meteo funzionano così male. Una specie di detective che indaga su se stesso.</p>
  <aside class="notes">
    <ul>
      <li>Edward Lorenz (1917-2008) si laurea in matematica ad Harvard.</li>
      <li>Durante la Seconda Guerra Mondiale è previsore meteorologico per le forze aeree americane, un lavoro allora più artigianale che scientifico.</li>
      <li>Ne ricava la sensazione che le previsioni, per quanto si affinino le tecniche, restino inaffidabili oltre pochi giorni: questo lo incuriosisce e dedica la carriera al MIT.</li>
      <li>Costruisce modelli semplificati dell'atmosfera (equazioni di convezione) per capire cosa renda il meteo così sfuggente.</li>
      <li>Contesto perfetto per l'aneddoto del 1961: non uno scienziato che inciampa per caso nel caos, ma qualcuno che lo stava quasi cercando, senza saperlo.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content9" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">1961, MIT, un pomeriggio noioso</p>
  <h2>Edward Lorenz e la <em>scorciatoia fatale</em></h2>
  <p class="mot-def fragment">Lorenz sta rifacendo una simulazione meteo già girata. Per risparmiare tempo digita <b>0.506</b> invece di <b>0.506127</b>: pensa che 3 decimali in meno non cambino nulla.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Va a farsi un caffè. Un'ora dopo torna e il "meteo" del suo computer è impazzito.</p>
  <aside class="notes">
    <ol>
      <li>La macchina è un Royal McBee LGP-30, lentissimo per gli standard odierni.</li>
      <li>Lorenz studia un modello semplificato di convezione atmosferica (12 equazioni).</li>
      <li>Vuole rivedere una sequenza già calcolata: invece di ripartire da capo, riparte "a metà", ridigitando a mano i valori intermedi stampati.</li>
      <li>La stampante arrotondava a 3 decimali (0.506), la memoria interna ne teneva 6 (0.506127).</li>
      <li>Lui pensa che una parte su mille sia irrilevante: meno di una folata di vento, o di uno starnuto, in un modello meteo reale.</li>
      <li>Torna dal caffè aspettandosi di rivedere la simulazione precedente.</li>
      <li>Dopo un breve tratto simile, le due curve divergono sempre di più, fino a non avere nulla in comune.</li>
    </ol>
    <ul>
      <li>Pausa comica: "e no, non aveva sbagliato lui i calcoli. Aveva scoperto il caos".</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content10" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <!-- SFONDO SUGGERITO: nessuno, qui probabilmente meglio uno screenshot/grafico live delle due curve che divergono -->
  <p class="mot-kicker">stesso punto di partenza, futuro diverso</p>
  <h2>La sensibilità alle <em>condizioni iniziali</em></h2>
  <p class="mot-def fragment">Due simulazioni, quasi identiche all'inizio (differenza: 1 su 10.000). Dopo poche settimane simulate, sono <b>completamente diverse</b>.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Non è un errore del computer. Non è nemmeno un errore di Lorenz. È una proprietà <em>delle equazioni stesse</em>.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">La prima vittima di questa scoperta è la fiducia di Lorenz nel demone di Laplace &mdash; e la seconda, qualche anno dopo, è quella di tutti i meteorologi del mondo.</p>
  <aside class="notes">
    <ul>
      <li>Concetto centrale della serata: scandirlo bene.</li>
      <li>La differenza tra le due traiettorie non resta piccola: cresce esponenzialmente nel tempo (base dell'"esponente di Lyapunov positivo").</li>
      <li>Il sistema resta perfettamente deterministico: stesse equazioni e stessi dati danno sempre lo stesso risultato.</li>
      <li>Il problema: "quasi identici" non è mai "identici", e in questi sistemi un errore minimo nella misura di partenza esplode.</li>
      <li>Frase che regge il resto della conferenza: "il caos non è assenza di leggi, è un eccesso di sensibilità alle leggi che già conosciamo".</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content11" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">1963-1972, il decennio del silenzio</p>
  <h2>Un articolo <em>ignorato</em> per dieci anni</h2>
  <p class="mot-def fragment">Lorenz pubblica i suoi risultati nel 1963 su una rivista di meteorologia, non di matematica o fisica. Quasi nessuno fuori dal suo campo se ne accorge.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Solo all'inizio degli anni '70 il matematico James Yorke lo scopre, ne intuisce la portata enorme e comincia a farlo circolare tra fisici e matematici. Sarà proprio Yorke, nel 1975, a usare per primo la parola "<b>chaos</b>" in questo contesto.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Una delle scoperte più importanti del Novecento ha passato un decennio scambiata per un articolo di meteorologia un po' noioso. Anche le rivoluzioni scientifiche, a volte, aspettano l'autobus giusto.</p>
  <aside class="notes">
    <ul>
      <li>Lorenz pubblica "Deterministic Nonperiodic Flow" nel 1963 sul Journal of the Atmospheric Sciences: rivista di meteorologia, letta da pochissimi fisici o matematici puri.</li>
      <li>Il lavoro contiene già gli ingredienti chiave (sensibilità alle condizioni iniziali, attrattore strano) ma resta invisibile alla comunità più ampia per circa un decennio.</li>
      <li>All'inizio degli anni '70 James Yorke (Università del Maryland) trova il paper, ne capisce l'importanza e lo fa conoscere a fisici e matematici.</li>
      <li>Questo contribuisce a innescare l'esplosione di interesse per il caos negli anni '70-'80.</li>
      <li>Nel 1975 Yorke e Tien-Yien Li pubblicano "Period Three Implies Chaos": per la prima volta "chaos" ha il significato tecnico moderno.</li>
      <li>Aneddoto di sociologia della scienza: le grandi scoperte non sempre vengono riconosciute subito, a volte serve la persona giusta che le trova nel posto sbagliato.</li>
    </ul>
  </aside>
</section>

<section data-background-video="butterfly.mp4" data-background-video-loop data-background-video-muted data-background-opacity="0.28">
  <div id="particles-ef-content12" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">1972, un titolo di conferenza da manuale di marketing</p>
  <h2>Nasce l'<em>effetto farfalla</em></h2>
  <p class="mot-def fragment">Lorenz tiene un intervento con un titolo che oggi definiremmo clickbait ante litteram:</p>
  <p class="fragment mot-result" style="margin-top: 1.5rem; font-size: 1.2em;">"Può il battito d'ali di una farfalla in Brasile scatenare un tornado in Texas?"</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Risposta onesta: probabilmente no, quella specifica farfalla. Ma il punto non è la farfalla, è che <b>qualcosa</b> di altrettanto piccolo, prima o poi, lo farà.</p>
  <aside class="notes">
    <ul>
      <li>Il titolo del talk del 1972 all'AAAS non è di Lorenz: pare lo abbia suggerito il moderatore, Philip Merilees, che non riuscì a farsi mandare un titolo in tempo e ne inventò uno.</li>
      <li>Ironia: la metafora più famosa della scienza del caos nasce, un po' caoticamente, da un titolo mancato all'ultimo minuto.</li>
      <li>Chiarire: non UNA farfalla che causa UN tornado (causalità isolabile e verificabile).</li>
      <li>Il senso: in un sistema caotico anche perturbazioni piccolissime, di qualunque origine, possono essere amplificate fino a conseguenze macroscopiche enormi.</li>
      <li>È un'affermazione sulla sensibilità del sistema, non sulla causalità puntuale.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content13" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <!-- SFONDO SUGGERITO: il grafico dell'attrattore di Lorenz (le due "ali"), reperibile libero da Wikimedia Commons, o generato al momento -->
  <!-- data-background-image="attrattore-lorenz.jpg" data-background-size="contain" data-background-position="center" data-background-opacity="0.35" -->
  <p class="mot-kicker">l'immagine icona del caos</p>
  <h2>L'<em>attrattore</em> di Lorenz</h2>
  <p class="mot-def fragment">Se disegni l'evoluzione del sistema nello spazio delle sue variabili, ottieni una forma che non si ripete mai due volte uguale &mdash; ma che assomiglia sempre a due ali di farfalla.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Persino il grafico ha deciso di essere in tema. A volte la matematica fa marketing da sola.</p>
  <aside class="notes">
    <ul>
      <li>L'attrattore di Lorenz nasce da 3 equazioni differenziali (versione ridotta del modello di convezione a 12 equazioni).</li>
      <li>Il sistema non si stabilizza in un punto fisso né in un ciclo periodico, ma nemmeno "esplode": resta confinato in una regione dello spazio.</li>
      <li>Le traiettorie non si intersecano mai e si avvolgono alternativamente attorno a due "centri": da qui la forma a farfalla (o a maschera).</li>
      <li>È il prototipo dell'"attrattore strano": deterministico, limitato, mai periodico, mai prevedibile a lungo termine.</li>
      <li>Momento ideale per una demo dal vivo (notebook Python o Desmos con l'equazione pronta), anche solo per far vedere la forma che si genera.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content14" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">un nome arrivato con due anni di ritardo</p>
  <h2>Chi ha battezzato l'<em>"attrattore strano"</em></h2>
  <p class="mot-def fragment">Il grafico esiste dal 1963. Il nome "strange attractor" (attrattore strano) arriva solo nel 1971, coniato dai fisici matematici David Ruelle e Floris Takens.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Otto anni per trovare un nome. In compenso, bisogna ammetterlo: "attrattore strano" resta uno dei nomi più azzeccati di tutta la fisica &mdash; suona bene anche a chi non ha capito nulla della matematica sotto.</p>
  <aside class="notes">
    <ul>
      <li>Ruelle e Takens introducono "strange attractor" in un articolo del 1971 sulla turbolenza nei fluidi.</li>
      <li>Significato tecnico: un attrattore (regione dello spazio delle fasi verso cui converge il sistema) con struttura frattale, su cui le traiettorie non sono mai periodiche.</li>
      <li>Recap, se il pubblico lo gradisce:<ul><li>attrattore "normale" = punto fisso o ciclo (un pendolo che si ferma, un'orbita periodica)</li><li>attrattore "strano" = il sistema resta confinato ma non si ripete mai esattamente, come in Lorenz.</li></ul></li>
      <li>Ironia meta: il nome nasce indipendentemente da Lorenz e viene applicato al suo grafico solo in seguito, un altro tassello della storia "caotica" di questa teoria.</li>
    </ul>
  </aside>
</section>

---

<!-- PAUSA 10' -->

<section class="mot-divider" data-background-color="#1a1a1a" data-background-video="timer.mp4" data-background-video-loop data-background-video-muted data-background-opacity="0.45" data-transition="fade" style="color: white;">
  <div id="particles-ef-content15" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <h1 class="r-fit-text">PAUSA &mdash; 10 MINUTI</h1>
</section>

---

<!-- ATTO III — Caos ≠ casualità (~35') — sfondo a particelle -->

<section class="mot-divider" data-background-color="#2a2a3d" data-transition="zoom" style="color: white;">
  <div id="particles-ef-atto3" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">ATTO III &mdash; IL CAOS NON È DISORDINE</h1>
</section>

<section>
  <div id="particles-ef-content17" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">mettiamo subito le cose in chiaro</p>
  <h2>Deterministico, ma <em>imprevedibile</em></h2>
  <p class="mot-def fragment">Sistema <b>caotico</b> ≠ sistema <b>casuale</b>. Le equazioni sono le stesse di sempre, obbediscono a leggi rigidissime, non lanciano mai un dado.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Il problema è un altro: per prevedere il futuro dovresti conoscere il presente con <em>precisione infinita</em>. E la precisione infinita, semplicemente, non esiste.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Non è che l'universo tiri a caso. È che l'universo, alla nona cifra decimale, non ce lo dice mai.</p>
  <aside class="notes">
    <ul>
      <li>Slide "manifesto" dell'Atto III: scandirla con calma, è il concetto più frainteso della teoria del caos.</li>
      <li>Nella cultura pop "effetto farfalla" viene confuso con "tutto è imprevedibile e casuale": è sbagliato.</li>
      <li>Ribadire: stesse condizioni iniziali esatte, stesso identico futuro, sempre.</li>
      <li>Il caos emerge SOLO perché non possiamo misurare le condizioni iniziali con infinite cifre decimali: ogni strumento ha precisione finita.</li>
      <li>In un sistema caotico quel margine di errore cresce esponenzialmente, fino a rendere impossibile la previsione a lungo termine, in linea di principio e non solo in pratica.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content18" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">quella domanda che fate sempre voi</p>
  <h2>"Ma tra 50 anni non avremo <em>computer</em> più potenti?"</h2>
  <p class="mot-def fragment">Certo. E allora potremo prevedere il tempo tra 11 giorni invece che 10. Poi tra 12. Poi la crescita si ferma comunque, perché il costo di ogni giorno in più aumenta <b>esponenzialmente</b>.</p>
  <p class="fragment mot-result" style="margin-top: 1.5rem;">Anche un computer grande quanto l'universo, con sensori perfetti, non saprebbe prevedere il meteo di un mese esatto.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Il colpevole non è l'ingegnere che ha progettato il supercomputer. È la matematica stessa, e con la matematica è inutile arrabbiarsi.</p>
  <aside class="notes">
    <ul>
      <li>Punto da difendere con fermezza: è l'obiezione che arriva sempre dal pubblico più tecnico.</li>
      <li>Il limite alla previsione meteo non è "computer troppo lenti" o "modelli imprecisi": è un limite di principio, legato alla crescita esponenziale degli errori.</li>
      <li>L'orizzonte di prevedibilità pratica dell'atmosfera è stimato intorno ai 10-14 giorni.</li>
      <li>Oltre quella soglia, anche raddoppiando calcolo o precisione dei sensori, si guadagnano pochi giorni, perché l'errore cresce esponenzialmente e non linearmente.</li>
      <li>Battuta finale: "i meteorologi non sbagliano perché sono pigri, sbagliano perché glielo abbiamo chiesto Lorenz".</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content19" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">la demo più semplice e più spettacolare di tutte</p>
  <h2>Il <em>pendolo doppio</em></h2>
  <img src="pendolo.png" alt="Schema tecnico del pendolo semplice e del pendolo doppio" style="max-width: 60%; margin: 0.3rem auto 0; display: block; border-radius: 4px; box-shadow: 0 2px 12px rgba(0,0,0,0.15);">
  <div class="fragment" style="margin-top: 0.6rem; text-align: center;">
    <p style="font-size: 0.55em; margin-bottom: 0;">$$\theta'' + \frac{g}{L}\sin\theta = 0$$</p>
    <p style="font-family: 'JetBrains Mono', monospace; font-size: 0.45em; color: #666; margin-top: -0.3rem;">(pendolo semplice)</p>
  </div>
  <div class="fragment" style="margin-top: 0.3rem; text-align: center; max-width: 100%; overflow-x: auto;">
    <p style="font-size: 0.42em; margin-bottom: 0; white-space: nowrap;">$$\ddot\theta_1 = \frac{-g(2m_1{+}m_2)\sin\theta_1 - m_2 g \sin(\theta_1{-}2\theta_2) - 2\sin(\theta_1{-}\theta_2)\, m_2(\dot\theta_2^2 L_2 + \dot\theta_1^2 L_1\cos(\theta_1{-}\theta_2))}{L_1(2m_1{+}m_2{-}m_2\cos(2\theta_1{-}2\theta_2))}$$</p>
    <p style="font-family: 'JetBrains Mono', monospace; font-size: 0.45em; color: #666; margin-top: -0.3rem;">(pendolo doppio)</p>
  </div>
  <aside class="notes">
    <ul>
      <li>Il confronto tra le due equazioni è il punto della slide: lasciarlo "parlare da solo".</li>
      <li>Aggiungendo una seconda massa si passa da un'equazione da liceo (pendolo semplice, θ'' + (g/L)sinθ = 0) a un sistema di equazioni accoppiate e fortemente non lineari, con termini incrociati tra masse e angoli.</li>
      <li>Non serve spiegarla termine per termine: l'effetto scenico è il salto di complessità a colpo d'occhio.</li>
      <li>Per chi vuole approfondire: si ricavano dal formalismo lagrangiano (L = energia cinetica - energia potenziale del sistema a due bracci).</li>
      <li>Pur essendo equazioni deterministiche esatte, il sistema è caotico per ampiezze non piccolissime.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content20" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">stessa fisica, due destini diversi</p>
  <h2>Guardateli <em>muoversi</em></h2>
  <video src="pendoli-animazione.mp4" autoplay loop muted playsinline style="max-width: 92%; margin: 0.3rem auto 0; display: block; border-radius: 6px; box-shadow: 0 2px 16px rgba(0,0,0,0.2);"></video>
  <aside class="notes">
    <ul>
      <li>Animazione fisica reale (motore a rigid body, non un disegno a mano).</li>
      <li>A sinistra il pendolo semplice oscilla in modo regolare e periodico, punto e basta.</li>
      <li>A destra il pendolo doppio, lanciato con angolo iniziale ampio, genera una traiettoria irregolare: la scia blu è il percorso della seconda massa e non si richiude mai.</li>
      <li>Far notare che la scia, da sola, assomiglia già a una farfalla: la matematica fa marketing per conto suo.</li>
      <li>Rilanciato con condizioni iniziali appena diverse, disegnerebbe ogni volta una scia diversa: stesso principio dell'attrattore di Lorenz, in un sistema meccanico invece che in un modello meteo.</li>
    </ul>
  </aside>
</section>

<section data-background-video="butterfly.mp4" data-background-video-loop data-background-video-muted data-background-opacity="0.15">
  <div id="particles-ef-content21" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">la demo più semplice e più spettacolare di tutte</p>
  <h2>Basta <em>una massa in più</em></h2>
  <p class="mot-def fragment">Attaccate un secondo pendolo in fondo al primo. Basta questo: un sistema meccanico semplicissimo, due sole masse, niente di esotico.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Fatelo partire due volte da posizioni quasi identiche (a occhio, indistinguibili). Dopo pochi secondi le due traiettorie non hanno più nulla in comune.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Un pendolo singolo è il simbolo della fisica prevedibile da tre secoli. Basta aggiungerne un secondo, letteralmente attaccato in fondo al primo, per costruirsi in casa un generatore di caos con due chiodi e dello spago.</p>
  <aside class="notes">
    <ul>
      <li>Il pendolo doppio è forse l'esempio più didattico e "dal vivo" di sistema caotico deterministico.</li>
      <li>Le equazioni sono complicate ma note e deterministiche (meccanica di Lagrange, slide precedente), eppure oltre pochi secondi il comportamento diventa imprevedibile e sensibilissimo alle condizioni di partenza.</li>
      <li>Se possibile, costruirne uno semplice (due aste rigide o due righelli imperniati) e fare una dimostrazione dal vivo.</li>
      <li>In alternativa, un video di due pendoli doppi lanciati da posizioni quasi identiche che divergono in pochi secondi.</li>
      <li>È la dimostrazione più "wow" per un pubblico non specialistico: meccanica classica pura, niente di esotico, eppure comportamento genuinamente impredicibile.</li>
      <li>Ponte visivo verso la mappa logistica, che è la stessa idea in versione puramente matematica.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content22" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">demo dal vivo (tenere pronto un notebook o un foglio di calcolo)</p>
  <h2>La <em>mappa logistica</em>: il caos in una riga</h2>
  <p class="mot-def fragment">Un modellino di popolazione animale, quasi ridicolo nella sua semplicità:</p>
  <p class="fragment mot-result" style="margin-top: 1rem; font-size: 1.3em;">$$x_{n+1} = r \, x_n (1 - x_n) \tag{1}$$</p>
  <p class="fragment" style="margin-top: 1.5rem;">Cambiate solo il numero <b>r</b>, un parametro innocuo. Per $r$ piccolo: popolazione stabile, noiosa, prevedibile. Aumentate $r$ un po' alla volta...</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">...e a un certo punto, senza preavviso, la stessa formuletta da terza superiore comincia a comportarsi come se avesse una vita propria e pessimo carattere.</p>
  <aside class="notes">
    <ul>
      <li>La mappa logistica (Robert May, anni '70) è l'esempio più semplice e potente da mostrare dal vivo: x è una popolazione normalizzata tra 0 e 1, r il tasso di crescita.</li>
    </ul>
    <ol>
      <li>Per r tra 0 e 3 il sistema converge a un valore fisso stabile.</li>
      <li>Attorno a r=3 iniziano le biforcazioni: la popolazione oscilla tra 2 valori, poi 4, poi 8, sempre più in fretta (cascata di biforcazioni di Feigenbaum).</li>
      <li>Oltre r≈3.57 il comportamento è caotico, pur restando un'equazione deterministica a una sola variabile, senza alcun elemento casuale.</li>
    </ol>
    <ul>
      <li>Se possibile, mostrare dal vivo il diagramma di biforcazione (r sull'asse x, valori asintotici di x sull'asse y): visivamente scioccante, simile a un frattale.</li>
      <li>Aneddoto opzionale su Feigenbaum: il "tasso" con cui le biforcazioni si infittiscono è una costante universale (≈4.669), la stessa in moltissimi sistemi caotici, una specie di "π del caos".</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content23" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">un numero che spunta ovunque, senza motivo apparente</p>
  <h2>La costante di <em>Feigenbaum</em></h2>
  <p class="mot-def fragment">Mitchell Feigenbaum, studiando la cascata di biforcazioni della mappa logistica, nota che ogni biforcazione arriva sempre più in fretta della precedente, secondo un rapporto fisso:</p>
  <p class="fragment mot-result" style="margin-top: 1rem; font-size: 1.3em;">$$\delta \approx 4.6692016...$$</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">La stessa identica costante spunta in centinaia di sistemi caotici completamente diversi tra loro &mdash; popolazioni, circuiti elettronici, gocce d'acqua. Come se il caos avesse una propria "impronta digitale universale", uguale per tutti.</p>
  <aside class="notes">
    <ul>
      <li>Alla fine degli anni '70 Feigenbaum studia la cascata di raddoppi di periodo che precede il caos nella mappa logistica (e in famiglie simili).</li>
      <li>Scopre che il rapporto tra le distanze successive dei punti di biforcazione tende a una costante universale, δ ≈ 4.6692016...</li>
      <li>Vale indipendentemente dai dettagli dell'equazione di partenza (purché abbia un massimo "a campana" simile).</li>
      <li>Risultato sorprendente: sistemi molto diversi mostrano la stessa costante nella transizione al caos:<ul><li>modelli di popolazione</li><li>circuiti elettrici non lineari</li><li>gocce da un rubinetto che gocciola sempre più in fretta</li><li>convezione in certi fluidi.</li></ul></li>
      <li>È l'equivalente, nel caos, di ciò che π è per i cerchi: un numero universale che emerge dalla struttura profonda del fenomeno, non dal sistema specifico.</li>
      <li>Aneddoto: Feigenbaum scoprì la regolarità con una delle prime calcolatrici tascabili, la HP-65, premendo tasti e osservando i numeri. Non un supercomputer, una calcolatrice da 200 dollari.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content24" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">il caos non vive solo nei laboratori</p>
  <h2>Biliardo, cuore, <em>popolazioni di conigli</em></h2>
  <p class="mot-def fragment">Al biliardo, dopo appena <b>9 urti</b>, per prevedere la traiettoria della palla dovresti già includere nel calcolo l'attrazione gravitazionale di una persona in piedi ai bordi del tavolo.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Il battito del vostro cuore, il numero di conigli in un prato, l'andamento di un'epidemia: stessa mappa logistica, stesso comportamento imprevedibile oltre una certa soglia.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">La prossima volta che perdete a biliardo, non è mancanza di talento. È fisica statistica del caos. Usatela, funziona sempre come scusa.</p>
  <aside class="notes">
    <ul>
      <li>Esempio del biliardo, di Michael Berry (fisico, Bristol): dopo circa 9 collisioni tra le sfere, per prevedere la traiettoria bisognerebbe tenere conto anche del campo gravitazionale di una persona ai bordi del tavolo.</li>
      <li>Un effetto minuscolo che di norma ignoreremmo sempre, ma che nel caos si amplifica abbastanza in fretta da diventare determinante.</li>
      <li>Aggancio ai sistemi biologici:<ul><li>variabilità del battito cardiaco (utile clinicamente: un battito "troppo regolare" è talvolta un segnale di rischio, controintuitivamente)</li><li>modelli preda-predatore (Lotka-Volterra, che in certe condizioni diventano caotici)</li><li>modelli epidemiologici SIR con parametri stagionali.</li></ul></li>
      <li>Messaggio di fondo: il caos non è un fenomeno raro di laboratorio, è probabilmente la norma per qualunque sistema con più di 2-3 variabili che interagiscono in modo non lineare.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content25" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <!-- SFONDO SUGGERITO: immagine del sistema solare/orbite planetarie, trasparente -->
  <p class="mot-kicker">torniamo da dove eravamo partiti, con una brutta notizia</p>
  <h2>Anche il <em>Sistema Solare</em> è caotico</h2>
  <p class="mot-def fragment">Ricordate Newton e Halley, l'apice della predicibilità nell'Atto I? Nel 1988-89 Gerald Sussman e Jack Wisdom, simulando il sistema solare per centinaia di milioni di anni, scoprono che anche le orbite dei pianeti sono <b>caotiche</b> su tempi lunghissimi.</p>
  <p class="fragment mot-result" style="margin-top: 1.5rem;">Non "instabili" nel senso che i pianeti voleranno via: ma la posizione precisa della Terra tra 100 milioni di anni è, in linea di principio, incalcolabile.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Il sistema più prevedibile della storia della fisica, quello con cui abbiamo aperto la serata, alla fine ci tradisce pure lui. Persino Newton, a lungo termine, gioca secondo le regole di Lorenz.</p>
  <aside class="notes">
    <ul>
      <li>Momento per "chiudere il cerchio" con l'Atto I.</li>
      <li>Sussman e Wisdom usano un computer specializzato (il "Digital Orrery" al MIT) per integrare le equazioni del moto planetario su centinaia di milioni di anni.</li>
      <li>Risultato: il moto dei pianeti, in particolare quelli interni (Mercurio, Venere, Terra, Marte), è caoticamente sensibile alle condizioni iniziali.</li>
      <li>Tempo di Lyapunov di circa 5 milioni di anni: l'incertezza sulla posizione raddoppia grosso modo ogni 5 milioni di anni.</li>
      <li>Non significa che il sistema solare sia instabile in senso catastrofico: i pianeti non stanno per schiantarsi.</li>
      <li>Significa che è impossibile, anche in linea di principio, calcolare la posizione esatta della Terra sulla sua orbita tra, diciamo, 200 milioni di anni.</li>
      <li>Piccole incertezze di oggi (corpi minori, asteroidi, effetti relativistici trascurabili) si amplificano fino a rendere la previsione priva di senso su quelle scale.</li>
      <li>Ironia perfetta da riportare al pubblico: il sistema che Newton, Halley e Laplace consideravano l'esempio supremo di prevedibilità è caotico quanto la mappa logistica o il pendolo doppio, solo su una scala temporale molto più lunga.</li>
    </ul>
  </aside>
</section>

<section data-background-video="fractals2.mp4" data-background-video-loop data-background-video-muted data-background-opacity="0.4">
  <div id="particles-ef-content26" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">la firma visiva del caos</p>
  <h2><em>Frattali</em>: infinito dentro il finito</h2>
  <p class="mot-def fragment">Il set di Mandelbrot: un'equazione di 7 caratteri, $z_{n+1} = z_n^2 + c$, generatrice di un contorno che, per quanto tu zoomi, <b>non smette mai</b> di rivelare nuovi dettagli.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Gli attrattori strani (come quello di Lorenz visto prima) sono frattali. Il confine tra "ordinato" e "caotico", in moltissimi sistemi, ha proprio questa struttura infinitamente dettagliata.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">È l'unico oggetto matematico che, più lo guardi da vicino, più ti fa sentire piccolo. Complimenti a $z_{n+1} = z_n^2 + c$, la formula più economica e più inquietante della matematica.</p>
  <aside class="notes">
    <ul>
      <li>Il set di Mandelbrot (Benoît Mandelbrot, 1980) nasce da un'iterazione semplicissima nel piano complesso.</li>
    </ul>
    <ol>
      <li>Si parte da z=0.</li>
      <li>Si applica ripetutamente z → z²+c.</li>
      <li>Si colora il punto c: nero se la sequenza resta limitata (appartiene al set), colorato secondo la velocità di divergenza se diverge (le sfumature dell'immagine di sfondo).</li>
    </ol>
    <ul>
      <li>Proprietà sorprendente: autosimilarità a tutte le scale. Zoomando sul bordo si trovano infinite repliche in miniatura della forma principale, mai identiche ma sempre riconoscibili.</li>
      <li>Collegamento con Lorenz (Atto II): anche l'attrattore è un frattale (dimensione non intera, circa 2.06), ed è questa struttura a far restare le traiettorie in una regione finita senza ripetersi mai.</li>
      <li>Se c'è tempo, gancio filosofico: i confini tra ordine e caos tendono ad avere questa granularità infinita. Coste, nuvole, vasi sanguigni, fulmini sono esempi di geometria frattale "naturale".</li>
    </ul>
  </aside>
</section>

---

<!-- ATTO IV — Perché ci riguarda (~25') -->

<section class="mot-divider" data-background-color="#2a2a3d" data-transition="zoom" style="color: white;">
  <div id="particles-ef-atto4" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">ATTO IV &mdash; PERCHÉ CI RIGUARDA</h1>
</section>

<section>
  <div id="particles-ef-content28" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">il caos, usato bene, è utilissimo</p>
  <h2>Crittografia: il disordine come <em>cassaforte</em></h2>
  <p class="mot-def fragment">I generatori di numeri "casuali" nei computer non sono davvero casuali (sono deterministici, come tutto ciò che gira su un chip): ma alcuni si basano proprio su mappe caotiche, perché ne imitano benissimo l'imprevedibilità pratica.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">La stessa proprietà che rovina le previsioni del tempo protegge il numero della vostra carta di credito. Il caos non sceglie mai da che parte stare.</p>
  <aside class="notes">
    <ul>
      <li>Distinguere numeri "veramente casuali" (fenomeni fisici quantistici o rumore termico) da numeri "pseudocasuali" generati da algoritmi deterministici.</li>
      <li>I pseudocasuali sono comunissimi in crittografia e simulazioni.</li>
      <li>Alcuni generatori sfruttano mappe caotiche (variazioni della mappa logistica o simili).</li>
      <li>Le sequenze sono calcolabili esattamente conoscendo il seed, ma praticamente indistinguibili dal rumore per chi non lo conosce.</li>
      <li>È lo stesso principio della sensibilità alle condizioni iniziali, usato "a fin di bene": rende la sequenza imprevedibile a un attaccante, come rende imprevedibile il meteo a un modello senza condizioni iniziali a precisione infinita.</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content29" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <!-- SFONDO SUGGERITO: fotogramma o locandina di Jurassic Park (attenzione al copyright: meglio un'immagine generica di dinosauro/goccia d'acqua se si vuole restare royalty-free) -->
  <p class="mot-kicker">quella scena con il bicchiere d'acqua</p>
  <h2>Il caos è arrivato anche a <em>Hollywood</em></h2>
  <p class="mot-def fragment">In Jurassic Park (1993) il matematico Ian Malcolm versa una goccia d'acqua sulla mano di una ragazza e le fa scommettere da che parte scivolerà. Sbaglia ogni volta: è proprio quello il punto.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Malcolm passa il film a ripetere che un parco di dinosauri ingegnerizzato "alla perfezione" è comunque un sistema complesso e non lineare: prima o poi qualcosa di piccolo e imprevisto lo farà collassare.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Aveva ragione lui, non gli ingegneri del parco. Morale della storia: se un matematico vi avverte che il vostro sistema è caotico, fategli dare retta prima che arrivi il T-Rex, non dopo.</p>
  <aside class="notes">
    <ul>
      <li>Ian Malcolm (Jeff Goldblum) in Jurassic Park è scritto esplicitamente come "esperto di teoria del caos".</li>
      <li>La scena della goccia d'acqua sulla mano di Ellie Sattler mostra in modo tattile la sensibilità alle condizioni iniziali: la stessa goccia, versata "nello stesso punto", scivola ogni volta in una direzione diversa per via di minuscole irregolarità della pelle.</li>
      <li>Ottimo aggancio pop per rendere concreto quanto detto finora. Battuta facile: "l'avevate già vista la teoria del caos, semplicemente non sapevate che si chiamasse così".</li>
      <li>Michael Crichton si documentò seriamente (anche con veri matematici): è una delle rappresentazioni più fedeli, per quanto romanzate, del concetto nella cultura di massa.</li>
      <li>Buon momento per alleggerire dopo le slide più tecniche (Feigenbaum, sistema solare).</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content30" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">stessa storia, posta più alta</p>
  <h2>Clima, mercati, <em>epidemie</em></h2>
  <p class="mot-def fragment">Modelli climatici, modelli finanziari, modelli epidemiologici: tutti sistemi non lineari con moltissime variabili che interagiscono. Tutti, in qualche misura, caotici.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Questo non significa "non sappiamo nulla". Significa che un buon modello dà <b>scenari e probabilità</b>, non certezze puntuali su singoli eventi lontani nel tempo.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Chi vi promette di sapere con certezza cosa farà la borsa tra sei mesi, o il clima tra trent'anni esatti al grado, o non ha capito il caos, o sta cercando di vendervi qualcosa.</p>
  <aside class="notes">
    <ul>
      <li>Distinzione da chiarire bene, per non passare né da negazionisti né da catastrofisti.</li>
      <li>Clima caotico NON significa modelli climatici inaffidabili in generale.</li>
      <li>Significa che sono inaffidabili nel predire il tempo di un singolo giorno lontano nel futuro.</li>
      <li>Restano affidabilissimi su tendenze statistiche e scenari probabilistici su scale ampie: non prevediamo il singolo lancio di una moneta, ma su un milione di lanci prevediamo circa il 50% testa.</li>
      <li>Stesso discorso per altri ambiti:<ul><li>economia: non il valore esatto di un titolo il 15 marzo del prossimo anno, ma rischi e scenari</li><li>epidemiologia: curve di contagio come scenari probabilistici, non profezie.</li></ul></li>
      <li>Messaggio filosofico centrale: il vero errore non è avere un modello imperfetto, è pretendere certezza dove il sistema, per sua natura matematica, non può darla.</li>
      <li>Chiudere ricollegando alla frase-chiave dell'Atto III: "il limite non è nostro, è delle equazioni. E sapere dove sta il limite è già una forma di conoscenza, non una sconfitta".</li>
    </ul>
  </aside>
</section>

<section>
  <div id="particles-ef-content31" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">l'ultima domanda, quella vera</p>
  <h2>Il caos ci rende più <em>liberi</em>, non meno</h2>
  <p class="mot-def fragment">Se Laplace avesse ragione, il futuro sarebbe già scritto fin dal Big Bang: ogni vostra scelta di stasera sarebbe solo l'ingranaggio di un orologio partito 14 miliardi di anni fa.</p>
  <p class="fragment" style="margin-top: 1.5rem;">Il caos non dimostra che esiste il libero arbitrio (resta un dibattito filosofico aperto), ma dimostra che il determinismo <b>non implica</b> la prevedibilità. Un universo di leggi rigide può comunque essere, nella pratica, radicalmente aperto.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Quindi la prossima volta che qualcuno vi dice "tanto è tutto già scritto", potete rispondere: "sì, forse, ma nemmeno l'autore sa come va a finire".</p>
  <aside class="notes">
    <ul>
      <li>Chiusura filosofica: tenerla leggera e non dogmatica.</li>
      <li>La teoria del caos non risolve il dibattito sul libero arbitrio (causalità, coscienza, responsabilità morale).</li>
      <li>Smonta però un'inferenza ingenua e comune: "se l'universo è deterministico, il futuro è calcolabile, quindi non c'è spazio per la libertà".</li>
      <li>Il caos mostra determinismo rigorosissimo (stesse leggi, sempre) insieme a imprevedibilità pratica assoluta e permanente, anche con conoscenza e potenza di calcolo arbitrariamente grandi.</li>
      <li>Non è il libero arbitrio in senso filosofico forte, ma è un'ottima base per una discussione aperta col pubblico.</li>
      <li>Modo elegante per ricollegare tutta la serata (da Laplace all'ultima slide) in un arco narrativo unico prima dei saluti.</li>
    </ul>
  </aside>
</section>

<section class="mot-divider" data-background-color="#2a2a3d" data-background-video="butterfly-home.mp4" data-background-video-loop data-background-video-muted data-background-opacity="0.32" data-transition="zoom" style="color: white;">
  <div id="particles-ef-grazie" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1;"></div>
  <h1 class="r-fit-text" style="position: relative; z-index: 10;">GRAZIE</h1>
  <p class="fragment" style="position: relative; z-index: 10; color: rgba(255,255,255,0.85); margin-top: 1rem;">(e scusate se non riesco a prevedere le vostre domande)</p>
  <aside class="notes">
    <ul>
      <li>Chiusura leggera, per stemperare la parte filosofica e tornare al tono ironico dell'inizio.</li>
      <li>Se c'è tempo per le domande, rilanciare la battuta: "fatemi pure domande difficili, tanto secondo Lorenz la mia risposta di oggi dipenderà in modo sensibile da quanto caffè ho bevuto stamattina".</li>
    </ul>
  </aside>
</section>

<style>
.reveal { --mot-primary: #ed6f5c; }
.reveal .mot-divider h1 { color: #ffffff !important; }
</style>

<script src="https://cdn.jsdelivr.net/npm/tsparticles@2.12.0/tsparticles.bundle.min.js"></script>
<script>
(function () {
  if (typeof tsParticles === 'undefined') return;

  function baseParticles(color) {
    return {
      number: { value: 55, density: { enable: true, area: 800 } },
      color: { value: color },
      opacity: { value: { min: 0.15, max: 0.5 } },
      size: { value: { min: 0.5, max: 3 } },
      links: { enable: false },
      move: {
        enable: true,
        speed: { min: 0.3, max: 1.8 },
        direction: 'none',
        random: true,
        straight: false,
        outModes: { default: 'out' }
      }
    };
  }

  // Sfondo scuro (hero, divisori d'atto, chiusura): particelle chiare.
  var darkBgConfig = {
    fpsLimit: 60,
    particles: baseParticles('#ffffff'),
    interactivity: { events: { onHover: { enable: false }, onClick: { enable: false } } },
    detectRetina: true
  };

  // Slide di contenuto, sfondo chiaro: particelle scure/coral, discrete.
  var lightBgConfig = {
    fpsLimit: 60,
    particles: baseParticles('#ed6f5c'),
    interactivity: { events: { onHover: { enable: false }, onClick: { enable: false } } },
    detectRetina: true
  };

  // Atto III (divisore, sfondo scuro): effetto "calamita", le particelle vengono attratte al passaggio del mouse.
  var magnetConfig = {
    fpsLimit: 60,
    particles: Object.assign({}, baseParticles('#ffffff'), {
      number: { value: 80, density: { enable: true, area: 800 } },
      links: { enable: true, distance: 140, color: '#ffffff', opacity: 0.25, width: 1 }
    }),
    interactivity: {
      events: {
        onHover: { enable: true, mode: 'attract' },
        onClick: { enable: true, mode: 'attract' },
        resize: true
      },
      modes: { attract: { distance: 220, duration: 0.4, factor: 3 } }
    },
    detectRetina: true
  };

  // Atto III (slide di contenuto, sfondo chiaro): stessa calamita, in coral.
  var magnetLightConfig = {
    fpsLimit: 60,
    particles: Object.assign({}, baseParticles('#ed6f5c'), {
      number: { value: 70, density: { enable: true, area: 800 } },
      links: { enable: true, distance: 140, color: '#ed6f5c', opacity: 0.25, width: 1 }
    }),
    interactivity: {
      events: {
        onHover: { enable: true, mode: 'attract' },
        onClick: { enable: true, mode: 'attract' },
        resize: true
      },
      modes: { attract: { distance: 220, duration: 0.4, factor: 3 } }
    },
    detectRetina: true
  };

  var darkIds = ['particles-ef-hero', 'particles-ef-atto1', 'particles-ef-atto2', 'particles-ef-atto4', 'particles-ef-grazie', 'particles-ef-content15'];
  var magnetIds = ['particles-ef-atto3'];
  var magnetLightIds = [
    'particles-ef-content17', 'particles-ef-content18', 'particles-ef-content19', 'particles-ef-content20',
    'particles-ef-content21', 'particles-ef-content22', 'particles-ef-content23', 'particles-ef-content24',
    'particles-ef-content25', 'particles-ef-content26'
  ];
  var lightIds = [
    'particles-ef-content3', 'particles-ef-content4', 'particles-ef-content5', 'particles-ef-content6',
    'particles-ef-content8', 'particles-ef-content9', 'particles-ef-content10', 'particles-ef-content11',
    'particles-ef-content12', 'particles-ef-content13', 'particles-ef-content14',
    'particles-ef-content28', 'particles-ef-content29', 'particles-ef-content30', 'particles-ef-content31'
  ];

  function loadAll(ids, config) {
    ids.forEach(function (id) {
      if (document.getElementById(id)) tsParticles.load(id, config);
    });
  }

  loadAll(darkIds, darkBgConfig);
  loadAll(magnetIds, magnetConfig);
  loadAll(magnetLightIds, magnetLightConfig);
  loadAll(lightIds, lightBgConfig);
})();
</script>
