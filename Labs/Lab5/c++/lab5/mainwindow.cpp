#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QImage>
#include <QFileDialog>
#include <QMessageBox>
#include <QBitArray>
#include <QFile>
#include <QTextStream>

#define NDEBUG

void set_bit(QImage &img, int index, bool val) {
    int pixelIndex = index / 3;

    int x = pixelIndex % img.width();
    int y = pixelIndex / img.width();

#ifndef NDEBUG
    if (y >= img.height())
        throw std::out_of_range("выходит за пределы картинки");
#endif

    //img.pixel returns #AARRGGBB
    switch (index % 3) {
    case 0:
        img.setPixel(x, y, (img.pixel(x, y) & ~0x010000) | (val << 16));
    case 1:
        img.setPixel(x, y, (img.pixel(x, y) & ~0x000100) | (val << 8));
    default:
        img.setPixel(x, y, (img.pixel(x, y) & ~0x000001) | val);
    }
}

bool get_bit(const QImage &img, int index) {
    int pixelIndex = index / 3;

    int x = pixelIndex % img.width();
    int y = pixelIndex / img.width();

#ifndef NDEBUG
    if (y >= img.height())
        throw std::out_of_range("индекс бита выходит за пределы картинки");
#endif

    //img.pixel returns #AARRGGBB
    switch (index % 3) {
    case 0:
        return (img.pixel(x, y) >> 16) & 1;
    case 1:
        return (img.pixel(x, y) >> 8) & 1;
    default:
        return img.pixel(x, y) & 1;
    }

    Q_UNREACHABLE();
}

QByteArray read_bytes(const QImage& img, size_t begin, size_t length) {
    QByteArray byteArray;
    char buf = 0;

    size_t end = (begin + length) * 8;

#ifndef NDEBUG
    if (static_cast<size_t>(img.width() * img.height() * 8 * 3) <= end)
        throw std::out_of_range("попытка прочитать биты вне картинки");
#endif

    for (size_t i = begin * 8; i < end; ++i) {
        buf = (buf << 1) | get_bit(img, i);

        if (i % 8 == 7) {
            byteArray.push_back(buf);
            buf = 0;
        }
    }

    return byteArray;
}

void write_bytes(QImage& img, size_t begin, QByteArray& byteArray) {
    size_t end = (begin + byteArray.size()) * 8;

#ifndef NDEBUG
    if (static_cast<size_t>(img.width() * img.height() * 8 * 3) <= end)
        throw std::out_of_range("попытка записать биты вне картинки");
#endif

    for (size_t i = begin * 8; i < end; ++i) {
        set_bit(img, i, (byteArray[i / 8] >> (7 - i % 8)) & 1);
    }

}
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->pushButton, &QPushButton::clicked, this, &MainWindow::loadImage);
    connect(ui->pushButton_2, &QPushButton::clicked, this, &MainWindow::saveImage);
    connect(ui->pushButton_3, &QPushButton::clicked, this, &MainWindow::encodeMsg);
    connect(ui->pushButton_4, &QPushButton::clicked, this, &MainWindow::decodeMsg);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::loadImage()
{
    QString fileName = QFileDialog::getOpenFileName(this, tr("Загрузить картинку"), "", tr("Допустимые форматы (*.png)"));
    if(!img.load(fileName, "PNG"))
        ui->label->setText("Изображение не загружено");
    else
        ui->label->setText("Изображение успешно загружено");

    img.convertTo(QImage::Format_ARGB32);

    image_size = (img.width()*img.height()*3)/8 - marker.size() - message_length;
}

void MainWindow::saveImage()
{
    QString fileName = QFileDialog::getSaveFileName(this, tr("Сохранить картинку"), "", tr("Допустимые форматы (*.png)"));
    if(!img.save(fileName, "PNG"))
        ui->label->setText("Изображение не сохранено");
    else
         ui->label->setText("Изображение успешно сохранено");

}

void MainWindow::encodeMsg()
{
    QString text = ui->plainTextEdit->toPlainText();
    QByteArray byte = text.toUtf8();

    size_t bytes_count = byte.size();

    if(image_size < bytes_count){
        ui->label->setText("Ошибка. Не достаточно места!");
        return;
    }

    QByteArray bytes_array;
    bytes_array.push_back(marker);
    for (int i = message_length - 1; i >= 0; --i) {
        bytes_array.push_back((bytes_count >> i*8) & 0xff);
    }
    bytes_array.push_back(ui->plainTextEdit->toPlainText().toUtf8());

    write_bytes(img, 0, bytes_array);

    ui->label->setText("Сообщение добавлено в картинку");
}

void MainWindow::decodeMsg()
{
    int headerSize = marker.size() + message_length;
    QByteArray bytes_array;

    bytes_array = read_bytes(img, 0, headerSize);

    for (size_t i = 0; i < marker.size(); ++i) {
        if (marker[i] != bytes_array[i]) {
            ui->label->setText("Сообщение не обнаружено");
            return;
        }
    }

    size_t message_size = 0;
    for (size_t i = marker.size(); i < marker.size() + message_length; ++i) {
        message_size = (message_size << 8) + static_cast<unsigned char>(bytes_array[i]);
    }

    if (message_size > image_size) {
         ui->label->setText("Ошибка. Размер сообщения в заголовке превышает размер изображения");
        return;
    }

    bytes_array = read_bytes(img, headerSize, message_size);

    QString text = QString::fromUtf8(bytes_array);

    ui->plainTextEdit->setPlainText(text);

    ui->label->setText(QString("Присутствует сообщение длиной %1 байт").arg(message_size));
}
