const webpack = require('webpack');
const path = require('path');
const WebpackPwaManifest = require('webpack-pwa-manifest');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const {GenerateSW} = require('workbox-webpack-plugin');
const TerserJSPlugin = require('terser-webpack-plugin');
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const GLOBALS={
  'process.env.NODE_ENV':JSON.stringify('production')
};


module.exports={
  mode:process.env.NODE_ENV,
  entry:[
    path.resolve(__dirname, 'src/index')
  ],
  target: 'web',
  output: {
    path: __dirname + '/dist', 
    publicPath: '/',
    filename: '[name].[hash].js'
  },
  devServer: {
    contentBase: path.resolve(__dirname, 'src')
  },
  optimization: {
    minimizer: [new TerserJSPlugin({}), new OptimizeCSSAssetsPlugin({})],
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  },
  node: {
    fs: 'empty'
  },
  module:{
    rules:[
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader'
        }
      },
      {
        test:/(\.css)$/,
        use:[MiniCssExtractPlugin.loader, 'css-loader']
      },
      {
        test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
        use: [{
            loader: 'file-loader',
            options: {
                name: '[name].[ext]',
                outputPath: 'fonts/'
            }
        }]
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template:'src/index.html',
      title: 'Distance',
    }),
    new MiniCssExtractPlugin({
      // Options similar to the same options in webpackOptions.output
      // both options are optional
      filename: "[name].[contenthash].css",
      chunkFilename: "[id].css"
    }),
    new GenerateSW({
      maximumFileSizeToCacheInBytes:1e+7,
      skipWaiting:true,
      runtimeCaching: [{
        urlPattern: new RegExp('/\.(js|css)$/i'),
        handler: 'StaleWhileRevalidate'
      }],
      swDest:'sw.js'
    }),
    new WebpackPwaManifest({
      name: 'Distance',
      short_name: 'Distance',
      description: 'Distance',
      background_color: '#ffffff',
      includeDirectory:true,
      orientation:'portrait',
      crossorigin: 'anonymous', //can be null, use-credentials or anonymous
      "theme_color": "#3367D6",
      icons: [
        {
          src: path.resolve('src/publish_assets/logo-ios.png'),
          sizes: [96, 128, 192, 256, 384, 512] // multiple sizes
        }
      ],
      ios: {
        'apple-mobile-web-app-title': 'Distance',
        'apple-mobile-web-app-status-bar-style': 'black-translucent'
      }
    })
  ]
}