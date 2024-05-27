from PySide6.QtWidgets import QGraphicsDropShadowEffect

SHADOW_RESET = QGraphicsDropShadowEffect(xOffset=5, yOffset=5, blurRadius=10)
SHADOW_CALC = QGraphicsDropShadowEffect(xOffset=5, yOffset=5, blurRadius=10)
SHADOW_GOBACK = QGraphicsDropShadowEffect(xOffset=5, yOffset=5, blurRadius=10)
SHADOWS_ICONS = [QGraphicsDropShadowEffect(xOffset=5, yOffset=5, blurRadius=10) for _ in range(8)]

SHADOWS_ENTRY = [QGraphicsDropShadowEffect(xOffset=5, yOffset=5, blurRadius=10) for _ in range(2)]