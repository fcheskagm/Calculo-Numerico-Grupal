import flet as ft

def convert_bases(number, from_base, to_base):
    try:
        valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:from_base]
        if not all(char.upper() in valid_chars for char in str(number)):
            return "Error: Número inválido para la base seleccionada"

        base_10 = int(str(number), from_base)
        
        if to_base == 10:
            return str(base_10)
        elif to_base == 2:
            return bin(base_10).replace("0b", "")
        elif to_base == 8:
            return oct(base_10).replace("0o", "")
        elif to_base == 16:
            return hex(base_10).replace("0x", "")
        else:
            alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:to_base]
            base_n = ""
            while base_10 > 0:
                base_10, i = divmod(base_10, to_base)
                base_n = alphabet[i] + base_n
            return base_n
    except Exception as e:
        return f"Error: {str(e)}"

def main(page: ft.Page):
    page.title = "Traductor de números"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number1 = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    txt_number2 = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    bases = ['2', '3', '4', '8', '16']
    selected_base = ft.Dropdown(
        width=100,
        options=[ft.dropdown.Option(base) for base in bases],
    )

    def translate_click(e):
        try:
            base = int(selected_base.value)
            number = txt_number1.value
            txt_number2.value = convert_bases(number, 10, base)
        except ValueError:
            txt_number2.value = "Error: Entrada inválida"
        page.update()

    def invert_click(e):
        txt_number1.value, txt_number2.value = txt_number2.value, txt_number1.value
        page.update()

    page.add(
        ft.Row(
            [
                ft.Text("Número 1:"),
                txt_number1,
                ft.Text("Base:"),
                selected_base,
                ft.ElevatedButton("Traducir", on_click=translate_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    page.add(
        ft.Row(
            [
                ft.Text("Resultado:"),
                txt_number2,
                ft.ElevatedButton("Invertir", on_click=invert_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
