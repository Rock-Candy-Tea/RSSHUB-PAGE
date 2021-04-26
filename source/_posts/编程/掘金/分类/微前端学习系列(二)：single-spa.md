
---
title: '微前端学习系列(二)：single-spa'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f21e3f326ac49eaa3b168a4d94c9ae0~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 25 Apr 2021 22:00:03 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f21e3f326ac49eaa3b168a4d94c9ae0~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f21e3f326ac49eaa3b168a4d94c9ae0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">目录</h3>
<ul>
<li><a href="https://juejin.cn/post/6955342063235760164#1">前言</a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#2">初次使用 single-spa</a>
<ul>
<li><a href="https://juejin.cn/post/6955342063235760164#2-1">基座应用改造</a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#2-2">子应用改造</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6955342063235760164#3">single-spa 进阶使用：parcels</a>
<ul>
<li><a href="https://juejin.cn/post/6955342063235760164#3-1">组件改造</a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#3-2">应用改造</a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6955342063235760164#4">常用 API 用法 </a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#5">使用 single-spa 时,需要关注的点</a>
<ul>
<li><a href="https://juejin.cn/post/6955342063235760164#5-1">application 模式下子应用如何切换</a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#5-2">single spa 是如何工作的</a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#5-3">子应用/组件的生命周期方法如何被获取</a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#5-6">子应用/组件之间如何通信</a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#5-7">子应用/组件生命周期方法为什么要返回一个 promise 对象 </a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#5-8">single-spa 生命周期 hooks </a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#5-9">配合 single-spa 使用的 npm 包 </a></li>
</ul>
</li>
<li><a href="https://juejin.cn/post/6955342063235760164#6">single-spa 的不足</a></li>
<li><a href="https://juejin.cn/post/6955342063235760164#7">结束语</a></li>
</ul>
<h3 id="user-content-1" data-id="heading-1">前言</h3>
<p>通过对上一篇 <a href="https://juejin.cn/post/6955341801381167112/" target="_blank">微前端学习系列(一): 微前端介绍</a> 学习，相信大家对<strong>微前端及当前流行技术方案</strong>已经有了一个初步的认识了吧。本文将在上一篇的基础上，就 <strong>single-spa 方案</strong>从<strong>用法</strong>、<strong>常用API</strong>、<strong>实现原理</strong>等方面进行详细梳理，希望能给到大家一定的帮助。</p>
<h3 id="user-content-2" data-id="heading-2">初次使用 single-spa</h3>
<p>在开始之前，我们先做一个简单回顾。</p>
<p><strong>single-spa</strong> 提供了一种<strong>基于路由的基座化</strong>的<strong>微前端方案</strong>，它将应用分为两类：<strong>基座应用</strong>和<strong>子应用</strong>。其中，<strong>子应用</strong>对应前面我们讲到的需要聚合的应用，<strong>基座应用</strong>是另外一个单独的应用，用于聚合子应用。在<strong>基座应用</strong>中，我们会维护一个<strong>路由注册表</strong> - <strong>每个路由对应一个子应用</strong>。<strong>基座应用</strong>启动以后，当我们切换路由时，如果是一个新的子应用，会动态获取子应用的 js 脚本，然后执行脚本并渲染出相应的页面；如果是一个已经访问过的子应用，那么就会从<strong>基座应用的缓存</strong>中获取已经缓存的子应用，激活子应用并渲染出对应的页面。</p>
<p>接下来，我们就来通过一个简单的 demo - <a href="https://github.com/zjhILYxxq/micro-frontend/single-spa/application" target="_blank" rel="nofollow noopener noreferrer">micro-frontend/single-spa/application</a> 来具体看看 <strong>single-spa</strong> 该如何使用。</p>
<p>demo 的项目结构如下：</p>
<pre><code class="copyable">|-- single-spa
    |--application
        |--main
           |--package.json
           |--public
           |--src
           |--...
        |--app1
           |--package.json
           |--public
           |--src
           |--...
        |--app2
           |--package.json
           |--public
           |--src
           |--...
        |--app3
           |--package.json
           |--public
           |--src
           |--...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，<strong>app1</strong>、<strong>app2</strong>、<strong>app3</strong> 是三个<strong>子应用</strong>，其中 <strong>app1</strong> 使用 <strong>vue2</strong> 技术栈，<strong>app2</strong> 使用 <strong>vue3</strong> 技术栈，<strong>app3</strong> 使用 <strong>react</strong> 技术栈；<strong>main</strong> 是<strong>基座应用</strong>，使用的技术栈为 <strong>vue2</strong>。</p>
<p>所有应用启动后，效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7bbb9b88eff429d8b0a5e2d8c9a1450~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果想要 single-spa 能正常工作，我们需要做分别对<strong>基座应用</strong>和<strong>子应用</strong>进行改造。</p>
<ul>
<li>
<h4 id="user-content-2-1" data-id="heading-3">基座应用改造</h4>
<p>在 <strong>single-spa</strong> 中，<strong>基座应用</strong>主要用于<strong>管理子应用</strong>，包括<strong>根据路由切换子应用</strong>以及<strong>子应用间的通信</strong>等。</p>
<p><strong>基座应用</strong>的改造很简单，我们只需要创建一个<strong>关于子应用的路由注册表</strong>，然后根据<strong>路由注册表</strong>使用 <strong>single-spa</strong> 提供的 <strong>registerApplication</strong> 方法<strong>注册子应用</strong>，最后在<strong>基座应用</strong>挂载完成以后，执行 <strong>single-spa</strong> 提供的 <strong>start</strong> 方法即可。</p>
<p>具体代码如下：</p>
<pre><code class="copyable">import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
const  &#123; registerApplication, start &#125; =  require('single-spa');

Vue.use(VueRouter)

Vue.config.productionTip = false

// 接入 single-spa 的标志
window.__SINGLE_SPA__ = true

