import re

def process():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add CSS
    css_addition = """
      /* ─── EBOOK BONUS LABEL ─── */
      .ebook-bonus-label {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 10px;
        margin-top: 28px;
        font-size: 15px;
        color: #3A3A3A;
      }
      .ebook-bonus-item {
        display: flex;
        align-items: center;
        gap: 10px;
      }
      .ebook-bonus-dot.main {
        background: #1B4332;
        color: #fff;
        font-size: 12px;
        font-weight: 700;
        padding: 3px 9px;
        border-radius: 100px;
      }
      .ebook-bonus-dot.bonus {
        background: #C0392B;
        color: #fff;
        font-size: 11px;
        font-weight: 700;
        padding: 3px 9px;
        border-radius: 100px;
        letter-spacing: 0.05em;
      }
      .ebook-bonus-plus {
        font-size: 22px;
        font-weight: 700;
        color: #6B6B6B;
        line-height: 1;
      }
</style>"""
    content = content.replace("</style>", css_addition)

    # 2. HTML to insert below .ebook-pair
    bonus_label_html = """
        </div>
        <div class="ebook-bonus-label">
          <div class="ebook-bonus-item">
            <span class="ebook-bonus-dot main">✓</span>
            <span><strong>50 Dinâmicas de Educação Física</strong> — Guia principal</span>
          </div>
          <div class="ebook-bonus-plus">+</div>
          <div class="ebook-bonus-item">
            <span class="ebook-bonus-dot bonus">GRÁTIS</span>
            <span><strong>30 Dinâmicas Sem Quadra</strong> — Bônus incluído na compra</span>
          </div>
        </div>"""
    content = content.replace("</div>\n      </div>\n    </section>\n\n    <!-- SEÇÃO VÍDEO TIKTOK -->", bonus_label_html + "\n      </div>\n    </section>\n\n    <!-- SEÇÃO VÍDEO TIKTOK -->")

    # 3. Update secao-bonus cards
    old_bonus_grid = """      <div class="bonus-grid">
        <div class="bonus-card">
          <div class="bonus-tag">Principal</div>
          <div class="bonus-titulo">
            50 Dinâmicas de Ed. Física — Guia Completo
          </div>
          <div class="bonus-desc">
            PDF com todas as 50 dinâmicas estruturadas, 6 categorias, do 1.º ano
            ao Ensino Médio.
          </div>
          <div class="bonus-valor">R$ 47,00</div>
        </div>
        <div class="bonus-card">
          <div class="bonus-tag">Bônus 1</div>
          <div class="bonus-titulo">Calendário Semanal de Dinâmicas</div>
          <div class="bonus-desc">
            Modelo pronto para organizar sua semana letiva com variedade de
            atividades sem repetir.
          </div>
          <div class="bonus-valor">R$ 17,00</div>
        </div>
        <div class="bonus-card">
          <div class="bonus-tag">Bônus 2</div>
          <div class="bonus-titulo">Lista de Materiais por Dinâmica</div>
          <div class="bonus-desc">
            Planilha rápida pra você saber o que separar antes de cada aula. Sem
            improvisar material.
          </div>
          <div class="bonus-valor">R$ 9,00</div>
        </div>
      </div>"""
      
    new_bonus_grid = """      <div class="bonus-grid">
        <div class="bonus-card">
          <div class="bonus-tag" style="background: #1B4332;">Principal</div>
          <div class="bonus-titulo">
            50 Dinâmicas de Ed. Física — Guia Completo
          </div>
          <div class="bonus-desc">
            PDF com todas as 50 dinâmicas estruturadas, 6 categorias, do 1.º ano
            ao Ensino Médio.
          </div>
          <div class="bonus-valor">R$ 47,00</div>
        </div>
        <div class="bonus-card">
          <div class="bonus-tag" style="background: #C0392B;">Bônus 1 (GRÁTIS)</div>
          <div class="bonus-titulo">E-book: 30 Dinâmicas Sem Quadra</div>
          <div class="bonus-desc">
            Atividades alternativas perfeitas para dias de chuva ou falta de espaço.
          </div>
          <div class="bonus-valor">R$ 27,00</div>
        </div>
        <div class="bonus-card">
          <div class="bonus-tag">Bônus 2</div>
          <div class="bonus-titulo">Calendário Semanal de Dinâmicas</div>
          <div class="bonus-desc">
            Modelo pronto para organizar sua semana letiva.
          </div>
          <div class="bonus-valor">R$ 17,00</div>
        </div>
        <div class="bonus-card">
          <div class="bonus-tag">Bônus 3</div>
          <div class="bonus-titulo">Lista de Materiais por Dinâmica</div>
          <div class="bonus-desc">
            Planilha rápida pra você saber o que separar.
          </div>
          <div class="bonus-valor">R$ 9,00</div>
        </div>
      </div>"""
    content = content.replace(old_bonus_grid, new_bonus_grid)

    # 4. Update ancora-total
    old_ancora_total = """      <div class="ancora-total">
        <div class="ancora-linha">
          <span class="nome">Guia 50 Dinâmicas</span>
          <span class="val">R$ 47,00</span>
        </div>
        <div class="ancora-linha">
          <span class="nome">Bônus 1 — Calendário Semanal</span>
          <span class="val">R$ 17,00</span>
        </div>
        <div class="ancora-linha">
          <span class="nome">Bônus 2 — Lista de Materiais</span>
          <span class="val">R$ 9,00</span>
        </div>
        <div class="ancora-total-linha">
          <span class="label">HOJE TUDO POR:</span>
          <span class="preco-final">R$ 9,90</span>
        </div>
      </div>"""
      
    new_ancora_total = """      <div class="ancora-total">
        <div class="ancora-linha">
          <span class="nome">Guia 50 Dinâmicas</span>
          <span class="val">R$ 47,00</span>
        </div>
        <div class="ancora-linha">
          <span class="nome">Bônus 1 — 30 Dinâmicas Sem Quadra</span>
          <span class="val">R$ 27,00</span>
        </div>
        <div class="ancora-linha">
          <span class="nome">Bônus 2 — Calendário Semanal</span>
          <span class="val">R$ 17,00</span>
        </div>
        <div class="ancora-linha">
          <span class="nome">Bônus 3 — Lista de Materiais</span>
          <span class="val">R$ 9,00</span>
        </div>
        <div class="ancora-total-linha">
          <span class="label">HOJE TUDO POR:</span>
          <span class="preco-final">R$ 9,90</span>
        </div>
      </div>"""
    content = content.replace(old_ancora_total, new_ancora_total)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    process()
