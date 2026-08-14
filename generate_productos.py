# -*- coding: utf-8 -*-
"""Genera las páginas de categoría de producto restantes."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "productos")

WA_ICON = '''<svg viewBox="0 0 32 32"><path d="M16.001 3C9.373 3 4 8.373 4 15c0 2.386.71 4.607 1.929 6.464L4 29l7.73-1.9A11.94 11.94 0 0 0 16.001 27C22.63 27 28 21.627 28 15S22.63 3 16.001 3zm0 21.818a9.78 9.78 0 0 1-4.986-1.364l-.358-.213-4.59 1.128 1.15-4.47-.233-.365A9.77 9.77 0 0 1 5.182 15c0-5.964 4.854-10.818 10.819-10.818S26.818 9.036 26.818 15 21.965 24.818 16.001 24.818zm5.61-7.98c-.307-.154-1.818-.897-2.1-.999-.282-.102-.487-.153-.692.154-.205.307-.795.998-.975 1.203-.18.205-.36.23-.667.077-.307-.154-1.296-.478-2.469-1.524-.913-.814-1.53-1.82-1.71-2.127-.18-.307-.02-.473.135-.626.138-.138.307-.36.46-.54.154-.18.205-.307.307-.512.103-.205.052-.384-.026-.538-.077-.154-.692-1.667-.948-2.283-.25-.6-.503-.519-.692-.529-.18-.008-.384-.01-.59-.01-.204 0-.537.077-.818.384-.282.307-1.075 1.05-1.075 2.563s1.1 2.973 1.254 3.178c.154.205 2.166 3.31 5.25 4.64.734.317 1.306.507 1.753.649.736.234 1.406.201 1.936.122.59-.088 1.818-.743 2.075-1.46.256-.718.256-1.332.18-1.46-.077-.128-.282-.205-.59-.359z"/></svg>'''

HEAD = """<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://www.tirodearrastre.co/productos/{slug}.html">
<meta name="robots" content="index, follow">
<meta property="og:type" content="product">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://www.tirodearrastre.co/productos/{slug}.html">
<meta property="og:image" content="https://www.tirodearrastre.co/assets/img/productos/{slug}-cover.jpg">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="manifest" href="/manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/main.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type":"ListItem","position":1,"name":"Inicio","item":"https://www.tirodearrastre.co/"}},
    {{"@type":"ListItem","position":2,"name":"Productos","item":"https://www.tirodearrastre.co/productos/"}},
    {{"@type":"ListItem","position":3,"name":"{nombre}","item":"https://www.tirodearrastre.co/productos/{slug}.html"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{nombre}",
  "brand": {brands_json},
  "description": "{description}",
  "offers": {{
    "@type": "AggregateOffer",
    "priceCurrency": "COP",
    "availability": "https://schema.org/InStock",
    "areaServed": "CO"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": {faq_json}
}}
</script>
</head>
<body>
<a class="skip-link" href="#contenido">Saltar al contenido</a>
<header class="site-header">
  <div class="container">
    <a href="/" class="logo" aria-label="Tiro de Arrastre Colombia — Inicio">TIRO <span class="marca-tag">DE</span> ARRASTRE</a>
    <nav class="nav-principal" aria-label="Navegación principal">
      <a href="/productos/tiros-de-arrastre.html">Tiros de Arrastre</a>
      <a href="/productos/portabicicletas.html">Portabicicletas</a>
      <a href="/productos/parrillas-de-techo.html">Parrillas de Techo</a>
      <a href="/productos/cubre-carter.html">Cubre Cárter</a>
      <a href="/marcas/">Marcas</a>
      <a href="/contacto.html">Contacto</a>
    </nav>
    <div class="nav-cta">
      <a href="#" class="btn btn-outline" data-wa="Cotización {nombre}">WhatsApp</a>
      <button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
<main id="contenido">
  <div class="container breadcrumb"><a href="/">Inicio</a><span class="sep">/</span><a href="/productos/">Productos</a><span class="sep">/</span>{nombre}</div>
"""

FOOT = """
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="logo" style="margin-bottom:1em">TIRO <span class="marca-tag">DE</span> ARRASTRE</div>
        <p style="max-width:32ch;font-size:.9rem">Tiros de arrastre, portabicicletas y accesorios para camionetas en Colombia.</p>
      </div>
      <div><h4>Productos</h4><ul>
        <li><a href="/productos/tiros-de-arrastre.html">Tiros de arrastre</a></li>
        <li><a href="/productos/portabicicletas.html">Portabicicletas</a></li>
        <li><a href="/productos/parrillas-de-techo.html">Parrillas de techo</a></li>
        <li><a href="/productos/cubre-carter.html">Cubre cárter</a></li>
      </ul></div>
      <div><h4>Empresa</h4><ul>
        <li><a href="/marcas/">Marcas</a></li>
        <li><a href="/blog/index.html">Blog</a></li>
        <li><a href="/contacto.html">Contacto</a></li>
      </ul></div>
      <div><h4>Legal</h4><ul>
        <li><a href="/legal/privacidad.html">Política de privacidad</a></li>
        <li><a href="/legal/terminos.html">Términos y condiciones</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="anio"></span> Tiro de Arrastre Colombia.</span>
      <span>WhatsApp: +57 318 785 6238</span>
    </div>
  </div>
</footer>
<a href="#" class="wa-flotante" data-wa="Cotización {nombre}" aria-label="Escribir por WhatsApp">
""" + WA_ICON + """
</a>
<script src="/assets/js/main.js"></script>
<script>document.getElementById('anio').textContent = new Date().getFullYear();</script>
</body>
</html>
"""

import json

def faq_block(items):
    return json.dumps([
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
        for q, a in items
    ], ensure_ascii=False)

def brands_block(names):
    return json.dumps([{"@type": "Brand", "name": n} for n in names], ensure_ascii=False)

PAGES = []

# ---------- PORTABICICLETAS ----------
PAGES.append(dict(
    slug="portabicicletas",
    nombre="Portabicicletas",
    title="Portabicicletas para Carro en Colombia | Aerobike y Thule",
    og_title="Portabicicletas para Carro | Aerobike y Thule",
    description="Portabicicletas Aerobike y Thule para 2, 3 o 4 bicicletas, compatibles con tiro de arrastre. Modelos plegables, con luces y de sujeción automática. Instalación y asesoría en Colombia.",
    brands=["Aerobike", "Thule"],
    faq=[
        ("¿Cuántas bicicletas caben en un portabicicletas?", "Manejamos referencias para 2, 3 y 4 bicicletas, según el modelo Aerobike o Thule que elijas."),
        ("¿El portabicicletas sirve en cualquier tiro de arrastre?", "Se ajusta al receptor estándar de 2 pulgadas, presente en la gran mayoría de tiros de arrastre que instalamos."),
        ("¿Hay portabicicletas con luces traseras?", "Sí, contamos con versiones premium que incluyen luces para mayor visibilidad y cumplimiento normativo."),
    ],
    hero_sub="Portabicicletas Aerobike y Thule que se acoplan al receptor de tu tiro de arrastre. Versiones para 2, 3 o 4 bicicletas, plegables, de sujeción automática y con luces traseras.",
    secciones="""
  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Descripción</p>
        <h2>Portabicicletas para tiro de arrastre</h2>
        <p>Nuestros portabicicletas se acoplan al receptor del tiro de arrastre y permiten transportar bicicletas sin usar el techo del vehículo, lo que facilita la carga y reduce el consumo de combustible frente a un rack de techo.</p>
        <p>Distribuimos la línea Aerobike, con opciones económicas y prácticas, y somos representantes oficiales de Thule en Colombia para quienes buscan la gama premium.</p>
      </div>
      <div class="section-head"><p class="eyebrow">Capacidades</p><h2>Elige según el número de bicicletas</h2></div>
      <div class="grid-4">
        <div class="card"><span class="num">Aerobike</span><h3>2 Bicicletas</h3><p>Ideal para uso familiar básico o parejas.</p></div>
        <div class="card"><span class="num">Aerobike</span><h3>3 Bicicletas</h3><p>Disponible en versión estándar y automática.</p></div>
        <div class="card"><span class="num">Aerobike</span><h3>4 Bicicletas</h3><p>Para grupos o familias numerosas.</p></div>
        <div class="card"><span class="num">Aerobike</span><h3>Premium con luces</h3><p>Versiones de 2 y 3 bicicletas con iluminación trasera.</p></div>
      </div>
    </div>
  </section>
  <section class="seccion-oscura">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Tipos</p><h2>Formatos disponibles</h2></div>
      <div class="grid-3">
        <div class="card" style="background:var(--grafito-900);border-color:var(--grafito-700)"><h3 style="color:var(--hueso-50)">Plegable</h3><p style="color:var(--acero-300)">Se pliega hacia arriba cuando no está en uso, sin necesidad de desmontarlo del tiro de arrastre.</p></div>
        <div class="card" style="background:var(--grafito-900);border-color:var(--grafito-700)"><h3 style="color:var(--hueso-50)">Sujeción automática</h3><p style="color:var(--acero-300)">Sistema de anclaje rápido al receptor, sin herramientas.</p></div>
        <div class="card" style="background:var(--grafito-900);border-color:var(--grafito-700)"><h3 style="color:var(--hueso-50)">Con luces</h3><p style="color:var(--acero-300)">Incluye módulo de luces traseras para mayor visibilidad en carretera.</p></div>
      </div>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="section-head"><p class="eyebrow">Compatibilidad</p><h2>Se ajusta a tu tiro de arrastre</h2><p>Todos nuestros portabicicletas se acoplan al receptor estándar de 2 pulgadas. Si aún no tienes tiro de arrastre instalado, podemos cotizarte el conjunto completo.</p></div>
      <div class="hero-cta">
        <a href="#" class="btn btn-cobre" data-wa="Quiero cotizar un portabicicletas">Cotizar portabicicletas</a>
        <a href="/productos/tiros-de-arrastre.html" class="btn btn-outline">Ver tiros de arrastre</a>
      </div>
    </div>
  </section>
""",
))

# ---------- PARRILLAS DE TECHO ----------
PAGES.append(dict(
    slug="parrillas-de-techo",
    nombre="Parrillas de Techo",
    title="Parrillas y Racks de Techo en Colombia | Thule",
    og_title="Parrillas de Techo para Carro y Camioneta | Thule",
    description="Parrillas y racks de techo Thule para maletines, kayaks, bicicletas y carga adicional. Compatibles con barras originales de fábrica. Cotiza en Colombia.",
    brands=["Thule"],
    faq=[
        ("¿La parrilla de techo sirve en cualquier vehículo?", "Depende del tipo de techo y de si el vehículo tiene rieles o puntos de fijación de fábrica. Confirmamos la compatibilidad exacta al cotizar."),
        ("¿Qué se puede transportar en una parrilla de techo?", "Maletines de carga, kayaks, tablas, bicicletas y carga adicional dentro del límite de peso del techo del vehículo."),
        ("¿Afecta el consumo de combustible?", "Puede aumentar ligeramente el consumo por resistencia aerodinámica, sobre todo a velocidades altas en carretera."),
    ],
    hero_sub="Racks y parrillas de techo Thule para maletines, kayaks, tablas y carga adicional. Compatibles con barras y rieles originales de fábrica.",
    secciones="""
  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Descripción</p>
        <h2>Parrillas de techo Thule</h2>
        <p>Las parrillas de techo amplían la capacidad de carga del vehículo sin depender del tiro de arrastre, ideales para maletines rígidos, kayaks, tablas de surf o carga voluminosa.</p>
        <p>Como representantes oficiales de Thule en Colombia, ofrecemos sistemas compatibles con las barras y rieles originales de la mayoría de SUV y camionetas del mercado.</p>
      </div>
      <div class="section-head"><p class="eyebrow">Protección</p><h2>Materiales y resistencia</h2></div>
      <div class="grid-3">
        <div class="card"><h3>Estructura en aluminio</h3><p>Ligera y resistente a la corrosión, reduce el peso adicional sobre el techo.</p></div>
        <div class="card"><h3>Fijación segura</h3><p>Sistemas de anclaje con cierre que evitan el desplazamiento de la carga en carretera.</p></div>
        <div class="card"><h3>Diseño aerodinámico</h3><p>Perfiles pensados para reducir el ruido y el impacto en el consumo de combustible.</p></div>
      </div>
    </div>
  </section>
  <section class="seccion-oscura">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Compatibilidad</p><h2>Modelos compatibles</h2><p style="color:var(--acero-300)">Las parrillas de techo se ajustan según el tipo de techo del vehículo: con rieles integrados, rieles elevados o techo liso con puntos de fijación. Te confirmamos la referencia exacta con la marca y modelo de tu vehículo.</p></div>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="hero-cta">
        <a href="#" class="btn btn-cobre" data-wa="Quiero cotizar una parrilla de techo">Cotizar parrilla de techo</a>
        <a href="/marcas/" class="btn btn-outline">Buscar por marca</a>
      </div>
    </div>
  </section>
""",
))

# ---------- CUBRE CARTER ----------
PAGES.append(dict(
    slug="cubre-carter",
    nombre="Cubre Cárter",
    title="Cubre Cárter para Camioneta y SUV en Colombia",
    og_title="Cubre Cárter para Camioneta y SUV",
    description="Cubre cárter y protectores de motor a la medida de tu camioneta o SUV. Protección contra piedras, terrenos irregulares y golpes de bajo perfil. Instalación en Colombia.",
    brands=["Tiro de Arrastre Colombia"],
    faq=[
        ("¿Para qué sirve el cubre cárter?", "Protege el motor, el cárter y componentes bajos del vehículo contra piedras, terrenos irregulares y golpes al circular por vías destapadas."),
        ("¿El cubre cárter afecta el mantenimiento del vehículo?", "Está diseñado para permitir el acceso a los puntos de drenaje y mantenimiento habituales sin necesidad de retirarlo por completo."),
        ("¿Para qué vehículos hay cubre cárter disponible?", "Contamos con referencias para camionetas y SUV de las marcas más vendidas en Colombia. Confirmamos disponibilidad según tu modelo."),
    ],
    hero_sub="Protectores de cárter y motor fabricados a la medida de camionetas y SUV, pensados para terrenos irregulares y vías destapadas.",
    secciones="""
  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Descripción</p>
        <h2>Protección para la parte baja de tu vehículo</h2>
        <p>El cubre cárter es una plancha protectora que se instala en la parte baja del motor y el cárter para evitar daños por impacto con piedras, terrenos irregulares o baches profundos.</p>
        <p>Es especialmente recomendado para quienes usan su camioneta o SUV en carretera destapada, fincas o zonas rurales con frecuencia.</p>
      </div>
      <div class="section-head"><p class="eyebrow">Materiales</p><h2>Resistencia sin exceso de peso</h2></div>
      <div class="grid-3">
        <div class="card"><h3>Acero de alto calibre</h3><p>Mayor resistencia a impactos fuertes, para uso todoterreno exigente.</p></div>
        <div class="card"><h3>Aluminio reforzado</h3><p>Buena protección con menor peso adicional sobre el vehículo.</p></div>
        <div class="card"><h3>Diseño a la medida</h3><p>Cada cubre cárter respeta la geometría original del chasis del modelo.</p></div>
      </div>
    </div>
  </section>
  <section class="seccion-oscura">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Ventajas</p><h2>Por qué instalarlo</h2></div>
      <div class="grid-3">
        <div class="card" style="background:var(--grafito-900);border-color:var(--grafito-700)"><h3 style="color:var(--hueso-50)">Protección real</h3><p style="color:var(--acero-300)">Reduce el riesgo de daños costosos en el motor y el cárter.</p></div>
        <div class="card" style="background:var(--grafito-900);border-color:var(--grafito-700)"><h3 style="color:var(--hueso-50)">Instalación sin modificaciones</h3><p style="color:var(--acero-300)">Se ajusta a los puntos de anclaje existentes del vehículo.</p></div>
        <div class="card" style="background:var(--grafito-900);border-color:var(--grafito-700)"><h3 style="color:var(--hueso-50)">Acceso de mantenimiento</h3><p style="color:var(--acero-300)">Permite realizar cambios de aceite sin retirar la pieza completa.</p></div>
      </div>
    </div>
  </section>
  <section>
    <div class="container">
      <div class="hero-cta">
        <a href="#" class="btn btn-cobre" data-wa="Quiero cotizar un cubre cárter">Cotizar cubre cárter</a>
        <a href="/marcas/" class="btn btn-outline">Buscar por marca</a>
      </div>
    </div>
  </section>
""",
))

os.makedirs(OUT_DIR, exist_ok=True)
for p in PAGES:
    hero = f"""
  <section class="hero" style="padding-top:24px">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow">Categoría</p>
        <h1>{p['nombre']}</h1>
        <p class="hero-sub">{p['hero_sub']}</p>
        <div class="hero-cta">
          <a href="#" class="btn btn-cobre" data-wa="Quiero cotizar {p['nombre'].lower()}">Cotizar {p['nombre'].lower()}</a>
          <a href="/marcas/" class="btn btn-outline">Buscar por marca de vehículo</a>
        </div>
      </div>
      <div class="hero-visual" style="background-image:url('/assets/img/productos/{p['slug']}-hero.jpg')">
        <span class="tag">{p['nombre']}</span>
      </div>
    </div>
  </section>
"""
    head = HEAD.format(
        title=p["title"], description=p["description"], slug=p["slug"], og_title=p["og_title"],
        nombre=p["nombre"], brands_json=brands_block(p["brands"]), faq_json=faq_block(p["faq"]),
    )
    faq_html = "\n".join(
        f'''        <div class="faq-item" data-abierto="false">
          <button class="faq-pregunta" aria-expanded="false">{q}</button>
          <div class="faq-respuesta"><p>{a}</p></div>
        </div>''' for q, a in p["faq"]
    )
    faq_section = f"""
  <section>
    <div class="container" style="max-width:820px">
      <div class="section-head centro">
        <p class="eyebrow" style="justify-content:center">Preguntas frecuentes</p>
        <h2>{p['nombre']}</h2>
      </div>
      <div class="faq-lista">
{faq_html}
      </div>
    </div>
  </section>
"""
    full = head + hero + p["secciones"] + faq_section + FOOT.format(nombre=p["nombre"])
    with open(os.path.join(OUT_DIR, f"{p['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(full)

print("Generadas:", [p["slug"] for p in PAGES])
