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
    plugin: [],
    resolve: {},
    module: {
        noParse: [],
        loaders: [
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

