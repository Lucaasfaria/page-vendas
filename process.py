import re

def process():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Preloads in head
    head_addition = """    <link rel="preconnect" href="https://www.tiktok.com" />
    <link rel="preload" as="image" fetchpriority="high" href="./50.png" />
    <link rel="preload" as="image" fetchpriority="high" href="./30.png" />
"""
    content = content.replace("    <!-- Meta Pixel Code -->", head_addition + "    <!-- Meta Pixel Code -->")

    # Add decoding="async" to hero images
    content = re.sub(
        r'<img \s*src="\./50\.png"\s*alt="50 Dinâmicas de Educação Física"\s*class="ebook-mockup-img"\s*/>',
        '<img src="./50.png" alt="50 Dinâmicas de Educação Física" class="ebook-mockup-img" fetchpriority="high" decoding="async" />',
        content
    )
    content = re.sub(
        r'<img \s*src="\./30\.png"\s*alt="30 Dinâmicas Sem Quadra — Bônus Gratuito"\s*class="ebook-mockup-img"\s*/>',
        '<img src="./30.png" alt="30 Dinâmicas Sem Quadra — Bônus Gratuito" class="ebook-mockup-img" fetchpriority="high" decoding="async" />',
        content
    )

    # Note: re.sub above replaces ALL occurrences, so the ones in secao-produto get it too. 
    # But later in secao-produto we want loading="lazy". We can handle that. 
    # Let's fix the ones in secao-produto:
    
    produto_block = """      <div class="ebook-pair" style="margin-bottom: 40px;">
        <div class="ebook-wrap">
          <img src="./50.png" alt="50 Dinâmicas de Educação Física" class="ebook-mockup-img" fetchpriority="high" decoding="async" />
        </div>
        <div class="ebook-wrap bonus">
          <img src="./30.png" alt="30 Dinâmicas Sem Quadra — Bônus Gratuito" class="ebook-mockup-img" fetchpriority="high" decoding="async" />
        </div>
      </div>"""
      
    produto_block_lazy = """      <div class="ebook-pair" style="margin-bottom: 40px;">
        <div class="ebook-wrap">
          <img src="./50.png" alt="50 Dinâmicas de Educação Física" class="ebook-mockup-img" loading="lazy" decoding="async" />
        </div>
        <div class="ebook-wrap bonus">
          <img src="./30.png" alt="30 Dinâmicas Sem Quadra — Bônus Gratuito" class="ebook-mockup-img" loading="lazy" decoding="async" />
        </div>
      </div>"""
    content = content.replace(produto_block, produto_block_lazy)

    # Iframe lazy loading
    iframe_heavy = """        <iframe
          src="https://www.tiktok.com/embed/v2/7536385547774774533?autoplay=1&loop=1"
          allowfullscreen
          allow="autoplay; encrypted-media"
          style="width: 100%; height: 740px; border: none"
        ></iframe>"""
        
    iframe_lazy = """        <iframe
          src="https://www.tiktok.com/embed/v2/7536385547774774533?autoplay=1&loop=1"
          allowfullscreen
          allow="autoplay; encrypted-media"
          style="width: 100%; height: 740px; border: none"
          loading="lazy"
          title="Video demonstrativo da aula no TikTok"
        ></iframe>"""
    content = content.replace(iframe_heavy, iframe_lazy)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    process()
