/***************************************************************************
 *   Copyright (C) 2018 by Cyril Jacquet                                 *
 *   cyril.jacquet@plume-creator.eu                                        *
 *                                                                         *
 *  Filename: plugininterface.h                                                   *
 *  This file is part of Plume Creator.                                    *
 *                                                                         *
 *  Plume Creator is free software: you can redistribute it and/or modify  *
 *  it under the terms of the GNU General Public License as published by   *
 *  the Free Software Foundation, either version 3 of the License, or      *
 *  (at your option) any later version.                                    *
 *                                                                         *
 *  Plume Creator is distributed in the hope that it will be useful,       *
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of         *
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
 *  GNU General Public License for more details.                           *
 *                                                                         *
 *  You should have received a copy of the GNU General Public License      *
 *  along with Plume Creator.  If not, see <http://www.gnu.org/licenses/>. *
 ***************************************************************************/
#ifndef PLUGININTERFACE_H
#define PLUGININTERFACE_H

#include "plmbasewidget.h"
#include "plmpluginloader.h"


class PLMWriteLeftDockInterface
{
public:
    virtual ~PLMWriteLeftDockInterface() {}

    virtual PLMBaseWidget *dockBodyWidget(QWidget *parent) = 0;
};

#define PLMWriteLeftDockInterface_iid "com.PlumeSoft.Plume-Creator.WriteLeftDockInterface/1.0"

Q_DECLARE_INTERFACE(PLMWriteLeftDockInterface, PLMWriteLeftDockInterface_iid)


#endif // PLUGININTERFACE_H
