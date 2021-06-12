import wx
import myWindow

class ResultFrame (myWindow.ResultFrame):
    def __init__(self, parent, hasil, prediction):
        myWindow.ResultFrame.__init__(self, parent)
        self.score.SetValue(f'{hasil}')
        self.prediction.SetValue(prediction)

class MainFrame (myWindow.MainFrame):
    def __init__(self, parent):
        myWindow.MainFrame.__init__(self, parent)

    def calculate(self, event):
        berat = float(self.berat.GetValue())
        tinggi = float(self.tinggi.GetValue())
        tinggi = tinggi/100

        calc = berat/(tinggi**2)

        hasil = calc

        score = f'Body Mass Index anda adalah: {hasil}'
        prediction = 'Anda termasuk: '

        if (hasil < 18.5):
            prediction += 'Kurang berat badan'
        elif (hasil <= 24.9):
            prediction += 'Normal'
        elif (hasil <= 29.9):
            prediction += 'Kelebihan berat badan'
        else:
            prediction += 'Obesitas'

        hasil = format(hasil, '.2f')

        frame = ResultFrame(None, hasil, prediction)
        frame.Show()

app = wx.App()
frame = MainFrame(parent=None)
frame.Show()
app.MainLoop()