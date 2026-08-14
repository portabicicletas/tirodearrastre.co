# -*- coding: utf-8 -*-
"""Genera las páginas de marca restantes a partir de una plantilla común."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "marcas")

WA_ICON = '''<svg viewBox="0 0 32 32"><path d="M16.001 3C9.373 3 4 8.373 4 15c0 2.386.71 4.607 1.929 6.464L4 29l7.73-1.9A11.94 11.94 0 0 0 16.001 27C22.63 27 28 21.627 28 15S22.63 3 16.001 3zm0 21.818a9.78 9.78 0 0 1-4.986-1.364l-.358-.213-4.59 1.128 1.15-4.47-.233-.365A9.77 9.77 0 0 1 5.182 15c0-5.964 4.854-10.818 10.819-10.818S26.818 9.036 26.818 15 21.965 24.818 16.001 24.818zm5.61-7.98c-.307-.154-1.818-.897-2.1-.999-.282-.102-.487-.153-.692.154-.205.307-.795.998-.975 1.203-.18.205-.36.23-.667.077-.307-.154-1.296-.478-2.469-1.524-.913-.814-1.53-1.82-1.71-2.127-.18-.307-.02-.473.135-.626.138-.138.307-.36.46-.54.154-.18.205-.307.307-.512.103-.205.052-.384-.026-.538-.077-.154-.692-1.667-.948-2.283-.25-.6-.503-.519-.692-.529-.18-.008-.384-.01-.59-.01-.204 0-.537.077-.818.384-.282.307-1.075 1.05-1.075 2.563s1.1 2.973 1.254 3.178c.154.205 2.166 3.31 5.25 4.64.734.317 1.306.507 1.753.649.736.234 1.406.201 1.936.122.59-.088 1.818-.743 2.075-1.46.256-.718.256-1.332.18-1.46-.077-.128-.282-.205-.59-.359z"/></svg>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tiro de Arrastre para {nombre} en Colombia | {modelos_title}</title>
<meta name="description" content="Tiro de arrastre para {nombre} {modelos_desc}. Enganches Aerohitch, Defender y Easyhitch instalados a la medida, sin perforar el chasis. Cotiza por WhatsApp.">
<link rel="canonical" href="https://www.tirodearrastre.co/marcas/{slug}.html">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:title" content="Tiro de Arrastre para {nombre} en Colombia">
<meta property="og:description" content="Enganches para remolque a la medida de cada modelo {nombre} vendido en Colombia.">
<meta property="og:url" content="https://www.tirodearrastre.co/marcas/{slug}.html">
<meta property="og:image" content="https://www.tirodearrastre.co/assets/img/marcas/{slug}-cover.jpg">
<link rel="icon" href="../favicon.ico" sizes="any">
<link rel="manifest" href="../manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../assets/css/main.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{"@type":"ListItem","position":1,"name":"Inicio","item":"https://www.tirodearrastre.co/"}},
    {{"@type":"ListItem","position":2,"name":"Marcas","item":"https://www.tirodearrastre.co/marcas/"}},
    {{"@type":"ListItem","position":3,"name":"{nombre}","item":"https://www.tirodearrastre.co/marcas/{slug}.html"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type":"Question","name":"¿Tienen tiro de arrastre para {faq_modelo1}?","acceptedAnswer":{{"@type":"Answer","text":"Sí, contamos con referencias específicas para {modelos_desc} y otros modelos {nombre} vendidos en Colombia."}}}},
    {{"@type":"Question","name":"¿El tiro de arrastre para {nombre} afecta la garantía de fábrica?","acceptedAnswer":{{"@type":"Answer","text":"La instalación respeta los puntos de anclaje originales del chasis y no perfora ni modifica la estructura del vehículo."}}}},
    {{"@type":"Question","name":"¿Cuánto peso puede remolcar un {nombre} con tiro de arrastre?","acceptedAnswer":{{"@type":"Answer","text":"La capacidad de arrastre depende del modelo y motor específico; la confirmamos exactamente al cotizar por WhatsApp."}}}}
  ]
}}
</script>
</head>
<body>
<a class="skip-link" href="#contenido">Saltar al contenido</a>

<header class="site-header">
  <div class="container">
    <a href="../index.html" class="logo" aria-label="Tiro de Arrastre Colombia — Inicio">TIRO <span class="marca-tag">DE</span> ARRASTRE</a>
    <nav class="nav-principal" aria-label="Navegación principal">
      <a href="../productos/tiros-de-arrastre.html">Tiros de Arrastre</a>
      <a href="../productos/portabicicletas.html">Portabicicletas</a>
      <a href="../productos/parrillas-de-techo.html">Parrillas de Techo</a>
      <a href="../productos/cubre-carter.html">Cubre Cárter</a>
      <a href="../marcas/index.html">Marcas</a>
      <a href="../contacto.html">Contacto</a>
    </nav>
    <div class="nav-cta">
      <a href="#" class="btn btn-outline" data-wa="Cotización tiro de arrastre {nombre}">WhatsApp</a>
      <button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false">☰</button>
    </div>
  </div>
</header>

<main id="contenido">
  <div class="container breadcrumb">
    <a href="../index.html">Inicio</a><span class="sep">/</span><a href="../marcas/index.html">Marcas</a><span class="sep">/</span>{nombre}
  </div>

  <section class="hero" style="padding-top:24px">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow">Tiro de arrastre por marca</p>
        <h1>Tiro de arrastre para <span class="cobre">{nombre}</span></h1>
        <p class="hero-sub">Enganches para remolque fabricados a la medida de cada modelo {nombre} vendido en Colombia: {modelos_desc}. Instalación profesional sin perforar el chasis.</p>
        <div class="hero-cta">
          <a href="#" class="btn btn-cobre" data-wa="Quiero cotizar un tiro de arrastre para mi {nombre}">Cotizar para mi {nombre}</a>
          <a href="#modelos" class="btn btn-outline">Ver modelos disponibles</a>
        </div>
      </div>
      <div class="hero-visual" style="background-image:url('/assets/img/marcas/{slug}-hero.jpg')">
        <span class="tag">Tiro de arrastre {faq_modelo1}</span>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Descripción</p>
        <h2>Enganche a la medida de tu {nombre}</h2>
        <p>{parrafo_intro}</p>
        <p>Trabajamos con las marcas Aerohitch, Defender y Easyhitch, siguiendo los puntos de anclaje originales del chasis de cada {nombre} para que el enganche quede firme, alineado y sin comprometer la estructura de fábrica.</p>
      </div>

      <div class="grid-3">
        <div class="card"><span class="num">Ventaja</span><h3>Ajuste exacto por modelo</h3><p>Cada referencia se fabrica para el chasis específico de tu versión de {nombre}, no un modelo universal.</p></div>
        <div class="card"><span class="num">Ventaja</span><h3>Sin perforaciones</h3><p>La instalación usa los puntos de anclaje originales del vehículo.</p></div>
        <div class="card"><span class="num">Ventaja</span><h3>Compatible con portabicicletas</h3><p>El receptor estándar admite portabicicletas Aerobike y Thule.</p></div>
        <div class="card"><span class="num">Beneficio</span><h3>Respaldo de garantía</h3><p>Producto e instalación quedan cubiertos por nuestra garantía.</p></div>
        <div class="card"><span class="num">Beneficio</span><h3>Asesoría de capacidad</h3><p>Te confirmamos el peso máximo de arrastre según tu motor y versión.</p></div>
        <div class="card"><span class="num">Beneficio</span><h3>Instalación en el día</h3><p>La mayoría de instalaciones para {nombre} se completan en una sola jornada.</p></div>
      </div>
    </div>
  </section>

  <section class="seccion-oscura" id="modelos">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Modelos {nombre} disponibles</p>
        <h2>Encuentra tu modelo</h2>
      </div>
      <div class="grid-marcas">
        {chips_modelos}
      </div>
    </div>
  </section>

  <section>
    <div class="container" style="max-width:820px">
      <div class="section-head centro">
        <p class="eyebrow" style="justify-content:center">Preguntas frecuentes</p>
        <h2>Tiro de arrastre {nombre}</h2>
      </div>
      <div class="faq-lista">
        <div class="faq-item" data-abierto="false">
          <button class="faq-pregunta" aria-expanded="false">¿Tienen tiro de arrastre para {faq_modelo1}?</button>
          <div class="faq-respuesta"><p>Sí, contamos con referencias específicas para {modelos_desc} y otros modelos {nombre} vendidos en Colombia.</p></div>
        </div>
        <div class="faq-item" data-abierto="false">
          <button class="faq-pregunta" aria-expanded="false">¿El tiro de arrastre para {nombre} afecta la garantía de fábrica?</button>
          <div class="faq-respuesta"><p>La instalación respeta los puntos de anclaje originales del chasis y no perfora ni modifica la estructura del vehículo.</p></div>
        </div>
        <div class="faq-item" data-abierto="false">
          <button class="faq-pregunta" aria-expanded="false">¿Cuánto peso puede remolcar un {nombre} con tiro de arrastre?</button>
          <div class="faq-respuesta"><p>La capacidad de arrastre depende del modelo y motor específico; la confirmamos exactamente al cotizar por WhatsApp.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion-oscura text-center">
    <div class="container">
      <h2>Cotiza el tiro de arrastre para tu {nombre}</h2>
      <p style="color:var(--acero-300);max-width:50ch;margin-inline:auto">Escríbenos con el modelo y año exactos de tu vehículo y te confirmamos la referencia disponible.</p>
      <a href="#" class="btn btn-cobre" data-wa="Quiero cotizar un tiro de arrastre para mi {nombre}" style="margin-top:1em">Cotizar por WhatsApp</a>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="logo" style="margin-bottom:1em">TIRO <span class="marca-tag">DE</span> ARRASTRE</div>
        <p style="max-width:32ch;font-size:.9rem">Tiros de arrastre, portabicicletas y accesorios para camionetas en Colombia.</p>
      </div>
      <div><h4>Productos</h4><ul>
        <li><a href="../productos/tiros-de-arrastre.html">Tiros de arrastre</a></li>
        <li><a href="../productos/portabicicletas.html">Portabicicletas</a></li>
      </ul></div>
      <div><h4>Empresa</h4><ul>
        <li><a href="../marcas/index.html">Marcas</a></li>
        <li><a href="../blog/index.html">Blog</a></li>
        <li><a href="../contacto.html">Contacto</a></li>
      </ul></div>
      <div><h4>Legal</h4><ul>
        <li><a href="../legal/privacidad.html">Política de privacidad</a></li>
        <li><a href="../legal/terminos.html">Términos y condiciones</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="anio"></span> Tiro de Arrastre Colombia.</span>
      <span>WhatsApp: +57 318 785 6238</span>
    </div>
  </div>
</footer>

<a href="#" class="wa-flotante" data-wa="Cotización tiro de arrastre {nombre}" aria-label="Escribir por WhatsApp">
""" + WA_ICON + """
</a>

<script src="../assets/js/main.js"></script>
<script>document.getElementById('anio').textContent = new Date().getFullYear();</script>
</body>
</html>
"""

