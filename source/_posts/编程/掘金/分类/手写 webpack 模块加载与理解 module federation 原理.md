
---
title: '手写 webpack 模块加载与理解 module federation 原理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=491'
author: 掘金
comments: false
date: Tue, 25 May 2021 22:36:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=491'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近在使用 <code>qiankun</code> 构建子应用的时候，遇到了父子应用使用了相同 <code>lib</code> 的导致打包出来两份 ，增加了代码体积。为了优化这个问题，官方文档目前建议使用 <code>webpack</code> 的 external，但是需要共享的包很多，大量在 html 引入外部 js 导致页面首屏时间增长，且私下与 <code>qiankun</code> 开发沟通，目前最优方案还是使用 <code>module federation</code> 去共享模块，以下简称 mf。所以为了更深刻理解 <code>webpack</code> 的模块加载机制以理解 mf 的原理，故根据 <code>webpack</code> 模块加载原理自行手写实现一个简易的 <code>webpack</code> 模块加载。</p>
<blockquote>
<p>实现的代码跟源代码有比较大的差别，但是思路大致是相同的。为了本地可以跑，所以在异步加载模块这里仅提供实现的伪代码。</p>
</blockquote>
<pre><code class="copyable">// 入口执行函数
function entry(modules) &#123;
  // 已经安装的 module
  const installedModules = &#123;&#125;;
  // 已经加载好的 chunk
  const installedChunks = &#123;&#125;;
  
  // 核心引用 module 的函数
  function __webpack_require__(moduleId) &#123;
    if (installedModules[moduleId]) &#123;
      // 因为已经安装/执行过了，所以别的文件再引用的时候，直接导出这个 module 对外暴露的属性，即 exports
      return installedModules[moduleId].exports;
    &#125;
    
    // 初始化模块数据
    const module = installedModules[moduleId] = &#123;
      moduleId,
      installed: false, // 标记是否已经加载
      exports: &#123;&#125; // 初始模块为空
    &#125;
    
    // 执行模块内的代码
    modules[moduleId].call(null, module, module.exports, __webpack_require__);
    // 将模块的加载状态改为 true
    module.installed = true;
    
    // 返回模块导出的数据，方便外部在 __webpack_require__(id) 的时候，直接可以拿到模块导出的数据
    return module.exports;
  &#125;
  
  // 记录 ``webpack`` 配置中的 publicPath
  __webpack_require__.p = '/';
  
  // 异步加载 chunk 脚本
  __webpack_require__.e = function (chunkId) &#123;
    
    // 假如已经加载过了
    if (installedModules[chunkId] && installedModules[chunkId].installed) return Promise.resolve();
  
    installedModules[chunkId] = &#123;&#125;;
    
    const promise = new Promise(function(resolve, reject) &#123;
      installedModules[chunkId].resolve = resolve;
    &#125;);
    
    return new Promise((res) => &#123;
      // 通过往head头部插入script标签异步加载到chunk代码
      const script = document.createElement('script');
      script.src = `$&#123;__webpack_require__.p&#125;$&#123;chunkId&#125;`;
  
      // 模块是否加载成功
      script.onload = () => &#123;
        installedModules[chunkId].installed = flag
        // 加载完了返回 chunkId 供外部拿到 modules
        res(chunkId);
      &#125;;
      // 插入 script 标签
      document.head.appendChild(script);
    &#125;);
  &#125;;
  
  // webpackJsonp 就是用来连接异步加载 chunk 和 modules 之间的方法
  // 通过 webpackJsonp 将 chunk 内的 module 插入到 modules 中，__webpack_require__ 去引用
  // 这个 module
  function webpackJsonpCallback(chunk) &#123;
    const chunkId = chunk[0]; // chunkId
    const modules = chunk[1]; // 该 chunk 包含的 module
    
    if (installedChunks[chunkId]) &#123;
      return;
    &#125;
  
    installedChunks[chunkId] = chunk;
    
    Object.entries(modules).forEach(([k, v]) => &#123;
      modules[k] = v;
    &#125;)
  &#125;
  
  const webpackJsonp =  window['webpackJsonp'] || [];
  webpackJsonp.push = webpackJsonpCallback;
  
  // 因为我们在 ``webpack`` config 内设置的 entry 入口是 './src/home'，所以在这我们赋值入口给 __webpack_require__.s，以备其他地方使用
  // 同时执行 __webpack_require__ 去加载 './src/home'
  return __webpack_require__(__webpack_require__.s = './src/home.vue')
&#125;

假如有这么一个 home.vue 组件，里面需要加载 Header 组件
/*
template
* <div>我是主页
*   <Header/>
* </div>

script

return &#123;
   name: 'Header',
   setup() &#123;
     console.log('im home')
   &#125;
&#125;

style
header &#123; background: green; &#125;
* */

const modules = &#123;
  './src/home.vue': function(module, __webpack_exports__, __webpack_require__) &#123;
    
    const loaders = &#123;
      './src/home.vue?vue-template-loader': function() &#123;
        // new Vue(xxx).mount('#app');
        const container = document.getElementById('app');
        // vue template 解析
        const ele = document.createElement('div');
        ele.innerText = '我是主页';
        container.appendChild(ele);
  
        // vue template 解析 Header 发现他是一个 module 引用，所以使用 __webpack_require__
        ele.appendChild(__webpack_require__('./src/header'));
  
        // 假如是一个异步加载的 chunk
        //__webpack_require__.e('./src/header').then(() => &#123;
            // todo ...
        //&#125;)
      &#125;,
      // 源码中是 css-loader 先将样式转为 css 然后再用 style loader 插入 head 内，这里为了简便合成一步
      './src/home.vue?style-loader?css-loader': function() &#123;
        const cssText = 'header &#123; background: green; &#125;';
        const style = document.createElement('style');
        style.innerHTML = cssText;
        document.getElementsByTagName('head')[0].appendChild(style);
      &#125;,
      './src/home.vue?babel-loader': function() &#123;
        console.log('im home')
        
        // 源码上是导出这个 Vue 实例对象, 例如
        // return &#123;
        //   name: 'Header',
        //   setup() &#123;
        //     console.log('im home')
        //   &#125;
        // &#125;
      &#125;
    &#125;
  
    Object.entries(loaders).forEach(([k, v]) => v());
  &#125;,
  './src/header': function(module, __webpack_exports__, __webpack_require__) &#123;
    const ele = document.createElement('header');
    ele.innerText = '我是头部';
    // 源码 vue 解析 template 的时候导出的是一个 render 函数，这里为了理解导出一个该 render 出来的元素
    module.exports = ele;
  &#125;
&#125;

// 异步模块
const asyncModule = () => &#123;
  window['webpackJsonp'].push(['1'], &#123;
    './src/page1': function(module, __webpack_exports__, __webpack_require__) &#123;
      const ele = document.createElement('main');
      ele.innerText = '我是 page1';
      module.exports = ele;
    &#125;
  &#125;)
&#125;

entry(modules);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">简单理解 <code>module federation</code> 原理</h2>
<p>比如我们现在有一个 <code>host</code> 3000， <code>remote</code> 3001 ，在 <code>host</code> 的 router 里面有</p>
<pre><code class="copyable">path: '/child',
name: 'ChildApp',
// ``host `` 去消费 ``remote`` childApp 名字里面的 ChildAppHome chunk
component: () => import('childApp/ChildAppHome'),
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 <code>remote</code> 应用暴露出 remoteEntry.js ，然后在 <code>host</code> 的 html 的顶部引入，在 remoteEntry 里有</p>
<pre><code class="copyable">window.childApp = &#123;
  moduleMap = &#123;
    "./ChildAppHome": () => &#123;
        return __webpack_require__.e("src_components_ChildHome_vue").then(() => () => (__webpack_require__( "./src/components/ChildHome.vue")));
     &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么 import('childApp/ChildAppHome') 就会被解析成在 window 下拿 childApp 这个对象，然后在这个对象里面，通过 ChildAppHome 这个标识找到的 chunkId 去到 3001上去加载这个 ChildAppHome 的 chunk，从而完成异步加载。</p>
<p>再者，share 的 <code>lib</code>，比如 vue 这些，打包出来的 <code>remote</code> chunk 里面肯定是不会有 vue 的代码，那么 chunk 里面的 vue 去哪里找，就只能是通过 <code>host</code> 和 <code>remote</code> 配置 <code>ModuleFederationPlugin</code>
的时候表明那些 <code>lib</code> 是共享，必须要配置，不然子应用就不知道怎么去找到 vue 然后渲染 <code>remote</code> chunk 里面的 vue 节点，在配置了 shared 之后，比如配置了 share vue 和 <code>vue-router</code> ，host
应用在加载的时候就会将 <code>host</code> 内原本将 vue 和 <code>vue-router</code>  打包在 <code>vendor</code> 里面的内容，拆分出来为：</p>
<pre><code class="copyable">vendors-node_modules_vue-router_dist_vue-router_esm_js.js
vendors-node_modules_vue_runtime-dom_dist_runtime-dom_esm-bundler_js.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如此 <code>remote</code> 就知道拿 vue 的时候去 share 的 <code>vendor</code> 里面拿了。</p>
<h2 data-id="heading-2">总结</h2>
<p>查阅了比较多文档，总结了本地的项目实践的出来的结论。在 mf 和异步加载这里可能和源码有出入，但也是尽可能地想把原理给白话出来，主要为了理解。</p></div>  
</div>
            