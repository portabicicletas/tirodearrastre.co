# tirodearrastre.com.co — Estado del proyecto

## Fase 1 — Entregado
- Arquitectura de carpetas completa
- Sistema de diseño (paleta, tipografía, componentes) en `assets/css/main.css`
- `assets/js/main.js` (menú móvil, FAQ acordeón, formulario → WhatsApp)
- `index.html` — página de inicio completa con SEO on-page, Schema.org (AutoPartsStore + WebSite), Open Graph, Twitter Cards
- `robots.txt`, `manifest.json`, `404.html`

## Fase 2 — Entregado
- **20 páginas de marca completas** en `marcas/`: Toyota, Mazda, Renault, Chevrolet, Kia, Hyundai, Nissan, Suzuki, Volkswagen, Ford, Jeep, Honda, BYD, JAC, DFSK, Changan, Jetour, Mitsubishi, Subaru, Peugeot. Cada una con descripción propia, ventajas, beneficios, modelos del catálogo, FAQ con Schema FAQPage, breadcrumb con Schema BreadcrumbList y CTA a WhatsApp.
- `marcas/index.html` — página índice que lista las 20 marcas.
- `generate_marcas.py` — script generador: si necesitas ajustar copy o agregar una marca nueva, edita el diccionario `MARCAS` y vuelve a ejecutarlo (regenera todas las páginas de golpe, de forma consistente).
- `sitemap.xml` actualizado con las 22 URLs (home + índice de marcas + 20 marcas).

## Fase 3 — Entregado
- **4 páginas de categoría de producto completas** en `productos/`: `tiros-de-arrastre.html`, `portabicicletas.html`, `parrillas-de-techo.html`, `cubre-carter.html`. Cada una con descripción, tipos/capacidades, materiales/protección, compatibilidad, FAQ con Schema FAQPage, Schema Product y breadcrumb.
- `productos/index.html` — índice del catálogo.
- `generate_productos.py` — script generador de las 3 páginas de categoría (portabicicletas, parrillas, cubre cárter); `tiros-de-arrastre.html` se escribió a mano por ser la página ancla de mayor prioridad SEO.
- `sitemap.xml` actualizado (27 URLs).

## Fase 4 — Entregado
- `contacto.html` — formulario de cotización, tarjetas de contacto (WhatsApp, cobertura, horario) y mapa embebido de Colombia.
- `legal/privacidad.html`, `legal/cookies.html`, `legal/tratamiento-datos.html`, `legal/terminos.html` — las 4 páginas legales solicitadas, con `noindex` (no deben competir por posicionamiento) y excluidas en `robots.txt`. **Importante:** el texto de `tratamiento-datos.html` y `privacidad.html` es un borrador razonable inspirado en la Ley 1581 de 2012, pero no reemplaza una revisión legal — te recomiendo que un abogado las valide antes de publicar el sitio, sobre todo por el manejo de datos personales de clientes.
- `generate_legal.py` — script generador de las 4 páginas legales.
- `sitemap.xml` actualizado (28 URLs indexables; las legales no se incluyen porque son noindex).

## Fase 5 — Entregado
- **18 páginas individuales de modelo** en `productos/tiro-de-arrastre-{marca}-{modelo}.html`, todas con fotos reales de instalación: Toyota (Prado, Hilux, Fortuner, Corolla Cross), Renault (Duster, Arkana, Koleos), Nissan (X-Trail, Qashqai), Mitsubishi (Outlander), Jetour (X70), Kia (EV9), Suzuki (Jimny), Volkswagen (Gol), Mazda (CX-5, CX-30, BT-50), Honda (CR-V). Cada una con hero con foto real, galería de fotos adicionales (cuando hay más de una), Schema Product + FAQPage + BreadcrumbList, y botón de vuelta a la página de marca.
- `generate_modelos.py` — script generador: para agregar un modelo nuevo, añade una entrada a la lista `MODELOS` (marca, modelo, foto hero, fotos de galería, párrafo) y vuelve a ejecutarlo.
- Chevrolet Tracker: 19no modelo con página propia (productos/tiro-de-arrastre-chevrolet-tracker.html), y primera foto real de la marca Chevrolet (marcas/chevrolet.html).
- Marca 21 agregada: Audi (fuera de las 20 originales, a petición explícita), con página propia marcas/audi.html y modelo Q3 con página propia (productos/tiro-de-arrastre-audi-q3.html).
- Categoría Cubre Cárter: ya tiene foto real (hero + destacado), última de las 4 categorías de producto que seguía vacía.
- Los chips de modelo en las páginas de marca correspondientes (Toyota, Renault, Nissan, Mitsubishi, Jetour, Kia, Suzuki, Volkswagen, Mazda, Honda) ahora enlazan a la página de modelo real en lugar de abrir WhatsApp directo; el resto de modelos sin página propia siguen abriendo WhatsApp.
- `generate_marcas.py` corregido: se detectó y arregló una regresión de rutas absolutas (`/productos/...`) que había vuelto a aparecer en las 19 páginas de marca generadas por script al regenerarlas; ahora la plantilla usa rutas relativas de forma permanente, así que futuras regeneraciones no volverán a romperlo.
- `sitemap.xml` actualizado (46 URLs indexables).

## Pendiente (próximas fases, a solicitar en mensajes de seguimiento)
3. Más páginas de modelo: Fortuner ya tiene página pero sin foto propia (usa la foto hero de la marca); RAV4, Land Cruiser, Chevrolet Tracker, Kia Sportage/Seltos, Hyundai Tucson y otros modelos sin foto real todavía siguen abriendo WhatsApp directo desde el chip — se puede crear página propia en cuanto haya fotos, o sin fotos si prefieres avanzar solo con texto.
8. Blog: 40 artículos SEO de 2.500+ palabras (se recomienda entregarlos en lotes de 4-6 por mensaje)
9. Terminar de integrar imágenes reales en marcas/categorías que aún no las tienen
10. Decidir si SEAT se agrega como marca 21 (ya hay fotos de un Arona)
11. Precio pendiente: portabicicletas premium 3 bicis AeroBike

## Nota sobre imágenes
Las plantillas referencian rutas de imagen (`/assets/img/...`) que aún no existen como archivos — hay que reemplazarlas por fotos reales del producto instalado antes de publicar, o pedirme que genere imágenes de referencia.
