import QtQuick 2.5
import QtQuick.Layouts 1.1
import QtQuick.Controls 1.4

Item {
    property alias open_project_button: open_project_button
    property alias recent_list_view: recent_list_view
    property alias new_project: new_project
    property alias base: base
    anchors.fill: parent
    SystemPalette { id: myPalette; colorGroup: SystemPalette.Active}


    Rectangle {
        id: base
        color: myPalette.window
        anchors.fill: parent

        GridLayout {
            id: grid1
            anchors.rightMargin: 0
            anchors.bottomMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
            rows: 3
            columns: 3
            anchors.fill: parent
            flow: GridLayout.TopToBottom

            Item {
                id: item1
                width: 200
                height: 200
                Layout.preferredHeight: 0
                Layout.columnSpan: 3
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.maximumHeight: 100
                Layout.maximumWidth: 100
                Layout.minimumHeight: 40
                Layout.minimumWidth: 50
            }









            Item {
                id: item2
                width: 200
                height: 200
                Layout.fillWidth: true
                Layout.fillHeight: true
                Layout.columnSpan: 3
                Layout.maximumHeight: 200
                Layout.maximumWidth: 200
                Layout.minimumHeight: 100
                Layout.minimumWidth: 100
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
            }


            Item {
                id: item3
                width: 200
                height: 200
                Layout.minimumHeight: 40
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.preferredHeight: 0
                Layout.columnSpan: 3
                Layout.maximumWidth: 100
                Layout.minimumWidth: 50
                Layout.maximumHeight: 100
            }


            Item {
                id: item4
                width: 200
                height: 200
                Layout.minimumHeight: 40
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.preferredHeight: 0
                Layout.columnSpan: 3
                Layout.maximumWidth: 100
                Layout.minimumWidth: 50
                Layout.maximumHeight: 100
            }

            GridLayout {
                id: gridLayout1
                width: 100
                height: 100
                flow: GridLayout.TopToBottom
                rows: 2
                columns: 2
                Layout.alignment: Qt.AlignLeft | Qt.AlignTop


                Text {
                    id: text1
                    text: qsTr("Recent projects")
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    horizontalAlignment: Text.AlignHCenter
                    font.pixelSize: 12
                }

                ListView {
                    id: recent_list_view
                    width: 110
                    height: 160
                    boundsBehavior: Flickable.StopAtBounds
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    model: ListModel {
                        ListElement {
                            name: "Grey"
                            colorCode: "grey"
                        }

                        ListElement {
                            name: "Red"
                            colorCode: "red"
                        }

                        ListElement {
                            name: "Blue"
                            colorCode: "blue"
                        }

                        ListElement {
                            name: "Green"
                            colorCode: "green"
                        }
                    }
                    delegate: Item {
                        x: 5
                        width: 80
                        height: 40
                        Row {
                            id: row1
                            spacing: 10
                            Rectangle {
                                width: 40
                                height: 40
                                color: colorCode
                            }

                            Text {
                                text: name
                                font.bold: true
                                anchors.verticalCenter: parent.verticalCenter
                            }
                        }
                    }
                }



                Button {
                    id: new_project
                    text: qsTr("New project")
                }

                Button {
                    id: open_project_button
                    text: qsTr("Open project")
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter

                }



            }

            Item {
                id: item5
                width: 200
                height: 200
                Layout.fillHeight: true
                Layout.minimumHeight: 100
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.preferredHeight: 0
                Layout.columnSpan: 3
                Layout.maximumWidth: 100
                Layout.minimumWidth: 100
                Layout.maximumHeight: 100
            }

            Item {
                id: item6
                width: 200
                height: 200
                Layout.fillHeight: true
                Layout.fillWidth: true
                Layout.minimumHeight: 100
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.preferredHeight: 0
                Layout.columnSpan: 3
                Layout.maximumWidth: 200
                Layout.minimumWidth: 100
                Layout.maximumHeight: 200
            }

            Item {
                id: item7
                width: 200
                height: 200
                Layout.minimumHeight: 40
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.preferredHeight: 0
                Layout.columnSpan: 3
                Layout.maximumWidth: 100
                Layout.minimumWidth: 50
                Layout.maximumHeight: 100
            }

            Item {
                id: item8
                width: 200
                height: 200
                Layout.minimumHeight: 40
                Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                Layout.preferredHeight: 0
                Layout.columnSpan: 3
                Layout.maximumWidth: 100
                Layout.minimumWidth: 50
                Layout.maximumHeight: 100
            }
        }
    }
}
