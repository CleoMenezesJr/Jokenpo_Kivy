from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from random import randint

class Jokenpo(App):
    def build(self):
        box = BoxLayout(orientation='vertical')
        self.titulo = Label(text = '         Jo-Ken-Po!\n Escolha a tua jogada:', font_size=30)
        box.add_widget(self.titulo)

        box2 = BoxLayout(orientation='horizontal')
        button = Button(text='Pedra', font_size=30, on_release=self.jogada_pedra)
        button1 = Button(text='Papel', font_size=30, on_release=self.jogada_papel)
        button2 = Button(text='Tesoura', font_size=30, on_release=self.jogada_tesoura)
        box2.add_widget(button)
        box2.add_widget(button1)
        box2.add_widget(button2)

        box3 = BoxLayout(orientation='vertical')
        self.result = Label(text = 'Resultado', font_size=30)
        box3.add_widget(self.result)

        box.add_widget(box2)
        box.add_widget(box3)
        return box
#Açao caso jogador clique em Pedra
    def jogada_pedra(self, button):
        maquina = randint(0, 2)
        jogada = ['Pedra', 'Papel', 'Tesoura']
        jogada_maquina = jogada[maquina]
        if jogada_maquina == 'Tesoura':
            self.result.text = f'O adversário jogou:\n>>{jogada_maquina}\nVocê Ganhou!'
        elif jogada_maquina == 'Papel':
            self.result.text = f'O adversário jogou:\n>>{jogada_maquina}\nO Adversário Ganhou!'
        elif jogada_maquina == 'Pedra':
            self.result.text = f'O adversário jogou:\n>>{jogada_maquina}\nEmpataram!'
# Açao caso jogador clique em Papel
    def jogada_papel(self,button1):
        maquina = randint(0, 2)
        jogada = ['Pedra', 'Papel', 'Tesoura']
        jogada_maquina = jogada[maquina]
        if jogada_maquina == 'Pedra':
            self.result.text = f'O adversário jogou:\n>>{jogada_maquina}\nVocê Ganhou!'
        elif jogada_maquina == 'Tesoura':
            self.result.text = f'O adversário jogou:\n>>{jogada_maquina}\nO Adversário Ganhou!'
        elif jogada_maquina == 'Papel':
            self.result.text = f'O adversário jogou:\n>>{jogada_maquina}\nEmpataram!'
# Açao caso jogador clique em Tesoura
    def jogada_tesoura(self, button2):
        maquina = randint(0, 2)
        jogada = ['Pedra', 'Papel', 'Tesoura']
        jogada_maquina = jogada[maquina]
        if jogada_maquina == 'Papel':
            self.result.text = f'O adversário jogou:\n>>{jogada_maquina}\nVocê Ganhou!'
        elif jogada_maquina == 'Pedra':
            self.result.text = f'O adversário jogou:\n>>{jogada_maquina}\nO Adversário Ganhou!'
        elif jogada_maquina == 'Tesoura':
            self.result.text = f'O adversário jogou:\n>>{jogada_maquina}\nEmpataram!'
Jokenpo().run()