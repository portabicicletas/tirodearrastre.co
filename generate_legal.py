# -*- coding: utf-8 -*-
"""Genera las páginas legales: privacidad, cookies, tratamiento de datos, términos."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(BASE, "legal")

HEAD = """<!DOCTYPE html>
<html lang="es-CO">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Tiro de Arrastre Colombia</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://www.tirodearrastre.co/legal/{slug}.html">
<meta name="robots" content="noindex, follow">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="manifest" href="/manifest.json">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/main.css">
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
      <a href="#" class="btn btn-outline" data-wa="Cotización general">WhatsApp</a>
      <button class="nav-toggle" aria-label="Abrir menú" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
<main id="contenido">
  <div class="container breadcrumb"><a href="/">Inicio</a><span class="sep">/</span>{title}</div>
  <section style="padding-top:12px">
    <div class="container" style="max-width:820px">
      <h1>{title}</h1>
      <p style="color:var(--acero-500);font-size:.9rem">Última actualización: agosto de 2026</p>
{cuerpo}
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
        <li><a href="/productos/tiros-de-arrastre.html">Tiros de arrastre</a></li>
        <li><a href="/productos/portabicicletas.html">Portabicicletas</a></li>
      </ul></div>
      <div><h4>Empresa</h4><ul>
        <li><a href="/marcas/">Marcas</a></li>
        <li><a href="/blog/index.html">Blog</a></li>
        <li><a href="/contacto.html">Contacto</a></li>
      </ul></div>
      <div><h4>Legal</h4><ul>
        <li><a href="/legal/privacidad.html">Política de privacidad</a></li>
        <li><a href="/legal/cookies.html">Política de cookies</a></li>
        <li><a href="/legal/tratamiento-datos.html">Tratamiento de datos</a></li>
        <li><a href="/legal/terminos.html">Términos y condiciones</a></li>
      </ul></div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="anio"></span> Tiro de Arrastre Colombia.</span>
      <span>WhatsApp: +57 318 785 6238</span>
    </div>
  </div>
</footer>
<script src="/assets/js/main.js"></script>
<script>document.getElementById('anio').textContent = new Date().getFullYear();</script>
</body>
</html>
"""

PAGES = {
    "privacidad": dict(
        title="Política de Privacidad",
        description="Política de privacidad de tirodearrastre.co: qué información recopilamos y cómo la usamos.",
        cuerpo="""
      <p>En Tiro de Arrastre Colombia respetamos la privacidad de quienes visitan este sitio web y de nuestros clientes. Esta política explica, en términos generales, qué información podemos recopilar y cómo la usamos.</p>
      <h3>Información que recopilamos</h3>
      <p>Cuando completas el formulario de cotización o nos escribes por WhatsApp, recopilamos los datos que tú mismo nos proporcionas: nombre, teléfono, marca y modelo del vehículo, y cualquier mensaje adicional. No solicitamos información financiera a través del sitio web.</p>
      <h3>Uso de la información</h3>
      <p>Usamos estos datos exclusivamente para responder tu solicitud de cotización, coordinar la instalación del producto y darte seguimiento comercial si así lo autorizas.</p>
      <h3>Con quién compartimos la información</h3>
      <p>No vendemos ni cedemos tus datos a terceros con fines comerciales ajenos a nuestra operación. Solo la compartimos cuando es necesario para completar la instalación (por ejemplo, con un taller aliado en tu ciudad).</p>
      <h3>Tus derechos</h3>
      <p>Puedes solicitar en cualquier momento que actualicemos, corrijamos o eliminemos tus datos personales escribiéndonos por WhatsApp al +57 318 785 6238.</p>
      <p>Para más detalle sobre el tratamiento de datos personales conforme a la normativa colombiana, consulta nuestra <a href="/legal/tratamiento-datos.html">Política de tratamiento de datos</a>.</p>
