# -*- coding: utf-8 -*-
# Juicer - Administer Pulp and Release Carts
# Copyright © 2015, Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from juicer.juicer.JuicerCommand import JuicerCommand
from juicer.cart.Cart import Cart
from juicer.log import Log


class CartShowCommand(JuicerCommand):
    def __init__(self, args):
        super(CartShowCommand, self).__init__(args)

    def run(self):
        cart = Cart(self.args.cartname, autoload=True)
        Log.log_info(str(cart))