const router = new VueRouter(&#123;
  mode: 'history',
  routes: []
&#125;);

// 远程加载子应用
function createScript(url) &#123;
  return new Promise((resolve, reject) => &#123;
    const script = document.createElement('script')
    script.src = url
    script.onload = resolve
    script.onerror = reject
    const firstScript = document.getElementsByTagName('script')[0]
    firstScript.parentNode.insertBefore(script, firstScript)
  &#125;)
&#125;
// 加载子应用
function loadApp(url, globalVar, entrypoints) &#123;
  return async () => &#123;
    for(let i = 0; i < entrypoints.length; i++) &#123;
      await createScript(url + entrypoints[i])
    &#125;
    return window[globalVar]
  &#125;
&#125;
// 子应用路由注册表
const apps = [
  &#123;
    // 子应用名称
    name: 'app1',
    // 子应用加载函数
    app: loadApp('http://localhost:8081', 'app1', [ "/js/chunk-vendors.js", "/js/app.js" ]),
    // 当路由满足条件时（返回true），激活（挂载）子应用
    activeWhen: location => location.pathname.startsWith('/app1'),
    // 传递给子应用的对象
    customProps: &#123;&#125;
  &#125;,
  &#123;
    name: 'app2',
    app: loadApp('http://localhost:8082', 'app2', [ "/js/chunk-vendors.js", "/js/app.js" ]),
    activeWhen: location => location.pathname.startsWith('/app2'),
    customProps: &#123;&#125;
  &#125;,
  &#123;
    // 子应用名称
    name: 'app3',
    // 子应用加载函数
    app: loadApp('http://localhost:3000', 'app3', ["/main.js"]),
    // 当路由满足条件时（返回true），激活（挂载）子应用
    activeWhen: location => location.pathname.startsWith('/app3'),
    // 传递给子应用的对象
    customProps: &#123;&#125;
  &#125;
]

// 注册子应用
for (let i = apps.length - 1; i >= 0; i--) &#123;
  registerApplication(apps[i])
&#125;

new Vue(&#123;
  router,
  render: h => h(App),
  mounted() &#123;
    // 启动
    start()
  &#125;,
&#125;).$mount('#app')
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上述代码中，最关键的就是创建<strong>子应用的路由注册表</strong>。在<strong>注册表</strong>中，每个子应用对应的配置项需要指定 <strong>name</strong>、<strong>app</strong>、<strong>activeWhen</strong>、<strong>customProps</strong>。</p>
<ul>
<li>
<p><strong>name</strong></p>
<p><strong>子应用的唯一标识</strong>，是一个字符串，不可重复。</p>
</li>
<li>
<p><strong>activeWhen</strong></p>
<p><strong>子应用激活的条件</strong>，是一个函数。当页面 url 发生变化时，会遍历执行注册的子应用的 <strong>activeWhen</strong> 方法。如果 <strong>activeWhen</strong> 返回 <strong>true</strong>，对应的子应用就会被激活。</p>
</li>
<li>
<p><strong>app</strong></p>
<p>函数，用于获取<strong>子应用</strong>提供给<strong>基座应用</strong>的<strong>生命周期方法</strong>：<strong>bootstrap</strong>、<strong>mount</strong>、<strong>unmount</strong> 等。</p>
<p>我们知道，在基于 <strong>vue</strong>、<strong>react</strong> 的<strong>单页应用</strong>中，每个页面都是以<strong>组件</strong>的形式存在。根据路由切换页面时，通常会先执行<strong>上一个页面组件的卸载 - unmount 操作</strong>，然后再执行<strong>下一个页面组件的挂载 - mount 操作</strong>。</p>
<p><strong>基座应用</strong>切换<strong>子应用</strong>时，也是同样的操作，即先执行<strong>上一个子应用的 unmount 操作</strong>，然后再<strong>执行下一个子应用的 mount 操作</strong>。因此就需要子应用提供 <strong>mount</strong>、<strong>unmount</strong> 等生命周期方法，供基座应用调用。</p>
<p>和<strong>单页应用的懒加载</strong>一样，<strong>基座应用</strong>在<strong>激活子应用</strong>时，如果子应用是<strong>首次激活</strong>，就会执行 <strong>app</strong> 方法，<strong>动态去加载子应用的入口 js 文件</strong>，然后执行，得到子应用的生命周期方法。</p>
</li>
<li>
<p><strong>customProps</strong></p>
<p>子应用激活时，可以传递给子应用的自定义属性，是一个对象。</p>
</li>
</ul>
</li>
<li>
<h4 id="user-content-2-2" data-id="heading-4">子应用改造</h4>
<p>子应用的改造，涉及两个方面：</p>
<ul>
<li><strong>入口文件 index.js 添加生命周期方法 - mount、unmount、update 等</strong>；</li>
<li><strong>打包构建改造</strong>；</li>
</ul>
<p>以 app1 为例，代码如下：</p>
<pre><code class="copyable">// index.js

import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

const appOptions = &#123;
  render: (h) => h(App)
&#125;;

let vueInstance;

// 子应用没有接入 single-spa
if (!window.__SINGLE_SPA__) &#123;
  new Vue(appOptions).$mount('#app')
&#125;

// 提供 bootstrap 生命周期方法
export function bootstrap () &#123;
  console.log('app1 bootstrap')
  return Promise.resolve().then(() => &#123;

  &#125;);
&#125;
// 提供 mount 生命周期方法
export function mount (props) &#123;
  console.log('app1 mount', props)
  return Promise.resolve().then(() => &#123;
    vueInstance = new Vue(appOptions)
    vueInstance.$mount('#microApp')
  &#125;)
&#125;

// 提供 unmount 生命周期方法
export function unmount () &#123;
  console.log('app1 unmount')
  return Promise.resolve().then(() => &#123;
    if (!vueInstance.$el.id) &#123;
      vueInstance.$el.id = 'microApp'
    &#125;
    vueInstance.$destroy()
    vueInstance.$el.innerHTML = ''
  &#125;)
&#125;

// 提供 update 生命周期方法
export function update () &#123;
  console.log('app1 update');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述<strong>生命周期方法</strong>中，最关键的就是 <strong>mount</strong> 和 <strong>unmount</strong>。其中，<strong>mount</strong> 会在<strong>子应用激活</strong>时调用，通过框架(vue / react / angular)提供的 api，挂载子应用；<strong>unmount</strong> 会在<strong>子应用冻结</strong>时调用，也是通过框架提供的 api 来卸载子应用。</p>
<blockquote>
<p><strong>mount、unmount 缺失会抛出异常。</strong></p>
</blockquote>
<p>另外，我们还要对项目的<strong>构建脚本</strong>进行改造，如下：</p>
<pre><code class="copyable">// vue.config.js

module.exports = &#123;
    configureWebpack: &#123;
        ...
        publicPath: 'http://localhost:8081'
        output: &#123;
            library: 'app1',
            libraryTarget: 'var'
        &#125;,
        ...
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常情况下，通过 <strong>webpack</strong> 构建工具生成的 <strong>js 脚本</strong>，表现形式都是 <strong>IIFF</strong>，即<strong>立即执行函数表达式</strong>。这种情况下，各个子应用对应的 js 脚本执行时是<strong>相互隔离</strong>的。如果是这样，那么<strong>基座应用</strong>在<strong>激活子应用</strong>时，是无法获取到子应用的<strong>生命周期方法</strong>的，也就无法挂载子应用。</p>
<p>为了打破这种隔离，我们就需要对 <strong>output</strong> 配置项做改造，添加 <strong>libaray</strong>、<strong>libraryTarget</strong> 配置项，将<strong>子应用入口文件的返回值即生命周期方法</strong>暴露给 <strong>window</strong>，这样<strong>基座应用</strong>就可以从 <strong>window</strong> 中获取子应用的<strong>生命周期方法</strong>。</p>
<p>另外，我们还需要配置 <strong>publicPath</strong>。<strong>publicPath</strong> 配置项指定了输出目录(path)对应的公开URL，主要是<strong>对页面里面引入的资源的路径做对应的补全</strong>，默认值为 '/'。 以 app1 为例，如果未配置 <strong>publicPath</strong>，子应用在懒加载 js 文件时，使用的 url 默认为当前应用 host 和文件位置，如 <a href="http://localhost:8081/js/0.chunk.js" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8081/js/0.chunk.js</a> 。如果 app1 接入 single-spa，那么 app1 在懒加载 js 文件时使用的 url 为基座应用的 host 和文件位置，如 <a href="http://localhost:8080/js/0.chunk.js" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8080/js/0.chunk.js</a> ，加载文件失败。因此，我们需要在 app1 中添加 <strong>publicPath</strong> 配置项,指定 app1 懒加载文件的 host 为 <a href="http://localhost:8081/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:8081</a> 。</p>
</li>
</ul>
<p>以上示例，即 <strong>single-spa</strong> 的基本使用，该使用模式也称之为 <strong>application</strong> 模式。<strong>application</strong> 模式下，<strong>子应用的切换(挂载、卸载)<strong>都是由</strong>修改路由</strong>触发的，整个切换过程由 <strong>single-spa</strong> 框架控制，子应用仅需提供正确的<strong>生命周期方法</strong>即可。</p>
<h3 id="user-content-3" data-id="heading-5">single-spa 进阶使用: parcels</h3>
<p>在项目开发过程中，我们可能会遇到这样的情况：<strong>子应用 A</strong> 是使用 <strong>react</strong> 开发的，在项目迭代过程中，抽离出一个关于某个具体业务的<strong>通用组件 component1</strong> 并上传为 <strong>npm 包</strong>；<strong>子应用 B</strong> 是使用 <strong>vue</strong> 开发的，在项目迭代过程中，也需要用到刚才提到的某个具体业务，如果再开发一个 <strong>vue</strong> 的版本，那就有点重复造轮子了。</p>
<p>那么我们可不可以直接在 vue 应用中直接使用 react 组件呢? 答案是当然可以。我们可以利用 <strong>ReactDOM</strong> 提供的 <strong>render</strong>、<strong>unmountComponentAtNode</strong> 方法在 <strong>vue</strong> 应用中直接<strong>加载/更新/卸载</strong> react 组件。</p>
<p>同样的，我们还是通过一个简单的 demo - <a href="https://github.com/zjhILYxxq/micro-frontend/single-spa/parcel" target="_blank" rel="nofollow noopener noreferrer">micro-frontend/single-spa/parcel</a> 来具体看 <strong>react</strong> 组件是如何添加到 <strong>vue</strong> 应用的。</p>
<p>demo 的项目结构：</p>
<pre><code class="copyable">|-- single-spa
    |-- application
        |-- ...
    |-- parcel
        |-- app
            |-- package.json
            |-- public
            |-- src
                |-- main.js
                |-- App.vue
                |-- components
                    |-- vue-component.vue
                    |-- react-component.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面 demo 中，<strong>app</strong> 是一个基于 <strong>vue2</strong> 的应用。其中，<strong>react-component</strong> 是一个 <strong>react</strong> 组件，用来模拟一个外部的 <strong>npm 包</strong>，具体代码如下：</p>
<pre><code class="copyable">import React from 'react';
import ReactDOM from 'react-dom';

const ReactComponent = (props) => &#123;
    return React.createElement("div", null, `react component: $&#123;props.val&#125;`);
&#125;

export default ReactComponent;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>vue</strong> 组件 <strong>vue-component.vue</strong> 的代码如下：</p>
<pre><code class="copyable">// vue-component.vue
<template>
  <div>
    <div>vue 组件: <input v-model="val" /></div>
    <div id="parcel"></div>
  </div>
</template>

<script>
import ReactComponent from './react-component'
import ReactDOM from 'react-dom'

export default &#123;
  name: 'vue',
  data() &#123;
    return &#123;
      val: '123'
    &#125;
  &#125;,
  mounted() &#123;
    // vue 组件挂载完成以后，手动挂载 react 组件
    ReactDOM.render(ReactComponent(&#123;val: this.val&#125;), document.getElementById('parcel'))
  &#125;,
  updated() &#123;
    // vue 组件更新以后，重新手动挂载 react 组件
    ReactDOM.render(ReactComponent(&#123;val: this.val&#125;), document.getElementById('parcel'))
  &#125;,
  beforeDestory() &#123;
    // vue 组件卸载之前，手动卸载 react 组件
    ReactDOM.unmountComponentAtNode(document.getElementById('parcel'));
  &#125;
  
&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过上述代码，我们即可<strong>在 vue 应用中挂载/更新/卸载 react 组件</strong>。但是这种方式有一个问题，就是不够优雅，我们需要在 <strong>vue 应用</strong>中引入 <strong>react-dom</strong>。如果引入的多个 react 组件涉及的 react-dom 版本不一致，那么比较麻烦了。</p>
<p>那么，有没有一种更好的方式呢？</p>
<p>有的。<strong>single-spa</strong> 提供了一种称为 <strong>parcel</strong> 的模式来帮助我们更优雅方便的实现上述要求。</p>
<p>要使用 <strong>single-spa</strong> 的 <strong>parcel</strong> 模式，我们需要对 <strong>react 组件</strong>和 <strong>vue 应用</strong>做相关改造。</p>
<ul>
<li>
<h4 id="user-content-3-1" data-id="heading-6">组件改造</h4>
<p>首先是<strong>组件改造</strong>,我们需要像 <strong>application</strong> 模式中改造子应用一样来改造组件，给组件添加<strong>生命周期方法</strong>：<strong>bootstrap</strong>、<strong>mount</strong>、<strong>unmount</strong>、<strong>update</strong>。</p>
<p>具体如下：</p>
<pre><code class="copyable">import React from 'react';
import ReactDOM from 'react-dom';

const ReactComponent = (props) => &#123;
    return React.createElement("div", null, `react component: $&#123;props.val&#125;`);
&#125;

export default ReactComponent;

export function bootstrap() &#123;
    return Promise.resolve().then(() => &#123;
        console.log('bootstrap');
    &#125;)
&#125;

export function mount(props) &#123;
    return Promise.resolve().then(() => &#123;
        console.log('mount');
        ReactDOM.render(ReactComponent(props), props.domElement);
    &#125;);
&#125;

export function unmount(props) &#123;
    return Promise.resolve().then(() => &#123;
        console.log('unmount');
        ReactDOM.unmountComponentAtNode(props.domElement);
    &#125;)
&#125;

export function update(props) &#123;
    return Promise.resolve().then(() => &#123;
        console.log('update');
        ReactDOM.render(ReactComponent(props), props.domElement);
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<h4 id="user-content-3-2" data-id="heading-7">应用改造</h4>
<p>和 <strong>application</strong> 模式下<strong>基座应用</strong>的改造不同，在 <strong>parcel</strong> 模式下，我们需要使用 <strong>single-spa</strong> 提供的 <strong>mountRootParcel</strong> 方法来<strong>手动挂载/更新/卸载</strong>组件，具体代码如下：</p>
<pre><code class="copyable"><template>
  <div>
    <div>vue 组件: <input v-model="val" /></div>
    <div id="parcel"></div>
  </div>
</template>

<script>
import &#123; bootstrap, mount, unmount, update&#125; from './react-component'
import &#123; mountRootParcel &#125; from 'single-spa'
export default &#123;
  name: 'vue',
  data() &#123;
    return &#123;
      val: '123'
    &#125;
  &#125;,
  mounted() &#123;
    this.parcel = mountRootParcel(&#123;bootstrap, mount, unmount, update&#125;, &#123;
      val: this.val,
      domElement: document.getElementById('parcel')
    &#125;)

  &#125;,
  updated() &#123;
    if (this.parcel && this.parcel.update) &#123;
      this.parcel.update(&#123;
        val: this.val,
        domElement: document.getElementById('parcel')
      &#125;)
    &#125;
  &#125;,
  beforeDestory() &#123;
    if (this.parcel && this.parcel.unmount) &#123;
      this.parcel.unmount(&#123;
        domElement: document.getElementById('parcel1')
      &#125;)
    &#125;
  &#125;

&#125;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<p>通过上述改造，我们即可在一个 vue 应用中优雅方便的使用 react 组件，而且各个 react 组件的 react、react-dom 版本不一致也没有关系了。</p>
<p>另外，<strong>parcel</strong> 模式下，除了可以使用 <strong>single-spa</strong> 提供的 <strong>mountRootParcel</strong> 方法来挂载组件外，还可以通过另一个 <strong>api - mountParcel</strong> 来挂载组件。<strong>mountRootParcel</strong> 和 <strong>mountParcel</strong> 的用法完全一样，只不过 <strong>mountParcel</strong> 方法不能直接从 <strong>single-spa</strong> 中获取，需要从<strong>子应用/组件</strong>的 <strong>mount</strong> 生命周期方法执行时传入的 <strong>props</strong> 中获取，如下：</p>
<pre><code class="copyable">...

export function mount(props) &#123;
    ...
    props.mountParcel(...)
    ...
&#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>mountRootParcel</strong>、<strong>mountParcel</strong> 这两个方法<strong>获取方式</strong>的不同，导致它们的<strong>应用场景</strong>也不同。</p>
<p><strong>mountParcel</strong>，只能从<strong>子应用/组件</strong>的 <strong>mount</strong> 生命周期方法执行时传入的 <strong>props</strong> 中获取，这就使得 <strong>mountParcel</strong> 只有在<strong>子应用/组件中挂载其他组件</strong>时才能使用。<strong>mountParcel</strong> 将<strong>要挂载的组件和子应用(父组件)绑定到一起</strong>，当子应用(父组件)要被卸载时，<strong>组件</strong>的 <strong>unmount</strong> 方法自动被触发。</p>
<p><strong>mountRootParcel</strong> 没有 <strong>mountParcel</strong> 的使用限制，我们可以在任何地方通过 <strong>mountRootParcel</strong> 方法来挂载组件。不过要注意的是，通过 <strong>mountRootParcel</strong> 挂载的组件，必须自己<strong>手动卸载</strong>。</p>
<p>举个栗子，一个基于 <strong>vue</strong> 开发的子应用 <strong>app1</strong> 接入了 <strong>single-spa</strong>，在 <strong>app1</strong> 中我们又使用了一个基于 <strong>react</strong> 开发的组件 <strong>comp2</strong>。<strong>app1</strong>、<strong>comp2</strong> 都提供了完整的<strong>生命周期方法</strong> - <strong>bootstrap</strong>、<strong>mount</strong>、<strong>unmount</strong>。如果我们使用 <strong>mountParcel</strong> 挂载 <strong>comp2</strong>，那么我们就不需要在 <strong>comp2</strong> 的<strong>父组件的 componentWillUnmount</strong> 中<strong>显示</strong>的卸载 <strong>comp2</strong>，<strong>app1</strong> 应用卸载的时候会自动卸载 <strong>comp2</strong>。如果我们使用 <strong>mountRootParcel</strong> 挂载 <strong>comp2</strong>， 那我们必须要在 <strong>comp2</strong> 的父组件的 <strong>componentWillUnmount</strong> 中<strong>显示</strong>的卸载 <strong>comp2</strong>，否则 <strong>app1</strong> 卸载的时候是不会卸载 <strong>comp2</strong> 的。</p>
<p>到这里， <strong>parcel 模式</strong>的使用方式就介绍完了。在这里，我们对 <strong>application</strong> 和 <strong>parcel</strong> 模式，做一个简单的对比：</p>






























<table><thead><tr><th>标题</th><th>application</th><th>parcel</th></tr></thead><tbody><tr><td>路由控制</td><td>有</td><td>无</td></tr><tr><td>UI 渲染</td><td>有</td><td>有</td></tr><tr><td>生命周期方法</td><td>single-spa 管理</td><td>用户自己管理</td></tr><tr><td>应用场景</td><td>多个子应用聚合</td><td>跨框架使用组件</td></tr></tbody></table>
<h3 id="user-content-4" data-id="heading-8">常用 API 用法</h3>
<p>single-spa 的相关 API，<a href="https://zh-hans.single-spa.js.org/docs/api" target="_blank" rel="nofollow noopener noreferrer">官方文档</a> 已经有了详细说明，本文就不再一一说明。下面列出了 single-spa 所有 API 的官网链接，大家可以移步官网去查看。</p>
<ul>
<li>
<h4 data-id="heading-9"> application 类 API</h4>
<ul>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#registerapplication" target="_blank" rel="nofollow noopener noreferrer">registerApplication</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#start" target="_blank" rel="nofollow noopener noreferrer">start</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#triggerappchange" target="_blank" rel="nofollow noopener noreferrer">triggerAppChange</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#navigatetourl" target="_blank" rel="nofollow noopener noreferrer">navigateToUrl</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#getmountedapps" target="_blank" rel="nofollow noopener noreferrer">getMountedApps</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#getappnames" target="_blank" rel="nofollow noopener noreferrer">getAppNames</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#getappstatus" target="_blank" rel="nofollow noopener noreferrer">getAppStatus</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#unloadapplication" target="_blank" rel="nofollow noopener noreferrer">unloadApplication</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#checkactivityfunctions" target="_blank" rel="nofollow noopener noreferrer">checkActivityFunctions</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#adderrorhandler" target="_blank" rel="nofollow noopener noreferrer">addErrorHandler</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#removeerrorhandler" target="_blank" rel="nofollow noopener noreferrer">removeErrorHandler</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#pathtoactivewhen" target="_blank" rel="nofollow noopener noreferrer">pathToActiveWhen</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#ensurejquerysupport" target="_blank" rel="nofollow noopener noreferrer">ensureJQuerySupport</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#setbootstrapmaxtime" target="_blank" rel="nofollow noopener noreferrer">setBootstrapMaxTime</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#setmountmaxtime" target="_blank" rel="nofollow noopener noreferrer">setMountMaxTime</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#setunmountmaxtime" target="_blank" rel="nofollow noopener noreferrer">setUnmountMaxTime</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/api#setunloadmaxtime" target="_blank" rel="nofollow noopener noreferrer">setUnloadMaxTime</a></li>
</ul>
</li>
<li>
<h4 data-id="heading-10"> parcel 类 API </h4>
<ul>
<li><a href="https://zh-hans.single-spa.js.org/docs/parcels-api#mountparcel" target="_blank" rel="nofollow noopener noreferrer">mountParcel</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/parcels-api#mountrootparcel" target="_blank" rel="nofollow noopener noreferrer">mountRootParcel</a></li>
<li><a href="https://zh-hans.single-spa.js.org/docs/parcels-api#parcel-%E5%AF%B9%E8%B1%A1" target="_blank" rel="nofollow noopener noreferrer">parcel 对象</a></li>
</ul>
</li>
</ul>
<h3 id="user-content-5" data-id="heading-11">关于 single-spa，你需要深入了解的知识点</h3>
<ul>
<li>
<h4 id="user-content-5-1" data-id="heading-12">application 模式下子应用是如何切换的 </h4>
<p>当下流行的<strong>单页应用的路由切换功能</strong>都是基于 <strong>window.history( window.location.hash)</strong> 实现的。在单页面应用中，我们会给 <strong>window</strong> 对象注册 <strong>popstate(hashchange)</strong> 事件，在 <strong>popstate(hashchange)</strong> 的 <strong>callback</strong> 中，添加<strong>页面切换</strong>的逻辑。当通过<strong>执行 pushState(replaceState) 方法</strong>、<strong>修改 hash 值</strong>、<strong>使用浏览器前进后退(go、back、forward)功能</strong>改变 url 时，会触发 <strong>popstate(hashchange)</strong> 事件，然后切换页面。</p>
<p><strong>子应用的切换</strong>也是基于上述原理实现的。</p>
<p><strong>基座应用</strong>加载执行 <strong>single-spa</strong> 时，也会给 <strong>window</strong> 对象注册 <strong>popstate (hashchange)</strong> 事件， <strong>popstate(hashchange)</strong> 的 <strong>calback</strong> 中，就是<strong>激活子应用的逻辑</strong>。当<strong>基座应用</strong>通过<strong>执行pushState(replaceState)</strong>、<strong>修改 hash</strong>、<strong>使用浏览器前进后退(go、back、forward)功能</strong>的方式修改 url 时，<strong>popstate(hashchange)</strong> 就会触发，相应的<strong>子应用的激活逻辑</strong>就会执行。</p>
<p>我们知道，在使用 <strong>window.history</strong> 时，如果执行 <strong>pushState(repalceState)</strong> 方法，是不会触发 <strong>popstate</strong> 事件的，而 <strong>single-spa</strong> 通过一种巧妙的方式，实现了执行 <strong>pushState(replaceState)</strong> 方法可触发 <strong>popstate</strong> 事件，具体代码如下：</p>
<pre><code class="copyable">// 通过原生构造函数 - PopStateEvent，创建一个 popstate 事件对象
function createPopStateEvent(state, originalMethodName) &#123;
    var evt;
    try &#123;
      evt = new PopStateEvent("popstate", &#123;
        state: state
      &#125;);
    &#125; catch (err) &#123;
      evt = document.createEvent("PopStateEvent");
      evt.initPopStateEvent("popstate", false, false, state);
    &#125;
    evt.singleSpa = true;
    evt.singleSpaTrigger = originalMethodName;
    return evt;
&#125;
// 重写 updateState、replaceState 方法，通过 window.dispatchEvent 方法，手动触发 popstate 事件
function patchedUpdateState(updateState, methodName) &#123;
    return function () &#123;
      var urlBefore = window.location.href;
      var result = updateState.apply(this, arguments);
      var urlAfter = window.location.href;

      if (!urlRerouteOnly || urlBefore !== urlAfter) &#123;
        window.dispatchEvent(createPopStateEvent(window.history.state, methodName));
      &#125;
      return result;
    &#125;;
&#125;
// 重写 pushState 方法
window.history.pushState = patchedUpdateState(window.history.pushState, "pushState");
// 重写 replaceState 方法
window.history.replaceState = patchedUpdateState(window.history.replaceState, "replaceState");
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之所以能在执行 <strong>pushState</strong>、<strong>replaceState</strong> 方法时，触发 <strong>popstate</strong> 事件，是因为 <strong>single-spa</strong> 重写了 <strong>window.history</strong> 的 <strong>pushState</strong> 和 <strong>replaceState</strong> 方法。在执行 <strong>pushState</strong>、<strong>replaceState</strong> 方法时，会通过<strong>原生方法 - PopStateEvent</strong> 构建一个<strong>事件对象</strong>，然后调用 <strong>window.dispatchEvent</strong> 方法，<strong>手动触发 popState 事件</strong>。</p>
<p>另外，关于 <strong>single-spa</strong> 的路由控制，有一个点需要关注，那就是如果接入 <strong>single-spa</strong> 的子应用有自己的路由，那就需要对子应用的路由做改造，即<strong>给子应用的路由添加前缀</strong>，具体如下：</p>
<pre><code class="copyable">...
const router = new VueRouter(&#123;
  mode: 'history',
  base: '/app1',
  routes: [&#123;
    path: '/foo',
    name: 'foo',
    component: &#123;
      ...
    &#125;
  &#125;, &#123;
    path: '/bar',
    name: 'bar',
    component: &#123;
      ...
    &#125;
  &#125;]
&#125;)
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子应用 app1，如果基座应用中对应的路由为 '/app1', 那么子应用中的路由都需要添加前缀 '/app1'。这是因为，url 发生变化时，是先匹配子应用，然后再匹配子应用页面。如果子应用不添加前缀，那么修改以后的 url 可能就匹配不到子应用，也找不到对应的子应用页面了。</p>
<blockquote>
<p><strong>子应用切换页面时，尽管 url 发生变化，子应用也不会重复挂载。</strong></p>
</blockquote>
</li>
<li>
<h4 id="user-content-5-2" data-id="heading-13">single-spa 是如何工作的</h4>
<p><strong>single-spa</strong> 有两种使用模式：<strong>application</strong> 和 <strong>parcel</strong>。<strong>使用模式</strong>不同，<strong>single-spa</strong> 的<strong>工作流程</strong>也不相同。</p>
<ul>
<li>
<h5 data-id="heading-14">application 模式下，single-spa 的工作流程</h5>
<p><strong>application</strong> 模式下，我们需要先通过 <strong>registerApplication</strong> 注册子应用，然后在<strong>基座应用挂载完成</strong>以后执行 <strong>start</strong> 方法, 这样<strong>基座应用</strong>就可以根据 <strong>url</strong> 的变化来进行<strong>子应用切换</strong>，激活对应的子应用。</p>
<p>整个工作过程，具体如下：</p>
</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04819f2d36364b43990b3b66ceb5001a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<h5 data-id="heading-15">parcel 模式下，single-spa 的工作流程</h5>
<p>对比 <strong>application</strong> 模式， <strong>parcel</strong> 模式的工作流程就比较简单了，我们只需要获取到组件的<strong>生命周期方法</strong>，然后通过 <strong>mountRootParcel</strong> 方法直接挂载就可以了。</p>
<p><strong>mountRootParcel</strong> 方法会返回一个 <strong>parcel</strong> 实例对象，内部包含 <strong>update</strong>、<strong>unmount</strong> 方法。当我们需要<strong>更新组件</strong>时，直接调用 <strong>parcel</strong> 对象的 <strong>update</strong> 方法，就可以触发组件的 <strong>update</strong> 生命周期方法；当我们需要<strong>卸载组件</strong>时，直接调用 <strong>parcel</strong> 对象的 <strong>unmount</strong> 方法。</p>
<p>在执行 <strong>mountRootParcel</strong> 方法时，传入的<strong>第二个参数</strong>，会作为组件 <strong>mount 生命周期方法</strong>的<strong>入参</strong>；在执行 <strong>parcel.update</strong> 方法时，<strong>传入的参数</strong>，会作为组件 <strong>update 生命周期方法</strong>的<strong>入参</strong>。</p>
<blockquote>
<p><strong>组件的挂载、更新、卸载，都必须要有对应的 root 节点，因此参数中必须要有 domElement 属性，否则会抛出异常。</strong></p>
</blockquote>
</li>
</ul>
</li>
<li>
<h4 id="user-content-5-3" data-id="heading-16">子应用/组件的生命周期方法如何被获取</h4>
<p>为了能使<strong>子应用/组件</strong>的<strong>生命周期方法</strong>能被外部获取到，我们需要对项目的 <strong>webpack 配置文件</strong>的 <strong>output</strong> 配置项做改造，添加 <strong>library</strong> 和 <strong>libraryTarget</strong> 配置项。其中， <strong>library</strong> 定义了子应用/组件的 <strong>export</strong> 的名称，<strong>libraryTarget</strong> 定义了<strong>暴露 export 的方式</strong>。</p>
<p>在上面的 <a href="https://github.com/zjhILYxxq/micro-frontend/single-spa/application" target="_blank" rel="nofollow noopener noreferrer">micro-frontend/single-spa/application</a> 示例中，我们在 <strong>app1</strong> 中定义了 <strong>library</strong> 为 <strong>'app1'</strong>, <strong>libraryTarget</strong> 为 <strong>'var'</strong>， 那么<strong>基座应用</strong>就可以通过 <strong>window.app1</strong> 获取到子应用的 <strong>export</strong>，得到子应用的<strong>生命周期方法</strong>。</p>
<blockquote>
<p><strong>libraryTarget 配置项的值有很多，可以根据自身实际需要，进行配置。</strong></p>
</blockquote>
</li>
<li>
<h4 id="user-content-5-4" data-id="heading-17">如何判断一个子应用(组件)是否也被激活(挂载)</h4>
<p>每个子应用都有一个 <strong>status</strong> 字段，表示子应用生命周期中的各个阶段:</p>
<ul>
<li>
<p><strong>NOT_LOADED</strong>: 未加载/待加载</p>
<p>未加载(待加载)每个子应用的默认状态，意味着主应用还没有获取到子应用的 bootstrap、mount、unmount、unload 方法。</p>
<p><strong>NOT_LOADED</strong> 的下一个阶段为 <strong>LOAD_SOURCE_CODE</strong>。</p>
</li>
<li>
<p><strong>LOAD_SOURCE_CODE</strong>: 加载源代码</p>
<p>在这个阶段，single-spa 会执行子应用注册时提供的 loadApp 方法，去动态获取子应用的入口 js 文件，然后执行，得到子应用的 bootstrap、mount、unmount、unload 方法。</p>
<p><strong>LOAD_SOURCE_CODE</strong> 的下一个阶段为 <strong>NOT_BOOTSTRAPPED</strong>。</p>
</li>
<li>
<p><strong>NOT_BOOTSTRAPPED</strong>: 未启动/待启动</p>
<p>得到子应用的 bootstrap、mount、unmount、unload、update 方法以后，single-spa 会将这些方法添加到子应用对象中。 添加完毕以后，子应用的状态就变为 not_bootstrapped，等待被启动。</p>
<p><strong>NOT_BOOTSTRAPPED</strong> 的下一个阶段为 <strong>BOOTSTRAPPING</strong>。</p>
</li>
<li>
<p><strong>BOOTSTRAPPING</strong>: 子应用启动中</p>
<p>子应用被激活以后，就会进入 <strong>BOOTSTRAPPING</strong> 阶段。此时如果子应用提供了 bootstrap 方法，那么 bootstrap 方法就会触发。</p>
<p><strong>BOOTSTRAPPING</strong> 的下一个阶段为 <strong>NOT_MOUNTED</strong>。</p>
</li>
<li>
<p><strong>NOT_MOUNTED</strong>: 未挂载/待挂载</p>
<p>子应用启动以后，自动进入 <strong>NOT_MOUNTED</strong> 阶段。</p>
<p><strong>NOT_MOUNTED</strong> 的下一个阶段为 <strong>MOUNTING</strong>.</p>
</li>
<li>
<p><strong>MOUNTING</strong>: 子应用挂载中</p>
<p>在这个阶段，自动触发子应用提供的 <strong>mount</strong> 方法。</p>
<p><strong>MOUNTING</strong> 的下一个阶段为 <strong>MOUNTED</strong></p>
</li>
<li>
<p><strong>MOUNTED</strong>: 子应用已挂载</p>
<p>子应用挂载完毕，子应用的状态变为 <strong>MOUNTED</strong>。</p>
</li>
<li>
<p><strong>UNMOUNTING</strong></p>
<p>如果一个子应用需要被卸载，那么这个子应用的状态就会变为 <strong>UNMOUNTING</strong>。</p>
<p>此时，子应用的 <strong>unmount</strong> 方法会执行。</p>
</li>
<li>
<p><strong>UNMOUNTED</strong></p>
<p>子应用卸载完毕以后，子应用的状态就会变为 <strong>UNMOUNTED</strong>。</p>
</li>
<li>
<p><strong>LOAD_ERROR</strong></p>
<p>子应用加载失败，子应用的状态就会变为 <strong>LOAD_ERROR</strong>。</p>
</li>
</ul>
<p>组件和子应用的 <strong>status</strong> 基本相同，状态包含 <strong>NOT_BOOTSTRAPPED</strong>、<strong>BOOTSTRAPPING</strong>、<strong>NOT_MOUNTED</strong>、<strong>MOUNTED</strong>、<strong>UNMOUNTING</strong>、<strong>UNMOUNTED</strong> 等，此外还包含一个 <strong>UPDATING</strong>，即 <strong>parcel.update</strong> 方法执行时，组件的状态变为 <strong>UPDATING</strong>。</p>
<blockquote>
<p><strong>UPDATING 状态仅存在于 parcel 组件</strong>。</p>
</blockquote>
<p>当子应用(组件)的状态变为 <strong>MOUNTED</strong> 时，说明子应用(组件)已被激活(挂载)。</p>
<p>子应用的 <strong>status</strong> 值，可以通过 <strong>getAppStatus</strong> 获取；组件的 <strong>status</strong> 值，需要通过 <strong>parcel.getStatus</strong> 获取</p>
</li>
<li>
<h4 id="user-content-5-6" data-id="heading-18">子应用/组件如何通信</h4>
<p>使用 <strong>single-spa</strong> 时，不可避免的会遇到<strong>子应用/组件的通信</strong>，常见通信主要包括<strong>父组件和 parcel 组件之间的通信</strong>、<strong>parcel 组件之间的通信</strong>、<strong>基座应用和子应用的通信</strong>、<strong>子应用之间的通信</strong>。</p>
<ul>
<li>
<p><strong>父组件和 parcel 组件之间的通信</strong></p>
<p><strong>父组件和 parcel 组件之间的通信</strong>比较简单，父组件可以通过 <strong>props</strong> 属性向 parcel 组件传递值。</p>
<p>具体的方式为：<strong>mount</strong> 阶段，父组件在执行 <strong>mountRootParcel</strong> 时，可以将要传递给 parcel 组件的值作为<strong>第二个参数</strong>，这个参数会作为 parcel 组件 <strong>mount</strong> 方法执行时的<strong>入参</strong>，这样 parcel 组件就可以拿到父组件传递的值。<strong>update</strong> 阶段也一样，父组件执行 <strong>parcel.update</strong> 时，传入的参数会作为 parcel 组件 <strong>update</strong> 方法执行时的入参。</p>
<p>我们可以在父组件传递给 parcel 组件的值中添加一个方法，当 parcel 组件需要通知父组件更新时，可以执行这个方法。</p>
</li>
<li>
<p><strong>parcel 组件之间的通信</strong></p>
<p><strong>parcel 组件之间的通信</strong>也比较好实现，本质上也是 <strong>parcel 组件和父组件之间的通信</strong>。 parcel 组件可以通过父组件传递的方法，触发父组件的更新，父组件更新以后，在触发另一个 parcel 组件的更新。</p>
</li>
<li>
<p><strong>基座应用和子应用之间的通信</strong></p>
<p><strong>基座应用</strong>在定义<strong>路由注册表</strong>时，会给每个<strong>子应用</strong>定义一个 <strong>customProps</strong>，这个 <strong>customProps</strong> 会作为子应用 <strong>mount</strong> 方法的<strong>入参</strong>。在子应用中， <strong>customProps(或者 customProps 里面的某个值)</strong> 可以作为子应用的<strong>共享状态</strong>(使用 vuex、mobx、redux 等)。这样，当<strong>基座应用</strong>修改 <strong>customProps</strong> 时，子应用就可接受到通知，然后更新。</p>
<p>我们也可以在 <strong>cusProps</strong> 中添加一个方法，当<strong>子应用</strong>需要通知<strong>基座应用</strong>更新时，可以执行这个方法。</p>
</li>
<li>
<p><strong>子应用之间的通信</strong></p>
<p>子应用之间的通信也一样，本质上也是基座应用和子应用的通信。</p>
</li>
</ul>
</li>
<li>
<h4 id="user-content-5-7" data-id="heading-19">子应用/组件生命周期方法为什么必须要返回一个 promise 对象</h4>
<p>以子应用/组件的 <strong>mount</strong> 方法为例，我们需要以如下的形式定义一个 <strong>mount</strong> 方法：</p>
<pre><code class="copyable">export function mount(props) &#123;
    return Promise.resolve().then(() => &#123;
        // 子应用/组件具体的挂载逻辑
        ...
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <strong>single-spa</strong> 中，子应用/组件的生命周期方法触发的具体逻辑如下：</p>
<pre><code class="copyable">function reasonableTime(appOrParcel, lifecycle) &#123;
    ...
    return new Promise(function (resolve, reject) &#123;
      var finished = false;
      var errored = false; 
      // 子应用/组件的生命周期方法触发，返回一个 promise 对象
      appOrParcel[lifecycle](getProps(appOrParcel)).then(function (val) &#123;
        finished = true;
        resolve(val);
      &#125;).catch(function (val) &#123;
        finished = true;
        reject(val);
      &#125;);
      
      ...
    &#125;);
&#125;

...
// 执行子应用/组件的生命周期方法
reasonableTime(appOrParcel, "mount").then(function () &#123;
    // 子应用的状态变为 Mounted
    appOrParcel.status = MOUNTED;
    ...
  &#125;).catch(function (err) &#123;
    ...
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>综上，子应用/子组件的生命周期方法，需要返回一个 <strong>promise</strong> 对象，而且这个 <strong>promise</strong> 对象的状态可变为 <strong>resolved</strong>，否则 <strong>single-spa</strong> 在执行子应用的生命周期方法时会出现异常。</p>
</li>
<li>
<h4 id="user-content-5-8" data-id="heading-20"> single-spa 生命周期 hooks </h4>
<p><strong>single-spa</strong> 定义了一些生命周期 <strong>hooks</strong>，可以帮助我们在子应用/组件生命周期中执行<strong>自定义操作</strong>，这些 <strong>hooks</strong> 包括: <strong>'single-spa:before-first-mount'</strong>、<strong>'single-spa:first-mount'</strong>、<strong>'single-spa:before-no-app-change'</strong>、<strong>'single-spa:before-app-change'</strong>、<strong>'single-spa:before-routing-event'</strong>、<strong>'single-spa:before-mount-routing-event'</strong>、<strong>'single-spa:no-app-change'</strong>、<strong>'single-spa:app-change'</strong>、<strong>'single-spa:routing-event'</strong>。</p>
<p>以 <strong>single-spa:before-first-mount</strong> 为例，<strong>before-first-mount 表示第一次挂载子应用/组件开始之前</strong>，使用方式如下:</p>
<pre><code class="copyable">// 在 callback 中我们可以自定义操作
window.addEventListener('single-spa:before-first-mount', event => &#123;...&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>single-spa</strong> 在第一次挂载子应用/组件之前，会触发 <strong>single-spa:before-first-mount</strong> 事件，方式如下：</p>
<pre><code class="copyable">window.dispatch(new customEvent("single-spa:before-first-mount"));
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p><strong>single-spa:before-first-mount</strong></p>
<p><strong>single-spa</strong> 第一次挂载子应用/组件之前触发，之后就不会再触发。</p>
</li>
<li>
<p><strong>single-spa:first-mount</strong></p>
<p><strong>single-spa</strong> 第一次挂载子应用/组件之后触发，之后就不会在触发了。</p>
<blockquote>
<p><strong>子应用/组件挂载完成之后，fisrt-mount 才会触发。</strong></p>
</blockquote>
</li>
<li>
<p><strong>single-spa:before-no-app-change</strong></p>
<p><strong>application</strong> 模式下，修改 url 会触发子应用的切换。如果路由注册表中<strong>没有</strong>匹配当前 url 的子应用，那么 <strong>single-spa:before-no-app-change</strong> 事件会触发。</p>
</li>
<li>
<p><strong>single-spa:before-app-change</strong></p>
<p>和 <strong>single-spa:before-no-app-change</strong> 相反，修改 url 导致子应用切换时，如果路由注册表中<strong>有</strong>匹配当前 url 的子应用， <strong>single-spa:before-app-change</strong> 事件会触发。</p>
</li>
<li>
<p><strong>single-spa:before-routing-event</strong></p>
<p><strong>application</strong> 模式下， <strong>hashchange</strong>、<strong>popstate</strong> 触发以后，<strong>single-spa:before-routing-event</strong> 事件就会触发。</p>
</li>
<li>
<p><strong>single-spa:before-mount-routing-event</strong></p>
<p><strong>application</strong> 模式下, 旧的子应用卸载完成之后，新的子应用挂载之前触发。</p>
</li>
<li>
<p><strong>single-spa:app-change</strong></p>
<p><strong>application</strong> 模式下，旧的子应用卸载完成，新的子应用挂载完成之后触发。</p>
<p><strong>single-spa:before-app-change</strong> 触发， <strong>single-spa:app-change</strong> 就会触发。</p>
</li>
<li>
<p><strong>single-spa:no-app-change</strong></p>
<p><strong>application</strong> 模式下，如果 <strong>single-spa：before-no-app-change</strong> 触发，那么最后 <strong>single-spa：no-app-change</strong> 会触发。</p>
</li>
<li>
<p><strong>single-spa:routing-even</strong></p>
<p><strong>application</strong> 模式下， <strong>single-spa:no-app-change</strong> / <strong>single-spa:no-app-change</strong> 触发以后， <strong>single-spa:routing-event</strong> 触发。</p>
</li>
</ul>
</li>
<li>
<h4 id="user-content-5-9" data-id="heading-21">配合 single-spa 使用的 npm 包</h4>
<p>在实际的项目中，我们可以使用一些 <strong>npm</strong> 包配合 <strong>single-spa</strong> 使用，提高开发效率。常用的 <strong>npm</strong> 包有 <strong>single-spa-vue</strong>、<strong>single-spa-react</strong> 等。</p>
<ul>
<li>
<p><strong>single-spa-vue</strong></p>
<p>子应用/组件接入 <strong>single-spa</strong> 时，我们需在在 <strong>mount</strong> 方法中添加挂载逻辑，在 <strong>unmount</strong> 方法中添加卸载逻辑，在 <strong>update</strong> 方法中添加更新逻辑。如果我们有多个子应用/子组件要接入 <strong>single-spa</strong>，那我们就需要在每个子应用/组件中将同样的逻辑编写一遍。这种行为，对于任何一名稍微有点追求的程序员，都是深恶痛绝的。遇到这种情况，我们肯定会想着把这种相同的逻辑抽象封装，使其可复用，而 single-spa-vue 就是这样的一个 npm 包。</p>
<p><strong>single-spa-vue</strong> 可以快速帮我们给每个基于 <strong>vue</strong> 开发的子应用/组件定义 <strong>mount</strong>、<strong>unmount</strong>、<strong>update</strong> 方法。</p>
<p>具体用法详见：<a href="https://single-spa.js.org/docs/ecosystem-vue" target="_blank" rel="nofollow noopener noreferrer">single-spa-vue</a></p>
</li>
<li>
<p><strong>single-spa-react</strong></p>
<p><strong>single-spa-react</strong> 和 <strong>single-spa-vue</strong> 的作用一样，可以快速帮我们给每个基于 <strong>react</strong> 开发的子应用/组件定义 <strong>mount</strong>、<strong>unmount</strong>、<strong>update</strong> 方法。</p>
<p>具体用法详见：<a href="https://single-spa.js.org/docs/ecosystem-react" target="_blank" rel="nofollow noopener noreferrer">single-spa-react</a></p>
</li>
<li>
<p><strong>其他</strong></p>
<p>此外，可配合使用的 npm 包还有：<a href="https://single-spa.js.org/docs/ecosystem-angular" target="_blank" rel="nofollow noopener noreferrer">single-spa-angular</a>、<a href="https://single-spa.js.org/docs/ecosystem-angularjs/" target="_blank" rel="nofollow noopener noreferrer">single-spa-angularjs</a>、<a href="https://single-spa.js.org/docs/ecosystem-cycle/" target="_blank" rel="nofollow noopener noreferrer">single-spa-cycle</a> 等，具体详见：<a href="https://single-spa.js.org/docs/ecosystem" target="_blank" rel="nofollow noopener noreferrer">ecosystem</a>。</p>
</li>
</ul>
</li>
</ul>
<h3 id="user-content-6" data-id="heading-22">single-spa 的不足</h3>
<p>尽管 <strong>single-spa</strong> 给我们提供了一套完整的<strong>微前端解决方案</strong>，但在实际的项目中，依然有很多的问题需要我们去面对解决，如<strong>复杂的子应用加载逻辑</strong>、<strong>应用之间 js、css 的隔离</strong>、<strong>子应用切换遗留的副作用</strong>、<strong>子应用状态恢复</strong>以及<strong>子应用之间的通信</strong>、<strong>子应用的预加载</strong>等。</p>
<ul>
<li>
<h4 data-id="heading-23">复杂的子应用加载逻辑</h4>
<p>实际项目中的<strong>子应用加载过程</strong>，远比我们在示例 - <a href="https://github.com/zjhILYxxq/micro-frontend/single-spa/application" target="_blank" rel="nofollow noopener noreferrer">micro-frontend/single-spa/application</a> 中的要复杂的多，我们需要考虑的点很多，比如：</p>
<ul>
<li><strong>图片、css 等静态资源的加载</strong>；</li>
<li><strong>不同子应用的打包生成的入口文件的名称、数量不一致</strong>；</li>
<li><strong>子应用更新导致打包文件 hash 值发生变化</strong>；</li>
<li><strong>懒加载</strong>；</li>
</ul>
<p>对于第一个问题，我们可以通过<strong>将子应用中的图片、css 全部打包为 js 代码</strong>的方式来解决。但这样的话，<strong>css 独立打包</strong>、<strong>资源并行加载</strong>等优化就没有了。</p>
<p>对于第二个和第三个问题，我们可以在子应用打包时生成一个 <strong>manifest</strong> 文件，内部包含子应用的<strong>入口文件</strong>的名称，然后将这个 <strong>manifest</strong> 存起来。在<strong>基座应用构建路由注册表</strong>时，可以通过<strong>动态获取子应用对应的 manifest</strong> 文件来拿到<strong>子应用的入口文件</strong>。</p>
<p>对于最后一个<strong>懒加载</strong>的问题，我们可以在<strong>子应用配置文件</strong>中添加 <strong>publicPath</strong> 配置，对子应用资源的路径做<strong>补全</strong>。(详见 application - 子应用改造章节)。</p>
</li>
<li>
<h4 data-id="heading-24">应用之间的 js、css 隔离</h4>
<p>由于<strong>多个应用(基座应用 + 子应用、子应用 + 子应用)共存</strong>，我们就需要特别关注<strong>各个应用之间全局变量(如 window)、样式不能相互干扰</strong>。</p>
<p>针对这类问题，我们一般通过<strong>命名约定</strong>的方式来解决，<strong>给各个应用的全局变量、样式根据子应用来分别添加前缀</strong>。这种方式虽能解决问题，但重度依赖于<strong>人为约束</strong>，费时费力且容易引发 bug。</p>
</li>
<li>
<h4 data-id="heading-25">子应用切换遗留的副作用</h4>
<p>尽管<strong>子应用</strong>会提供 <strong>unmount</strong> 生命周期方法供<strong>基座应用</strong>在切换<strong>子应用</strong>时调用，但依然会遗留一些<strong>副作用</strong>，如：</p>
<ul>
<li><strong>子应用定义的 setInterval</strong></li>
<li><strong>子应用通过 window.addEventListener 注册的事件</strong>；</li>
<li><strong>子应用添加修改的 window 对象的属性</strong>；</li>
<li><strong>子应用动态添加的 dom 节点，如 style 节点</strong>；</li>
</ul>
<p>这些<strong>副作用</strong>的存在，有些会造成<strong>内存泄漏</strong>，有些会<strong>对下一个子应用造成影响</strong>，因此需要我们在切换子应用时对这些<strong>副作用</strong>做清除处理。</p>
</li>
<li>
<h4 data-id="heading-26">子应用状态恢复</h4>
<p>有些时候，我们需要在<strong>重新挂载子应用</strong>时，<strong>恢复子应用之前的状态</strong>，如<strong>子应用之前修改的 window</strong>、<strong>子应用动态添加的 style</strong> 等。这就要求我们需要在<strong>卸载子应用</strong>时，<strong>存储上述状态</strong>，然后在<strong>子应用重新挂载</strong>时，将存储的状态恢复。</p>
</li>
<li>
<h4 data-id="heading-27">应用之间的通信</h4>
<p>使用 <strong>single-spa</strong> 时，<strong>应用之间的通信</strong>也是我们需要重点关注的。在<a href="https://juejin.cn/post/6955342063235760164#5-6">子应用/组件之间如何通信</a>章节中，我们已做了说明，感兴趣的同学可以再回顾一下。</p>
</li>
<li>
<h4 data-id="heading-28">子应用预加载</h4>
<p>在使用 <strong>single-spa</strong> 进行微前端开发时，我们也可以应用<strong>资源预加载</strong>这种优化手段，在当前子应用工作过程中，利用空闲时间，<strong>提前加载其他子应用所需的资源</strong>，使得下一个子应用可以快速打开。</p>
</li>
</ul>
<p>上述这些问题，其实是微前端开发过程中的常见问题。我们虽然可以通过相关手段解决，但我们更希望的是框架能帮我们解决，使得微前端开发更加简单方便。</p>
<p>那么有没有一个框架能帮我们解决上述问题呢？</p>
<p>答案是有的。<strong>qiankun</strong> 就是这样的一个框架，它在 <strong>single-spa</strong> 的基础上做了二次开发，能帮我们很好的解决上述提到的问题。关于 <strong>qiankun</strong>，<a href="https://juejin.cn/post/6955342063235760164">微前端学习系列(三)：qiankun </a> 中已做了相关说明，感兴趣的同学可以前往了解。</p>
<h3 id="user-content-7" data-id="heading-29">结束语</h3>
<p>到这里，<strong>single-spa</strong> 的学习就结束了。本文主要介绍了 <strong>single-spa 的用法</strong>、<strong>一些关键知识点</strong>以及 <strong>single-spa 的不足</strong>。篇幅较长，阅读起来比较花时间，希望能给到大家帮助，如果有疑问或者错误，欢迎大家提出，共同学习，一起进步，😁。</p>
<p><a href="https://github.com/zjhILYxxq/micro-frontend/blob/main/single-spa/single-spa.dev.js" target="_blank" rel="nofollow noopener noreferrer">single-spa 源码注释</a></p>
<p>完成本文，参考文档如下：</p>
<ul>
<li><a href="https://single-spa.js.org/" target="_blank" rel="nofollow noopener noreferrer">single-spa 官网</a></li>
<li><a href="https://juejin.cn/post/6862661545592111111#comment" target="_blank">微前端框架之 single-spa 从入门到精通</a></li>
</ul></div>  
</div>
            