/********************************************************************************
** Form generated from reading UI file 'HellperUI.ui'
**
** Created by: Qt User Interface Compiler version 5.11.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef HELLPER_VER1_H
#define HELLPER_VER1_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QPushButton *ltBnt;
    QPushButton *rbButton;
    QLineEdit *ltPoint;
    QLineEdit *rbPoint;
    QPushButton *clrExcBtn;
    QLineEdit *ColorExt;
    QLabel *lblColor;
    QPushButton *ltThreadBtn;
    QPushButton *rtThreadBtn;
    QPushButton *rbThreadBtn;
    QPushButton *lbThreadBtn;
    QPushButton *ExitBtn;
    QPushButton *StartBtn;
    QLineEdit *ltThread;
    QLineEdit *lbThread;
    QLineEdit *rtThread;
    QLineEdit *rbThread;
    QPushButton *StopBtn;
    QLabel *copyright;
    QMenuBar *menubar;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(283, 314);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        ltBnt = new QPushButton(centralwidget);
        ltBnt->setObjectName(QStringLiteral("ltBnt"));
        ltBnt->setGeometry(QRect(30, 20, 75, 23));
        rbButton = new QPushButton(centralwidget);
        rbButton->setObjectName(QStringLiteral("rbButton"));
        rbButton->setGeometry(QRect(30, 50, 75, 23));
        ltPoint = new QLineEdit(centralwidget);
        ltPoint->setObjectName(QStringLiteral("ltPoint"));
        ltPoint->setGeometry(QRect(110, 20, 141, 20));
        rbPoint = new QLineEdit(centralwidget);
        rbPoint->setObjectName(QStringLiteral("rbPoint"));
        rbPoint->setGeometry(QRect(110, 50, 141, 20));
        clrExcBtn = new QPushButton(centralwidget);
        clrExcBtn->setObjectName(QStringLiteral("clrExcBtn"));
        clrExcBtn->setGeometry(QRect(30, 80, 75, 23));
        clrExcBtn->setLayoutDirection(Qt::LeftToRight);
        ColorExt = new QLineEdit(centralwidget);
        ColorExt->setObjectName(QStringLiteral("ColorExt"));
        ColorExt->setGeometry(QRect(130, 80, 121, 20));
        lblColor = new QLabel(centralwidget);
        lblColor->setObjectName(QStringLiteral("lblColor"));
        lblColor->setGeometry(QRect(110, 80, 16, 16));
        ltThreadBtn = new QPushButton(centralwidget);
        ltThreadBtn->setObjectName(QStringLiteral("ltThreadBtn"));
        ltThreadBtn->setGeometry(QRect(30, 120, 31, 23));
        rtThreadBtn = new QPushButton(centralwidget);
        rtThreadBtn->setObjectName(QStringLiteral("rtThreadBtn"));
        rtThreadBtn->setGeometry(QRect(160, 120, 31, 23));
        rbThreadBtn = new QPushButton(centralwidget);
        rbThreadBtn->setObjectName(QStringLiteral("rbThreadBtn"));
        rbThreadBtn->setGeometry(QRect(160, 150, 31, 23));
        lbThreadBtn = new QPushButton(centralwidget);
        lbThreadBtn->setObjectName(QStringLiteral("lbThreadBtn"));
        lbThreadBtn->setGeometry(QRect(30, 150, 31, 23));
        ExitBtn = new QPushButton(centralwidget);
        ExitBtn->setObjectName(QStringLiteral("ExitBtn"));
        ExitBtn->setGeometry(QRect(190, 180, 61, 23));
        StartBtn = new QPushButton(centralwidget);
        StartBtn->setObjectName(QStringLiteral("StartBtn"));
        StartBtn->setGeometry(QRect(30, 180, 61, 23));
        ltThread = new QLineEdit(centralwidget);
        ltThread->setObjectName(QStringLiteral("ltThread"));
        ltThread->setGeometry(QRect(69, 121, 51, 20));
        lbThread = new QLineEdit(centralwidget);
        lbThread->setObjectName(QStringLiteral("lbThread"));
        lbThread->setGeometry(QRect(69, 151, 51, 20));
        rtThread = new QLineEdit(centralwidget);
        rtThread->setObjectName(QStringLiteral("rtThread"));
        rtThread->setGeometry(QRect(200, 121, 51, 20));
        rbThread = new QLineEdit(centralwidget);
        rbThread->setObjectName(QStringLiteral("rbThread"));
        rbThread->setGeometry(QRect(200, 151, 51, 20));
        StopBtn = new QPushButton(centralwidget);
        StopBtn->setObjectName(QStringLiteral("StopBtn"));
        StopBtn->setGeometry(QRect(110, 180, 61, 23));
        copyright = new QLabel(centralwidget);
        copyright->setObjectName(QStringLiteral("copyright"));
        copyright->setGeometry(QRect(16, 250, 251, 20));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QStringLiteral("menubar"));
        menubar->setGeometry(QRect(0, 0, 283, 21));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        ltBnt->setText(QApplication::translate("MainWindow", "\354\242\214\354\203\201\353\213\250", nullptr));
        rbButton->setText(QApplication::translate("MainWindow", "\354\232\260\355\225\230\353\213\250", nullptr));
        clrExcBtn->setText(QApplication::translate("MainWindow", "\354\203\211\354\203\201\354\266\224\354\266\234", nullptr));
        lblColor->setText(QApplication::translate("MainWindow", "clr", nullptr));
        ltThreadBtn->setText(QApplication::translate("MainWindow", "\342\206\230", nullptr));
        rtThreadBtn->setText(QApplication::translate("MainWindow", "\342\206\231", nullptr));
        rbThreadBtn->setText(QApplication::translate("MainWindow", "\342\206\226", nullptr));
        lbThreadBtn->setText(QApplication::translate("MainWindow", "\342\206\227", nullptr));
        ExitBtn->setText(QApplication::translate("MainWindow", "\354\242\205\353\243\214", nullptr));
        StartBtn->setText(QApplication::translate("MainWindow", "\354\213\234\354\236\221", nullptr));
        StopBtn->setText(QApplication::translate("MainWindow", "\353\251\210\354\266\244", nullptr));
        copyright->setText(QApplication::translate("MainWindow", "Copyright 2019. KKIMSSI. All rights reserved.", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // HELLPER_VER1_H
