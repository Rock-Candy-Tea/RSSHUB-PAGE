
---
title: '通过Webpack 打包vue脚手架的初步教程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f483ee1afeea4eac96f911db2a8cbaaf~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 23:34:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f483ee1afeea4eac96f911db2a8cbaaf~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">配置开发时的前端工程（vue-loader+webpack）</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f483ee1afeea4eac96f911db2a8cbaaf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>我们通过快捷键 ‘ctrl + ·’，也就是esc下面的小点，打开终端,先来用 npm init 来初始化项目，大家实验的时候直接敲回车就行了.</p>
</blockquote>
<pre><code class="copyable">PS C:\Users\A\Desktop\reNew webpackVue> npm init 
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (renew-webpackvue)
version: (1.0.0)
description:
entry point: (index.js)
test command:
git repository:
keywords:
author:
license: (ISC)
About to write to C:\Users\A\Desktop\reNew webpackVue\package.json:

&#123;
  "name": "renew-webpackvue",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1"
  &#125;,
  "author": "",
  "license": "ISC"
&#125;


Is this OK? (yes)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这个时候细心的话会发现目录下面多一个package.json的文件，这个文件就是项目的配置文件。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de3b840ef6e547219fa8a968b8233d42~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>因为我们用到了vue以及webpack，所以需要安装两个依赖包，还有段落标题中的vue-loader，这个是为了用webpack加载.vue文件，并编译成浏览器能认识的js文件，我们先来执行这样的指令，注：我们这里是demo，所以这里就不区分是否是dev-dependency了。(详情可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.cnblogs.com%2Fayseeing%2Fp%2F4128612.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.cnblogs.com/ayseeing/p/4128612.html" ref="nofollow noopener noreferrer">www.cnblogs.com/ayseeing/p/…</a>)</p>
</blockquote>
<pre><code class="copyable">npm i webpack vue vue-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">PS C:\Users\A\Desktop\reNew webpackVue> npm i webpack vue vue-loader

added 118 packages, and audited 119 packages in 16s

13 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>安装完成之后可能会出现一些waring，这个waring其实就是告诉我们在安装vue-loader的同时必须要安装css-loader，这里我们想它继续安装完成就可以了。</p>
<p>npm WARN <a href="https://link.juejin.cn/?target=mailto%3Avue_web%401.0.0" target="_blank" title="mailto:vue_web@1.0.0" ref="nofollow noopener noreferrer">vue_web@1.0.0</a> No description <br>
npm WARN <a href="https://link.juejin.cn/?target=mailto%3Avue_web%401.0.0" target="_blank" title="mailto:vue_web@1.0.0" ref="nofollow noopener noreferrer">vue_web@1.0.0</a> No repository field.</p>
<p>这两个是我们项目初始化的时候由于都是回车回车，缺少一些描述，无需关心。</p>
<p>npm WARN optional SKIPPING OPTIONAL <br>
npm WARN notsup SKIPPING OPTIONAL</p>
<p>这两个是告诉我们项目初始化时候哪些是可选择安装的，哪些是可以不安装的，继续执行</p>
</blockquote>
<pre><code class="copyable">npm i css-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">PS C:\Users\A\Desktop\reNew webpackVue> npm i css-loader

up to date, audited 119 packages in 2s

13 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>好，到这里，我们项目的大概的初始化工作就完成了。接下来我们就基于这样的目录，填充一下更丰富的细节。</p>
<p>我们在工程目录下新建一个src文件夹用来存放源文件，并新建一个app.vue的文件：</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a5e6d70e287477e84fa2501cf82c49a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>app.vue代码如下:</p>
</blockquote>
<pre><code class="copyable">
<template>
  <div id="text">
    &#123;&#123;text&#125;&#125;
  </div>
</template>
 
<script>
  export default &#123;
    data() &#123;
      return &#123;
        text: 'hello world'
      &#125;
    &#125;
  &#125;
</script>
 
<style>
  #text &#123;
    color: blueviolet;
    font-family: fangsong;
  &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>大家都知道，浏览器其实只能够识别一些简单的文件，像js，css，html，img，font，但是如何让浏览器识别vue文件呢？</p>
</blockquote>
<h2 data-id="heading-1">webpack配置</h2>
<h3 data-id="heading-2"><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a><a href="https://link.juejin.cn/?target=" target="_blank" title ref="nofollow noopener noreferrer"></a>1. 输入输出</h3>
<p>到这其实我们应该有一些认知了，webpack其实就是一个帮我们打包的工具。接下来我们在工程目录下新建一个webpack.config.js文件。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f015e8557c944b3bad5305c3020fe669~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>大家都知道，webpack是用来打包的工具<br>
所以，接下来我们在新建的webpack.config.js里面做文章,配置webpack的入口和出口，让浏览器去访问，让webpack去打包并输出。</p>
<p>在src目录下新建一个index.js的文件作文工程的入口文件。</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86486e9a062b426facd08b7269366140~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>然后我们在index.js里面写一些内容,代码中我都做了注释，大家应该一眼就能看懂\</p>
</blockquote>
<p><code>index.js:</code></p>
<pre><code class="copyable">//这是工程的入口文件
import Vue from 'vue';
import App from './app.vue';
 
const root = document.createElement('div')
document.body.appendChild(root)
 
//mount就是讲我们的App挂载到root这样一个根节点中去
new Vue(&#123;
  render: (h) => h(App)
&#125;).$mount(root)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>我们这时候发现，浏览器要想运行这段代码，那是不可能的，因为浏览器不认识vue，更不认识new Vue,所以webpack要登场了。我们在webpack.config.js里配上entry入口和out出口，表示webpack文件会将将entry路径下的文件，打包到out的路径，</p>
</blockquote>
<p>具体如下：<br>
<code>webpack.config.js:</code></p>
<pre><code class="copyable">const path = require("path");//nodejs里面的基本包，用来处理路径
 
//__dirname表示文件相对于工程的路径
module.exports =&#123;
  entry: path.join(__dirname, 'src/index.js'),
  output: &#123;
    filename: 'bundle.js',
    path: path.join(__dirname, 'dist')
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里代码就不多说了，都有注释，这里卖个关子，也是经常会发生的场景，就是这里的join和resolve这两个函数的用法和区别，最好去官网看一下说明，直通车<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2F%25EF%25BC%258C%25E8%258B%25B1%25E6%2596%2587%25E4%25B8%258D%25E5%25A5%25BD%25E7%259A%2584%25E5%2590%258C%25E5%25AD%25A6%25E5%258F%25AF%25E4%25BB%25A5%25E5%258E%25BB%25E4%25B8%25AD%25E6%2596%2587%25E5%25AE%2598%25E7%25BD%2591%25E5%25AD%25A6%25E4%25B9%25A0%25E9%2583%25BD%25E6%2598%25AF%25E5%258F%25AF%25E4%25BB%25A5%25E7%259A%2584%25EF%25BC%258C%25E6%25B2%25A1%25E6%259C%2589%25E5%2585%25B3%25E7%25B3%25BB%25E7%259A%2584%25EF%25BC%258C%25E7%259C%258B%25E4%25B8%258D%25E6%2587%2582%25E7%259A%2584%25E6%2597%25B6%25E5%2580%2599%25E6%2588%2591%25E4%25B9%259F%25E4%25BC%259A%25E5%258E%25BB%25E7%259C%258B%25E4%25B8%25AD%25E6%2596%2587%25E6%2596%2587%25E6%25A1%25A3%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/%EF%BC%8C%E8%8B%B1%E6%96%87%E4%B8%8D%E5%A5%BD%E7%9A%84%E5%90%8C%E5%AD%A6%E5%8F%AF%E4%BB%A5%E5%8E%BB%E4%B8%AD%E6%96%87%E5%AE%98%E7%BD%91%E5%AD%A6%E4%B9%A0%E9%83%BD%E6%98%AF%E5%8F%AF%E4%BB%A5%E7%9A%84%EF%BC%8C%E6%B2%A1%E6%9C%89%E5%85%B3%E7%B3%BB%E7%9A%84%EF%BC%8C%E7%9C%8B%E4%B8%8D%E6%87%82%E7%9A%84%E6%97%B6%E5%80%99%E6%88%91%E4%B9%9F%E4%BC%9A%E5%8E%BB%E7%9C%8B%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3%E3%80%82" ref="nofollow noopener noreferrer">webpack.js.org/，英文不好的同学可以去…</a></p>
<p>好上面的代码就是做了这样一件事，将src下的index.js文件以js的形式打包到dist目录下的bundle.js中去。大家有疑问了，这两个目录我还没有新建呢！没有关系out属性中定义的路径如果没有的话，webpack会自动创建的，我们需要做的是就是新建src目录并添加index.js文件。那这个动作我们已经新建完成了，不记得的同学返回文章内容再看看。</p>
<p>这时候我们打开package.json文件添加一句:</p>
<pre><code class="copyable">"build": "webpack --config webpack.config.js"
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11191a5eb105458c946277828559445a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>很多有经验的同学应该都用过npm run build 这段指令，之后webpack帮我们干的一些事情，执行我们新建的webpack.config.js文件。注意:这里我们使用webpack来执行指令，同样可以在终端执行这段指令，但是我们要清楚在终端直接执行build后面的指令会出现一个问题,如我们在终端执行该指令，意味着使用的是全局的webpack，但是我们写在package.json文件下的话，意味着执行工程下面的局部wepackage，全局和局部可能会版本不一样，所以为了避免不必要的麻烦，我们在package.json文件下执行，也就是说使用的局部的webpack来打包。</p>
<p>好到这里，我们编译打包输入输出的相关配置已经完成，我们先执行一下：npm run build。可能有经验的小伙伴会发现还有一些配置没有完成，没关系，我们一步步来，带着错误把问题一个一个解决。</p>
<pre><code class="copyable">npm run build
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">PS C:\Users\A\Desktop\reNew webpackVue> npm run build

> renew-webpackvue@1.0.0 build      
> webpack --config webpack.config.js

CLI for webpack must be installed.
  webpack-cli (https://github.com/webpack/webpack-cli)

We will use "npm" to install the CLI via "npm install -D webpack-cli".
Do you want to install 'webpack-cli' (yes/no): yes
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我使用的是webpack4，所以这里必须要安装一下cli。这里有人就问了，不是不用cli的嘛，怎么要安装这个包。如果你有这样的想法，证明你有自己用过cli搭建过vue项目框架的一些经验。我们知道用cli脚手架搭建出来的项目结构应该是这样的：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbbad7aa5e35404bbeaac7c376451d5b~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>该图来源于网络，我们这里安装这个cli包是因为webpack4之后强制要求安装的，但是我们并没有通过该工具来初始化整个工程，所以建出来的目录也是不一样的，所以大家仔细想想就明白了。好了，接下来直接yes就可以,安装完成之后，再执行一下 npm run build，有些不需要再执行，但没有关系，反正都会报错：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3481bf64061470d83c8e85052630032~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个错误呢就是告诉我们，需要为app.vue这个文件声明一个loader，因为webpack只支持js类型的文件，像这种vue文件是不支持的，所以我们要使用一些工具，来帮助它认识超出它理解范畴的语法。接下来便到了我们的module环节。</p>
<h3 data-id="heading-3">2. Module</h3>
<p>由于webpack存在这样的一个限制，我们就需要来使用一些工具，我们在webpack.config.js里添加module配置项</p>
<p>webpack.config.js:</p>
<pre><code class="copyable">const path = require("path");//nodejs里面的基本包，用来处理路径
 
//__dirname表示文件相对于工程的路径
module.exports =&#123;
  entry: path.join(__dirname, 'src/index.js'),
  output: &#123;
    filename: 'bundle.js',
    path: path.join(__dirname, 'dist')
  &#125;,
  module: &#123;
    rules: [
       &#123;//通过vue-loader来识别以vue结尾的文件
         test: /.vue$/, 
         loader: 'vue-loader'
       &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好添加完成之后，再次执行 npm run build 指令。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd267145c6ca45df8302b4b1faa36d4a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>好，又报错了，这时候的错误是告诉我使用vue-loader的方式不正确。Vue-loader在15.*之后的版本都是 vue-loader的使用都是需要伴生 VueLoaderPlugin的，所以我们这里再来修改一下。这里会使用plugin属性，不了解的同学可以先跳过，也可以去官网查看一下这个属性的作用，这里我就先不介绍了。我们在package.config.js文件中添加VueLoaderPlugin，代码如下：</p>
<pre><code class="copyable">const path = require("path");//nodejs里面的基本包，用来处理路径
const VueLoaderPlugin = require('vue-loader/lib/plugin');
 
//__dirname表示文件相对于工程的路径
module.exports =&#123;
  entry: path.join(__dirname, 'src/index.js'),
  output: &#123;
    filename: 'bundle.js',
    path: path.join(__dirname, 'dist')
  &#125;,
  plugins: [
    // make sure to include the plugin for the magic
    new VueLoaderPlugin()
],
  mode:'none',
  module: &#123;
    rules: [
       &#123;//通过vue-loader来识别以vue结尾的文件
         test: /.vue$/, 
         loader: 'vue-loader'
       &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再次执行一次 <code>npm run build</code> 还会报错，哈哈，到这有人会抱怨啦，是不是没玩没了啦。不用担心，保证这个问题解决完之后就可以啦。先看错误信息</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7976399bed9b4f8d8c94f81b292a4335~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>不知道大家还记不记的我在<code>app.vue</code>文件中用“style标签嵌入”的方的式写css样式了</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/249e30b7524940bda3b22a3f32cc2d91~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是<code>webpack并没有处理css的能力</code>，所以我们还需要在moudle添加rules配置项，如下</p>
<pre><code class="copyable">const path = require("path");//nodejs里面的基本包，用来处理路径
const VueLoaderPlugin = require('vue-loader/lib/plugin');
 
//__dirname表示文件相对于工程的路径
module.exports =&#123;
  entry: path.join(__dirname, 'src/index.js'),
  output: &#123;
    filename: 'bundle.js',
    path: path.join(__dirname, 'dist')
  &#125;,
  plugins: [
    // make sure to include the plugin for the magic
    new VueLoaderPlugin()
],
  mode:'none',
  module: &#123;
    rules: [
       &#123;//通过vue-loader来识别以vue结尾的文件
         test: /.vue$/, 
         loader: 'vue-loader'
       &#125;,
       &#123;//通过vue-loader来识别以vue结尾的文件
        test: /.css$/, 
        //css的处理方式不同，有嵌入在页面style标签里的，有从外部文件引入的，我们这里用use来声明
        use: [
          'style-loader',//接受潜在页面内部的style标签的文件。
          'css-loader'
        ]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，别忘了执行一下，</p>
<pre><code class="copyable"> npm i style-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为之前没有安装过这个包，否则又要报错了。这部分属于配置静态资源的部分了，这里遇到了问题，就先介绍了。我们最后执行一下 <code>npm run build</code> 指令，不出意外的话，应该是这样的：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4f7feb58e7b46858448ad19a51c0656~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">webpack配置项目加载各种静态资源及css预处理器</h2>
<h3 data-id="heading-5">1. 静态资源</h3>
<p>上一张我们详细使用了webpack加载并打包vue文件，以及最后处理的css文件，就针对静态资源这块，我们可以稍微更详细地了解一下。</p>
<p>好，在上一张的末尾，我们接触了css样式加载，我们稍微复习一下，大家也可以回头在巩固一下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d426cfd9692244ed8ecfa87c675c8527~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里用了use属性而不是loader属性，是因为我们处理css文件的方式有多种，所以这里出多种方式的css加载需要用到use属性，所以这里用到了use，style-loader也就是处理html文件内部的style标签内的css样式，也就是我们俗称的内联，css-loader处理的是从文件外部引入的css文件，这里大家简单了解一下。</p>
<p>然后我们的图片怎么做呢？我相信大家举一反三的能力比我强多了，我们加载图片用到的loader叫‘url-loader’,它的作用是将我们的图片转换成一个base64的字串存放于我们打包生成的js里面，而不是重新生成一个文件。对于一些小的文件，几kb的文件可以帮助我们减少过多的http请求。那么url-loader其实封装了我们的file-loader，file-loader其实是将文件进行处理后换个名字存放于另一个地方。那么我们先看下配置：</p>
<pre><code class="copyable">const path = require("path");//nodejs里面的基本包，用来处理路径
const VueLoaderPlugin = require('vue-loader/lib/plugin');
 
//__dirname表示文件相对于工程的路径
module.exports =&#123;
  entry: path.join(__dirname, 'src/index.js'),
  output: &#123;
    filename: 'bundle.js',
    path: path.join(__dirname, 'dist')
  &#125;,
  plugins: [
    // make sure to include the plugin for the magic
    new VueLoaderPlugin()
],
  mode:'none',
  module: &#123;
    rules: [
       &#123;//通过vue-loader来识别以vue结尾的文件,正则表达式中的点需要转义
         test: /\.vue$/, 
         loader: 'vue-loader'
       &#125;,
       &#123;//通过vue-loader来识别以vue结尾的文件
        test: /\.css$/, 
        //css的处理方式不同，有嵌入在页面style标签里的，有从外部文件引入的，我们这里用use来声明
        use: [
          'style-loader',//接受潜在页面内部的style标签的文件。
          'css-loader'
        ]
      &#125;,
      &#123;//处理图片文件
        test: /\.(gif|jpg|jpeg|png|svg)$/ ,
        use: [
          &#123;
            loader: 'url-loader',
            options: &#123;
              limit: 1024,
              name: '[name]-aaa.[ext]'
            &#125;
          &#125;,
        ]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们这里同样使用的use属性，不同的是数组里面使用的对象，因为我们对图片还需要进行一些更细化的配置，像图片的大小(limit)，文件名称(name)有时都是需要进行配置的，所以这里使用了对象。下面呢，我们将使用到的loader安装一下。</p>
<pre><code class="copyable">npm i url-loader file-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们安装完成了之后，所有的包是可以通过import来使用的。</p>
<p>接下来我们介绍一下图片的loader，新建一个assets目录，然后放几张图片进去，并同时新建一个styles目录新建一个test样式</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b289271e0f343218e090b882dddce21~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图片大家可以自行下载，css就简单的给body设置了样式:</p>
<p>test.css:</p>
<pre><code class="copyable">body&#123;
  color: red;
  background-image: url('../images/logo.png');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且将我们项目的入口文件添加几行代码：</p>
<pre><code class="copyable">//这是工程的入口文件
import Vue from 'vue';
import App from './app.vue';
 
import './assets/styles/test.css';
import './assets/images/vue.png'
 
const root = document.createElement('div')
document.body.appendChild(root)
 
//mount就是讲我们的App挂载到root这样一个根节点中去
new Vue(&#123;
  render: (h) => h(App)
&#125;).$mount(root)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好，我们现在执行一下npm run build 指令，可以看到webpack将图片打包成base64字串存放于js中，并且重新生成了新的文件</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca5fdded6be3489482c30d57be4b7fb3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>配置信息的参数“limit=1024”表示将所有小于1kb的图片都转为base64形式，而我们的图片的大小：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e0e0822eb094814bc0cee7ea59ef519~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>都超过了1KB，webpack表示不是我的锅，我不背...</p>
<p>我们将limit稍微改大一点设置100k，按照理论小一点的图片应该会被处理成base64的图片。我们再次执行一下npm run build</p>
<h3 data-id="heading-6">2. css预处理</h3>
<p>我们经常听到过 sass less style-component这些比较火热的css预处理器，那这些我们webpack能不能处理呢？答案是肯定的。</p>
<p>这里我给大家推荐一款预处理器-stylus,大家多多少少听过或者使用过。我们新增一个配置项，注意：我们这里新增了stylus-loader，所以需要将这个安装包执安装,由于stylus-loader这个包依赖于stylus这个包，所以我们这里执行安装指令：</p>
<pre><code class="copyable">npm i stylus-loader stylus
<span class="copy-code-btn">复制代码</span></code></pre>
<p>webpack.config.js 代码更新如下：</p>
<pre><code class="copyable">const path = require("path");//nodejs里面的基本包，用来处理路径
const VueLoaderPlugin = require('vue-loader/lib/plugin');
 
//__dirname表示文件相对于工程的路径
module.exports =&#123;
  entry: path.join(__dirname, 'src/index.js'),
  output: &#123;
    filename: 'bundle.js',
    path: path.join(__dirname, 'dist')
  &#125;,
  plugins: [
    // make sure to include the plugin for the magic
    new VueLoaderPlugin()
],
  mode:'none',
  module: &#123;
    rules: [
       &#123;//通过vue-loader来识别以vue结尾的文件,正则表达式中的点需要转义
         test: /\.vue$/, 
         loader: 'vue-loader'
       &#125;,
       &#123;//通过vue-loader来识别以vue结尾的文件
        test: /\.css$/, 
        //css的处理方式不同，有嵌入在页面style标签里的，有从外部文件引入的，我们这里用use来声明
        use: [
          'style-loader',//接受潜在页面内部的style标签的文件。
          'css-loader'
        ]
      &#125;,
      &#123;
        test: /\.styl$/, 
        use: [
          'style-loader',
          'css-loader',
          'stylus-loader'
        ]
      &#125;,
      &#123;//处理图片文件
        test: /\.(gif|jpg|jpeg|png|svg)$/ ,
        use: [
          &#123;
            loader: 'url-loader',
            options: &#123;
              limit: 1024 * 20, //将所有小于1kb的图片都转为base64形式
              name: '[name]-aaa.[ext]'
            &#125;
          &#125;,
        ]
      &#125;
    ]
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们新建一个styls，我们想要在vscode中使用stylus需要安装一个插件：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98cd106b3cac448b9acd0eff4d215e92~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装完成之后，重新启动就可以了。我们新建的styl文件如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b1d17e27cd1454099e204fd2e2121a7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>代码：</p>
<p>test-stylus-.styl</p>
<pre><code class="copyable">body 
  font-size  20px
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种写法是不是看上去落落大方，透露一股简约风范。我们再将这个styl文件在入口文件中引用进来。</p>
<p>入口文件 index.js</p>
<pre><code class="copyable">//这是工程的入口文件
import Vue from 'vue';
import App from './app.vue';
 
import './assets/styles/test.css';
import './assets/styles/test-stylus.styl';
import './assets/images/vue.png';
 
const root = document.createElement('div')
document.body.appendChild(root)
 
//mount就是讲我们的App挂载到root这样一个根节点中去
new Vue(&#123;
  render: (h) => h(App)
&#125;).$mount(root)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着我们就可以编译一下，继续执行npm run build 指令编译</p>
<h2 data-id="heading-7">webpack配置webpack-dev-server</h2>
<p>这个包是咱们在开发环境用的包处理工具，我们这里先install这个包。</p>
<pre><code class="copyable">npm i webpack-dev-server
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这部分内容是在换了个网络环境下完成的，因为移动的网速度不快，这里使用了cnpm来安装。使用方式就是在package.json文件里添加：</p>
<pre><code class="copyable"> "scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack --config webpack.config.js",
    "dev": "webpack-dev-server --config webpack.config.js"
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里添加完dev指令后需要到webpack.config.js下修改一部分内容来专门适应我们的开发环境。</p>
<p>首先我们需要添加target属性，将其设置为‘web’，由于我们使用的是浏览器编译平台，所以这里设置为web，这也是webpack这个属性的默认设置，所以写不写无所谓。更多的target属性值我这里给他家提供腾讯云的解释：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcloud.tencent.com%2Fdeveloper%2Fsection%2F1477500%25EF%25BC%258C%25E5%25A4%25A7%25E5%25AE%25B6%25E5%258F%25AF%25E4%25BB%25A5%25E5%258E%25BB%25E5%258F%2582%25E8%2580%2583%25E4%25B8%2580%25E4%25B8%258B%25EF%25BC%258C%25E4%25B9%259F%25E5%258F%25AF%25E5%258E%25BB%25E5%25AE%2598%25E7%25BD%2591%25E4%25B8%258A%25E5%258E%25BB%25E6%259F%25A5%25E9%2598%2585%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://cloud.tencent.com/developer/section/1477500%EF%BC%8C%E5%A4%A7%E5%AE%B6%E5%8F%AF%E4%BB%A5%E5%8E%BB%E5%8F%82%E8%80%83%E4%B8%80%E4%B8%8B%EF%BC%8C%E4%B9%9F%E5%8F%AF%E5%8E%BB%E5%AE%98%E7%BD%91%E4%B8%8A%E5%8E%BB%E6%9F%A5%E9%98%85%E3%80%82" ref="nofollow noopener noreferrer">cloud.tencent.com/developer/s…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/666d069b9fd046829f539cdfdf8c0ffa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来我们需要区分全局的一个环境，很容易就想到需设置一个全局的环境变量来做区分控制，我们在build指令后面添加代码</p>
<p>我们如果不想区分不同系统，写一套代码来适应多个系统，我们这里就使用到了 cross-env，我们在指令前面添加cross-env</p>
<p>当然这个包也是需要安装的，执行</p>
<pre><code class="copyable">cnpm i cross-env
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们还需要给dev下的指令配置一个变量值,用来区分两套环境</p>
<pre><code class="copyable">  "scripts": &#123;
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "cross-env NODE_ENV=production webpack --config webpack.config.js",
    "dev": "cross-env NODE_ENV=development webpack-dev-server --config webpack.config.js"
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里完成之后我们就可以在webpack.config.js文件里面进行判断了。</p>
<p>我们现在文件下新建一个变量</p>
<pre><code class="copyable">const isDev = process.env.NODE_ENV === 'development';
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们启动时设置的脚本变量都是可以通过process.env这个对象来获取的。更多关于process.env的内容可以到<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.docschina.org%2Fguides%2Fenvironment-variables" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.docschina.org/guides/environment-variables" ref="nofollow noopener noreferrer">webpack.docschina.org/guides/envi…</a> 读阅</p>
<p>这里我们判断如果是dev环境的话，我们就给webpack.config.js添加一些配置。</p>
<pre><code class="copyable">if(isDev)&#123;
  config.devServer = &#123;
    port: 8080,
    host: '0.0.0.0',
    overlay: &#123;
      erros: true,
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先我们给devServer属性添加一个port，因为我们新建的是一个服务，所以肯定要一个端口，接下来我们配置host，这里使用‘0.0.0.0’也是有好处的。这样可以通过127.0.0.1（本地默认地址）来进行访问，同时还可以在别人的机器上来访问，因为如果设置成‘localhost’的话通过ip是不能访问的。这里大家了解一下，更多相关derserver内容可以去这里参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.webpackjs.com%2Fconfiguration%2Fdev-server%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.webpackjs.com/configuration/dev-server/" ref="nofollow noopener noreferrer">www.webpackjs.com/configurati…</a>
overlay属性是在我们编译的过程中能够让任何的错误都显示到网页上面。最后我们加完了这些基础的配置之后回过头来发现，我们好像配置的只是js、css、img文件，没有html页面去容纳它们。这个时候我们用到一个webpack的一个插件html-webpack-plugin,我们照样来安装一下它：</p>
<pre><code class="copyable">cnpm i html-webpack-plugin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>并且在webpack.config.js文件的头部将它require进来，同时在plugin中新建。这里推荐一篇博客关于html-webpack-plugin的，大家可以参阅一下<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.cnblogs.com%2Fwonyun%2Fp%2F6030090.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.cnblogs.com/wonyun/p/6030090.html" ref="nofollow noopener noreferrer">www.cnblogs.com/wonyun/p/60…</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/777755487a0d4e529a60d2269366e74c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/480faf8f47be4651a58e470af6b84338~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>到这里我们基本的配置就完成了，最后需要了解一下webpack.DefinePlugin，我们在代码中的plugin里添加：</p>
<pre><code class="copyable"> plugins: [
    // make sure to include the plugin for the magic
    new webpack.DefinePlugin(&#123;
      'process.env': &#123;
        NODE_ENV: isDev ? '"development"' : '"production"'
      &#125;
    &#125;),
    new VueLoaderPlugin(),
    new HTMLPlugin()
],
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们用到了webpack，所以需要将 webpack 这个变量引用进来。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c61b6dab2a5b4da1993d1ff8b34a4839~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>说到这里，理论上我们已经完成的本地开发环境的编译，通过npm run dev就可以进行编译，我们来试验一下。</p>
<p>执行：<code>npm run dev</code></p>
<p>这里在浏览器里面输入localhost:8000会出现：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35d3eb23dd9140e9a2eda8275b6119aa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>说明我们<code>npm run dev</code>已经启动成功了。</p>
<p>这里我们再介绍一些devserver其他的一些配置。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f071ef9c7e64b1c9cf2a41feb4660a6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>文章出处引自于此，更详细的内容，希望大家参考:
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fu013368397%2Farticle%2Fdetails%2F86467581" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/u013368397/article/details/86467581" ref="nofollow noopener noreferrer">blog.csdn.net/u013368397/…</a></p></div>  
</div>
            