# window.py
#
# Copyright 2023 Jared
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gio, Gtk

@Gtk.Template(resource_path='/com/example/GnomeReminder/window.ui')
class GnomeReminderWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'GnomeReminderWindow'

    add_reminder_view = Gtk.Template.Child()
    add_button = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        add_action = Gio.SimpleAction(name="add")
        add_action.connect("activate", self.test)
        self.add_action(add_action)

    def test(action, _):
        print("HI")
        print(add_reminder_view)
        
