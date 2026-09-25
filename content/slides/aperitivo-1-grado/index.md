---
title: Equazioni di Primo Grado
summary: Aperitivo matematico — quarta, ripasso lampo
authors: [Diego Fantinelli]
tags: [equazioni, quarta, ripasso]
categories: [lesson]
date: "2026-09-25T00:00:00Z"
draft: false
unlisted: true
slides:
  theme: mathofthings
  transition: convex
  particles: true
  reveal_options:
    center: false
---

<style>
.sol-inner{ padding-top: 10px; font-size: 0.62em; line-height: 1.5; max-width: 900px; margin: 0 auto; }
.sol-step{
  display: grid;
  grid-template-columns: 1.3fr 1fr;
  column-gap: 24px;
  align-items: center;
  margin-bottom: 8px;
  padding-bottom: 8px;
  border-bottom: 1px solid rgba(237,111,92,0.15);
}
.sol-step:last-child{ border-bottom: none; }
.sol-step .sol-math{ text-align: left; }
.sol-step .sol-label{
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.78em;
  letter-spacing: .3px;
  color: #ed6f5c;
  opacity: .85;
  text-align: left;
  line-height: 1.35;
}
.mot-quiz-expr.big{ font-size: 1.6em; margin-top: 24px; }
.reveal .slides section.mot-hero{ display: flex !important; flex-direction: column; justify-content: center; min-height: 100%; }
.reveal .slides section:not(.mot-hero){
  display: flex !important;
  flex-direction: column !important;
  justify-content: flex-start !important;
  align-items: center;
  padding-top: 4vh;
}
</style>

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
  <p class="mot-kicker">quarta — aperitivo matematico</p>
  <h1>Equazioni di <span class="math-word">Primo Grado</span></h1>
  <p class="mot-tagline">Cinque portate &laquo;di grado superiore&raquo;: prima di servirle, si riducono tutte al primo (piatto)</p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section>
  <p class="mot-kicker">esercizio 1 di 5 &mdash; l'aperitivo leggero</p>
  <h2 class="mot-quiz-q">Riduci alla forma di primo grado e risolvi.</h2>
  <p class="mot-quiz-expr big">$$(x+2)(x-2) = (x+3)(x-5) + 17$$</p>
</section>

<section>
  <p class="mot-kicker">esercizio 1 &mdash; soluzione</p>
  <div class="sol-inner">
    <div class="sol-step"><div class="sol-math">$$(x+2)(x-2) = x^2 - 4$$</div><div class="sol-label">primo membro &mdash; prodotto notevole (diff. di quadrati)</div></div>
    <div class="sol-step"><div class="sol-math">$$(x+3)(x-5) + 17 = x^2 - 2x + 2$$</div><div class="sol-label">secondo membro &mdash; prodotto NON notevole, poi +17</div></div>
    <div class="sol-step"><div class="sol-math">$$x^2 - 4 = x^2 - 2x + 2$$</div><div class="sol-label">equazione ottenuta</div></div>
    <div class="sol-step"><div class="sol-math">$$-4 = -2x + 2 \;\Rightarrow\; -2x = -6$$</div><div class="sol-label">i termini di secondo grado si elidono</div></div>
    <div class="sol-step"><div class="sol-math">$$x = 3$$</div><div class="sol-label">soluzione</div></div>
    <div class="sol-step"><div class="sol-math">$$5 = 5 \;\checkmark$$</div><div class="sol-label">verifica: sostituendo $x=3$ in entrambi i membri</div></div>
  </div>
</section>

---

<section>
  <p class="mot-kicker">esercizio 2 di 5 &mdash; il piatto medio</p>
  <h2 class="mot-quiz-q">Riduci alla forma di primo grado e risolvi.</h2>
  <p class="mot-quiz-expr big">$$(x-4)^2 = (x+2)(x-6) + 8$$</p>
</section>

<section>
  <p class="mot-kicker">esercizio 2 &mdash; soluzione</p>
  <div class="sol-inner">
    <div class="sol-step"><div class="sol-math">$$(x-4)^2 = x^2 - 8x + 16$$</div><div class="sol-label">primo membro &mdash; prodotto notevole (quadrato di binomio)</div></div>
    <div class="sol-step"><div class="sol-math">$$(x+2)(x-6) + 8 = x^2 - 4x - 4$$</div><div class="sol-label">secondo membro &mdash; prodotto NON notevole, poi +8</div></div>
    <div class="sol-step"><div class="sol-math">$$x^2 - 8x + 16 = x^2 - 4x - 4$$</div><div class="sol-label">equazione ottenuta</div></div>
    <div class="sol-step"><div class="sol-math">$$-8x + 16 = -4x - 4 \;\Rightarrow\; -4x = -20$$</div><div class="sol-label">i termini di secondo grado si elidono</div></div>
    <div class="sol-step"><div class="sol-math">$$x = 5$$</div><div class="sol-label">soluzione</div></div>
    <div class="sol-step"><div class="sol-math">$$1 = 1 \;\checkmark$$</div><div class="sol-label">verifica: sostituendo $x=5$ in entrambi i membri</div></div>
  </div>
</section>

---

<section>
  <p class="mot-kicker">esercizio 3 di 5 &mdash; il piatto forte</p>
  <h2 class="mot-quiz-q">Riduci alla forma di primo grado e risolvi.</h2>
  <p class="mot-quiz-expr big">$$(x+2)^3 = (x+1)(x+2)(x+3) + 9$$</p>
