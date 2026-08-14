# -*- coding: utf-8 -*-
"""Genera páginas individuales de modelo (marca + modelo) con fotos reales de instalación.
Se guardan en productos/tiro-de-arrastre-{marca}-{modelo}.html
Si necesitas agregar un modelo nuevo, añade una entrada al listado MODELOS y vuelve a ejecutar."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "productos")

WA_ICON = '''<svg viewBox="0 0 32 32"><path d="M16.001 3C9.373 3 4 8.373 4 15c0 2.386.71 4.607 1.929 6.464L4 29l7.73-1.9A11.94 11.94 0 0 0 16.001 27C22.63 27 28 21.627 28 15S22.63 3 16.001 3zm0 21.818a9.78 9.78 0 0 1-4.986-1.364l-.358-.213-4.59 1.128 1.15-4.47-.233-.365A9.77 9.77 0 0 1 5.182 15c0-5.964 4.854-10.818 10.819-10.818S26.818 9.036 26.818 15 21.965 24.818 16.001 24.818zm5.61-7.98c-.307-.154-1.818-.897-2.1-.999-.282-.102-.487-.153-.692.154-.205.307-.795.998-.975 1.203-.18.205-.36.23-.667.077-.307-.154-1.296-.478-2.469-1.524-.913-.814-1.53-1.82-1.71-2.127-.18-.307-.02-.473.135-.626.138-.138.307-.36.46-.54.154-.18.205-.307.307-.512.103-.205.052-.384-.026-.538-.077-.154-.692-1.667-.948-2.283-.25-.6-.503-.519-.692-.529-.18-.008-.384-.01-.59-.01-.204 0-.537.077-.818.384-.282.307-1.075 1.05-1.075 2.563s1.1 2.973 1.254 3.178c.154.205 2.166 3.31 5.25 4.64.734.317 1.306.507 1.753.649.736.234 1.406.201 1.936.122.59-.088 1.818-.743 2.075-1.46.256-.718.256-1.332.18-1.46-.077-.128-.282-.205-.59-.359z"/></svg>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tiro de Arrastre para {marca} {modelo} en Colombia | Instalación a la Medida</title>
<meta name="description" content="Tiro de arrastre para {marca} {modelo} fabricado a la medida del chasis. Enganche Aerohitch instalado sin perforar, con fotos reales de instalación. Cotiza por WhatsApp.">
<link rel="canonical" href="https://www.tirodearrastre.co/productos/tiro-de-arrastre-{slug}.html">
<meta name="robots" content="index, follow">
<meta property="og:type" content="product">
<meta property="og:title" content="Tiro de Arrastre para {marca} {modelo} en Colombia">
<meta property="og:description" content="Enganche para remolque instalado a la medida del {marca} {modelo}.">
<meta property="og:url" content="https://www.tirodearrastre.co/productos/tiro-de-arrastre-{slug}.html">
<meta property="og:image" content="https://www.tirodearrastre.co/assets/img/instalacion/{hero_img}">
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
    {{"@type":"ListItem","position":3,"name":"{marca}","item":"https://www.tirodearrastre.co/marcas/{marca_slug}.html"}},
    {{"@type":"ListItem","position":4,"name":"{modelo}","item":"https://www.tirodearrastre.co/productos/tiro-de-arrastre-{slug}.html"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Tiro de Arrastre para {marca} {modelo}",
  "brand": {{"@type":"Brand","name":"Aerohitch"}},
  "description": "Tiro de arrastre fabricado a la medida del chasis del {marca} {modelo}, instalado sin perforar la carrocería.",
  "category": "Enganches para remolque",
  "offers": {{
    "@type": "Offer",
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
  "mainEntity": [
    {{"@type":"Question","name":"¿El tiro de arrastre para {marca} {modelo} viene a la medida?","acceptedAnswer":{{"@type":"Answer","text":"Sí, se fabrica según el chasis específico del {marca} {modelo}, usando los puntos de anclaje originales del vehículo."}}}},
    {{"@type":"Question","name":"¿Puedo instalar portabicicletas en el tiro de arrastre de mi {marca} {modelo}?","acceptedAnswer":{{"@type":"Answer","text":"Sí, el receptor estándar admite portabicicletas Aerobike y Thule, además de otros accesorios de enganche."}}}},
    {{"@type":"Question","name":"¿Cuánto tarda la instalación en un {marca} {modelo}?","acceptedAnswer":{{"@type":"Answer","text":"La mayoría de instalaciones en {marca} {modelo} se completan en el mismo día, en nuestro local o en el punto que coordinemos contigo."}}}}
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
      <a href="#" class="btn btn-outline" data-wa="Cotización tiro de arrastre {marca} {modelo}">WhatsApp</a>
      <button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false">☰</button>
    </div>
  </div>
</header>

<main id="contenido">
  <div class="container breadcrumb">
    <a href="../index.html">Inicio</a><span class="sep">/</span><a href="../marcas/index.html">Marcas</a><span class="sep">/</span><a href="../marcas/{marca_slug}.html">{marca}</a><span class="sep">/</span>{modelo}
  </div>

  <section class="hero" style="padding-top:24px">
    <div class="container hero-grid">
      <div>
        <p class="eyebrow">Tiro de arrastre por modelo</p>
        <h1>Tiro de arrastre para <span class="cobre">{marca} {modelo}</span></h1>
        <p class="hero-sub">{intro}</p>
        <div class="hero-cta">
          <a href="#" class="btn btn-cobre" data-wa="Quiero cotizar un tiro de arrastre para mi {marca} {modelo}">Cotizar para mi {modelo}</a>
          <a href="../marcas/{marca_slug}.html" class="btn btn-outline">Ver más modelos {marca}</a>
        </div>
      </div>
      <div class="hero-visual" style="background-image:url('../assets/img/instalacion/{hero_img}')">
        <span class="tag">Instalación real en {marca} {modelo}</span>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Descripción</p>
        <h2>Enganche fabricado para tu {marca} {modelo}</h2>
        <p>{parrafo}</p>
        <p>Trabajamos con Aerohitch, siguiendo los puntos de anclaje originales del chasis del {marca} {modelo} para que el enganche quede firme, alineado y sin comprometer la estructura de fábrica ni la garantía del vehículo.</p>
      </div>

      <div class="grid-3">
        <div class="card"><span class="num">Ventaja</span><h3>Ajuste exacto</h3><p>Fabricado para el chasis específico del {marca} {modelo}, no un enganche universal.</p></div>
        <div class="card"><span class="num">Ventaja</span><h3>Sin perforaciones</h3><p>La instalación usa los puntos de anclaje originales del vehículo.</p></div>
        <div class="card"><span class="num">Ventaja</span><h3>Compatible con accesorios</h3><p>El receptor estándar admite portabicicletas Aerobike, Thule y otros accesorios de enganche.</p></div>
        <div class="card"><span class="num">Beneficio</span><h3>Respaldo de garantía</h3><p>Producto e instalación quedan cubiertos por nuestra garantía.</p></div>
        <div class="card"><span class="num">Beneficio</span><h3>Asesoría de capacidad</h3><p>Te confirmamos el peso máximo de arrastre según tu versión y motor exactos.</p></div>
        <div class="card"><span class="num">Beneficio</span><h3>Instalación en el día</h3><p>La mayoría de instalaciones en {marca} {modelo} se completan en una sola jornada.</p></div>
      </div>
    </div>
  </section>
{galeria}
  <section>
    <div class="container" style="max-width:820px">
      <div class="section-head centro">
        <p class="eyebrow" style="justify-content:center">Preguntas frecuentes</p>
        <h2>Tiro de arrastre {marca} {modelo}</h2>
      </div>
      <div class="faq-lista">
        <div class="faq-item" data-abierto="false">
          <button class="faq-pregunta" aria-expanded="false">¿El tiro de arrastre para {marca} {modelo} viene a la medida?</button>
          <div class="faq-respuesta"><p>Sí, se fabrica según el chasis específico del {marca} {modelo}, usando los puntos de anclaje originales del vehículo.</p></div>
        </div>
        <div class="faq-item" data-abierto="false">
          <button class="faq-pregunta" aria-expanded="false">¿Puedo instalar portabicicletas en el tiro de arrastre de mi {marca} {modelo}?</button>
          <div class="faq-respuesta"><p>Sí, el receptor estándar admite portabicicletas Aerobike y Thule, además de otros accesorios de enganche.</p></div>
        </div>
        <div class="faq-item" data-abierto="false">
          <button class="faq-pregunta" aria-expanded="false">¿Cuánto tarda la instalación en un {marca} {modelo}?</button>
          <div class="faq-respuesta"><p>La mayoría de instalaciones en {marca} {modelo} se completan en el mismo día, en nuestro local o en el punto que coordinemos contigo.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion-oscura text-center">
    <div class="container">
      <h2>Cotiza el tiro de arrastre para tu {marca} {modelo}</h2>
      <p style="color:var(--acero-300);max-width:50ch;margin-inline:auto">Escríbenos con la versión y año exactos de tu {modelo} y te confirmamos la referencia disponible.</p>
      <a href="#" class="btn btn-cobre" data-wa="Quiero cotizar un tiro de arrastre para mi {marca} {modelo}" style="margin-top:1em">Cotizar por WhatsApp</a>
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

<a href="#" class="wa-flotante" data-wa="Cotización tiro de arrastre {marca} {modelo}" aria-label="Escribir por WhatsApp">
""" + WA_ICON + """
</a>

<script src="../assets/js/main.js"></script>
<script>document.getElementById('anio').textContent = new Date().getFullYear();</script>
</body>
</html>
"""

