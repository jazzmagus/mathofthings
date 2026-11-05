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

<section id="lorenz-live">
  <div id="particles-ef-content13" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">l'immagine icona del caos</p>
  <h2>L'<em>attrattore</em> di Lorenz</h2>
  <canvas id="lorenz-canvas" style="display: block; width: 86%; margin: 0.2rem auto 0;"></canvas>
  <p class="mot-def fragment">Se disegni l'evoluzione del sistema nello spazio delle sue variabili, ottieni una forma che non si ripete mai due volte uguale &mdash; ma che assomiglia sempre a due ali di farfalla.</p>
  <p class="fragment mot-joke" style="margin-top: 1.5rem;">Persino il grafico ha deciso di essere in tema. A volte la matematica fa marketing da sola.</p>
  <aside class="notes">
    <ul>
      <li>L'attrattore di Lorenz nasce da 3 equazioni differenziali (versione ridotta del modello di convezione a 12 equazioni).</li>
      <li>Il sistema non si stabilizza in un punto fisso né in un ciclo periodico, ma nemmeno "esplode": resta confinato in una regione dello spazio.</li>
      <li>Le traiettorie non si intersecano mai e si avvolgono alternativamente attorno a due "centri": da qui la forma a farfalla (o a maschera).</li>
      <li>È il prototipo dell'"attrattore strano": deterministico, limitato, mai periodico, mai prevedibile a lungo termine.</li>
      <li>La figura è calcolata in diretta nella pagina (integrazione Runge-Kutta, parametri classici σ = 10, ρ = 28, β = 8/3) e ruota lentamente.</li>
      <li>Le due traiettorie partono con uno scarto di 0,001: restano sovrapposte per un po', poi si separano e finiscono sulle ali opposte. Stessa idea della slide sulla sensibilità alle condizioni iniziali, ora vista nello spazio delle fasi.</li>
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
  <p style="font-family: 'Playfair Display', serif; font-style: italic; color: rgba(255,255,255,0.95); font-size: 1.4em; position: relative; z-index: 10; margin-top: 0.5rem;">Il caso non è caos, il caos non è caso.</p>
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

<section id="pendoli-live">
  <div id="particles-ef-content20" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">stessa fisica, due destini diversi</p>
  <h2>Guardateli <em>muoversi</em></h2>
  <canvas id="pendoli-canvas" style="display: block; width: 86%; margin: 0.3rem auto 0;"></canvas>
  <p class="fragment" style="font-family: 'JetBrains Mono', monospace; font-size: 0.5em; text-align: center; margin-top: 0.3rem;">e se li lanciamo da due posizioni quasi identiche?</p>
  <aside class="notes">
    <ul>
      <li>Animazione fisica reale, calcolata in diretta nella pagina (integrazione Runge-Kutta), non un video: parte da sola ogni volta che si arriva sulla slide.</li>
      <li>Un click in più: compaiono due pendoli doppi lanciati con uno scarto di 0,001 rad. Per qualche secondo sono indistinguibili, poi si separano. Il contatore mostra la distanza tra le masse.</li>
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

<section id="bifurcazione-live">
  <div id="particles-ef-content32" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">per ogni r, dove va a finire la popolazione</p>
  <h2>Il diagramma di <em>biforcazione</em></h2>
  <canvas id="bifurcazione-canvas" style="display: block; width: 86%; margin: 0.2rem auto 0;"></canvas>
  <p class="fragment" style="font-family: 'JetBrains Mono', monospace; font-size: 0.5em; text-align: center; margin-top: 0.3rem;">zoomiamo in una piccola finestra dentro il caos</p>
  <aside class="notes">
    <ul>
      <li>Il diagramma si disegna da solo: per ogni valore di r si scartano i primi 700 passi e si riportano i valori che la popolazione continua a visitare.</li>
      <li>Fino a r=3 una sola linea (popolazione stabile), poi 2 valori, 4, 8... fino a r≈3.5699, dove comincia il caos.</li>
      <li>Nel caos non è tutto rumore: ci sono finestre di ordine (la più larga attorno a r≈3.83, con periodo 3).</li>
      <li>Click: zoom di circa 45 volte sulla finestra di periodo 3. Dentro si ritrova la stessa cascata di raddoppi vista prima, in miniatura: autosimilarità, cioè un frattale. Ponte verso la slide sui frattali.</li>
      <li>Il tutto è calcolato dal vivo nella pagina: la funzione è sempre x &rarr; r x (1 &minus; x).</li>
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

