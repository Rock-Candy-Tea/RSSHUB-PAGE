
---
title: 'webpack 配置进阶知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5046'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 04:05:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=5046'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">提取css成单独文件</h4>
<ul>
<li>原因</li>
</ul>
<p>不提取css文件，打包时会放在js文件中，不仅会增加js文件体积，使js文件下载时间延长，而且进行解析js文件往往都是在dom树生成之后，就增加了延迟，影响渲染速度，用户体验差</p>
<ul>
<li>好处</li>
</ul>
<p>将css文件单独提取出来，就可以先在页面的最前面引入这个单独的css文件，浏览器先解析css文件就会生成cssom从而与domtree生成渲染树，从而以最快速度渲染出页面。</p>
<pre><code class="copyable">安装：npm i mini-css-exreact-plugin -D

配置：

module.exports =&#123;
  ...
  module:&#123;
     rules:[
    &#123;
    test:/\.css$/,
    use:[
       // style-loader //创建style标签到head上但是要分离css时候不适用
       MiniCssExtractPlugin.loader, //使用插件特有的loader提取js中的css成为单独的文件
       'css-loader'
    ]
    &#125;
  ]
  &#125;
  plugins:&#123;
     new MiniCssExtractPlugin(&#123;
       // 对输出的css重命名
       template:'./src/built.css'
     &#125;)
  &#125;
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">css兼容性处理</h4>
<ul>
<li>原因：</li>
</ul>
<p>系统需要兼容多个浏览器，就会在css文件添加-webkit-等厂商前缀。由于webpack无法识别这些前缀，所以引入postcss-loader,这个可以自动帮我们添加厂商前缀的信息。</p>
<pre><code class="copyable">安装：npm install postcss-loader postcss-preset-env -D
module.exports = &#123;
   ...
   module:&#123;
      rules:[
         &#123;
           test:/\.css$/,
           use:[
              MiniCssExtractPlugin.loader,
              'css-loader',
              
              &#123;
              loader:'postcss-loader',
              options:&#123;
                ident:'postcss',
                plugins:() =>[
                // postcss的插件，帮助postcss找到package.json中的browserslist里面的配置，通过配置加载指定的css兼容
                  require('postcss-preset-env')()
                ]
              &#125;
              &#125;
           ]
         &#125;
      ]
   &#125;
&#125;


package.json中的配置
&#123;
  "browserslist":&#123;
  // 开发环境 ，需要设置nodejs环境变量
      "development":[
          "last 1 chrome version",//最近的chrome浏览器版本
      ],
      // 生产环境(默认的)
      "production":[
          ">0.2%",
          "not dead",
          "not op_mimi all"
      ]
      
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">js语法检查eslint</h4>
<pre><code class="copyable">安装：npm i eslint-config-airbnb-base eslint-plugin-import eslint -D
配置：
module.exports = &#123;
   ...
   module:&#123;
      rules:[
      /*
      js语法检查eslint
      */
         &#123;
             test:/\.js$/,
             exclude:/node_modules/,  // 不检查第三方库
             loader:'eslint-loader',
             options:&#123;
               // 自动修复eslint的错误
               fix:true
             &#125;
         &#125;,
         /*
         js兼容性处理： babel-loader  @babel/core @babel-preset-env
         1：@babel-preset-env,只能处理部分兼容性问题
         2:全部的兼容性处理，需要下载@babel/polyfill
         3:按需加载，做兼容性处理---》core-js
         */
         &#123;
           test:/\.js$/,
           exclude:/node_modules/,
           loader:'babel-loader',
           options:&#123;
              // 预设：指示babel做怎么样的兼容处理
              presets:['@babel/preset-env']
           &#125;
         &#125;
       ]
    &#125;
&#125;


package.json中eslintConfig中配置
"eslintConfig":&#123;
  "extends":"airbnb-base"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            