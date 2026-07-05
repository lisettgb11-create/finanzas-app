# 💰 Organiza Tus Finanzas · Streamlit App

**Finanzas con Lisett García** | Del desorden a la Paz

Esta es tu app profesional de planificación financiera personal, basada en la estructura de tu PDF.

---

## ✨ ¿Qué incluye?

✅ **💰 INGRESOS** — Registra todos tus ingresos (sueldo, freelance, etc.)
✅ **📌 GASTOS FIJOS** — Gastos que no cambian (arriendo, servicios)
✅ **📊 GASTOS VARIABLES** — Gastos que cambian cada mes (comida, transporte)
✅ **💳 TARJETA DE CRÉDITO** — 15 categorías para organizar gastos de tarjeta
✅ **💸 DEUDAS** — Seguimiento de cuotas y fechas de pago
✅ **💵 SALDO RESTANTE** — Ve exactamente cuánto dinero te queda
✅ **📊 GRÁFICOS** — Visualización bonita de tus gastos
✅ **💭 REFLEXIÓN** — Espacio para aprendizajes mensuales

---

## 🚀 Cómo desplegar en Streamlit Cloud (GRATIS)

### Paso 1: Crear cuenta en GitHub
1. Ve a https://github.com/signup
2. Crea tu cuenta (es gratis)
3. Verifica tu email

### Paso 2: Crear repositorio
1. Una vez logueado, haz clic en el **"+"** arriba a la derecha
2. Selecciona **"New repository"**
3. Completa:
   - **Name:** `finanzas-lisett` (o el que prefieras)
   - **Description:** "App para organizar mis finanzas"
   - **Public:** (marca este)
   - Clic en **"Create repository"**

### Paso 3: Subir archivos a GitHub
En tu nuevo repositorio, haz clic en **"Add file" → "Upload files"**

Sube estos **3 archivos:**
- `app.py` (es el app_profesional.py renombrado)
- `requirements.txt` (es el requirements_profesional.txt renombrado)
- `.gitignore` (contenido: `finanzas_completo.json`)

### Paso 4: Crear cuenta en Streamlit Cloud
1. Ve a https://streamlit.io/cloud
2. Haz clic en **"Sign up"** (arriba a la derecha)
3. Selecciona **"Sign up with GitHub"**
4. Autoriza Streamlit para acceder a GitHub

### Paso 5: Desplegar la app
1. En Streamlit Cloud, haz clic en **"New app"** (botón azul)
2. Completa:
   - **Repository:** Selecciona tu repositorio (finanzas-lisett)
   - **Branch:** main
   - **Main file path:** app.py
3. Haz clic en **"Deploy"**

¡**LISTO!** En unos 30-60 segundos tu app estará viva 🎉

Tu URL será algo como:
```
https://finanzas-lisett-tuusuario.streamlit.app
```

---

## 💰 Costo

- **Primeras 3 apps:** GRATIS ($0)
- **Apps adicionales:** $5/mes cada una
- **Almacenamiento de datos:** Gratis hasta 1GB

---

## 📲 Compartir con tus clientes

Una vez esté deployado en Streamlit Cloud:

1. **Opción A - Vender en Beacoms:**
   - Reemplaza el link del HTML con el link de Streamlit
   - Sube el precio ($19.99 o $24.99 porque es más profesional)
   - Actualiza la descripción: "Ahora con DEUDAS, TARJETA, SALDO RESTANTE"

2. **Opción B - Regalar como bonus:**
   - Dale el link a tus clientes de seguros
   - Diferencial tu servicio

3. **Opción C - Cobrar por acceso:**
   - (Requiere agregar login/password - después podemos hacerlo)
   - Cobra $9.99-$19.99/mes por acceso

---

## 🎨 Personalización

Si quieres cambiar colores, textos o agregar cosas:

### Cambiar colores:
Busca en `app.py`:
```python
WINE_DARK = "#4f1326"  # Vino oscuro
WINE = "#7a1f3d"       # Vino
WINE_LIGHT = "#a13a5c" # Vino claro
GOLD = "#b08d57"       # Dorado
```

### Cambiar nombre de categorías de tarjeta:
Busca `TARJETA_CATEGORIAS` en `app.py` y modifica la lista

### Cambiar título:
Busca `st.markdown("<h1 class='main-title'>💰 Organiza Tus Finanzas</h1>")` y cambia el texto

---

## 📊 Características técnicas

- **Base de datos:** JSON local (datos guardados en el servidor Streamlit)
- **Seguridad:** Cada usuario tiene su propia sesión
- **Gráficos:** Plotly (bonitos e interactivos)
- **Responsive:** Funciona en celular, tablet, computadora
- **Sin código:** Si necesitas cambios, solo pedimelo

---

## ❓ Preguntas frecuentes

**¿Dónde se guardan los datos?**
En un archivo JSON en el servidor de Streamlit Cloud. No se pierden.

**¿Mis clientes necesitan cuenta?**
No. Entran con el link y listo. Sin login.

**¿Cuántos usuarios pueden usar la app?**
Ilimitados (hasta que Streamlit se sature, pero para 100+ usuarios estamos bien)

**¿Puedo descargar los datos?**
Sí, hay un botón "Descargar datos (JSON)" al final.

**¿Qué pasa si quiero agregar más cosas después?**
Fácil. Nos contactas y lo hacemos. Los cambios se actualizan automáticamente.

---

## 🔄 Próximos pasos (después)

Una vez que esté funcionando, podemos:

1. **Agregar login** → Cobrar por acceso ($9.99-$19.99/mes)
2. **Reportes PDF** → Descargar análisis profesional
3. **Base de datos real** → PostgreSQL (más usuarios, mejor seguridad)
4. **Integración Stripe** → Pagos automáticos
5. **Móvil nativa** → App real para iOS/Android
6. **Dashboard ejecutivo** → Para ver múltiples usuarios (si lo haces con clientes)

---

## 📧 Soporte

Si tienes problemas al desplegar:
1. Verifica que los 3 archivos estén en GitHub
2. Verifica que el nombre de la rama sea "main"
3. Verifica que el archivo se llame "app.py"
4. Reinicia el deploy en Streamlit Cloud

Si nada funciona, me avisa y lo hacemos juntas.

---

**Creado para Finanzas con Lisett García 💜**

*Del desorden a la Paz*
