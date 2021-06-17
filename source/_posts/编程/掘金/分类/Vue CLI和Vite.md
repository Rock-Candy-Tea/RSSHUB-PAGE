
---
title: 'Vue CLI和Vite'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4319'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 19:48:20 GMT
thumbnail: 'https://picsum.photos/400/300?random=4319'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一.  Vue CLI安装和使用</h2>
<h3 data-id="heading-1">1.1 安装</h3>
<ul>
<li>全局安装，任何时候都可以通过<code>vue</code>的命令来创建项目</li>
</ul>
<pre><code class="copyable">npm install @vue/cli -g
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">1.2 升级</h3>
<ul>
<li>如果是旧版本，可通过该命令升级</li>
</ul>
<pre><code class="copyable">npm update @vue/cli -g
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">1.3 创建</h3>
<pre><code class="copyable">vue create 项目的名称
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">1.4 配置</h3>
<ul>
<li>空格可以控制是否选择</li>
</ul>
<pre><code class="copyable">Choose Vue version是否选择 vue 版本，目前默认版本 vue2
Babel是否选择 babel(例如: es6 转换 es5)
TypeScript是否使用 TypeScript
Progressive Web App (PWA) Support项目是否支持 PWA
Router是否默认添加 router 路由
Vuex是否默认添加 Vuex 状态管理
CSS Pre-processors是否选择 CSS 预处理器
Linter / Formatter是否选择 ESLint 对代码进行格式化限制
Unit Testing是否添加单元测试
E2E Testing是否添加 E2E 测试
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>选择<code>vue</code>版本</li>
</ul>
<pre><code class="copyable">2.x
3.x
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>配置信息文件储放位置</li>
</ul>
<pre><code class="copyable">> In dedicated config files存放独立的文件中
  In package.json存放package.json
  (全都存放到一个文件中，会让文件变得臃肿，推荐第一项)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">二. Vite</h2>
<blockquote>
<p>官方定位：下一代前端开发与构建工具</p>
</blockquote>
<blockquote>
<p>随着项目越来越大，需要处理的<code>JavaScript</code>呈指数级增长，模块越来越多；构建工具需要很长时间才能开启服务器，HMR也需要几秒钟才能在浏览器反映出来；<code>Vite</code>是一种新型前端构建工具，能够显著提升前端开发体验</p>
</blockquote>
<p>主要由两部分组成</p>
<ul>
<li>一个开发服务器，它基于原生ES模块提供了丰富的内建功能，HMR的速度非常快速；</li>
<li>一套构建指令，它使用rollup打开我们的代码，并且它是预配置的，可以输出生成环境的优化过的静态资源；</li>
</ul>
<h3 data-id="heading-6">2.1 安装</h3>
<p>==Vite要求Node版本是大于12版本的==</p>
<pre><code class="copyable">npm install vite –g # 全局安装
npm install vite –D # 局部安装
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">2.2 使用</h3>
<ul>
<li>启动</li>
</ul>
<pre><code class="copyable">npx vite
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>css</li>
</ul>
<pre><code class="copyable">默认支持 css 不需要额外配置
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>less</li>
</ul>
<pre><code class="copyable">npm install less -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>vue</li>
</ul>
<pre><code class="copyable">Vue 3 单文件组件支持：@vitejs/plugin-vue
Vue 3 JSX 支持：@vitejs/plugin-vue-jsx
Vue 2 支持：underfin/vite-plugin-vue2
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>安装支持vue的插件</li>
</ul>
<pre><code class="copyable">npm install @vitejs/plugin-vue -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>vite.config.js 配置插件</li>
</ul>
<pre><code class="copyable">import vue from '@vitejs/plugin-vue'

module.exports = &#123;
  plugins: [
    vue()
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">2.3 打包</h3>
<pre><code class="copyable">npx vite build
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.4 开启本地服务来预览打包后的效果</h3>
<pre><code class="copyable">npx vite preview
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.5 脚手架</h3>
<ul>
<li>安装</li>
</ul>
<pre><code class="copyable">npm install @vitejs/create-app -g
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用</li>
</ul>
<pre><code class="copyable">create-app
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            