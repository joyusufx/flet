import flet as ft
import time
res = []
checkers = []

def main(page : ft.Page) :
    global i
    coins = 400
    def refresh_tasks():
        i = 0
        res = []
        checkers = []
        with open('data.ini' , 'r') as thedata :
            for line in thedata :
                checkers.append(line)
        try :
            checkers.remove("\n")
        except :
            pass
        for checker in checkers :
            combo = ft.Checkbox(label='' , value=True)
            container_check = ft.Container(content=combo , border_radius=1000 , width=20 , height=20)
            txt = ft.Text(checker.rstrip('\ns'))
            stack.controls.append(ft.Row([container_check ,txt ] , top=110 + i , left = 20))
            i += 40
            column.update()
    def button_clicked(e):
        with open("data.ini" , 'a') as thedata :
            thedata.write('\n'+str(text_field_addt.value))
        refresh_tasks()
    def clear_all(e) :
        with open("data.ini" , 'w') as thedata :
            thedata.write('')
        for s in stack.controls[4 : 14] :
            stack.controls.remove(s)
            stack.update()
        coins_add()
    def coins_update() :
        global coins
        coins = 0
        with open('data_coins.ini' , 'r') as thedata :
            coins = int(thedata.read())
            text_span_coins.text = str(coins)
            print(coins)
            text_span_coins.update()
    def coins_add() :
        with open('data_coins.ini' , 'r') as thedata :
            coins = thedata.read()
        with open('data_coins.ini' , 'w') as thedata :
            coins = int(coins) + 100
            thedata.write(str(coins))
        coins_update()
    page.window_bgcolor = '#000000'
    page.add(
        ft.Row([
        ft.Text(
        spans=[
            ft.TextSpan("StudySpace",
                        style=ft.TextStyle(
        size=40,
        weight= ft.FontWeight.BOLD,
        color="#4E4FEB"
                        ))
        ]
        )
        ] , alignment=ft.MainAxisAlignment.CENTER)
    )
    
    text_span_coins = ft.TextSpan(str(coins) , style = ft.TextStyle(size=24 , color='orange' , weight=ft.FontWeight.BOLD))
    column_coins = ft.Column(controls=[ft.Stack([ft.Text(top=10 , left =80 , spans=[ft.TextSpan('Coins' , style=ft.TextStyle(weight = ft.FontWeight.BOLD , color='Orange'))]) , ft.Text(text_align=ft.TextAlign.CENTER, spans=[text_span_coins] , top=40 , left = 77)])])
    text_field_addt = ft.TextField(hint_text="Any homework ? Add it here 🙌", border_radius=23 )
    btn_add = ft.FloatingActionButton(icon=ft.icons.ADD , bgcolor="#068FFF" , on_click=button_clicked)
    row = ft.Row(top = 20 , left=10,alignment=ft.MainAxisAlignment.END , controls=[text_field_addt ,btn_add])
    stack = ft.Stack(controls=[row ,  ft.Row(top=90 , left=125 , controls=[ft.Text('______________________')]) , ft.TextButton("Send to Completion ✅" , icon = ft.icons.SEND , top=270 , left = 90, on_click=clear_all ,style=ft.ButtonStyle(color='green' , bgcolor="#068FFF")) , ft.Container(width=200 , height = 100 , bgcolor="#FFFFFF" , top=400 , left = 95 , border_radius=23 , content=column_coins)])
    column = ft.Column(controls=[stack])
    page.scroll = ft.ScrollMode.ALWAYS
    container = ft.Container(
        height=800,
        width=400,
        bgcolor="#4E4FEB",
        border_radius=23,
        content=column)

    
    page.add(container)
    refresh_tasks()
    coins_update()
ft.app(target=main , web_renderer = ft.WebRenderer.CANVAS_KIT)