</section>

<section>
  <p class="mot-kicker">esercizio 3 &mdash; soluzione</p>
  <div class="sol-inner">
    <div class="sol-step"><div class="sol-math">$$(x+2)^3 = x^3 + 6x^2 + 12x + 8$$</div><div class="sol-label">primo membro &mdash; prodotto notevole (cubo di binomio)</div></div>
    <div class="sol-step"><div class="sol-math">$$(x+1)(x+2) = x^2+3x+2$$</div><div class="sol-label">secondo membro &mdash; primi due fattori (NON notevole)</div></div>
    <div class="sol-step"><div class="sol-math">$$(x^2+3x+2)(x+3) = x^3+6x^2+11x+6$$</div><div class="sol-label">per il terzo fattore, poi +9</div></div>
    <div class="sol-step"><div class="sol-math">$$x^3+6x^2+12x+8 = x^3+6x^2+11x+15$$</div><div class="sol-label">equazione ottenuta</div></div>
    <div class="sol-step"><div class="sol-math">$$12x + 8 = 11x + 15 \;\Rightarrow\; x = 7$$</div><div class="sol-label">termini di terzo e secondo grado elisi</div></div>
    <div class="sol-step"><div class="sol-math">$$729 = 729 \;\checkmark$$</div><div class="sol-label">verifica: sostituendo $x=7$ in entrambi i membri</div></div>
  </div>
</section>

---

<section>
  <p class="mot-kicker">esercizio 4 di 5 &mdash; il fuori menu</p>
  <h2 class="mot-quiz-q">Riduci alla forma di primo grado e risolvi.</h2>
  <p class="mot-quiz-expr big">$$2(x+1)(x+4) + (x-3)^2 = 3(x+1)(x-1)$$</p>
</section>

<section>
  <p class="mot-kicker">esercizio 4 &mdash; soluzione</p>
  <div class="sol-inner">
    <div class="sol-step"><div class="sol-math">$$2(x+1)(x+4) = 2x^2+10x+8$$</div><div class="sol-label">primo termine &mdash; prodotto NON notevole, poi &times;2</div></div>
    <div class="sol-step"><div class="sol-math">$$(x-3)^2 = x^2-6x+9$$</div><div class="sol-label">secondo termine &mdash; prodotto notevole (quadrato di binomio)</div></div>
    <div class="sol-step"><div class="sol-math">$$3(x+1)(x-1) = 3x^2-3$$</div><div class="sol-label">secondo membro &mdash; prodotto notevole (diff. di quadrati), poi &times;3</div></div>
    <div class="sol-step"><div class="sol-math">$$3x^2+4x+17 = 3x^2-3$$</div><div class="sol-label">equazione ottenuta (sommando i due termini a sinistra)</div></div>
    <div class="sol-step"><div class="sol-math">$$4x+17 = -3 \;\Rightarrow\; 4x = -20$$</div><div class="sol-label">i termini di secondo grado si elidono</div></div>
    <div class="sol-step"><div class="sol-math">$$x = -5$$</div><div class="sol-label">soluzione</div></div>
    <div class="sol-step"><div class="sol-math">$$72 = 72 \;\checkmark$$</div><div class="sol-label">verifica: sostituendo $x=-5$ in entrambi i membri</div></div>
  </div>
</section>

---

<section>
  <p class="mot-kicker">esercizio 5 di 5 &mdash; il digestivo (con i denominatori)</p>
  <h2 class="mot-quiz-q">Riduci alla forma di primo grado e risolvi.</h2>
  <p class="mot-quiz-expr big">$$\dfrac{2(x+1)^2}{4} = \dfrac{3(x-3)(x+2)}{6} + \dfrac{1}{2}$$</p>
</section>

<section>
  <p class="mot-kicker">esercizio 5 &mdash; soluzione</p>
  <div class="sol-inner">
    <div class="sol-step"><div class="sol-math">$$\text{MCM}(4,6,2) = 12 \;\Rightarrow\; \times 12$$</div><div class="sol-label">moltiplico entrambi i membri per il MCM dei tre denominatori</div></div>
    <div class="sol-step"><div class="sol-math">$$6(x+1)^2 = 6x^2+12x+6$$</div><div class="sol-label">primo membro &mdash; prodotto notevole (quadrato di binomio), con coefficiente</div></div>
    <div class="sol-step"><div class="sol-math">$$6(x-3)(x+2) + 6 = 6x^2-6x-30$$</div><div class="sol-label">secondo membro &mdash; prodotto NON notevole, con coefficiente</div></div>
    <div class="sol-step"><div class="sol-math">$$6x^2+12x+6 = 6x^2-6x-30$$</div><div class="sol-label">equazione ottenuta</div></div>
    <div class="sol-step"><div class="sol-math">$$12x+6 = -6x-30 \;\Rightarrow\; 18x = -36$$</div><div class="sol-label">i termini di secondo grado si elidono</div></div>
    <div class="sol-step"><div class="sol-math">$$x = -2$$</div><div class="sol-label">soluzione</div></div>
    <div class="sol-step"><div class="sol-math">$$\dfrac{1}{2} = \dfrac{1}{2} \;\checkmark$$</div><div class="sol-label">verifica: sostituendo $x=-2$ in entrambi i membri</div></div>
  </div>
</section>