# slug de marca -> {modelo: slug de archivo de modelo} para los modelos que ya tienen página propia con fotos reales
MODELOS_CON_PAGINA = {
    "chevrolet": {"Tracker": "tracker", "Traverse": "traverse", "Onix": "onix", "Blazer EV": "blazer", "Colorado": "colorado", "Sail": "sail", "Aveo": "aveo"},
    "audi": {"Q3": "q3", "Q5": "q5"},
    "hyundai": {"Kona": "kona", "Tucson": "tucson"},
    "ford": {"Bronco Sport": "bronco-sport", "Explorer": "explorer", "Escape": "escape", "EcoSport": "ecosport"},
    "peugeot": {"3008": "3008"},
    "subaru": {"Forester": "forester"},
    "volvo": {"XC40": "xc40", "XC60": "xc60"},
    "mazda": {"CX-5": "cx5", "CX-30": "cx30", "BT-50": "bt50"},
    "renault": {"Duster": "duster", "Arkana": "arkana", "Koleos": "koleos"},
    "kia": {"EV9": "ev9"},
    "nissan": {"X-Trail": "xtrail", "Qashqai": "qashqai"},
    "suzuki": {"Jimny": "jimny"},
    "volkswagen": {"Gol": "gol"},
    "honda": {"CR-V": "crv"},
    "mitsubishi": {"Outlander": "outlander"},
    "jetour": {"X70": "x70"},
    "seat": {"Arona": "arona", "Ateca": "ateca", "Ibiza": "ibiza"},
    "jeep": {"Renegade": "renegade", "Compass": "compass", "Wrangler": "wrangler", "Cherokee": "cherokee"},
}

