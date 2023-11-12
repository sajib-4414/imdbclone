const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
mode: 'development',
entry: './src/index.tsx',
devtool: 'inline-source-map',
output: {
path: path.join(__dirname, '/dist'),
filename: 'bundle.js',
publicPath: '/'
},
devtool: 'inline-source-map',
devServer: {
static: './dist',
historyApiFallback: true,
},
module: {
rules: [
{
test: /\.jsx?$/,
exclude: /node_modules/,
loader: 'babel-loader'
},
{
test: /\.tsx?$/,
use: 'ts-loader',
exclude: /node_modules/,
},
{
    test: /\.s?[ac]ss$/,
    use: ['style-loader', 'css-loader', 'sass-loader'],
    exclude: [/node_modules/],
},
{
    test: /\.css$/,
    use: ['style-loader', 'css-loader'],
  }
]
},
resolve: {
extensions: ['.tsx', '.ts', '.js'],
},
plugins:[
new HtmlWebpackPlugin({
template: './src/index.html'
})
]
}