

# 1. Configuración de la página
st.set_page_config(page_title=" rebajas ", page_icon="🏥")

# Título y Descripción
st.title("calculadora de rebajas")
st.markdown("Bienvenido. Introduce tus datos para calcular las rebajas q estas visualizando.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Tus Datos")
precio = st.sidebar.number_input("Tu precio (€)", min_value=0, max_value=200, value=60)
porcentaje = st.sidebar.slider("Tu porcentaje (%)", 0,100,50,1)

# 3. Botón de Cálculo y Lógica
if st.button("Calcular ahora"):
    
    # Fórmula Matemática: Peso entre altura al cuadrado
    rebajado = precio*(1-(porcentaje/100))
    
    # 4. Mostrar Resultado con Diseño
    col1, col2 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Tu precio es:", value=f"{rebajado:.2f}")
        
    with col2:
        # Usamos condicionales (if/elif/else) para el diagnóstico
        if porcentaje < 20:
            st.error("felicidades este es tu precio")
            st.write("felicidades este es tu precio")
        elif 20 <= porcentaje < 40:
            st.warning("es un chollo")
            st.balloons() # ¡Premio!
        elif 40 <= porcentaje < 60:
            st.warning("es muy bueno deberias comprarlo")
            st.balloons()
        else:
            st.success("es un chollazo compralo ya!!!")
            st.balloons()