<section id="mandelbrot-live">
  <div id="particles-ef-content26" class="bg-particles" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none;"></div>
  <p class="mot-kicker">la firma visiva del caos</p>
  <h2><em>Frattali</em>: infinito dentro il finito</h2>
  <div style="display: flex; align-items: center; gap: 1.5rem; margin-top: 0.4rem;">
    <div style="flex: 1; text-align: left; font-size: 0.8em;">
      <p class="mot-def fragment">Il set di Mandelbrot: un'equazione di 7 caratteri, $z_{n+1} = z_n^2 + c$, generatrice di un contorno che, per quanto tu zoomi, <b>non smette mai</b> di rivelare nuovi dettagli.</p>
      <p class="fragment" style="margin-top: 1rem; font-size: 0.75em;">Gli attrattori strani (come quello di Lorenz visto prima) sono frattali. Il confine tra "ordinato" e "caotico", in moltissimi sistemi, ha proprio questa struttura infinitamente dettagliata.</p>
      <p class="fragment mot-joke" style="margin-top: 1rem;">È l'unico oggetto matematico che, più lo guardi da vicino, più ti fa sentire piccolo. Complimenti a $z_{n+1} = z_n^2 + c$, la formula più economica e più inquietante della matematica.</p>
    </div>
    <canvas id="mandelbrot-canvas" style="flex: none; width: 380px; height: 380px;"></canvas>
  </div>
  <aside class="notes">
    <ul>
      <li>Il set di Mandelbrot (Benoît Mandelbrot, 1980) nasce da un'iterazione semplicissima nel piano complesso.</li>
    </ul>
    <ol>
      <li>Si parte da z=0.</li>
      <li>Si applica ripetutamente z → z²+c.</li>
      <li>Si colora il punto c: nero se la sequenza resta limitata (appartiene al set), altrimenti si disegnano le curve di livello della velocità con cui diverge (le linee del disegno).</li>
    </ol>
    <ul>
      <li>L'immagine è calcolata dal vivo sulla scheda grafica e fa uno zoom continuo verso la "valle dei cavallucci marini" (circa 7000 volte), poi torna indietro. Più in là la precisione dei numeri a 32 bit non basta.</li>
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

