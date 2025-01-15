from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.graphics import Rectangle

class GlassButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''  # Remove o fundo padrão
        self.background_color = (1, 1, 1, 0.2)  # Cor de fundo translúcida
        self.color = (1, 1, 1, 1)  # Cor do texto
        self.radius = [25]  # Maior arredondamento

class HomeScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        
        # Adicionar vídeo como plano de fundo
        self.video = Video(source='background.gif', state='play', options={'eos': 'loop'}, allow_stretch=True)
        self.video.size_hint = (1, 1)
        self.add_widget(self.video)

        # Layout principal sobre o vídeo
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20, size_hint=(1, 1))
        
        # Imagem de perfil no topo
        layout.add_widget(Image(source='profile_icon.png', size_hint=(1, 0.3)))

        # Texto central
        layout.add_widget(Label(
            text="ANTES DE COMEÇAR, SELECIONE\nABAIXO UMA DAS OPÇÕES",
            halign="center",
            size_hint=(1, 0.2),
            font_size="18sp",
            color=(1, 1, 1, 1)
        ))

        # Botões centrais
        button_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.3), spacing=10, padding=20)
        button_layout.add_widget(GlassButton(text="Modo Simples", size_hint=(1, 0.5)))
        button_layout.add_widget(GlassButton(text="Modo Avançado", size_hint=(1, 0.5)))
        layout.add_widget(button_layout)

        # Botões de configuração e saída na parte inferior
        footer_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10, padding=20)
        footer_layout.add_widget(GlassButton(text="Sair", size_hint=(0.5, 1)))
        footer_layout.add_widget(GlassButton(text="Configurações", size_hint=(0.5, 1)))
        layout.add_widget(footer_layout)

        # Adicionar layout principal acima do vídeo
        self.add_widget(layout)

class CarRandomizerApp(App):
    def build(self):
        return HomeScreen()

if __name__ == "__main__":
    CarRandomizerApp().run()
