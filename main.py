from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import cv2
import socket


class BarcodeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Scan a barcode')
        self.button = Button(text='Scan', on_press=self.scan_barcode)
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        return self.layout

    def scan_barcode(self, instance):
        # فتح الكاميرا وقراءة الباركود
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # هنا يجب إضافة كود قراءة الباركود باستخدام pyzbar أو أي مكتبة أخرى

            # إذا تم قراءة باركود، أرسل البيانات إلى البرنامج على الكمبيوتر

            # إغلاق الكاميرا عند الانتهاء
            cap.release()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    BarcodeApp().run()