<script>
(function () {
  var sec = document.getElementById('pendoli-live');
  var cv = document.getElementById('pendoli-canvas');
  if (!sec || !cv) return;

  var W = 1100, H = 560, G = 9.81, STEP = 1 / 240, TRAIL = 520, ARM = 150, R = 15;
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W * dpr;
  cv.height = H * dpr;
  var ctx = cv.getContext('2d');
  if (document.fonts) document.fonts.load('600 15px "JetBrains Mono"');

  function simpleD(s) { return [s[1], -G * Math.sin(s[0])]; }

  // Pendolo doppio, m1 = m2 = 1, L1 = L2 = 1.
  function doubleD(s) {
    var d = s[0] - s[2], c = Math.cos(d), sn = Math.sin(d);
    var den = 3 - Math.cos(2 * d);
    var a1 = (-3 * G * Math.sin(s[0]) - G * Math.sin(s[0] - 2 * s[2]) - 2 * sn * (s[3] * s[3] + s[1] * s[1] * c)) / den;
    var a2 = (2 * sn * (2 * s[1] * s[1] + 2 * G * Math.cos(s[0]) + s[3] * s[3] * c)) / den;
    return [s[1], a1, s[3], a2];
  }

  function rk4(f, s, h) {
    var n = s.length, i;
    function add(a, b, k) { var r = []; for (i = 0; i < n; i++) r.push(a[i] + b[i] * k); return r; }
    var k1 = f(s), k2 = f(add(s, k1, h / 2)), k3 = f(add(s, k2, h / 2)), k4 = f(add(s, k3, h));
    var out = [];
    for (i = 0; i < n; i++) out.push(s[i] + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]));
    return out;
  }

  function mk(simple, s, px, py, color, tint) {
    return { simple: simple, f: simple ? simpleD : doubleD, s: s, px: px, py: py, color: color, tint: tint, trail: [] };
  }

  function tips(p) {
    var x1 = p.px + ARM * Math.sin(p.s[0]), y1 = p.py + ARM * Math.cos(p.s[0]);
    if (p.simple) return [x1, y1];
    return [x1, y1, x1 + ARM * Math.sin(p.s[2]), y1 + ARM * Math.cos(p.s[2])];
  }

  var items = [], t = 0;

  function build(phase) {
    t = 0;
    ARM = phase === 0 ? 110 : 120;
    if (phase === 0) {
      items = [
        mk(true, [1.1, 0], 275, 240, 'ink', false),
        mk(false, [2.4, 0, 2.0, 0], 825, 240, 'coral', false)
      ];
    } else {
      items = [
        mk(false, [2.2, 0, 2.5, 0], 550, 260, 'ink', true),
        mk(false, [2.201, 0, 2.5, 0], 550, 260, 'coral', true)
      ];
    }
  }

  function palette() {
    var dark = document.body.classList.contains('dark');
    return { ink: dark ? '#d0d0d0' : '#1a1a1a', coral: dark ? '#f08e7c' : '#ed6f5c' };
  }

  function line(ax, ay, bx, by) {
    ctx.beginPath();
    ctx.moveTo(ax, ay);
    ctx.lineTo(bx, by);
    ctx.stroke();
  }

  function seg(ax, ay, bx, by, ra, rb) {
    var dx = bx - ax, dy = by - ay, l = Math.hypot(dx, dy), ux = dx / l, uy = dy / l;
    line(ax + ux * ra, ay + uy * ra, bx - ux * rb, by - uy * rb);
  }

  function mass(x, y, col) {
    ctx.strokeStyle = col;
    ctx.fillStyle = col;
    ctx.lineWidth = 1.8;
    ctx.beginPath();
    ctx.arc(x, y, R, 0, 2 * Math.PI);
    ctx.globalAlpha = 0.12;
    ctx.fill();
    ctx.globalAlpha = 1;
    ctx.stroke();
    ctx.lineWidth = 1;
    line(x - R * 0.45, y, x + R * 0.45, y);
    line(x, y - R * 0.45, x, y + R * 0.45);
  }

  function ceiling(px, py, P) {
    ctx.strokeStyle = P.ink;
    ctx.fillStyle = P.ink;
    ctx.lineWidth = 1.6;
    ctx.beginPath();
    ctx.arc(px, py, 8, 0, 2 * Math.PI);
    ctx.stroke();
    ctx.beginPath();
    ctx.arc(px, py, 3, 0, 2 * Math.PI);
    ctx.fill();
  }

  function plumb(px, py, P) {
    ctx.strokeStyle = P.ink;
    ctx.lineWidth = 1;
    ctx.globalAlpha = 0.45;
    ctx.setLineDash([6, 5]);
    line(px, py, px, py + ARM + 30);
    ctx.setLineDash([]);
    ctx.globalAlpha = 1;
  }

  function grid(P) {
    ctx.strokeStyle = P.ink;
    ctx.lineWidth = 1;
    ctx.globalAlpha = 0.07;
    for (var y = 20; y < H - 60; y += 80) line(20, y, W - 20, y);
    for (var x = 110; x < W - 20; x += 110) line(x, 20, x, H - 60);
    ctx.globalAlpha = 1;
  }

  function label(txt, x, y, size, col, align) {
    ctx.font = '600 ' + size + 'px "JetBrains Mono", monospace';
    if ('letterSpacing' in ctx) ctx.letterSpacing = '3px';
    ctx.fillStyle = col;
    ctx.textAlign = align || 'center';
    ctx.fillText(txt, x, y);
  }

  function drawItem(p, P) {
    var col = p.color === 'coral' ? P.coral : P.ink;
    var armCol = p.tint ? col : P.ink;
    var tr = p.trail, n = tr.length, i;
    ctx.lineCap = 'round';
    ctx.strokeStyle = col;
    ctx.lineWidth = 1.6;
    for (i = 1; i < n; i++) {
      ctx.globalAlpha = (i / n) * (p.color === 'coral' ? 0.85 : 0.5);
      line(tr[i - 1][0], tr[i - 1][1], tr[i][0], tr[i][1]);
    }
    ctx.globalAlpha = 1;
    var q = tips(p);
    ctx.strokeStyle = armCol;
    ctx.lineWidth = 1.6;
    if (p.simple) {
      seg(p.px, p.py, q[0], q[1], 0, R);
      mass(q[0], q[1], armCol);
    } else {
      seg(p.px, p.py, q[0], q[1], 0, R);
      seg(q[0], q[1], q[2], q[3], R, R);
      mass(q[0], q[1], armCol);
      mass(q[2], q[3], col);
    }
  }

  function drawAngle(p, P) {
    var th = p.s[0];
    ctx.strokeStyle = P.coral;
    ctx.lineWidth = 1.4;
    ctx.beginPath();
    ctx.arc(p.px, p.py, 46, Math.PI / 2, Math.PI / 2 - th, th > 0);
    ctx.stroke();
    var mid = Math.PI / 2 - th / 2;
    ctx.fillStyle = P.coral;
    ctx.font = 'italic 22px Georgia, serif';
    if ('letterSpacing' in ctx) ctx.letterSpacing = '0px';
    ctx.textAlign = 'center';
    ctx.fillText('θ', p.px + 66 * Math.cos(mid), p.py + 66 * Math.sin(mid) + 7);
  }

  function draw(phase) {
    var P = palette();
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    grid(P);
    var i;
    if (phase === 0) {
      ctx.strokeStyle = P.ink;
      ctx.lineWidth = 1;
      ctx.globalAlpha = 0.35;
      ctx.setLineDash([8, 6]);
      line(W / 2, 20, W / 2, H - 50);
      ctx.setLineDash([]);
      ctx.globalAlpha = 1;
      for (i = 0; i < items.length; i++) { ceiling(items[i].px, items[i].py, P); plumb(items[i].px, items[i].py, P); }
      drawAngle(items[0], P);
      for (i = 0; i < items.length; i++) drawItem(items[i], P);
      label('PENDOLO SEMPLICE', 275, H - 14, 15, P.ink);
      label('PENDOLO DOPPIO', 825, H - 14, 15, P.ink);
    } else {
      ceiling(550, 260, P);
      plumb(550, 260, P);
      for (i = 0; i < items.length; i++) drawItem(items[i], P);
      var a = tips(items[0]), b = tips(items[1]);
      var d = Math.hypot(a[2] - b[2], a[3] - b[3]) / ARM;
      if (d > 0.05) {
        ctx.strokeStyle = P.coral;
        ctx.lineWidth = 1;
        ctx.globalAlpha = 0.6;
        ctx.setLineDash([4, 4]);
        line(a[2], a[3], b[2], b[3]);
        ctx.setLineDash([]);
        ctx.globalAlpha = 1;
      }
      label('DUE PENDOLI DOPPI, SCARTO INIZIALE 0.001 rad', W / 2, H - 36, 15, P.ink);
      label('t = ' + t.toFixed(1) + ' s', W / 2 - 30, H - 10, 14, P.ink, 'right');
      label('distanza = ' + d.toFixed(2) + ' m', W / 2 + 30, H - 10, 14, P.coral, 'left');
    }
  }

  var phase = -1, last = 0, wasOn = false;

  function frame(now) {
    requestAnimationFrame(frame);
    if (!sec.classList.contains('present')) { wasOn = false; return; }
    var ph = sec.querySelector('.fragment.visible') ? 1 : 0;
    if (!wasOn || ph !== phase || (ph === 1 && t > 24)) {
      phase = ph;
      wasOn = true;
      last = now;
      build(ph);
    }
    var dt = Math.min((now - last) / 1000, 0.05);
    last = now;
    var n = Math.max(1, Math.ceil(dt / STEP)), h = dt / n, k;
    for (k = 0; k < n; k++) items.forEach(function (p) { p.s = rk4(p.f, p.s, h); });
    t += dt;
    items.forEach(function (p) {
      var q = tips(p);
      p.trail.push([q[q.length - 2], q[q.length - 1]]);
      if (p.trail.length > TRAIL) p.trail.shift();
    });
    draw(phase);
  }

  requestAnimationFrame(frame);
})();
</script>

