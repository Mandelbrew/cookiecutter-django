/**
 * Project: {{cookiecutter.project_slug}}
 *
 * Created by {{cookiecutter.project_author}}
 */

"use strict";

const path = require('path');
const webpack = require('webpack');
const autoprefixer = require('autoprefixer');
const ProvidePlugin = webpack.ProvidePlugin;
const CommonsChunkPlugin = webpack.optimize.CommonsChunkPlugin;
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

//region Plugins
const providePlugin = new ProvidePlugin({ // Provide jquery to all
    $: 'jquery',
    jQuery: 'jquery',
    'window.jQuery': 'jquery',
    'Tether': 'tether',
    'window.Tether': 'tether'
});
const extractSassPlugin = new ExtractTextPlugin({filename: '[name].css'});
const uglifyJSPlugin = new UglifyJSPlugin({compress: true});
const vendorChunkPlugin = new CommonsChunkPlugin("application");
//endregion

module.exports = {
    entry: {
        'application': './assets/js/main',
        'stylesheet': './assets/css/main.scss',
    },
    output: {
        path: path.resolve(process.env.WEBPACK_OUTPUT),
        filename: '[name].js',
    },
    resolve: {
        alias: {
            jquery: 'jquery/src/jquery'
        }
    },
    plugins: [
        providePlugin,
        extractSassPlugin,
        uglifyJSPlugin,
        vendorChunkPlugin,
    ],
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: [
                    {
                        loader: 'babel-loader',
                        options: {
                            presets: [
                                ['es2015', {'modules': false}]
                            ],
                            plugins: ['transform-runtime', 'transform-es2015-classes']

                        }
                    }
                ]
            },
            {
                test: /\.scss$/,
                use: extractSassPlugin.extract({
                    use: [
                        // {
                        //     loader: 'style-loader' // creates style nodes from JS strings
                        // },
                        {
                            loader: 'css-loader', // translates CSS into CommonJS
                            options: {
                                sourceMap: true,
                                minimize: true
                            }
                        },
                        {
                            loader: 'postcss-loader',
                            options: {
                                plugins () {
                                    return [
                                        autoprefixer({browsers: '> 1%, last 2 versions'}),
                                    ];
                                }
                            }
                        },
                        {
                            loader: 'resolve-url-loader',
                            options: {
                                sourceMap: true,
                                // debug: true
                            }
                        },
                        {
                            loader: 'sass-loader', // compiles Sass to CSS
                            options: {
                                precision: 8,
                                sourceMap: true,
                            }
                        }

                    ]
                })
            },
            {
                test: /\.(png|jpg|gif|svg|eot|ttf|woff|woff2)$/,
                loader: 'url-loader',
                options: {
                    limit: 10000
                }
            }
            // { // Some modules don't import jquery on their own.
            //     test: /\.js$/,
            //     loader: 'imports?$=jquery,jQuery=jquery'
            // },
            // { // Some legacy modules rely on this being the window object.
            //     test: /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/,
            //     loader: 'imports?this=>window'
            // },
            // { // It executes the module in a global context, just as if you had included them via the <script> tag.
            //     test: /script.js$/,
            //     loader: 'script?'
            // },
            // { // Disable/fix AMD
            //     test: /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/,
            //     loader: 'imports?define=>false'
            // },
            // { // Disable/fix CommonJS
            //     test: /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/,
            //     loader: 'imports?require=>false'
            // },
        ]
        // noParse: [ // If there is no AMD/CommonJS version of the module and you only want to include the /dist.
        //     /[\/\\]node_modules[\/\\]some-module[\/\\]index\.js$/
        // ],
    }
};