# slug, nombre, [modelos], parrafo_intro
MARCAS = [
    ("mazda", "Mazda", ["CX-5", "CX-30", "CX-3", "BT-50", "Mazda 3", "Mazda 2"],
     "Mazda combina camionetas como la BT-50 con SUV muy vendidos en Colombia como la CX-5 y la CX-30. Cada tiro de arrastre se selecciona según el modelo, la versión y el año exactos del vehículo."),
    ("renault", "Renault", ["Duster", "Koleos", "Arkana", "Oroch", "Sandero Stepway", "Captur"],
     "Renault es una de las marcas más vendidas en Colombia, con la Duster y la Oroch entre los modelos más solicitados para instalar tiro de arrastre. Fabricamos cada referencia a la medida del chasis específico."),
    ("chevrolet", "Chevrolet", ["Tracker", "Traverse", "Onix", "Blazer EV", "Colorado", "Sail", "Aveo", "Trailblazer", "Captiva", "Groove", "Spark GT"],
     "Chevrolet mantiene una de las mayores participaciones del mercado colombiano, con SUV como la Tracker y la Trailblazer entre los modelos que más solicitan tiro de arrastre para remolque."),
    ("kia", "Kia", ["Sportage", "Seltos", "Sorento", "EV9", "Soluto"],
     "Kia ofrece SUV muy populares en Colombia como la Sportage y la Seltos. Fabricamos el tiro de arrastre a la medida exacta del chasis de cada versión."),
    ("hyundai", "Hyundai", ["Kona", "Tucson", "Santa Fe", "Creta", "Grand i10"],
     "Hyundai es una de las marcas asiáticas con mayor presencia en Colombia, con la Tucson y la Creta entre los modelos más solicitados para tiro de arrastre."),
    ("nissan", "Nissan", ["Kicks", "X-Trail", "Qashqai", "Frontier", "Versa"],
     "Nissan combina camionetas como la Frontier con SUV como la X-Trail y la Kicks, todos con referencias específicas de tiro de arrastre en nuestro catálogo."),
    ("suzuki", "Suzuki", ["Grand Vitara", "Jimny", "Swift", "S-Presso"],
     "Suzuki es reconocida en Colombia por modelos todoterreno como el Jimny y SUV como la Grand Vitara, ambos con alta demanda de tiro de arrastre para remolque liviano."),
    ("volkswagen", "Volkswagen", ["Tiguan", "T-Cross", "Amarok", "Gol", "Taos"],
     "Volkswagen ofrece desde la camioneta Amarok hasta SUV como la Tiguan y la T-Cross, todos con tiro de arrastre fabricado a la medida del chasis."),
    ("ford", "Ford", ["Bronco Sport", "Explorer", "Escape", "Territory", "Ranger", "EcoSport"],
     "Ford es reconocida en Colombia por la Ranger, una de las camionetas más usadas para remolque, además de SUV como la Territory y la Explorer."),
    ("jeep", "Jeep", ["Renegade", "Compass", "Wrangler", "Cherokee", "Grand Cherokee"],
     "Jeep es sinónimo de vehículos todoterreno en Colombia, con el Wrangler, el Compass y el Renegade entre los modelos más solicitados para instalar tiro de arrastre."),
    ("honda", "Honda", ["CR-V", "HR-V", "Pilot"],
     "Honda ofrece SUV familiares como la CR-V y la HR-V, con tiro de arrastre fabricado a la medida del chasis de cada versión vendida en Colombia."),
    ("byd", "BYD", ["Song Plus", "Yuan Plus", "Tan"],
     "BYD ha crecido rápidamente en el mercado colombiano con SUV eléctricos e híbridos como el Song Plus y el Yuan Plus, para los que ya contamos con referencias de tiro de arrastre."),
    ("jac", "JAC", ["S3", "S2", "T6", "T8"],
     "JAC combina SUV como el S3 con camionetas como la T6, ambos con alta demanda de tiro de arrastre en el mercado colombiano."),
    ("dfsk", "DFSK", ["Glory 580", "Glory 500", "K07"],
     "DFSK ha ganado terreno en Colombia con SUV como el Glory 580, para el que ya contamos con referencia específica de tiro de arrastre."),
    ("changan", "Changan", ["CS35", "CS55", "Hunter"],
     "Changan ofrece SUV como el CS35 y el CS55, y la camioneta Hunter, todos con tiro de arrastre fabricado a la medida del chasis."),
    ("jetour", "Jetour", ["X70", "Dashing", "X90"],
     "Jetour es una de las marcas chinas de más rápido crecimiento en Colombia, con el X70 y el Dashing entre los modelos más consultados para tiro de arrastre."),
    ("mitsubishi", "Mitsubishi", ["Outlander", "ASX", "L200"],
     "Mitsubishi mantiene una fuerte tradición todoterreno en Colombia con la camioneta L200 y SUV como el Outlander y el ASX."),
    ("subaru", "Subaru", ["Forester", "XV", "Outback"],
     "Subaru es reconocida por su tracción integral de fábrica, con el Forester y el Outback entre los modelos más solicitados para tiro de arrastre en Colombia."),
    ("peugeot", "Peugeot", ["2008", "3008", "5008", "Landtrek"],
     "Peugeot combina SUV como el 3008 y el 5008 con la camioneta Landtrek, todos con tiro de arrastre disponible a la medida del chasis."),
    ("audi", "Audi", ["Q3", "Q5", "A3", "A4"],
     "Audi es una de las marcas premium con mayor presencia en Colombia, con el Q3 como una de las SUV compactas más solicitadas para tiro de arrastre. Fabricamos cada referencia a la medida exacta del chasis."),
    ("volvo", "Volvo", ["XC40", "XC60", "XC90"],
     "Volvo es una de las marcas premium suecas con mayor presencia en Colombia, con el XC40 y el XC60 como sus SUV más solicitadas para tiro de arrastre. Fabricamos cada referencia a la medida exacta del chasis."),
    ("seat", "SEAT", ["Arona", "Ateca", "Ibiza", "León"],
     "SEAT es una de las marcas españolas con presencia creciente en Colombia, con la Arona y la Ateca como sus SUV más solicitadas para tiro de arrastre. Fabricamos cada referencia a la medida exacta del chasis."),
]

