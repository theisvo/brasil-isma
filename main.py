import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Calculadora Pra Brasiuul By Isma"
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = "auto"
    page.padding = 20

    # Título Principal
    titulo = ft.Text(
        "Cotizaciones Pra Brasiuul By Isma",
        size=28,
        weight="bold",
        color=ft.colors.GREEN_ACCENT,
        text_align="center"
    )

    # Campos de entrada
    dp = ft.TextField(label="Dólar/Peso Argentina", prefix_text="$ ", value="1490", keyboard_type=ft.KeyboardType.NUMBER)
    dr = ft.TextField(label="Dólar/Real Brasil", prefix_text="R$ ", value="5.5", keyboard_type=ft.KeyboardType.NUMBER)
    pp = ft.TextField(label="PIX/Peso", prefix_text="$ ", value="290", keyboard_type=ft.KeyboardType.NUMBER)

    # Contenedor de Resultado
    res_card = ft.Column(visible=False, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    res_titulo = ft.Text("", size=22, weight="bold")
    res_costo = ft.Text("", size=18)
    res_dif = ft.Text("", size=16, color=ft.colors.RED_400)
    res_empate = ft.Text("", size=15, italic=True, text_align="center")

    def calcular(e):
        try:
            v_dp = float(dp.value)
            v_dr = float(dr.value)
            v_pp = float(pp.value)
            
            costo_tarjeta = v_dp / v_dr
            costo_pix = v_pp
            
            dolar_arg_empate = v_pp * v_dr
            dolar_br_empate = v_dp / v_pp

            res_card.visible = True
            
            if costo_tarjeta < costo_pix:
                dif = costo_pix - costo_tarjeta
                res_titulo.value = "✅ CONVIENE TARJETA"
                res_titulo.color = ft.colors.GREEN_ACCENT
                res_costo.value = f"Pagas el Real a: ${costo_tarjeta:.2f}"
                res_dif.value = f"Con PIX pagarías ${costo_pix:.2f} (+${dif:.2f} más caro)"
                res_empate.value = f"Para que convenga PIX:\nDol. Arg debe subir a ${dolar_arg_empate:.2f}\no Dol. Br bajar a {dolar_br_empate:.2f} R$"
            else:
                dif = costo_tarjeta - costo_pix
                res_titulo.value = "✅ CONVIENE PIX"
                res_titulo.color = ft.colors.GREEN_ACCENT
                res_costo.value = f"Pagas el Real a: ${costo_pix:.2f}"
                res_dif.value = f"Con Tarjeta pagarías ${costo_tarjeta:.2f} (+${dif:.2f} más caro)"
                res_empate.value = f"Para que convenga TARJETA:\nDol. Arg debe bajar a ${dolar_arg_empate:.2f}\no Dol. Br subir a {dolar_br_empate:.2f} R$"
            
            page.update()
        except Exception:
            res_titulo.value = "Error: Ingresa números"
            res_titulo.color = ft.colors.RED
            res_card.visible = True
            page.update()

    # Botón Calcular
    btn = ft.ElevatedButton(
        "CALCULAR",
        icon=ft.icons.CALCULATE,
        on_click=calcular,
        style=ft.ButtonStyle(
            bgcolor=ft.colors.GREEN_700,
            color=ft.colors.WHITE,
            padding=20
        ),
        width=200
    )

    # Agregar elementos a la página
    res_card.controls = [res_titulo, res_costo, res_dif, ft.Divider(), res_empate]
    
    page.add(
        titulo,
        ft.Container(height=10),
        dp, dr, pp,
        ft.Container(height=10),
        btn,
        ft.Container(height=20),
        res_card
    )

ft.app(target=main)
