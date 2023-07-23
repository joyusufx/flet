import flet as ft
from pytube import YouTube , Search
import webbrowser
import time
import requests
import base64
def main(page : ft.Page) :
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ALWAYS
    search_key = ft.TextField(hint_text="Search Videos")
    def button_clicked_fetch(e) :
        try :
            page.remove(pb)
        except :
            pass
        page.add(pb)
        try :
            yt = Search(search_key.value)
        except :
            ("Error ! Invalid Search!")
        yt_results = yt.results
        res = []
        for result in yt_results :
            result = str(result)
            x = result[41 : -1]
            result = "www.youtube.com/watch?v=" + x
            res.append(result)
        print(res)
        i = 0
        for url in res :
            pb.value = i
            i = i + 0.05
            def add_web(webpage = str) :
                webbrowser.open(webpage)
            yt = YouTube(url)
            content =  requests.get(yt.thumbnail_url)
            base64bytes = base64.b64encode(content.content)
            base64bytes_string = base64bytes.decode()
            image = ft.Image(src_base64= base64bytes_string , height = 300 , width=400 , fit= ft.ImageFit.SCALE_DOWN)
            time.sleep(2)
            details = str(yt.title) + '\n  ' + str(yt.author)
            text = ft.Text(spans=[ft.TextSpan(text=details , url=yt.embed_url)])
            column = ft.Row(controls= [image , text] , scroll= ft.ScrollMode.ALWAYS , width=1300)
            page.add(column)
        page.remove(pb)
    bt = ft.TextButton("Search" , on_click=button_clicked_fetch)
    title = ft.Text( spans=[ft.TextSpan('Youtube : Joyusufx Edition' , style=ft.TextStyle(weight =ft.FontWeight.BOLD , size= 40 , foreground=ft.Paint(gradient=ft.PaintLinearGradient((150 , 155) , (160 , 200) , colors=[ft.colors.GREEN , ft.colors.YELLOW]))))])
    pb = ft.ProgressBar(color=ft.colors.PURPLE , width= 900)
    page.add(title , search_key , bt)
ft.app(target=main , name="Youtube : Joyusufx Edition" , view=ft.AppView.WEB_BROWSER)