os.makedirs(OUT_DIR, exist_ok=True)
generadas = []
for slug, nombre, modelos, intro in MARCAS:
    modelos_desc = ", ".join(modelos[:-1]) + " y " + modelos[-1] if len(modelos) > 1 else modelos[0]
    modelos_title = ", ".join(modelos[:3])
    faq_modelo1 = f"{nombre} {modelos[0]}"
    enlaces_modelo = MODELOS_CON_PAGINA.get(slug, {})
    chips_list = []
    for m in modelos:
        if m in enlaces_modelo:
            chips_list.append(
                f'<a class="chip-marca" href="../productos/tiro-de-arrastre-{slug}-{enlaces_modelo[m]}.html">{m}</a>'
            )
        else:
            chips_list.append(
                f'<a class="chip-marca" href="#" data-wa="Tiro de arrastre {nombre} {m}">{m}</a>'
            )
    chips = "\n        ".join(chips_list)
    html = TEMPLATE.format(
        nombre=nombre, slug=slug, modelos_desc=modelos_desc, modelos_title=modelos_title,
        faq_modelo1=faq_modelo1, chips_modelos=chips, parrafo_intro=intro,
    )
    path = os.path.join(OUT_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    generadas.append(slug)

print(f"Generadas {len(generadas)} páginas:", generadas)
