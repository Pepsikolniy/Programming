#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

public slots:
    void loadImage();
    void saveImage();
    void encodeMsg();
    void decodeMsg();

private:
    Ui::MainWindow *ui;

    QImage img;
    size_t image_size;

    const size_t message_length = 4;
    const std::array<char, 3> marker {
        static_cast<char>(0b11100010),
        static_cast<char>(0b10011101),
        static_cast<char>(0b10100100)
    };

};
#endif // MAINWINDOW_H
