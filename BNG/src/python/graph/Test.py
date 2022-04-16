import math
import numpy as np

from BNG.src.python.graph import GraphModel as graph_model
from BNG.src.python.graph import Controller as controller

from PyQt5.QtCore import Qt, QRect, QPointF
from PyQt5.QtGui import QPainter, QColor, QIcon, QPolygonF
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QToolBar, QAction

# функция для вычисления точек полигона стрелки
def calculate_arrow_points(start_point = QPointF, end_point = QPointF, radius = 30):
    try:
        arrow_height = 10
        arrow_width = 10

        dx = start_point.x() - end_point.x()
        dy = start_point.y() - end_point.y()

        length = math.sqrt(dx ** 2 + dy ** 2)

        # нормализуем
        norm_x, norm_y = dx / length, dy / length

        # перпендикулярный вектор
        perpendicular_x = -norm_y
        perpendicular_y = norm_x

        middle_point_x = end_point.x() + radius * norm_x
        middle_point_y = end_point.y() + radius * norm_y
        middle_point = QPointF(middle_point_x, middle_point_y)

        left_point_x = middle_point.x() + arrow_height * norm_x + arrow_width * perpendicular_x
        left_point_y = middle_point.y() + arrow_height * norm_y + arrow_width * perpendicular_y
        left_point = QPointF(left_point_x, left_point_y)

        right_point_x = middle_point.x() + arrow_height * norm_x - arrow_height * perpendicular_x
        right_point_y = middle_point.y() + arrow_height * norm_y - arrow_width * perpendicular_y
        right_point = QPointF(right_point_x, right_point_y)

        return QPolygonF([left_point, middle_point, right_point])

    except (ZeroDivisionError, Exception):
        return None



class Display(QWidget):

    def __init__(self):
        super().__init__()
        self.functionAble = ""
        self.initUI()
        self.Graph = graph_model.Graph(30)

    def initUI(self):
        self.cntPoints = 0  # число вершин в графе
        self.r = 30  # радиус вершины
        self.points = np.array(object=[], dtype=list)  # массив координат центров вершин графа
        self.marked = np.array(object=[], dtype=int)  # массив индексов связанных вершин

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(0, 0, 0))
        # painter.setRenderHint(painter.Antialiasing)

        # как только были отмечены для соединения две вершины, начинаем отрисовывать ребра
        if (len(self.marked) >= 2):
            painter.setPen(QColor(0, 0, 0))
            painter.setPen(Qt.PenStyle.SolidLine) # тут можно использовать Qt.PenStyle.DashLine для пунктирных линий
            # проходимся по массиву с шагом 2 и соединяем отмеченные вершины
            # тут берутся актуальные координаты из массива points
            for i in range(0, len(self.marked), 2):
                # проверка на случай, если число отмеченных вершин нечетное
                # а именно, чтобы индекс текущей парной вершины была в массиве
                if (i + 1 < len(self.marked) and (self.points[self.marked[i]][1] == True and self.points[self.marked[i+1]][1])):
                    triangle_source = calculate_arrow_points(self.points[self.marked[i]][0], self.points[self.marked[i+1]][0])
                    if triangle_source is not None:
                        painter.setBrush(QColor(0, 0, 0))
                        painter.drawPolygon(triangle_source)
                        painter.setPen(QColor(0, 0, 0))
                        painter.setPen(Qt.PenStyle.SolidLine)
                    painter.drawLine((int)(self.points[self.marked[i]][0].x()),
                                    (int)(self.points[self.marked[i]][0].y()),
                                    (int)(self.points[self.marked[i+1]][0].x()),
                                    (int)(self.points[self.marked[i+1]][0].y()))

        # обеспечиваем закрашивание вершин графа
        painter.setBrush(QColor(0, 0, 0))

        # отрисовываем вершины и цифры
        offset = QPointF(-2.5, 5)
        for i in range(len(self.Graph.PointsIsVisible)):
            if (self.Graph.PointsIsVisible[i][1] == True):
                painter.drawEllipse(self.Graph.PointsIsVisible[i][0], self.r, self.r)
                painter.setPen(QColor("white"))
                painter.drawText(self.points[i][0] + offset, f'{i}')
                painter.setPen(QColor(0, 0, 0))

    def mousePressEvent(self, event):
        # нажатие на ЛКМ
        if (self.functionAble == "Добавить вершину"):
           controller.CAddPoint(self.Graph, event, Qt.LeftButton)
        elif (self.functionAble == "Добавить связь"):
            # смотрим на все вершины и проверяем не нажали ли на них ПКМ
            # если да, то добавляем в marked
            # окно чувствительности rxr
            for i in range(self.cntPoints):
                if ((event.button() == Qt.LeftButton) and
                    (event.pos().x() >= self.points[i][0].x() - self.r and event.pos().x() <= self.points[i][0].x() + self.r and
                    event.pos().y() >= self.points[i][0].y() - self.r and event.pos().y() <= self.points[i][0].y() + self.r)):
                    self.marked = np.append(self.marked, i)
                    break
        elif (self.functionAble == "Удалить вершину"):
            sensitivity = 50
            for i in range(self.cntPoints):

                if ((event.pos().x() >= self.points[i][0].x() - sensitivity and event.pos().x() <= self.points[i][0].x() + sensitivity and
                    event.pos().y() >= self.points[i][0].y() - sensitivity and event.pos().y() <= self.points[i][0].y() + sensitivity)):
                    self.points[i][1] = False
                    index = []
                    for j in range(0, len(self.marked), 2):
                        if (j + 1 < len(self.marked) and (self.marked[j] == i or self.marked[j+1] == i)):
                            index.append([j, j+1])

                    self.marked = np.delete(self.marked, index)
                    break
            self.update()

        elif (self.functionAble == "Новый файл"):
            self.cntPoints = 0
            self.points = np.array(object=[], dtype=QPointF)  # массив координат центров вершин графа
            self.marked = np.array(object=[], dtype=int)  # массив индексов связанных вершин
            self.update()

        self.update()

    def mouseMoveEvent(self, event):
        # смотрим на все вершины и проверяем не двигают ли их
        # если да, то добавляем новые координаты в points
        # окно чувствительности rxr
        if (self.functionAble == "Переместить вершины"):
            for i in range(self.cntPoints):
                if (event.pos().x() >= self.points[i][0].x() - self.r and event.pos().x() <= self.points[i][0].x() + self.r and
                    event.pos().y() >= self.points[i][0].y() - self.r and event.pos().y() <= self.points[i][0].y() + self.r):
                    self.points[i][0] = event.pos()
                    break

        self.update()
