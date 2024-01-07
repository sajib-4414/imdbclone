const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const Dotenv = require('dotenv-webpack');
module.exports = {
  mode: 'development',
  entry: './src/index.tsx',
  devtool: 'inline-source-map',
  output: {
    path: path.join(__dirname, '/dist'),
    filename: 'bundle.js',
    publicPath: 'http://localhost:3003/',
  },
  devServer: {
    static: './dist',
    historyApiFallback: true,
    allowedHosts: 'all', //to allow host when running in docker, nginx
    hot: true,
    client: {
      webSocketURL: 'auto://0.0.0.0:0/ws',
    }
  },
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
      {
        test:/.scss$/, 
        use: ["style-loader", "css-loader", "sass-loader" ]
      },
      {
        test: /\.css$/, 
        use: ["style-loader", "css-loader"]
      },
    ],
  },
  resolve: {
    alias: {
      styles: path.resolve(__dirname, 'styles'),
    },
    extensions: ['.tsx', '.ts', '.js'],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
    }),
    new Dotenv()
  ],
};