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
import "tether";
import "bootstrap";

$(document).ready(() => {
    document.documentElement.classList.remove('no-js');
});