""",
    ),
    "cookies": dict(
        title="Política de Cookies",
        description="Política de cookies de tirodearrastre.co: qué cookies usamos y cómo puedes gestionarlas.",
        cuerpo="""
      <p>Este sitio web puede usar cookies y tecnologías similares para mejorar la experiencia de navegación y entender cómo se usa el sitio.</p>
      <h3>¿Qué es una cookie?</h3>
      <p>Una cookie es un pequeño archivo de texto que se almacena en tu navegador al visitar un sitio web. No accede a otra información de tu dispositivo.</p>
      <h3>Tipos de cookies que usamos</h3>
      <p><strong>Cookies técnicas:</strong> necesarias para el funcionamiento básico del sitio (por ejemplo, recordar el estado del menú móvil).</p>
      <p><strong>Cookies analíticas:</strong> si están habilitadas, nos ayudan a entender qué páginas se visitan más, para mejorar el contenido del sitio.</p>
      <h3>Cómo gestionar las cookies</h3>
      <p>Puedes configurar tu navegador para bloquear o eliminar las cookies en cualquier momento. Ten en cuenta que algunas funciones del sitio podrían no funcionar correctamente sin ellas.</p>
""",
    ),
    "tratamiento-datos": dict(
        title="Política de Tratamiento de Datos Personales",
        description="Política de tratamiento de datos personales de tirodearrastre.co conforme a la normativa colombiana.",
        cuerpo="""
      <p>Tiro de Arrastre Colombia trata los datos personales de sus clientes y usuarios del sitio web conforme a los principios generales de la protección de datos personales en Colombia (Ley 1581 de 2012 y sus decretos reglamentarios).</p>
      <h3>Responsable del tratamiento</h3>
      <p>Tiro de Arrastre Colombia, contacto: WhatsApp +57 318 785 6238.</p>
      <h3>Finalidad del tratamiento</h3>
      <p>Los datos personales que recopilamos (nombre, teléfono, información del vehículo) se usan para: gestionar cotizaciones, coordinar instalaciones, brindar soporte postventa y, si el titular lo autoriza, enviar información comercial sobre nuestros productos.</p>
      <h3>Derechos del titular</h3>
      <p>Como titular de tus datos personales, tienes derecho a conocer, actualizar, rectificar y solicitar la supresión de tu información, así como a revocar la autorización otorgada para su tratamiento, salvo que exista un deber legal o contractual que impida su eliminación.</p>
      <h3>Cómo ejercer tus derechos</h3>
      <p>Puedes ejercer estos derechos escribiéndonos por WhatsApp al +57 318 785 6238, indicando tu solicitud de forma clara.</p>
      <p><em>Este documento describe de forma general nuestras prácticas de tratamiento de datos y no sustituye una asesoría legal específica. Recomendamos su revisión por un abogado antes de la publicación definitiva del sitio, para garantizar el cumplimiento completo de la Ley 1581 de 2012.</em></p>
""",
    ),
    "terminos": dict(
        title="Términos y Condiciones",
        description="Términos y condiciones de uso del sitio web tirodearrastre.co y de los servicios ofrecidos.",
        cuerpo="""
      <p>El acceso y uso de este sitio web implica la aceptación de los siguientes términos y condiciones.</p>
      <h3>Sobre nuestros productos</h3>
      <p>Los tiros de arrastre, portabicicletas, parrillas de techo y cubre cárter que ofrecemos se cotizan de forma personalizada según la marca, modelo y año del vehículo. Los precios y la disponibilidad se confirman directamente por WhatsApp.</p>
      <h3>Instalación</h3>
      <p>La instalación de nuestros productos se realiza siguiendo las especificaciones técnicas de cada vehículo. El cliente es responsable de proporcionar información correcta sobre su vehículo al momento de cotizar.</p>
      <h3>Garantía</h3>
      <p>Los productos e instalaciones cuentan con garantía según las condiciones informadas al momento de la venta. Cualquier reclamo debe reportarse a través de nuestros canales de contacto oficiales.</p>
      <h3>Propiedad del contenido</h3>
      <p>El contenido de este sitio web (textos, imágenes, diseño) es propiedad de Tiro de Arrastre Colombia y no puede reproducirse sin autorización.</p>
      <h3>Modificaciones</h3>
      <p>Nos reservamos el derecho de actualizar estos términos y condiciones en cualquier momento. Los cambios entrarán en vigencia desde su publicación en este sitio.</p>
""",
    ),
}

os.makedirs(OUT_DIR, exist_ok=True)
for slug, p in PAGES.items():
    html = HEAD.format(title=p["title"], description=p["description"], slug=slug, cuerpo=p["cuerpo"])
    with open(os.path.join(OUT_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)

print("Generadas:", list(PAGES.keys()))
