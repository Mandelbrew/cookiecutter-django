/**
 *
 * Created by cavila on 7/12/16.
 *
 */

var webpack = require("webpack");

module.exports = {
    entry: {
        main: "./src/main"
    },
    output: {
        path: './bin',
        filename: "[name].js"
    },
    resolve: {
        // alias: { // make jquery point to the right source file
        //     jquery: "jquery/src/jquery"
        // }
    },
    plugins: [
        // new webpack.ProvidePlugin({ // Provide jquery to all
        //     $: "jquery",
        //     jQuery: "jquery",
        //     "window.jQuery": "jquery"
        // })
    ],
    module: {
        // noParse: [ // If there is no AMD/CommonJS version of the module and you only want to include the /dist.
        //     /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/
        // ],
        loaders: [
            // { // Some modules don't import jquery on their own.
            //     test: /\.js$/,
            //     loader: "imports?$=jquery,jQuery=jquery"
            // },
            // { // Some legacy modules rely on this being the window object.
            //     test: /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/,
            //     loader: "imports?this=>window"
            // },
            // { // It executes the module in a global context, just as if you had included them via the <script> tag.
            //     test: /script.js$/,
            //     loader: "script?"
            // },
            // { // Disable/fix AMD
            //     test: /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/,
            //     loader: "imports?define=>false"
            // },
            // { // Disable/fix CommonJS
            //     test: /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/,
            //     loader: "imports?require=>false"
            // },
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components|vendors)/,
                loader: "babel-loader",
                query: {
                    presets: ["es2015"],
                    plugins: ["transform-runtime", "transform-es2015-classes"]
                }
            }
        ]
    }
};

