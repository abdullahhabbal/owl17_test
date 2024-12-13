/* @odoo-module */

import { registry } from "@web/core/registry";
import { Component, useState } from "@odoo/owl";

export class ListViewAction extends Component {
    static template = "owl_17.ListView";
}

registry.category("actions").add("owl_17.action_list_view", ListViewAction);