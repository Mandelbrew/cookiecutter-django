/**
 * Project: {{cookiecutter.project_slug}}
 *
 * Created by {{cookiecutter.project_author}}
 */

"use strict";

//  Base
// --------------------------
import "babel-polyfill";

//  Vendors
// --------------------------
import "tether"; // Bootstrap 4 requirement
import "bootstrap";
import "holderjs"; // Image placeholders

$(document).ready(() => {
    document.documentElement.classList.remove('no-js');
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    });
    $(function () {
        $('[data-toggle="popover"]').popover()
    })
});
