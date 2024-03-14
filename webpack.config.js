const path = require('path');

module.exports = {
    entry: './assets/index.js', //input file
    output: {
        filename: 'index-bundle.js', //ouput file
        path: path.resolve(__dirname, './static')
    },

    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /nodue_modules/,
                loader: "babel-loader",
                options: { presets: ["@babel/preset-env", "@babel/preset-react"]}
            },
        ]
    },
};
//^^^
//may be asking WHAT THE **** IS THIS??????
//well im not to sure either, something about compiling and babel
//compiling .js and .jsx stuff so we can process them
// ~ dylan