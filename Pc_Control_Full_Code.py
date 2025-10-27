import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QStackedWidget, QFrame)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import  QIcon, QPixmap
import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFrame, QSizePolicy, QHBoxLayout)
from PyQt5.QtGui import QPixmap, QImage, QFont, QColor, QPalette
from PyQt5.QtCore import QTimer, Qt, QSize
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea, QPushButton, QVBoxLayout, QWidget, QFrame, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import os
import os
import signal


class StylishButton(QPushButton):       #just for the styleshet of BUTTONS
    def __init__(self, text):
        super().__init__(text)
        self.setMinimumHeight(40)
        self.setFont(QFont('Arial', 10, QFont.Bold))
        self.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)

class VideoFrame(QFrame):    #just for the video Frame styleshet
    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.StyledPanel)
        self.setLineWidth(2)
        self.setMinimumSize(500, 400)
        self.setStyleSheet("""
            background-color: #f0f0f0;
            border: 2px solid #ccc;
            border-radius: 15px;
        """)

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Scroll Area to make the content scrollable
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_content_widget = QWidget(scroll_area)  # The actual content will go inside this widget
        scroll_area.setWidget(scroll_content_widget)
        scroll_layout = QVBoxLayout(scroll_content_widget)

        # Hero section
        hero_section = QFrame()
        hero_section.setStyleSheet("""
            QFrame {
                color: black;
                background-color: white;
            }
        """)
        hero_layout = QHBoxLayout(hero_section)
        hero_layout.setContentsMargins(30, 30, 30, 30)

        # Left side of hero (headings and tagline in a single border)
        hero_text = QWidget()
        hero_text_layout = QVBoxLayout(hero_text)
        hero_text_layout.setContentsMargins(0, 0, 0, 0)

        # All headings inside one border
        heading_frame = QFrame()

        heading_layout = QVBoxLayout(heading_frame)
        heading_layout.setContentsMargins(0, 0, 0, 0)

        heading1 = QLabel("From Gesture")
        heading1.setFont(QFont("Arial", 24))
        heading2 = QLabel("Translation")
        heading2.setFont(QFont("Arial", 24))
        heading3 = QLabel("to Device Control,")
        heading3.setFont(QFont("Arial", 24))
        heading4 = QLabel("All in One")
        heading4.setFont(QFont("Arial", 24))

        heading_layout.addWidget(heading1)
        heading_layout.addWidget(heading2)
        heading_layout.addWidget(heading3)
        heading_layout.addWidget(heading4)

        tagline = QLabel("Experience the power of gesture recognition")
        tagline.setFont(QFont("Arial", 12))

        # Add heading and tagline to the layout
        hero_text_layout.addWidget(heading_frame)
        hero_text_layout.addWidget(tagline)

        # Buttons container
        button_container = QWidget()
        button_layout = QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 10, 0, 0)

        translate_button = QPushButton("Gesture translation!")
        translate_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                padding: 5px 15px;
                margin: 5px 10px;
                min-width: 300px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        translate_button.clicked.connect(lambda: self.window().stacked_widget.setCurrentIndex(1))

        control_button = QPushButton("Control your Device!")
        control_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border-radius: 10px;
                font-weight: bold;
                padding: 5px 15px;
                margin: 5px 10px;
                min-width: 300px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        control_button.clicked.connect(lambda: self.window().stacked_widget.setCurrentIndex(2))

        button_layout.addWidget(translate_button)
        button_layout.addWidget(control_button)

        hero_text_layout.addWidget(button_container)

        # Right side of hero - image
        hero_image = QLabel()
        pixmap = QPixmap("image_for_home2.png")
        if not pixmap.isNull():
            hero_image.setPixmap(pixmap.scaled(570, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            # Fallback if image not found
            hero_image.setText("Image not found")
            hero_image.setStyleSheet("background-color: #f0f0f0; padding: 140px; border-radius: 10px;")

        # Add hero elements to hero layout
        hero_layout.addWidget(hero_text)
        hero_layout.addWidget(hero_image)

        # Add hero section to main layout
        scroll_layout.addWidget(hero_section)

        # Categories grid
        categories_section = QFrame()
        categories_section.setStyleSheet("""
            QFrame {
                margin-top: 20px;
                background-color: white;
            }
        """)
        categories_layout = QVBoxLayout(categories_section)

        # Header for Features
        features_header = QLabel("🖐️ Features That Empower Your Hands")
        features_header.setFont(QFont("Arial", 18, QFont.Bold))
        features_desc = QLabel("We bring together gesture recognition and artificial intelligence to let you communicate and control devices in a whole new way.")
        features_desc.setWordWrap(True)

        categories_layout.addWidget(features_header)
        categories_layout.addWidget(features_desc)





        # Features grid
        features_container = QFrame()
        features_container.setStyleSheet("""
            QFrame {
                border: 1px solid gray;
                border-radius: 20px;
                background-color: white;
                margin-top: 10px;
            }
        """)
        features_layout = QHBoxLayout(features_container)
        features_layout.setContentsMargins(20, 20, 20, 40)

        # Feature 1: Gesture Translation
        feature1 = self.create_feature_card(
            "Gesture Translation",
            "images/no.webp",
            "Upload an image of your hand gesture or use your webcam to capture it in real-time. Our intelligent system will instantly interpret the gesture, translating it into one of several powerful commands like 'Go', 'I Love You', or 'Thank You'. This feature is designed to break communication barriers, helping users express themselves through simple, visual cues."
        )

        # Feature 2: Device Control
        feature2 = self.create_feature_card(
            "Device Control",
            "images/device_contol.jpeg",
            "Use your hands as remote controls! Whether you're navigating your PC, switching slides during a presentation, adjusting screen brightness, or controlling your TV and smart home devices all you need are simple, natural gestures. Touchless interaction makes device control intuitive, fast, and accessible."
        )

        # Feature 3: AI Powered
        feature3 = self.create_feature_card(
            "AI Powered",
            "images/bb.webp",
            "At the core of our system is a powerful Convolutional Neural Network (CNN) trained to understand human gestures with high accuracy. This AI continuously learns and adapts to your movements, enabling real-time gesture recognition and flawless execution of your commands."
        )

        # Add features to grid
        features_layout.addWidget(feature1)
        features_layout.addWidget(feature2)
        features_layout.addWidget(feature3)

        # Add features container to categories layout
        categories_layout.addWidget(features_container)

        # Add categories section to scroll layout
        scroll_layout.addWidget(categories_section)

        # Quick access icons grid
        quick_access = QFrame()
        quick_access_layout = QHBoxLayout(quick_access)

        # First row of quick access icons
        quick_row1 = QWidget()
        quick_row1_layout = QHBoxLayout(quick_row1)

        hands_speak = self.create_icon_widget("Hands Speak", "images/hadns_speaks.jpeg")
        gesture_control = self.create_icon_widget("Gesture Control", "images/gestur control.jpeg")

        quick_row1_layout.addWidget(hands_speak)
        quick_row1_layout.addWidget(gesture_control)

        # Second row of quick access icons
        quick_row2 = QWidget()
        quick_row2_layout = QHBoxLayout(quick_row2)

        gesture_power = self.create_icon_widget("Gesture Power", "images/gestur power.jpg")
        quiet_comm = self.create_icon_widget("Quiet Communication", "images/quite communication.webp")

        quick_row2_layout.addWidget(gesture_power)
        quick_row2_layout.addWidget(quiet_comm)

        # Add icon rows to quick access layout
        quick_access_layout.addWidget(quick_row1)
        quick_access_layout.addWidget(quick_row2)

        # Add quick access to scroll layout
        scroll_layout.addWidget(quick_access, 0, Qt.AlignCenter)

        # Add a stretch to push everything up
        scroll_layout.addStretch()

        # Add the scroll area to the main layout
        main_layout.addWidget(scroll_area)

    def create_feature_card(self, title, image_path, description):
        """Create a feature card widget"""
        card = QWidget()
        card.setFixedWidth(500)
        card.setFixedHeight(700)

        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(10, 10, 10, 10)

        # Title
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 14, QFont.Bold))
        title_label.setStyleSheet("padding:20px;padding-right:15px;padding-left:15px;width:200px;max-height:40px;")
        card_layout.addWidget(title_label)

        # Image
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            image_label.setPixmap(pixmap.scaled(500, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            image_label.setStyleSheet("border-radius: 10px;")
        else:
            # Fallback if image not found
            image_label.setText("Image not found")
            image_label.setStyleSheet("background-color: #f0f0f0; padding: 80px; border-radius: 10px;")

        card_layout.addWidget(image_label)

        # Description
        desc_label = QLabel(description)
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: #666;padding:30px;")
        desc_label.setFont(QFont("Arial", 10))
        card_layout.addWidget(desc_label)

        return card

    def create_icon_widget(self, title, image_path):
        """Create a small icon widget"""
        widget = QWidget()
        widget.setFixedSize(430,300)
        widget.setStyleSheet("margin:0px 30px;")

        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Image
        image_label = QLabel()
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            image_label.setPixmap(pixmap.scaled(490, 340, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            image_label.setStyleSheet("border-radius: 10px;")
        else:
            # Fallback if image not found
            image_label.setText("Image not found")
            image_label.setStyleSheet("background-color: #f0f0f0; padding: 30px; border-radius: 10px;")

        layout.addWidget(image_label)

        # Title
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 17))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("""
            QLabel:hover {
                color: #9d4edd;
            }
        """)
        layout.addWidget(title_label)

        return widget

class TranslatorPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the Hand Gesture Recognition UI components"""
        # Configure the main window
        self.setWindowTitle("Hand Gesture Recognition")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #e6e6e6;")
        
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)
        
        # Title section
        title_label = QLabel("Hand Gesture Recognition")
        title_label.setFont(QFont('Arial', 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #333; margin-bottom: 10px;")
        main_layout.addWidget(title_label)
        
        # How It Works Section
        how_frame = QFrame()
        how_frame.setStyleSheet("""
            background-color: #ffffff;
            border-radius: 15px;
            padding: 10px;
        """)
        how_layout = QVBoxLayout(how_frame)
        
        how_title = QLabel("How It Works")
        how_title.setFont(QFont('Arial', 12, QFont.Bold))
        how_title.setStyleSheet("color: #333;")
        
        how_steps = QLabel(
            "1. Click the 'Start Webcam' button to begin\n"
            "2. Show your hand to the camera\n"
            "3. The system detects hand gestures in real-time"
        )
        how_steps.setFont(QFont('Arial', 10))
        how_steps.setStyleSheet("color: #555;")
        how_steps.setContentsMargins(10, 5, 10, 5)
        
        how_layout.addWidget(how_title)
        how_layout.addWidget(how_steps)
        main_layout.addWidget(how_frame)
        
        # Webcam section
        self.webcam_frame = VideoFrame()
        webcam_layout = QVBoxLayout(self.webcam_frame)
        
        # Webcam label for the video feed
        self.webcam_label = QLabel("Webcam Feed")
        self.webcam_label.setAlignment(Qt.AlignCenter)
        self.webcam_label.setFont(QFont('Arial', 12))
        self.webcam_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        webcam_layout.addWidget(self.webcam_label)
        
        main_layout.addWidget(self.webcam_frame)
        
        # Buttons section
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(50, 10, 50, 10)
        
        self.webcam_button = StylishButton("Start Webcam")
        self.webcam_button.clicked.connect(self.toggle_webcam)
        
        button_layout.addStretch()
        button_layout.addWidget(self.webcam_button)
        button_layout.addStretch()
        
        main_layout.addLayout(button_layout)
        
        # Webcam properties
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_webcam)
        self.cap = None
        self.webcam_running = False

    def toggle_webcam(self):
        if self.webcam_running:
            self.stop_webcam()
            self.webcam_button.setText("Start Webcam")
            self.webcam_button.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 10px;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
                QPushButton:pressed {
                    background-color: #3d8b40;
                }
            """)
        else:
            self.start_webcam()
            self.webcam_button.setText("Stop Webcam")
            self.webcam_button.setStyleSheet("""
                QPushButton {
                    background-color: #f44336;
                    color: white;
                    border-radius: 10px;
                    padding: 8px 16px;
                }
                QPushButton:hover {
                    background-color: #d32f2f;
                }
                QPushButton:pressed {
                    background-color: #b71c1c;
                }
            """)

    def start_webcam(self):
        self.cap = cv2.VideoCapture(0)
        if self.cap.isOpened():
            self.timer.start(30)
            self.webcam_running = True
        else:
            self.webcam_label.setText("Error: Could not access webcam")
            self.webcam_label.setStyleSheet("color: red; font-weight: bold;")
    
    def stop_webcam(self):
        if self.cap:
            self.timer.stop()
            self.cap.release()
            self.cap = None
            self.webcam_running = False
            self.webcam_label.setText("Webcam Feed")
        
    def update_webcam(self):
        ret, frame = self.cap.read()
        if ret:
            # Optional: Add hand gesture detection processing here
            
            # Convert to RGB for Qt
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            
            # Convert to QImage and display
            q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.webcam_label.setPixmap(QPixmap.fromImage(q_img).scaled(
                self.webcam_frame.width() - 30, 
                self.webcam_frame.height() - 30,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            ))
    
    def closeEvent(self, event):
        self.stop_webcam()
        event.accept()

class HelpPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        """Initialize the Help Page UI components"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Create a scroll area for the content
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_content_widget = QWidget(scroll_area)
        scroll_area.setWidget(scroll_content_widget)
        scroll_layout = QVBoxLayout(scroll_content_widget)
        scroll_layout.setSpacing(20)

        # Title section
        title_section = QFrame()
        title_section.setStyleSheet("""
            QFrame {
                background-color: #2c3e50;
                border-radius: 15px;
                color: white;
            }
        """)
        title_layout = QVBoxLayout(title_section)
        
        title_label = QLabel("Gesture Master - Help Guide")
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: white;")
        
        subtitle_label = QLabel("Learn how to use our gesture recognition technology")
        subtitle_label.setFont(QFont("Arial", 14))
        subtitle_label.setAlignment(Qt.AlignCenter)
        subtitle_label.setStyleSheet("color: #ecf0f1;")
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(subtitle_label)
        
        scroll_layout.addWidget(title_section)

        # Introduction section
        intro_section = self.create_section(
            "Introduction",
            "Gesture Master is an application that allows you to communicate and control your devices using hand gestures. "
            "This guide will help you understand how to use the different features of the application."
        )
        scroll_layout.addWidget(intro_section)

        # Getting Started section
        getting_started = self.create_section(
            "Getting Started",
            "To get started with Gesture Master, navigate through the application using the navigation bar at the top. "
            "There are three main sections: Home, Translator, and PC Control."
        )
        scroll_layout.addWidget(getting_started)

        # Gesture Translation section
        translator_section = self.create_section(
            "Gesture Translation",
            "The Gesture Translation feature allows you to translate hand gestures into meaningful commands or expressions.\n\n"
            "How to use:\n"
            "1. Click on 'Translator' in the navigation bar\n"
            "2. Click the 'Start Webcam' button to activate your camera\n"
            "3. Show your hand gesture to the camera\n"
            "4. The system will recognize your gesture and display the translation\n"
            "5. Click 'Stop Webcam' when you're done\n\n"
            "Supported gestures include: 'Go', 'I Love You', 'Thank You', and more."
        )
        scroll_layout.addWidget(translator_section)

        # PC Control section
        pc_control_section = self.create_section(
            "PC Control",
            "The PC Control feature allows you to control your device using hand gestures.\n\n"
            "Available controls:\n"
            "• Mouse Control - Move your hand to control the mouse cursor\n"
            "• Windows + D - Wave up/down to minimize all windows\n"
            "• PowerPoint Control - Swipe left/right to navigate between slides\n"
            "• Brightness Control - Bring fingers close/apart to adjust screen brightness\n"
            "• Volume Control - Pinch/spread fingers to adjust system volume\n\n"
            "To use any control, click on its button in the PC Control page and follow the on-screen instructions."
        )
        scroll_layout.addWidget(pc_control_section)

        # Tips and Tricks section
        tips_section = self.create_section(
            "Tips and Tricks",
            "• Ensure good lighting for better gesture recognition\n"
            "• Position your hand clearly in front of the camera\n"
            "• Keep a neutral background for better detection\n"
            "• Start with simple gestures until you get comfortable\n"
            "• For PC Control, practice the gestures before using them for important tasks"
        )
        scroll_layout.addWidget(tips_section)

        # Troubleshooting section
        troubleshooting_section = self.create_section(
            "Troubleshooting",
            "Common issues and solutions:\n\n"
            "Camera not working?\n"
            "• Make sure your camera is connected and not being used by another application\n"
            "• Check if your camera permissions are enabled\n\n"
            "Gestures not recognized?\n"
            "• Ensure your hand is clearly visible in the frame\n"
            "• Try adjusting the lighting\n"
            "• Make sure your gestures are clear and match the expected patterns\n\n"
            "Controls not responding?\n"
            "• Restart the specific control module\n"
            "• Check if any required dependencies are missing"
        )
        scroll_layout.addWidget(troubleshooting_section)

        # Contact section
        contact_section = self.create_section(
            "Contact and Support",
            "Need more help? Contact our support team:\n\n"
            "• Email: support@gesturemaster.com\n"
            "• Website: www.gesturemaster.com/support\n"
            "• Technical documentation: www.gesturemaster.com/docs"
        )
        scroll_layout.addWidget(contact_section)

        # Add a stretch to push everything up
        scroll_layout.addStretch()

        # Add the scroll area to the main layout
        main_layout.addWidget(scroll_area)

    def create_section(self, title, content):
        """Create a styled section with title and content"""
        section = QFrame()
        section.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #ddd;
            }
        """)
        
        section_layout = QVBoxLayout(section)
        
        # Section title
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setStyleSheet("color: #2c3e50;")
        
        # Section content
        content_label = QLabel(content)
        content_label.setFont(QFont("Arial", 11))
        content_label.setWordWrap(True)
        content_label.setStyleSheet("color: #34495e; padding: 10px;")
        
        section_layout.addWidget(title_label)
        section_layout.addWidget(content_label)
        
        return section

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gesture Master")
        self.setMinimumSize(1200, 800)
        
        # Create stacked widget to hold pages
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Create home page and add it to the stacked widget
        self.home_page = HomePage()
        self.stacked_widget.addWidget(self.home_page)
        
        # Create translator page and add it to the stacked widget
        self.translator_page = TranslatorPage()
        self.stacked_widget.addWidget(self.translator_page)
        
        # Placeholder for other pages (you can implement these later)
        self.PCControlPage = PCControlPage()
        self.stacked_widget.addWidget(self.PCControlPage)

        # PC Control page placeholder
        self.help_page = HelpPage()
        self.stacked_widget.addWidget(self.help_page)
        # Set up window
        self.setup_window()
        
    def setup_window(self):
        """Set up the main window properties"""
        self.setStyleSheet("""
            QMainWindow {
                background-color: white;
            }
            QLabel {
                color: #333;
            }
        """)
        
        # Add a navigation bar with a home button
        self.add_navigation_bar()
        
    def add_navigation_bar(self):
        """Add a navigation bar to the main window"""
        nav_bar = QWidget()
        nav_bar.setStyleSheet("background-color: #2c3e50;")
        nav_bar.setFixedHeight(50)
        
        layout = QHBoxLayout(nav_bar)
        layout.setContentsMargins(10, 0, 10, 0)
        
        # Home button
        home_button = QPushButton("Home")
        home_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                font-weight: bold;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
        """)
        home_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        layout.addWidget(home_button)
        
        # Add placeholder buttons for other pages
        translator_button = QPushButton("Translator")
        translator_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                font-weight: bold;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
        """)
        translator_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(translator_button)
        
        control_button = QPushButton("PC Control")
        control_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: white;
                border: none;
                font-weight: bold;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
        """)
        control_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        layout.addWidget(control_button)
        help_button = QPushButton("Help")
        help_button.setStyleSheet("""
    QPushButton {
        background-color: transparent;
        color: white;
        border: none;
        font-weight: bold;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #34495e;
    }
