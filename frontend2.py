import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QRadialGradient
from PyQt5.QtWidgets import QApplication, QWidget
from math import sin, cos, radians

class FuturisticAnimation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("High-Accuracy Futuristic Animation")
        self.setGeometry(100, 100, 600, 600)
        self.angle_outer = 0
        self.angle_inner = 0
        self.angle_middle = 0

        # Timer for animation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(20)  # Increased frame rate for smoother rotation

        # Movement factors for oscillation
        self.movement_factor_outer = 0
        self.movement_factor_inner = 0
        self.movement_speed = 0.05  # Speed of the movement in and out

    def update_animation(self):
        self.angle_outer += 1.5  # Fine-tuned outer rotation speed
        self.angle_inner -= 2  # Opposite direction, slightly faster
        self.angle_middle += 0.8  # Middle circle slower

        if self.angle_outer >= 360: self.angle_outer = 0
        if self.angle_inner <= -360: self.angle_inner = 0
        if self.angle_middle >= 360: self.angle_middle = 0

        # Update movement factors for oscillation
        self.movement_factor_outer += self.movement_speed
        self.movement_factor_inner += self.movement_speed

        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Central coordinates
        cx, cy = self.width() / 2, self.height() / 2

        # Dark background
        painter.fillRect(self.rect(), QColor(0, 0, 0))

        # Draw glowing center and rings
        self.draw_glowing_center(painter, cx, cy, radius=100, glow_color=QColor(0, 255, 255, 200))
        
        # Calculate dynamic radii for outer and inner arcs using sine for oscillation
        dynamic_radius_outer = 250 + 20 * sin(self.movement_factor_outer)  # Outer ring
        dynamic_radius_inner = 180 + 15 * sin(self.movement_factor_inner)  # Inner ring

        # Draw arcs with oscillation effect
        self.draw_rotating_arcs(painter, cx, cy, radius=dynamic_radius_outer, thickness=12, 
                                 segments=90, angle_offset=self.angle_outer, color=QColor(0, 255, 255), gap=8)
        self.draw_rotating_arcs(painter, cx, cy, radius=dynamic_radius_inner, thickness=8, 
                                 segments=60, angle_offset=self.angle_inner, color=QColor(0, 200, 255), gap=10)
        
        # Draw rotating dots
        self.draw_rotating_dots(painter, cx, cy, radius=120, segments=40, angle_offset=self.angle_middle, color=QColor(0, 255, 200))

    def draw_rotating_arcs(self, painter, x, y, radius, thickness, segments, angle_offset, color, gap):
        # Rotating arcs with finer gaps and better spacing control
        painter.setPen(QPen(color, thickness, Qt.SolidLine, Qt.RoundCap))
        segment_angle = 360 / segments
        arc_length = segment_angle - gap

        for i in range(segments):
            angle = i * segment_angle + angle_offset
            rad_angle_start = radians(angle)
            rad_angle_end = radians(angle + arc_length)
            start_x = x + radius * cos(rad_angle_start)
            start_y = y + radius * sin(rad_angle_start)
            end_x = x + radius * cos(rad_angle_end)
            end_y = y + radius * sin(rad_angle_end)

            painter.drawLine(start_x, start_y, end_x, end_y)

    def draw_rotating_dots(self, painter, x, y, radius, segments, angle_offset, color):
        # Rotating dots inside the middle circle
        painter.setPen(QPen(color, 2, Qt.SolidLine, Qt.RoundCap))
        segment_angle = 360 / segments

        for i in range(segments):
            angle = i * segment_angle + angle_offset
            rad_angle = radians(angle)
            start_x = x + radius * cos(rad_angle)
            start_y = y + radius * sin(rad_angle)
            painter.drawEllipse(start_x - 5, start_y - 5, 10, 10)  # Smaller rotating dots

    def draw_glowing_center(self, painter, x, y, radius, glow_color):
        # Increased glow intensity for central effect
        gradient = QRadialGradient(x, y, radius)
        gradient.setColorAt(0, glow_color)
        gradient.setColorAt(1, Qt.transparent)
        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(x - radius, y - radius, 2 * radius, 2 * radius)

# Main execution
app = QApplication(sys.argv)
window = FuturisticAnimation()
window.show()
sys.exit(app.exec_())
