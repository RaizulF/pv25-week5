import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qt_material import apply_stylesheet

class FormValidation(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(500, 500)
        self.setWindowTitle("Form Validation")

        main_layout = QVBoxLayout()

        # identitas
        self.label_nama = QLabel("<span style='font-weight: bold; color: #000; font-size:10pt;'>Nama: Raizul Furkon</span>")
        self.label_nim = QLabel("<span style='font-weight: bold; color: #000; font-size:10pt'>NIM: F1D022024</span>")
        self.label_kelas = QLabel("<span style='font-weight: bold; color: #000; font-size:10pt'>Kelas: C</span>")
        self.label_nama.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label_nim.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label_kelas.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        # form
        form_layout = QFormLayout()
        self.nama = QLineEdit()
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Nama</span>"), self.nama)
        
        self.email = QLineEdit()
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Email</span>"), self.email)
        
        self.age = QLineEdit()
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Age</span>"), self.age)
        
        self.phone_number = QLineEdit()
        self.phone_number.setInputMask('+62 999 9999 9999') 
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Phone Number</span>"), self.phone_number)

        self.address = QPlainTextEdit()
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Address</span>"), self.address)

        self.gender = QComboBox()
        self.gender.addItems(["", "Male", "Female"])
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Gender</span>"), self.gender)

        self.education = QComboBox()
        self.education.addItems(["", "Elementary School", "Junior High School", "Senior High School", "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral's Degree"])
        form_layout.addRow(QLabel("<span style='font-weight: bold; color: #000;'>Education</span>"), self.education)
        
        button_layout = QHBoxLayout()
        self.button_submit = QPushButton("Save")
        self.button_submit.setProperty('class', 'success')
        self.button_submit.clicked.connect(self.submitForm)
        self.button_clear = QPushButton("Clear")
        self.button_clear.setProperty('class', 'danger')
        self.button_clear.clicked.connect(self.clearForm)
        button_layout.addWidget(self.button_submit)
        button_layout.addWidget(self.button_clear)


        main_layout.addWidget(self.label_nama)
        main_layout.addWidget(self.label_nim)
        main_layout.addWidget(self.label_kelas)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.close_shortcut = QShortcut(QKeySequence('Q'), self)
        self.close_shortcut.activated.connect(self.close)

    def submitForm(self):
        if not self.nama.text() or not self.email.text() or not self.age.text() or not self.phone_number.text() or not self.address.toPlainText() or self.gender.currentIndex() == 0 or self.education.currentIndex() == 0:
            self.show_warning("All fields are required!")
            return
        else:
            email_input = self.email.text().strip()
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email_input):
                self.show_warning("Please enter a valid email address!")
                return
            
            age_input = self.age.text().strip()
            if not age_input.isdigit() or int(age_input) <= 0:
                self.show_warning("Please enter a valid age!")
                return
            
            phone_input = self.phone_number.text().strip()
            phone_digits = ''.join(filter(str.isdigit, phone_input))
            if len(phone_digits) != 13:
                self.show_warning("Please enter a valid 13-digit phone number!")
                return
            
            QMessageBox.information(self, "Success", "Form submitted successfully!")
            self.clearForm()

    def clearForm(self):
        self.nama.clear()
        self.email.clear()
        self.age.clear()
        self.phone_number.clear()
        self.address.clear()        
        self.gender.setCurrentIndex(0)
        self.education.setCurrentIndex(0)

    def show_warning(self, message):
        QMessageBox.warning(self, "Warning", message, QMessageBox.Ok)

extra = {
    'danger': '#dc3545',
    'success': '#8BC34A',
}


if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='light_blue.xml')
    form = FormValidation()
    form.show()
    sys.exit(app.exec_())
            
            
            