<script>
(function () {
  var sec = document.getElementById('lorenz-live');
  var cv = document.getElementById('lorenz-canvas');
  if (!sec || !cv) return;

  var W = 1100, H = 420, SIGMA = 10, RHO = 28, BETA = 8 / 3, DT = 0.008, RATE = 1.5;
  var TRAIL = 2600, SC = 8, EL = 0.4, CX = 600, CY = 205, CHUNK = 40;
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W * dpr;
  cv.height = H * dpr;
  var ctx = cv.getContext('2d');
  if (document.fonts) document.fonts.load('600 15px "JetBrains Mono"');

  function lorenz(s) {
    return [SIGMA * (s[1] - s[0]), s[0] * (RHO - s[2]) - s[1], s[0] * s[1] - BETA * s[2]];
  }

  function rk4(f, s, h) {
    var n = s.length, i;
    function add(a, b, k) { var r = []; for (i = 0; i < n; i++) r.push(a[i] + b[i] * k); return r; }
    var k1 = f(s), k2 = f(add(s, k1, h / 2)), k3 = f(add(s, k2, h / 2)), k4 = f(add(s, k3, h));
    var out = [];
    for (i = 0; i < n; i++) out.push(s[i] + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]));
    return out;
  }

  var a, b, t = 0, phi = 0.6;

  function build() {
    var s = [1, 1, 1], i;
    for (i = 0; i < 2600; i++) s = rk4(lorenz, s, DT);
    a = { s: s, trail: [], ink: true };
    b = { s: [s[0] + 0.001, s[1], s[2]], trail: [], ink: false };
    t = 0;
  }

  function palette() {
    var dark = document.body.classList.contains('dark');
    return { ink: dark ? '#d0d0d0' : '#1a1a1a', coral: dark ? '#f08e7c' : '#ed6f5c' };
  }

  function project(p) {
    var c = Math.cos(phi), sn = Math.sin(phi);
    var X = p[0] * c + p[1] * sn, Y = -p[0] * sn + p[1] * c, Z = p[2] - 25;
    return [CX + X * SC, CY - (Z * Math.cos(EL) + Y * Math.sin(EL)) * SC];
  }

  function line(ax, ay, bx, by) {
    ctx.beginPath();
    ctx.moveTo(ax, ay);
    ctx.lineTo(bx, by);
    ctx.stroke();
  }

  function text(txt, x, y, size, col, align, spacing) {
    ctx.font = '600 ' + size + 'px "JetBrains Mono", monospace';
    if ('letterSpacing' in ctx) ctx.letterSpacing = spacing || '0px';
    ctx.fillStyle = col;
    ctx.textAlign = align;
    ctx.fillText(txt, x, y);
  }

  function drawTrail(o, col, alpha) {
    var tr = o.trail, n = tr.length, c, i, q;
    var pts = [];
    for (i = 0; i < n; i++) pts.push(project(tr[i]));
    ctx.strokeStyle = col;
    ctx.lineWidth = 1.3;
    ctx.lineJoin = 'round';
    var chunks = Math.ceil(n / CHUNK);
    for (c = 0; c < chunks; c++) {
      ctx.globalAlpha = alpha * Math.pow((c + 1) / chunks, 1.5);
      ctx.beginPath();
      i = Math.max(0, c * CHUNK - 1);
      ctx.moveTo(pts[i][0], pts[i][1]);
      for (i = i + 1; i < Math.min(n, (c + 1) * CHUNK); i++) ctx.lineTo(pts[i][0], pts[i][1]);
      ctx.stroke();
    }
    ctx.globalAlpha = 1;
    if (n) {
      q = pts[n - 1];
      ctx.strokeStyle = col;
      ctx.fillStyle = col;
      ctx.lineWidth = 1.6;
      ctx.beginPath();
      ctx.arc(q[0], q[1], 7, 0, 2 * Math.PI);
      ctx.globalAlpha = 0.15;
      ctx.fill();
      ctx.globalAlpha = 1;
      ctx.stroke();
    }
  }

  function draw() {
    var P = palette(), i;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    ctx.strokeStyle = P.ink;
    ctx.lineWidth = 1;
    ctx.globalAlpha = 0.07;
    for (i = 20; i < H - 20; i += 80) line(20, i, W - 20, i);
    for (i = 110; i < W - 20; i += 110) line(i, 20, i, H - 20);
    ctx.globalAlpha = 1;

    drawTrail(a, P.ink, 0.55);
    drawTrail(b, P.coral, 0.9);

    text('dx/dt = σ (y − x)', 40, 160, 17, P.ink, 'left');
    text('dy/dt = x (ρ − z) − y', 40, 190, 17, P.ink, 'left');
    text('dz/dt = x y − β z', 40, 220, 17, P.ink, 'left');
    ctx.globalAlpha = 0.6;
    text('σ = 10   ρ = 28   β = 8/3', 40, 255, 14, P.ink, 'left');
    ctx.globalAlpha = 1;

    var d = Math.hypot(a.s[0] - b.s[0], a.s[1] - b.s[1], a.s[2] - b.s[2]);
    text('DUE TRAIETTORIE, SCARTO 0.001', W - 40, 300, 14, P.ink, 'right', '2px');
    text('t = ' + t.toFixed(1), W - 40, 330, 14, P.ink, 'right');
    text('distanza = ' + d.toFixed(2), W - 40, 355, 14, P.coral, 'right');
  }

  var wasOn = false, last = 0;

  function frame(now) {
    requestAnimationFrame(frame);
    if (!sec.classList.contains('present')) { wasOn = false; return; }
    if (!wasOn || t > 40) {
      wasOn = true;
      last = now;
      build();
    }
    var dt = Math.min((now - last) / 1000, 0.05);
    last = now;
    phi += 0.12 * dt;
    var n = Math.max(1, Math.round(RATE * dt / DT)), k;
    for (k = 0; k < n; k++) {
      a.s = rk4(lorenz, a.s, DT);
      b.s = rk4(lorenz, b.s, DT);
      a.trail.push(a.s);
      b.trail.push(b.s);
      if (a.trail.length > TRAIL) { a.trail.shift(); b.trail.shift(); }
    }
    t += n * DT;
    draw();
  }

  requestAnimationFrame(frame);
})();
</script>