""")
        help_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(3))
        layout.addWidget(help_button)
        
        # Add spacer to push logo to the right
        layout.addStretch()
        
        # App logo/name
        logo = QLabel("Gesture Master")
        logo.setStyleSheet("color: white; font-weight: bold;")
        layout.addWidget(logo)
        
        # Add the navigation bar to the main window
        self.setMenuWidget(nav_bar)
        self.showMaximized()

class PCControlPage(QWidget):
    def __init__(self):
        super().__init__()
        self.running_processes = []  # Track running processes - ADD THIS!
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Hand Gesture Control Panel')
        self.setGeometry(100, 100, 550, 450)
        
        self.setStyleSheet("background-color: white;")
        
        layout = QVBoxLayout()
        
        # Get the directory where the main script is located
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        button_info = [
            ("Mouse Control",       "icons/mouse.jpeg", "Move hand to control the mouse",                    os.path.join(base_dir, "controls", "Soufaine_pc_control_mouse.py")),

            ("Brightness Control",  "icons/brightnes.png", "Bring fingers close/apart to adjust brightness", os.path.join(base_dir, "controls", "zBrightness_Control.py")),

            ("Volume Control",      "icons/volum.png", "Pinch/spread fingers to control volume",             os.path.join(base_dir, "controls", "volome_controle.py")),

            ("Windows + D",         "icons/WINDOWS.jpg", "Wave up/down to minimize all",                     os.path.join(base_dir, "controls", "Soufaine_pc_control_WINDOWS_D.py")),

            ("PowerPoint Control",  "icons/power_point.jpg", "Swipe left/right to skip slides",              os.path.join(base_dir, "controls", "power_point_controle.py"))
        ]
        
        for name, icon_path, description, script in button_info:
            hbox = QHBoxLayout()

            # Action Button
            button = QPushButton(name, self)
            button.setFont(QFont("Arial", 12, QFont.Bold))
            button.setStyleSheet("width:10px;background-color: #058a00; color: white; border-radius: 10px;padding:10px;")
            button.clicked.connect(lambda _, s=script: self.run_script(s))
            
            # Icon Label
            icon_label = QLabel(self)
            pixmap = QPixmap(icon_path)
            if pixmap.isNull():
                print(f"Warning: Could not load icon {icon_path}")
            else:
                icon_label.setPixmap(pixmap.scaled(200, 200))
                icon_label.setStyleSheet("margin:0px 80px;")

            # Description Label
            desc_label = QLabel(description)
            desc_label.setFont(QFont("Arial", 10))
            desc_label.setStyleSheet("color: black;")
            
            hbox.addWidget(button, 2)
            hbox.addWidget(icon_label, 2)
            hbox.addWidget(desc_label, 2)

            layout.addLayout(hbox)
        
        # ADD BIG RED STOP BUTTON
        stop_button = QPushButton("🛑 STOP ALL CONTROLS", self)
        stop_button.setFont(QFont("Arial", 14, QFont.Bold))
        stop_button.setStyleSheet("""
            QPushButton {
                background-color: #dc3545; 
                color: white; 
                border-radius: 10px;
                padding: 15px;
                margin-top: 20px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
            QPushButton:pressed {
                background-color: #bd2130;
            }
        """)
        stop_button.clicked.connect(self.stop_all_scripts)
        layout.addWidget(stop_button)
        
        self.setLayout(layout)

    def run_script(self, script_name):
        if not os.path.exists(script_name):
            print(f'Error: File {script_name} not found.')
            return
            
        try:
            import sys
            # Use Popen instead of run so we can track it
            process = subprocess.Popen([sys.executable, script_name])
            self.running_processes.append(process)
            print(f'Started {os.path.basename(script_name)} with PID: {process.pid}')
        except Exception as e:
            print(f'Error executing {script_name}: {e}')

    def stop_all_scripts(self):
        """Stop all running control scripts"""
        if not self.running_processes:
            print("No scripts running")
            return
            
        for process in self.running_processes:
            try:
                if process.poll() is None:  # Check if still running
                    process.terminate()  # Gracefully stop
                    try:
                        process.wait(timeout=2)  # Wait for it to stop
                    except:
                        process.kill()  # Force stop if needed
                    print(f"Stopped process PID: {process.pid}")
            except Exception as e:
                print(f"Error stopping process: {e}")
        
        self.running_processes.clear()
        print("✅ All scripts stopped")
    
    def closeEvent(self, event):
        """Called when window closes"""
        self.stop_all_scripts()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

