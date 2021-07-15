
---
title: 'Vue的webpack2.0升级到webpack4.0解决方案（utils篇）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4512'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 02:55:07 GMT
thumbnail: 'https://picsum.photos/400/300?random=4512'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>由于项目最开始使用了vuecli脚手架搭建项目，webpack版本为2.0。后续由于项目引入插件需要支持webpack4.0。所以有了这次升级篇，我先来看看Vue的webpack</p>
<h2 data-id="heading-0">webpack目录</h2>
<ul>
<li>utils.js</li>
<li>webpack.dev.js</li>
<li>webpack.base.js</li>
<li>webpack.prod.js</li>
</ul>
<h2 data-id="heading-1">utils.js</h2>
<p>附上升级后的utils.js</p>
<p>将extract-text-webpack-plugin 换成mini-css-extract-plugin</p>
<blockquote>
<p>generateLoaders</p>
</blockquote>
<p>这里是配置loader的地方，在webpack的rules有加入。如果嫌麻烦可以去掉Vue的这一块。当然这里我是在原来的基础上改造，将<code>mini-css-extract-plugin</code>插件加入数组前面，直接返回loaders。把之前Vue的判断去了。<code>[MiniCssExtractPlugin.loader, cssLoader, postcssLoader]</code></p>
<pre><code class="copyable">   function generateLoaders(loader, loaderOptions) &#123;
        const loaders = options.usePostCSS ? [MiniCssExtractPlugin.loader, cssLoader, postcssLoader] : [cssLoader]

        if (loader) &#123;
            loaders.push(&#123;
                loader: loader + '-loader',
                options: Object.assign(&#123;&#125;, loaderOptions, &#123;
                    sourceMap: options.sourceMap
                &#125;)
            &#125;)
        &#125;
        console.log(loaders, 'lodaers')

        return loaders

        // Extract CSS when that option is specified
        // (which is the case during production build)

        // if (options.extract) &#123;
        //     return ExtractTextPlugin.extract(&#123;
        //         use: loaders,
        //         fallback: 'vue-style-loader'
        //     &#125;)
        // &#125; else &#123;
        //     return ['vue-style-loader'].concat(loaders)
        // &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>完整代码</p>
</blockquote>
<pre><code class="copyable">'use strict'
const path = require('path')
const config = require('../config')
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const packageConfig = require('../package.json')

exports.assetsPath = function(_path) &#123;
    const assetsSubDirectory = process.env.NODE_ENV === 'production' ?
        config.build.assetsSubDirectory :
        config.dev.assetsSubDirectory

    return path.posix.join(assetsSubDirectory, _path)
&#125;

exports.cssLoaders = function(options) &#123;
    options = options || &#123;&#125;

    const cssLoader = &#123;
        loader: 'css-loader',
        options: &#123;
            sourceMap: options.sourceMap
        &#125;
    &#125;

    const postcssLoader = &#123;
        loader: 'postcss-loader',
        options: &#123;
            sourceMap: options.sourceMap
        &#125;
    &#125;



    // generate loader string to be used with extract text plugin
    function generateLoaders(loader, loaderOptions) &#123;
        const loaders = options.usePostCSS ? [MiniCssExtractPlugin.loader, cssLoader, postcssLoader] : [cssLoader]

        if (loader) &#123;
            loaders.push(&#123;
                loader: loader + '-loader',
                options: Object.assign(&#123;&#125;, loaderOptions, &#123;
                    sourceMap: options.sourceMap
                &#125;)
            &#125;)
        &#125;
        console.log(loaders, 'lodaers')

        return loaders

        // Extract CSS when that option is specified
        // (which is the case during production build)

        // if (options.extract) &#123;
        //     return ExtractTextPlugin.extract(&#123;
        //         use: loaders,
        //         fallback: 'vue-style-loader'
        //     &#125;)
        // &#125; else &#123;
        //     return ['vue-style-loader'].concat(loaders)
        // &#125;
    &#125;

    // https://vue-loader.vuejs.org/en/configurations/extract-css.html
    return &#123;
        css: generateLoaders(),
        postcss: generateLoaders(),
        less: generateLoaders('less'),
        sass: generateLoaders('sass', &#123; indentedSyntax: true &#125;),
        scss: generateLoaders('sass'),
        stylus: generateLoaders('stylus'),
        styl: generateLoaders('stylus')
    &#125;
&#125;

// Generate loaders for standalone style files (outside of .vue)
exports.styleLoaders = function(options) &#123;
    const output = []
    const loaders = exports.cssLoaders(options)

    for (const extension in loaders) &#123;
        const loader = loaders[extension]
        output.push(&#123;
            test: new RegExp('\\.' + extension + '$'),
            use: loader
        &#125;)
    &#125;

    return output
&#125;

exports.createNotifierCallback = () => &#123;
    const notifier = require('node-notifier')

    return (severity, errors) => &#123;
        if (severity !== 'error') return

        const error = errors[0]
        const filename = error.file && error.file.split('!').pop()

        notifier.notify(&#123;
            title: packageConfig.name,
            message: severity + ': ' + error.name,
            subtitle: filename || '',
            icon: path.join(__dirname, 'logo.png')
        &#125;)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，关于Utils篇的修改就结束了，有什么问题欢迎反馈质询哦。后续有新的优化也会新增帖子。</p></div>  
</div>
            