<script>
(function () {
  var sec = document.getElementById('bifurcazione-live');
  var cv = document.getElementById('bifurcazione-canvas');
  if (!sec || !cv) return;

  var W = 1100, H = 470, PX = 80, PY = 24, PW = 960, PH = 350;
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = W * dpr;
  cv.height = H * dpr;
  var ctx = cv.getContext('2d');
  if (document.fonts) document.fonts.load('600 14px "JetBrains Mono"');

  var BW = Math.round(PW * dpr), BH = Math.round(PH * dpr);
  var off = document.createElement('canvas');
  off.width = BW;
  off.height = BH;
  var octx = off.getContext('2d');
  var img = octx.createImageData(BW, BH);

  var FULL = { r0: 2.5, r1: 4, x0: 0, x1: 1 };
  var ZOOM = { r0: 3.826, r1: 3.858, x0: 0.43, x1: 0.56 };
  var RINF = 3.5699, TR = 700, NP = 220, SWEEP = 8, ZOOM_T = 11;

  var view = FULL, done = 0, mode = 'sweep', sweepT = 0, u = 0, wasOn = false, last = 0, lastKey = '';
  var ink, coral;

  function hexRgb(h) { return [parseInt(h.substr(1, 2), 16), parseInt(h.substr(3, 2), 16), parseInt(h.substr(5, 2), 16)]; }

  function palette() {
    var dark = document.body.classList.contains('dark');
    return { key: dark ? 'd' : 'l', ink: dark ? '#d0d0d0' : '#1a1a1a', coral: dark ? '#f08e7c' : '#ed6f5c' };
  }

  function compute(v, c0, c1) {
    var d = img.data, rs = (v.r1 - v.r0) / BW, xs = BH / (v.x1 - v.x0), c, i, r, x, y, k, col;
    for (c = c0; c < c1; c++) {
      r = v.r0 + (c + 0.5) * rs;
      col = r > RINF ? coral : ink;
      x = 0.5;
      for (i = 0; i < TR; i++) x = r * x * (1 - x);
      for (i = 0; i < NP; i++) {
        x = r * x * (1 - x);
        y = ((v.x1 - x) * xs) | 0;
        if (y >= 0 && y < BH) {
          k = (y * BW + c) * 4;
          d[k] = col[0];
          d[k + 1] = col[1];
          d[k + 2] = col[2];
          d[k + 3] = Math.min(255, d[k + 3] + 90);
        }
      }
    }
  }

  function redo(v, upto) {
    img.data.fill(0);
    compute(v, 0, upto);
  }

  function interp(e) {
    var sa = [FULL.r1 - FULL.r0, FULL.x1 - FULL.x0], sb = [ZOOM.r1 - ZOOM.r0, ZOOM.x1 - ZOOM.x0];
    var ca = [(FULL.r0 + FULL.r1) / 2, (FULL.x0 + FULL.x1) / 2], cb = [(ZOOM.r0 + ZOOM.r1) / 2, (ZOOM.x0 + ZOOM.x1) / 2];
    var out = [], i, span, v;
    for (i = 0; i < 2; i++) {
      span = Math.exp(Math.log(sa[i]) + (Math.log(sb[i]) - Math.log(sa[i])) * e);
      v = (sa[i] - span) / (sa[i] - sb[i]);
      out.push([ca[i] + (cb[i] - ca[i]) * v - span / 2, ca[i] + (cb[i] - ca[i]) * v + span / 2]);
    }
    return { r0: out[0][0], r1: out[0][1], x0: out[1][0], x1: out[1][1] };
  }

  function line(ax, ay, bx, by) {
    ctx.beginPath();
    ctx.moveTo(ax, ay);
    ctx.lineTo(bx, by);
    ctx.stroke();
  }

  function text(txt, x, y, size, col, align, spacing) {
    ctx.font = '600 ' + size + 'px "JetBrains Mono", monospace';
    if ('letterSpacing' in ctx) ctx.letterSpacing = spacing || '0px';
    ctx.fillStyle = col;
    ctx.textAlign = align;
    ctx.fillText(txt, x, y);
  }

  function rx(r) { return PX + (r - view.r0) / (view.r1 - view.r0) * PW; }

  function draw(P, e) {
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, W, H);
    octx.putImageData(img, 0, 0);
    ctx.drawImage(off, 0, 0, BW, BH, PX, PY, PW, PH);

    ctx.strokeStyle = P.ink;
    ctx.lineWidth = 1;
    ctx.globalAlpha = 0.6;
    line(PX, PY, PX, PY + PH);
    line(PX, PY + PH, PX + PW, PY + PH);
    var span = view.r1 - view.r0, mag = Math.pow(10, Math.floor(Math.log(span / 4) / Math.LN10)), step = mag, m;
    var cand = [1, 2, 5, 10];
    for (m = 0; m < cand.length; m++) { step = cand[m] * mag; if (span / step <= 6) break; }
    var dec = Math.max(0, -Math.floor(Math.log(step) / Math.LN10 + 1e-9));
    var r, px;
    for (r = Math.ceil(view.r0 / step - 1e-9) * step; r <= view.r1 + 1e-9; r += step) {
      px = rx(r);
      line(px, PY + PH, px, PY + PH + 6);
      ctx.globalAlpha = 1;
      text(r.toFixed(dec), px, PY + PH + 26, 13, P.ink, 'center');
      ctx.globalAlpha = 0.6;
    }
    ctx.globalAlpha = 1;
    text('r', PX + PW + 4, PY + PH + 5, 14, P.coral, 'left');
    text('x', PX - 10, PY + 10, 14, P.coral, 'right');
    text(view.x1.toFixed(2), PX - 10, PY + 28, 12, P.ink, 'right');
    text(view.x0.toFixed(2), PX - 10, PY + PH, 12, P.ink, 'right');

    if (mode === 'sweep' || mode === 'hold') {
      var front = FULL.r0 + done / BW * (FULL.r1 - FULL.r0);
      var marks = [[3, '2 VALORI'], [3.4495, '4'], [RINF, 'CAOS']], i;
      ctx.lineWidth = 1;
      for (i = 0; i < marks.length; i++) {
        if (marks[i][0] > front) continue;
        px = rx(marks[i][0]);
        ctx.strokeStyle = P.ink;
        ctx.globalAlpha = 0.35;
        ctx.setLineDash([6, 5]);
        line(px, PY + 18, px, PY + PH);
        ctx.setLineDash([]);
        ctx.globalAlpha = 1;
        text(marks[i][1], px, PY + 12, 13, P.ink, 'center', '2px');
      }
      if (mode === 'sweep') {
        px = rx(front);
        ctx.strokeStyle = P.coral;
        ctx.globalAlpha = 0.8;
        line(px, PY, px, PY + PH);
        ctx.globalAlpha = 1;
        text('r = ' + front.toFixed(3), PX + PW - 4, PY + PH - 10, 14, P.coral, 'right');
      }
    } else {
      text('INGRANDIMENTO ×' + Math.round((FULL.r1 - FULL.r0) / span), PX + PW - 4, PY + 14, 14, P.coral, 'right', '2px');
    }
  }

  function setPalette(P) {
    ink = hexRgb(P.ink);
    coral = hexRgb(P.coral);
  }

  function frame(now) {
    requestAnimationFrame(frame);
    if (!sec.classList.contains('present')) { wasOn = false; return; }
    var P = palette(), ph = sec.querySelector('.fragment.visible') ? 1 : 0, e = 0, target;
    if (!wasOn) {
      wasOn = true;
      last = now;
      lastKey = P.key;
      setPalette(P);
      view = FULL;
      done = 0;
      mode = 'sweep';
      sweepT = 0;
      u = 0;
      img.data.fill(0);
    }
    var dt = Math.min((now - last) / 1000, 0.05);
    last = now;

    if (P.key !== lastKey) {
      lastKey = P.key;
      setPalette(P);
      if (mode === 'sweep' || mode === 'hold') redo(FULL, done);
    }

    if (mode === 'sweep') {
      if (ph === 1) {
        compute(FULL, done, BW);
        done = BW;
        mode = 'zoom';
        u = 0;
      } else {
        sweepT += dt;
        target = Math.min(BW, Math.floor(sweepT / SWEEP * BW));
        compute(FULL, done, target);
        done = target;
        if (done >= BW) mode = 'hold';
      }
    } else if (mode === 'hold') {
      if (ph === 1) { mode = 'zoom'; u = 0; }
    } else if ((mode === 'zoom' || mode === 'zoomed') && ph === 0) {
      view = FULL;
      mode = 'hold';
      done = BW;
      redo(FULL, BW);
    }

    if (mode === 'zoom') {
      u = Math.min(1, u + dt / ZOOM_T);
      e = u * u * (3 - 2 * u);
      view = interp(e);
      redo(view, BW);
      if (u >= 1) mode = 'zoomed';
    } else if (mode === 'zoomed') {
      e = 1;
    }
    draw(P, e);
  }

  requestAnimationFrame(frame);
})();
</script>

