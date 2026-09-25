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
---

<style>
.sol-toggle{
  margin-top: 28px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.5px;
  color: #ed6f5c;
  background: rgba(237,111,92,0.08);
  border: 1px solid rgba(237,111,92,0.35);
  border-radius: 8px;
  padding: 10px 22px;
  cursor: pointer;
  transition: all .2s ease;
}
.sol-toggle:hover{ background: rgba(237,111,92,0.16); border-color: rgba(237,111,92,0.6); }
.sol-toggle .arrow{ display:inline-block; transition: transform .25s ease; margin-left: 6px; }
.sol-toggle.open .arrow{ transform: rotate(180deg); }
.sol-body{
  max-height: 0;
  overflow: hidden;
  transition: max-height .35s ease;
  text-align: left;
  margin: 0 auto;
  max-width: 720px;
}
.sol-body.open{ max-height: 1400px; }
.sol-inner{ padding-top: 18px; font-size: 0.62em; line-height: 1.6; }
.sol-step{ margin-bottom: 10px; }
.sol-step .lbl{ font-family: 'JetBrains Mono', monospace; font-size: 0.72em; letter-spacing: .5px; text-transform: uppercase; color: #ed6f5c; opacity: .8; }
.mot-quiz-expr.big{ font-size: 1.5em; margin-top: 18px; }
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
  <p class="mot-tagline">Tre portate &laquo;di grado superiore&raquo;: prima di servirle, si riducono tutte al primo (piatto)</p>
  <p class="mot-meta">prof. Diego Fantinelli &mdash; <a href="https://mathofthings.netlify.app/" target="_blank" class="mono">The Math of Things</a></p>
</section>

---

<section>
  <p class="mot-kicker">esercizio 1 di 3 &mdash; l'aperitivo leggero</p>
  <h2 class="mot-quiz-q">Riduci alla forma di primo grado e risolvi.</h2>
  <p class="mot-quiz-expr big">$$(x+2)(x-2) = (x+3)(x-5) + 17$$</p>

  <button class="sol-toggle" onclick="motSolToggle(this)">Mostra soluzione <span class="arrow">&#9660;</span></button>
  <div class="sol-body">
    <div class="sol-inner">
      <div class="sol-step"><span class="lbl">Primo membro &mdash; prodotto notevole</span><br>
        $$(x+2)(x-2) = x^2 - 4$$
      </div>
      <div class="sol-step"><span class="lbl">Secondo membro &mdash; prodotto NON notevole</span><br>
        $$(x+3)(x-5) + 17 = x^2 - 2x - 15 + 17 = x^2 - 2x + 2$$
      </div>
      <div class="sol-step"><span class="lbl">Equazione ottenuta</span><br>
        $$x^2 - 4 = x^2 - 2x + 2$$
      </div>
      <div class="sol-step"><span class="lbl">I termini di secondo grado si elidono</span><br>
        $$-4 = -2x + 2 \;\Rightarrow\; -2x = -6$$
      </div>
      <div class="sol-step"><span class="lbl">Soluzione</span><br>
        $$x = 3$$
      </div>
      <div class="sol-step"><span class="lbl">Verifica</span><br>
        $$(3+2)(3-2) = 5 \qquad (3+3)(3-5)+17 = -12+17 = 5 \;\checkmark$$
      </div>
    </div>
  </div>
</section>

---

<section>
  <p class="mot-kicker">esercizio 2 di 3 &mdash; il piatto medio</p>
  <h2 class="mot-quiz-q">Riduci alla forma di primo grado e risolvi.</h2>
  <p class="mot-quiz-expr big">$$(x-4)^2 = (x+2)(x-6) + 8$$</p>

  <button class="sol-toggle" onclick="motSolToggle(this)">Mostra soluzione <span class="arrow">&#9660;</span></button>
  <div class="sol-body">
    <div class="sol-inner">
      <div class="sol-step"><span class="lbl">Primo membro &mdash; prodotto notevole (quadrato di binomio)</span><br>
        $$(x-4)^2 = x^2 - 8x + 16$$
      </div>
      <div class="sol-step"><span class="lbl">Secondo membro &mdash; prodotto NON notevole</span><br>
        $$(x+2)(x-6) + 8 = x^2 - 4x - 12 + 8 = x^2 - 4x - 4$$
      </div>
      <div class="sol-step"><span class="lbl">Equazione ottenuta</span><br>
        $$x^2 - 8x + 16 = x^2 - 4x - 4$$
      </div>
      <div class="sol-step"><span class="lbl">I termini di secondo grado si elidono</span><br>
        $$-8x + 16 = -4x - 4 \;\Rightarrow\; -4x = -20$$
      </div>
      <div class="sol-step"><span class="lbl">Soluzione</span><br>
        $$x = 5$$
      </div>
      <div class="sol-step"><span class="lbl">Verifica</span><br>
        $$(5-4)^2 = 1 \qquad (5+2)(5-6)+8 = -7+8 = 1 \;\checkmark$$
      </div>
    </div>
  </div>
</section>

---

<section>
  <p class="mot-kicker">esercizio 3 di 3 &mdash; il piatto forte</p>
  <h2 class="mot-quiz-q">Riduci alla forma di primo grado e risolvi.</h2>
  <p class="mot-quiz-expr big">$$(x+2)^3 = (x+1)(x+2)(x+3) + 9$$</p>

  <button class="sol-toggle" onclick="motSolToggle(this)">Mostra soluzione <span class="arrow">&#9660;</span></button>
  <div class="sol-body">
    <div class="sol-inner">
      <div class="sol-step"><span class="lbl">Primo membro &mdash; prodotto notevole (cubo di binomio)</span><br>
        $$(x+2)^3 = x^3 + 6x^2 + 12x + 8$$
      </div>
      <div class="sol-step"><span class="lbl">Secondo membro &mdash; prodotto di tre fattori NON notevole</span><br>
        $$(x+1)(x+2) = x^2+3x+2$$
        $$(x^2+3x+2)(x+3) = x^3+6x^2+11x+6$$
        $$\text{quindi: } x^3+6x^2+11x+6+9 = x^3+6x^2+11x+15$$
      </div>
      <div class="sol-step"><span class="lbl">Equazione ottenuta</span><br>
        $$x^3+6x^2+12x+8 = x^3+6x^2+11x+15$$
      </div>
      <div class="sol-step"><span class="lbl">I termini di terzo e secondo grado si elidono</span><br>
        $$12x + 8 = 11x + 15 \;\Rightarrow\; x = 7$$
      </div>
      <div class="sol-step"><span class="lbl">Verifica</span><br>
        $$(7+2)^3 = 9^3 = 729 \qquad (7+1)(7+2)(7+3)+9 = 720+9 = 729 \;\checkmark$$
      </div>
    </div>
  </div>
</section>

---

<section class="mot-divider" data-transition="zoom">
  <h1 class="r-fit-text" style="opacity:0.75">SALUTE</h1>
  <p class="mot-joke fragment">tre portate ridotte al primo grado, zero indigestioni</p>
</section>

<script>
function motSolToggle(btn) {
  var body = btn.nextElementSibling;
  var opening = !body.classList.contains('open');
  body.classList.toggle('open');
  btn.classList.toggle('open');
  btn.innerHTML = opening
    ? 'Nascondi soluzione <span class="arrow">&#9660;</span>'
    : 'Mostra soluzione <span class="arrow">&#9660;</span>';
  if (opening && window.MathJax && MathJax.typesetPromise) {
    MathJax.typesetPromise([body]);
  }
}
</script>