GALERIA_BLOCK = """  <section class="seccion-oscura">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Fotos reales</p>
        <h2>Instalación en {marca} {modelo}</h2>
      </div>
      <div class="grid-galeria">
        {imgs}
      </div>
    </div>
  </section>
"""

# marca_slug, marca_nombre, modelo_slug, modelo_nombre, hero_img, [galeria_imgs], parrafo
MODELOS = [
    ("toyota", "Toyota", "prado", "Prado",
     "prado-tiro-arrastre-2026.jpg", [
         "prado-detalle-aerohitch.jpg",
         "prado-instalada.jpg",
         ("prado-remolque-aerobike-motos.jpg", "Toyota Prado remolcando un remolque AERO Bike abatible para motos"),
         "prado-portamotos.jpg",
         "prado-portamotos-2.jpg",
     ],
     "La Toyota Prado, incluida la generación 2026, es una de las SUV todoterreno más usadas en Colombia para remolque pesado y transporte de motos o bicicletas. Fabricamos el tiro de arrastre a la medida exacta de su chasis, compatible incluso con remolques abatibles para motos."),
    ("toyota", "Toyota", "hilux", "Hilux",
     "hilux-instalada.jpg", [
         "hilux-detalle-aerohitch.jpg",
         ("hilux-roja-detalle-aerohitch.jpg", "Detalle del receptor Aero Hitch en Toyota Hilux 2025"),
         "hilux-portamotos.jpg",
     ],
     "La Toyota Hilux es una de las camionetas más vendidas en Colombia, con alta demanda de tiro de arrastre para remolque de carga, portamotos y portabicicletas."),
    ("toyota", "Toyota", "fortuner", "Fortuner",
     "fortuner-instalada.jpg", [
         "fortuner-detalle-aerohitch.jpg",
         ("fortuner-portabicicletas-thule.jpg", "Toyota Fortuner con portabicicletas Thule VeloCompact instalado en el tiro de arrastre"),
     ],
     "La Toyota Fortuner combina espacio familiar con capacidad real de remolque. Fabricamos el enganche a la medida exacta de su chasis, siguiendo los puntos de anclaje de fábrica, y es compatible con portabicicletas de enganche como el Thule VeloCompact."),
    ("toyota", "Toyota", "corolla-cross", "Corolla Cross",
     "corolla-cross-instalada.jpg", [],
     "La Toyota Corolla Cross es una de las SUV compactas más vendidas en Colombia. Su tiro de arrastre permite instalar portabicicletas y accesorios de enganche sin perforar la carrocería."),
    ("renault", "Renault", "duster", "Duster",
     "duster-instalada.jpg", ["duster-hitch-detalle.jpg", "duster-hibrida-instalada.jpg"],
     "La Renault Duster, incluida su versión híbrida E-Tech, es una de las SUV más vendidas en Colombia. Fabricamos el tiro de arrastre a la medida de cada versión."),
    ("renault", "Renault", "arkana", "Arkana",
     "arkana2-instalada.jpg", ["arkana2-detalle-aerohitch.jpg", "arkana2-portabicicletas-2.jpg"],
     "La Renault Arkana combina un diseño tipo coupé con la posibilidad de instalar tiro de arrastre para portabicicletas y otros accesorios de enganche."),
    ("renault", "Renault", "koleos", "Koleos",
     "koleos-instalada.jpg", ["koleos-detalle-aerohitch.jpg"],
     "La Renault Koleos es la SUV grande de la marca en Colombia, con buena capacidad de remolque y compatibilidad con nuestro tiro de arrastre a la medida."),
    ("nissan", "Nissan", "xtrail", "X-Trail",
     "xtrail-instalada.jpg", ["xtrail-instalada-2.jpg"],
     "La Nissan X-Trail es una SUV familiar muy solicitada en Colombia para instalar tiro de arrastre y transportar portabicicletas en viajes largos."),
    ("nissan", "Nissan", "qashqai", "Qashqai",
     "nissan-qashqai-instalada.jpg", ["nissan-qashqai-detalle-aerohitch.jpg", "nissan-qashqai-detalle-1.jpg"],
     "La Nissan Qashqai es una SUV compacta con alta demanda de tiro de arrastre para portabicicletas y accesorios de enganche en Colombia."),
    ("mitsubishi", "Mitsubishi", "outlander", "Outlander",
     "outlander-instalada.jpg", ["outlander-instalada-2.jpg", "outlander-instalada-3.jpg"],
     "La Mitsubishi Outlander es una SUV familiar con buena capacidad de remolque, ideal para tiro de arrastre fabricado a la medida de su chasis."),
    ("jetour", "Jetour", "x70", "X70",
     "jetour-x70-instalada.jpg", ["jetour-x70-instalada-2.jpg", "jetour-x70-bicicletas.jpg"],
     "El Jetour X70 es uno de los modelos chinos de mayor crecimiento en Colombia. Ya contamos con referencia de tiro de arrastre fabricada a la medida de su chasis, compatible con portabicicletas."),
    ("kia", "Kia", "ev9", "EV9",
     "ev9-portabicicletas-4.jpg", [],
     "El Kia EV9 es una SUV eléctrica de gran tamaño. Su tiro de arrastre permite instalar portabicicletas Aerobike de hasta 4 bicicletas sin comprometer la batería ni la carrocería."),
    ("suzuki", "Suzuki", "jimny", "Jimny",
     "jimny2-instalado.jpg", [
         "jimny2-detalle-aerohitch.jpg",
         "jimny2-instalado-2.jpg",
         "jimny-canasta-hibrida.jpg",
         ("jimny2-parrilla-techo.jpg", "Parrilla de techo AERO instalada en Suzuki Jimny"),
     ],
     "El Suzuki Jimny es uno de los todoterreno más queridos en Colombia. Fabricamos su tiro de arrastre a la medida, con opción de canasta trasera para remolque liviano, y también instalamos parrilla de techo AERO para carga adicional."),
    ("volkswagen", "Volkswagen", "gol", "Gol",
     "gol-instalada.jpg", ["gol-portabicicletas-2.jpg"],
     "El Volkswagen Gol es uno de los modelos compactos más comunes en Colombia. Su tiro de arrastre es ideal para instalar portabicicletas Aerobike en viajes familiares."),
    ("mazda", "Mazda", "cx5", "CX-5",
     "cx5-instalada.jpg", ["cx5-instalada-2.jpg", "cx5-portabicicletas-4.jpg"],
     "La Mazda CX-5 es una de las SUV más vendidas en Colombia. Fabricamos su tiro de arrastre a la medida, compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
    ("mazda", "Mazda", "cx30", "CX-30",
     "cx30-instalada.jpg", ["cx30-detalle-aerohitch.jpg", "cx30-portabicicletas-4.jpg"],
     "La Mazda CX-30 es una SUV compacta muy popular en Colombia. Su tiro de arrastre se fabrica a la medida del chasis, compatible con portabicicletas Aerobike."),
    ("mazda", "Mazda", "bt50", "BT-50",
     "bt50-instalada.jpg", ["bt50-detalle-aerohitch.jpg", "bt50-instalada-2.jpg"],
     "La Mazda BT-50 es una camioneta con alta capacidad de remolque. Fabricamos su tiro de arrastre a la medida del chasis para carga pesada y accesorios de enganche."),
    ("honda", "Honda", "crv", "CR-V",
     "crv-instalada.jpg", ["crv-portabicicletas-4.jpg", "crv-instalada-2.jpg"],
     "La Honda CR-V es una SUV familiar muy solicitada en Colombia para tiro de arrastre e instalación de portabicicletas Aerobike de hasta 4 bicicletas."),
    ("chevrolet", "Chevrolet", "tracker", "Tracker",
     "tracker-instalada.jpg", [
         "tracker-detalle-aerohitch.jpg",
         ("tracker-portabicicletas-4bicis.jpg", "Chevrolet Tracker con portabicicletas Aerobike 4 bicicletas instalado"),
     ],
     "La Chevrolet Tracker es una de las SUV más vendidas en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
    ("chevrolet", "Chevrolet", "traverse", "Traverse",
     "traverse-portabicicletas-4bicis.jpg", [
         ("traverse-detalle-portabicicletas.jpg", "Detalle del portabicicletas Aerobike 4 bicicletas en Chevrolet Traverse"),
     ],
     "La Chevrolet Traverse es una SUV grande de 7 puestos. Su tiro de arrastre es ideal para instalar portabicicletas Aerobike de hasta 4 bicicletas en viajes familiares largos."),
    ("chevrolet", "Chevrolet", "onix", "Onix",
     "onix-instalada.jpg", [
         "onix-detalle-enganche.jpg",
         ("onix-portabicicletas-3bicis.jpg", "Chevrolet Onix con portabicicletas Aerobike 3 bicicletas instalado"),
     ],
     "El Chevrolet Onix es uno de los modelos compactos más vendidos en Colombia. Su tiro de arrastre se instala sin perforar la carrocería y es compatible con portabicicletas Aerobike de hasta 3 bicicletas."),
    ("chevrolet", "Chevrolet", "blazer", "Blazer EV",
     "blazer-instalada.jpg", ["blazer-detalle-aerohitch.jpg", "blazer-detalle-aerohitch-2.jpg"],
     "La Chevrolet Blazer 2026 es la SUV eléctrica de nueva generación de la marca en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, instalado sin perforar la carrocería ni afectar la garantía de fábrica."),
    ("chevrolet", "Chevrolet", "colorado", "Colorado",
     "colorado-instalada.jpg", ["colorado-detalle-aerohitch.jpg", "colorado-detalle-placa-aerohitch.jpg"],
     "La Chevrolet Colorado es una camioneta con motor Duramax Diesel de alta capacidad de remolque. Fabricamos su tiro de arrastre a la medida del chasis para carga pesada y accesorios de enganche."),
    ("chevrolet", "Chevrolet", "sail", "Sail",
     "sail-instalada.jpg", [
         "sail-detalle-portabicicletas-2.jpg",
         ("sail-portabicicletas-3bicis.jpg", "Chevrolet Sail con portabicicletas Aerobike 3 bicicletas instalado"),
         "sail-detalle-portabicicletas.jpg",
     ],
     "El Chevrolet Sail es uno de los sedanes más usados en flotas y para uso particular en Colombia. Su tiro de arrastre es compatible con portabicicletas Aerobike de hasta 3 bicicletas."),
    ("chevrolet", "Chevrolet", "aveo", "Aveo",
     "aveo-portabicicletas-3bicis.jpg", [
         ("chevy-portabicicletas-4bicis.jpg", "Chevrolet Aveo con portabicicletas Aerobike 4 bicicletas instalado"),
     ],
     "El Chevrolet Aveo es uno de los sedanes compactos más comunes en Colombia. Su tiro de arrastre es compatible con portabicicletas Aerobike de 3 y 4 bicicletas."),
    ("audi", "Audi", "q3", "Q3",
     "q3-plateado-instalada.jpg", [
         "q3-detalle-aerohitch-2.jpg",
         ("q3-rojo-portabicicletas-3bicis.jpg", "Audi Q3 rojo con portabicicletas Aerobike 3 bicicletas instalado"),
         "q3-detalle-aerohitch.jpg",
         ("q3-plateado-portabicicletas-3bicis.jpg", "Audi Q3 plateado con portabicicletas Aerobike 3 bicicletas instalado"),
     ],
     "El Audi Q3 es una de las SUV compactas premium más solicitadas en Colombia para tiro de arrastre. Fabricamos el enganche a la medida exacta del chasis, compatible con portabicicletas Aerobike de hasta 3 bicicletas."),
    ("audi", "Audi", "q5", "Q5",
     "q5-instalada.jpg", ["q5-detalle-aerohitch.jpg", "q5-detalle-receptor.jpg"],
     "El Audi Q5 45 TFSI quattro es una de las SUV premium con mayor capacidad de remolque de la marca en Colombia. Fabricamos su tiro de arrastre a la medida exacta del chasis, sin perforar la carrocería."),
    ("hyundai", "Hyundai", "kona", "Kona",
     "kona-arena-instalada.jpg", [
         "kona-arena-detalle-aerohitch.jpg",
         ("kona-verde-portabicicletas-4bicis.jpg", "Hyundai Kona con portabicicletas Aerobike 4 bicicletas instalado"),
         "kona-verde-detalle-aerohitch.jpg",
         ("kona-verde-portabicicletas-4bicis-2.jpg", "Hyundai Kona con portabicicletas Aerobike 4 bicicletas, otro ángulo"),
     ],
     "El Hyundai Kona, incluida su versión híbrida, es una de las SUV más vendidas en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
    ("hyundai", "Hyundai", "tucson", "Tucson",
     "tucson-portabicicletas-4bicis.jpg", [
         ("tucson-detalle-aerohitch.jpg", "Detalle del receptor Aero Hitch en Hyundai Tucson 2025"),
     ],
     "El Hyundai Tucson 2025 es una de las SUV medianas más vendidas en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
    ("ford", "Ford", "bronco-sport", "Bronco Sport",
     "bronco-tiro-instalada.jpg", [
         "bronco-tiro-detalle-aerohitch.jpg",
         ("bronco-portabicicletas-4bicis.jpg", "Ford Bronco Sport con portabicicletas Aerobike 4 bicicletas instalado"),
         ("bronco-portabicicletas-4bicis-2.jpg", "Ford Bronco Sport con portabicicletas Aerobike 4 bicicletas, otra unidad"),
     ],
     "El Ford Bronco Sport es una de las SUV todoterreno más distintivas en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
    ("ford", "Ford", "explorer", "Explorer",
     "explorer-instalada.jpg", ["explorer-detalle-aerohitch.jpg"],
     "La Ford Explorer es una de las SUV grandes más solicitadas en Colombia para tiro de arrastre. Fabricamos el enganche a la medida exacta del chasis, sin perforar la carrocería."),
    ("ford", "Ford", "escape", "Escape",
     "escape-portabicicletas-6bicis-calle.jpg", [
         "escape-instalada.jpg",
         "escape-detalle-aerohitch.jpg",
         ("escape-rejilla-carga.jpg", "Ford Escape con rejilla de carga plegable instalada en el tiro de arrastre"),
         ("escape-portabicicletas-4bicis.jpg", "Ford Escape con portabicicletas Aerobike 4 bicicletas instalado"),
         ("escape-rojo-instalada.jpg", "Ford Escape Titanium Hybrid con tiro de arrastre instalado"),
         ("escape-titanium-instalada.jpg", "Ford Escape Titanium Hybrid AWD con tiro de arrastre instalado"),
         ("escape-vino-portabicicletas-6bicis.jpg", "Ford Escape con portabicicletas Aerobike 6 bicicletas instalado"),
     ],
     "La Ford Escape, incluida su versión Titanium Hybrid, es una de las SUV compactas más solicitadas en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, compatible con portabicicletas Aerobike de hasta 6 bicicletas y rejilla de carga plegable."),
    ("ford", "Ford", "ecosport", "EcoSport",
     "ecosport-negro-instalada.jpg", [
         "ecosport-negro-detalle-aerohitch.jpg",
         "ecosport-negro-detalle-placa-aerohitch.jpg",
         ("ecosport-blanco-portabicicletas-4bicis.jpg", "Ford EcoSport con portabicicletas Aerobike 4 bicicletas instalado"),
     ],
     "El Ford EcoSport es una de las SUV compactas con llanta de repuesto exterior más reconocibles en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
    ("peugeot", "Peugeot", "3008", "3008",
     "peugeot-3008-instalada.jpg", [],
     "El Peugeot 3008 es una de las SUV francesas más solicitadas en Colombia para tiro de arrastre. Fabricamos el enganche a la medida exacta del chasis, compatible con portabicicletas Aerobike."),
    ("subaru", "Subaru", "forester", "Forester",
     "forester-vino-instalada.jpg", [
         "forester-vino-detalle-aerohitch.jpg",
         ("forester-plata-instalada.jpg", "Subaru Forester Advance plateado con tiro de arrastre instalado"),
         "forester-plata-detalle-aerohitch.jpg",
         ("forester-azul-instalada.jpg", "Subaru Forester AWD con tiro de arrastre instalado"),
         ("forester-portabicicletas-4bicis.jpg", "Subaru Forester con portabicicletas Aerobike 4 bicicletas instalado"),
     ],
     "El Subaru Forester, con su tracción integral AWD de fábrica, es uno de los modelos más solicitados de la marca en Colombia para tiro de arrastre. Fabricamos el enganche a la medida exacta del chasis, compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
    ("volvo", "Volvo", "xc40", "XC40",
     "xc40-instalada.jpg", [
         "xc40-detalle-aerohitch.jpg",
         "xc40-instalada-2.jpg",
     ],
     "El Volvo XC40 T4 es una de las SUV compactas premium más solicitadas en Colombia para tiro de arrastre. Fabricamos el enganche a la medida exacta del chasis, sin perforar la carrocería."),
    ("volvo", "Volvo", "xc60", "XC60",
     "xc60-plata-instalada.jpg", [
         "xc60-plata-detalle-aerohitch.jpg",
         "xc60-plata-detalle-placa-aerohitch.jpg",
         ("xc60-plata-portabicicletas-4bicis.jpg", "Volvo XC60 con portabicicletas Thule 4 bicicletas instalado"),
         "xc60-plata-detalle-portabici.jpg",
         ("xc60-negro-portabicicletas-6bicis.jpg", "Volvo XC60 con portabicicletas Aerobike 6 bicicletas instalado"),
         "xc60-negro-portabicicletas-6bicis-2.jpg",
     ],
     "El Volvo XC60 es una de las SUV premium más solicitadas de la marca en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, compatible con portabicicletas Thule y Aerobike de hasta 6 bicicletas."),
    ("seat", "SEAT", "arona", "Arona",
     "seat-arona-instalada.jpg", [
         "seat-arona-detalle-aerohitch.jpg",
         ("seat-arona-instalada-2.jpg", "SEAT Arona con tiro de arrastre instalado, otro ángulo"),
         "seat-arona-detalle-1.jpg",
         ("seat-arona-instalada-3.jpg", "SEAT Arona con tiro de arrastre instalado, vista trasera"),
         "seat-arona-detalle-2.jpg",
         ("seat-arona-instalada-4.jpg", "SEAT Arona FR con tiro de arrastre instalado, otra unidad"),
         "seat-arona-detalle-3.jpg",
         ("seat-arona-portabicicletas-6bicis.jpg", "SEAT Arona con portabicicletas Aerobike 6 bicicletas instalado"),
     ],
     "El SEAT Arona es una de las SUV compactas españolas con mayor crecimiento en Colombia. Fabricamos su tiro de arrastre a la medida exacta del chasis, instalado sin perforar la carrocería ni afectar la garantía de fábrica, compatible con portabicicletas Aerobike de hasta 6 bicicletas."),
    ("seat", "SEAT", "ateca", "Ateca",
     "seat-ateca-portabicicletas-4bicis.jpg", [
         ("seat-ateca-portabicicletas-4bicis-2.jpg", "SEAT Ateca con portabicicletas Aerobike 4 bicicletas instalado, vista frontal"),
         "seat-ateca-detalle-aerohitch.jpg",
         ("seat-ateca-instalada.jpg", "SEAT Ateca con tiro de arrastre instalado"),
     ],
     "El SEAT Ateca es la SUV mediana de la marca en Colombia, con buena capacidad de remolque. Fabricamos su tiro de arrastre a la medida exacta del chasis, compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
    ("seat", "SEAT", "ibiza", "Ibiza",
     "seat-ibiza-portabicicletas-4bicis.jpg", [],
     "El SEAT Ibiza es uno de los hatchback más reconocidos de la marca en Colombia. Su tiro de arrastre es compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
    ("jeep", "Jeep", "renegade", "Renegade",
     "jeep-renegade-portabicicletas-6bicis.jpg", [],
     "El Jeep Renegade es una de las SUV todoterreno más populares de la marca en Colombia. Fabricamos su tiro de arrastre a la medida exacta del chasis, compatible con portabicicletas Aerobike de hasta 6 bicicletas."),
    ("jeep", "Jeep", "wrangler", "Wrangler",
     "jeep-wrangler-verde-instalada.jpg", [
         "jeep-wrangler-verde-detalle-aerohitch.jpg",
         ("jeep-wrangler-canasta-aerohitch.jpg", "Jeep Wrangler con canasta de carga Aerohitch instalada en el tiro de arrastre"),
         "jeep-wrangler-detalle-aerohitch.jpg",
     ],
     "El Jeep Wrangler es uno de los todoterreno más emblemáticos en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, instalado junto a la llanta de repuesto, compatible con canasta de carga y portabicicletas."),
    ("jeep", "Jeep", "compass", "Compass",
     "jeep-compass-longitude-portabicicletas-4bicis.jpg", [
         ("jeep-compass-sport-portabicicletas-4bicis.jpg", "Jeep Compass Sport con portabicicletas Aerobike 4 bicicletas instalado"),
         ("jeep-compass-sport-portabicicletas-4bicis-2.jpg", "Jeep Compass Sport con portabicicletas Aerobike 4 bicicletas, vista frontal"),
         ("jeep-compass-parrilla-portabicicletas-4bicis.jpg", "Jeep Compass con parrilla de techo y portabicicletas Aerobike 4 bicicletas instalado"),
         ("jeep-compass-portabicicletas-4bicis-3.jpg", "Jeep Compass con portabicicletas Aerobike 4 bicicletas instalado, otra unidad"),
     ],
     "El Jeep Compass, incluida su versión Longitude y Sport, es una de las SUV más vendidas de la marca en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, compatible con portabicicletas Aerobike de hasta 4 bicicletas y parrilla de techo."),
    ("jeep", "Jeep", "cherokee", "Cherokee",
     "jeep-cherokee-limited-portabicicletas-4bicis.jpg", [],
     "El Jeep Cherokee Limited es una de las SUV medianas de la marca con mayor presencia en Colombia. Fabricamos su tiro de arrastre a la medida del chasis, compatible con portabicicletas Aerobike de hasta 4 bicicletas."),
]

os.makedirs(OUT_DIR, exist_ok=True)
generadas = []
for marca_slug, marca, modelo_slug, modelo, hero_img, galeria_imgs, parrafo in MODELOS:
    slug = f"{marca_slug}-{modelo_slug}"
    intro = parrafo  # se usa también como intro corta del hero

    if galeria_imgs:
        imgs_html_parts = []
        for img in galeria_imgs:
            if isinstance(img, tuple):
                filename, alt = img
            else:
                filename, alt = img, f"Instalación tiro de arrastre {marca} {modelo}"
            imgs_html_parts.append(
                f'<img src="../assets/img/instalacion/{filename}" alt="{alt}" loading="lazy">'
            )
        imgs_html = "\n        ".join(imgs_html_parts)
        galeria = GALERIA_BLOCK.format(marca=marca, modelo=modelo, imgs=imgs_html)
    else:
        galeria = ""

    html = TEMPLATE.format(
        marca=marca, marca_slug=marca_slug, modelo=modelo, slug=slug,
        hero_img=hero_img, intro=intro, parrafo=parrafo, galeria=galeria,
    )
    path = os.path.join(OUT_DIR, f"tiro-de-arrastre-{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    generadas.append(slug)

print(f"Generadas {len(generadas)} páginas de modelo:", generadas)