<script>
(function () {
  var sec = document.getElementById('mandelbrot-live');
  var cv = document.getElementById('mandelbrot-canvas');
  if (!sec || !cv) return;

  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  cv.width = Math.round(380 * dpr);
  cv.height = Math.round(380 * dpr);
  var gl = cv.getContext('webgl2', { alpha: true, premultipliedAlpha: true, antialias: false });
  if (!gl) return;

  var vs = '#version 300 es\n' +
    'void main() {\n' +
    '  vec2 p = vec2(float((gl_VertexID << 1) & 2), float(gl_VertexID & 2));\n' +
    '  gl_Position = vec4(p * 2.0 - 1.0, 0.0, 1.0);\n' +
    '}\n';

  var fs = '#version 300 es\n' +
    'precision highp float;\n' +
    'uniform vec2 uRes;\n' +
    'uniform vec2 uCenter;\n' +
    'uniform float uScale;\n' +
    'uniform float uMax;\n' +
    'uniform vec3 uInk;\n' +
    'uniform vec3 uCoral;\n' +
    'out vec4 o;\n' +
    'vec4 shade(vec2 frag) {\n' +
    '  vec2 c = uCenter + (frag - 0.5 * uRes) / uRes.y * uScale;\n' +
    '  vec2 z = vec2(0.0);\n' +
    '  float it = 0.0;\n' +
    '  bool inside = true;\n' +
    '  for (int i = 0; i < 1200; i++) {\n' +
    '    if (float(i) >= uMax) break;\n' +
    '    z = vec2(z.x * z.x - z.y * z.y, 2.0 * z.x * z.y) + c;\n' +
    '    if (dot(z, z) > 1024.0) { inside = false; it = float(i); break; }\n' +
    '  }\n' +
    '  if (inside) return vec4(uInk * 0.92, 0.92);\n' +
    '  float mu = it + 1.0 - log2(log2(dot(z, z)) * 0.5);\n' +
    '  float lm = log(max(mu, 1.0));\n' +
    '  float tone = smoothstep(0.5, 1.0, lm / log(uMax));\n' +
    '  float a = pow(tone, 1.2) * 0.9;\n' +
    '  a *= 0.9 + 0.1 * sin(lm * 4.0);\n' +
    '  vec3 col = mix(uCoral, uInk, smoothstep(0.3, 0.85, tone));\n' +
    '  return vec4(col * a, a);\n' +
    '}\n' +
    'void main() {\n' +
    '  vec4 s = shade(gl_FragCoord.xy + vec2(-0.25, -0.25)) + shade(gl_FragCoord.xy + vec2(0.25, -0.25)) +\n' +
    '           shade(gl_FragCoord.xy + vec2(-0.25, 0.25)) + shade(gl_FragCoord.xy + vec2(0.25, 0.25));\n' +
    '  o = s * 0.25;\n' +
    '}\n';

  function shader(type, src) {
    var sh = gl.createShader(type);
    gl.shaderSource(sh, src);
    gl.compileShader(sh);
    return sh;
  }

  var prog = gl.createProgram();
  gl.attachShader(prog, shader(gl.VERTEX_SHADER, vs));
  gl.attachShader(prog, shader(gl.FRAGMENT_SHADER, fs));
  gl.linkProgram(prog);
  if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) return;
  gl.useProgram(prog);
  gl.viewport(0, 0, cv.width, cv.height);

  var U = {};
  ['uRes', 'uCenter', 'uScale', 'uMax', 'uInk', 'uCoral'].forEach(function (n) { U[n] = gl.getUniformLocation(prog, n); });

  var TARGET = [-0.743643887037151, 0.13182590420533];
  var START = [-0.5, 0], S0 = 3.2, S1 = 5e-4, PERIOD = 70;

  function rgb(h) { return [parseInt(h.substr(1, 2), 16) / 255, parseInt(h.substr(3, 2), 16) / 255, parseInt(h.substr(5, 2), 16) / 255]; }

  var wasOn = false, t0 = 0, lastDraw = 0;

  function frame(now) {
    requestAnimationFrame(frame);
    if (!sec.classList.contains('present')) { wasOn = false; return; }
    if (!wasOn) { wasOn = true; t0 = now; }
    if (now - lastDraw < 30) return;
    lastDraw = now;
    var tau = ((now - t0) / 1000) % PERIOD;
    var e = 0.5 - 0.5 * Math.cos(2 * Math.PI * tau / PERIOD);
    var scale = Math.exp(Math.log(S0) + (Math.log(S1) - Math.log(S0)) * e);
    var v = (S0 - scale) / (S0 - S1);
    var dark = document.body.classList.contains('dark');
    var ink = rgb(dark ? '#d0d0d0' : '#1a1a1a'), coral = rgb(dark ? '#f08e7c' : '#ed6f5c');
    gl.uniform2f(U.uRes, cv.width, cv.height);
    gl.uniform2f(U.uCenter, START[0] + (TARGET[0] - START[0]) * v, START[1] + (TARGET[1] - START[1]) * v);
    gl.uniform1f(U.uScale, scale);
    gl.uniform1f(U.uMax, Math.min(1200, 150 + 70 * Math.log(S0 / scale) / Math.LN2));
    gl.uniform3fv(U.uInk, ink);
    gl.uniform3fv(U.uCoral, coral);
    gl.clearColor(0, 0, 0, 0);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  }

  requestAnimationFrame(frame);
})();
</script>

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
    'particles-ef-content25', 'particles-ef-content26', 'particles-ef-content32'
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
