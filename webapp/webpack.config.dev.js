const webpack = require('webpack');
const path = require('path');
const WebpackPwaManifest = require('webpack-pwa-manifest');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const {GenerateSW} = require('workbox-webpack-plugin');

process.env.NODE_ENV = "development";

module.exports={
  mode:process.env.NODE_ENV,
  devtool: 'inline-source-map',
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
        use:['style-loader', 'css-loader']
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
    new GenerateSW({
      maximumFileSizeToCacheInBytes:1e+7,
      skipWaiting:true,
      runtimeCaching: [{
        urlPattern: new RegExp('/\.(js|css)$/i'),
        handler: 'StaleWhileRevalidate'
      }],
      exclude: [/\.(md|png|jpe?g|gif|xml|toml|txt|gz)$/i,/CNAME/i,/md\.js/i],
      swDest:'sw.js'
    }),
    new WebpackPwaManifest({
      name: 'Distance',
      short_name: 'Distance',
      description: 'Distance',
      background_color: '#ffffff',
      includeDirectory:true,
      orientation:'any',
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