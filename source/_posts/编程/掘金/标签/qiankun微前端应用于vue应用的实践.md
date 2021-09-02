
---
title: 'qiankun微前端应用于vue应用的实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c2029c71cb2404281626d18c5d651fe~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 00:28:31 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c2029c71cb2404281626d18c5d651fe~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h1 data-id="heading-0">前言✨</h1>
<p>本文介绍了用qiankun微前端框架用来集成vue应用的基本方案以及集成过程中遇到的一些常见问题。</p>
<h1 data-id="heading-1">一、基本使用</h1>
<h2 data-id="heading-2">主应用</h2>
<p>1.先安装 <code>qiankun</code> ：</p>
<pre><code class="copyable">$ yarn add qiankun # 或者 npm i qiankun -S
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.注册微应用并启动：</p>
<pre><code class="copyable">import &#123; registerMicroApps, start &#125; from 'qiankun'

/**
 * step1 注册微应用
 */
registerMicroApps([
  &#123;
    name: 'child-vue2', // 注册应用名
    entry: '//localhost:7012',// 注册服务
    container: '#sub-container', // 挂载的容器
    activeRule: '/vue2', // 路由匹配规则
  &#125;,
  &#123;
    name: 'child-vue3',
    entry: '//localhost:7013',
    container: '#sub-container',
    activeRule: '/vue3',
  &#125;
])

/**
 * Step2 设置默认进入的子应用（可选）
 */
setDefaultMountApp('/')

/**
 * Step3 启动qiankun应用
 */
start()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">微应用</h2>
<h3 data-id="heading-4">Vue 微应用</h3>
<p>微应用不需要额外安装任何其他依赖即可接入 qiankun 主应用。</p>
<p>以 <code>vue 2.x</code> 项目为例</p>
<ol>
<li>
<p>在 <code>src</code> 目录新增 <code>public-path.js</code>，并在<code>main.js</code>最顶部引入 <code>public-path.js</code></p>
<pre><code class="copyable">if (window.__POWERED_BY_QIANKUN__) &#123;
  __webpack_public_path__ = window.__INJECTED_PUBLIC_PATH_BY_QIANKUN__;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>微应用建议使用 <code>history</code> 模式的路由，需要设置路由 <code>base</code>，值和它的 <code>activeRule</code> 是一样的</p>
</li>
</ol>
<pre><code class="copyable">const router = new VueRouter(&#123;
  mode: 'history',
  base: window.__POWERED_BY_QIANKUN__ ? '/vue2' : '/',
  routes
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>
<p>在入口文件<code>main.js</code>中修改并导出<code>bootstrap</code>、<code>mount</code>、<code>unmount</code>三个生命周期函数，保证微应用单独运行且能在qiankun环境中运行。为了避免根 id <code>#app</code> 与其他的 DOM 冲突，需要限制查找范围。</p>
<pre><code class="copyable">import './public-path'
import Vue from 'vue'
import App from './App.vue'
import routes from './router'
import store from './store'

Vue.config.productionTip = false

let instance = null
function render(props = &#123;&#125;) &#123;
  const &#123; container &#125; = props
  instance = new Vue(&#123;
    router,
    store,
    render: (h) => h(App)
  &#125;).$mount(container ? container.querySelector('#app') : '#app')
&#125;

// 独立运行微应用时
if (!window.__POWERED_BY_QIANKUN__) &#123;
  render()
&#125;

export async function bootstrap() &#123;
  console.log('[vue] vue app bootstraped')
&#125;

// 在qiankun中运行时
export async function mount(props) &#123;
  render(props)
&#125;

export async function unmount() &#123;
  instance.$destroy()
  instance.$el.innerHTML = ''
  instance = null
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>修改 <code>webpack</code> 打包，允许开发环境跨域和 <code>umd</code> 打包（<code>vue.config.js</code>）：</p>
<pre><code class="copyable">const &#123; name &#125; = require('./package');
module.exports = &#123;
  devServer: &#123;
    headers: &#123;
      'Access-Control-Allow-Origin': '*',
    &#125;,
  &#125;,
  configureWebpack: &#123;
    output: &#123;
      library: `$&#123;name&#125;-[name]`,
      libraryTarget: 'umd', // 把微应用打包成 umd 库格式
      jsonpFunction: `webpackJsonp_$&#123;name&#125;`,
    &#125;,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<h1 data-id="heading-5">二、细节</h1>
<h3 data-id="heading-6">1.生命周期</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c2029c71cb2404281626d18c5d651fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">2.样式隔离</h3>
<p>样式隔离，需在启动主应用时加上以下配置：</p>
<pre><code class="copyable">start(&#123;sandbox: &#123;strictStyleIsolation: true&#125;&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是此种情况下，父应用的body样式会被子应用继承，要使子应用原来的body样式生效，需把子应用的body样式拷贝出来挂在#app节点下（可单独提取成一个css文件），当子应用走qiankun的逻辑时加载</p>
<pre><code class="copyable">export async function mount(props) &#123;
  require('./style/config.css')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>基于 ShadowDOM 的严格样式隔离并不是一个可以无脑使用的方案，大部分情况下都需要接入应用做一些适配后才能正常在 ShadowDOM 中运行起来。</p>
</blockquote>
<h4 data-id="heading-8">fix shadow dom</h4>
<ul>
<li>getComputedStyle</li>
</ul>
<p>当获取shadow dom的计算样式的时候传入的element是DocumentFragment，会报错。</p>
<pre><code class="copyable">// 解决报错问题
const getComputedStyle = window.getComputedStyle;
window.getComputedStyle = (el, ...args) => &#123;
  // 如果为shadow dom则直接返回
  if (el instanceof DocumentFragment) &#123;
    return &#123;&#125;;
  &#125;
  return Reflect.apply(getComputedStyle, window, [el, ...args]);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>elementFromPoint</li>
</ul>
<p>根据坐标（x, y）当获取一个子应用的元素的时候，会返回shadow root，并不会返回真正的元素。</p>
<pre><code class="copyable">const elementFromPoint = document.elementFromPoint;
document.elementFromPoint = function (x, y) &#123;
  const result = Reflect.apply(elementFromPoint, this, [x, y]);
  // 如果坐标元素为shadow则用该shadow再次获取
  if (result && result.shadowRoot) &#123;
    return result.shadowRoot.elementFromPoint(x, y);
  &#125;
  return result;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>document 事件 target 为 shadow</li>
</ul>
<p>当我们在document添加click、mousedown、mouseup等事件的时候，回调函数中的event.target不是真正的目标元素，而是shadow root元素。</p>
<pre><code class="copyable">// fix: 点击事件target为shadow元素的问题
const &#123;addEventListener: oldAddEventListener, removeEventListener: oldRemoveEventListener&#125; = document;
const fixEvents = ['click', 'mousedown', 'mouseup'];
const overrideEventFnMap = &#123;&#125;;
const setOverrideEvent = (eventName, fn, overrideFn) => &#123;
  if (fn === overrideFn) &#123;
    return;
  &#125;
  if (!overrideEventFnMap[eventName]) &#123;
    overrideEventFnMap[eventName] = new Map();
  &#125;
  overrideEventFnMap[eventName].set(fn, overrideFn);
&#125;;
const resetOverrideEvent = (eventName, fn) => &#123;
  const eventFn = overrideEventFnMap[eventName]?.get(fn);
  if (eventFn) &#123;
    overrideEventFnMap[eventName].delete(fn);
  &#125;
  return eventFn || fn;
&#125;;
document.addEventListener = (event, fn, options) => &#123;
  const callback = (e) => &#123;
    // 当前事件对象为qiankun盒子，并且当前对象有shadowRoot元素，则fix事件对象为真实元素
    if (e.target.id?.startsWith('__qiankun_microapp_wrapper') && e.target?.shadowRoot) &#123;
      fn(&#123;...e, target: e.path[0]&#125;);
      return;
    &#125;
    fn(e);
  &#125;;
  const eventFn = fixEvents.includes(event) ? callback : fn;
  setOverrideEvent(event, fn, eventFn);
  Reflect.apply(oldAddEventListener, document, [event, eventFn, options]);
&#125;;
document.removeEventListener = (event, fn, options) => &#123;
  const eventFn = resetOverrideEvent(event, fn);
  Reflect.apply(oldRemoveEventListener, document, [event, eventFn, options]);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">3.history模式下<code>publicPath</code>不能使用相对路径，需使用绝对路径</h3>
<p>主应用需配置</p>
<pre><code class="copyable">publicPath:'/'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">4.应用间的通信</h3>
<p>qiankun提供了<code>initGlobalState</code> <code>onGlobalStateChange</code> <code>setGlobalState</code>用于通信。</p>
<p>主应用我们可以直接导入</p>
<pre><code class="copyable">import &#123; initGlobalState &#125; from 'qiankun'
// 初始化全局变量
const &#123; onGlobalStateChange, setGlobalState &#125; = initGlobalState(&#123;
  user: 'qiankun'
&#125;)

// 把监测变量改变和改变状态挂载到Vue上
Vue.prototype.$onGlobalStateChange = onGlobalStateChange
Vue.prototype.$setGlobalState = setGlobalState

// 监测变量改变
onGlobalStateChange((value, prev) => console.log('[onGlobalStateChange - master]:', value, prev),true)

// 改变全局变量
setGlobalState(&#123;
  user: 'master'
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子应用我们需在生命周期里把<code>onGlobalStateChange</code> <code>setGlobalState</code>挂载到子应用的vue对象上：</p>
<pre><code class="copyable">export async function mount(props) &#123;
    Vue.prototype.$onGlobalStateChange = props.onGlobalStateChange
    Vue.prototype.$setGlobalState = props.setGlobalState
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">5.如何在主应用的多级嵌套路由页面下加载微应用</h3>
<p>主应用注册这个路由时给 <code>path</code> 加一个 <code>*</code>，使其在未匹配到主应用的某个页面时，也能加载主应用的外框，确保子应用要挂载的容易存在。</p>
<pre><code class="copyable">import empty from "./../empty"

export default &#123;
  path: '/app',
  name: 'AppLayout',
  component: AppLayout,
  children: [&#123;
    path: "manage",
    name: 'AppManage',
    component: Manage,
  &#125;,&#123;
    path: "*",
    name: 'empty',
    component: empty //空的div标签
  &#125;]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外在注册微应用时，<code>activeRule</code> 需要包含主应用的这个路由 <code>path</code></p>
<pre><code class="copyable">registerMicroApps([
  &#123;
    name: 'website', // 注册应用名
    entry: '//localhost:8888',// 注册服务
    container: '#con', // 挂载的容器
    activeRule: '/app/website', // 路由匹配规则
  &#125;
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子应用的路由注册时<code>base</code>也需要加上这个<code>path</code></p>
<pre><code class="copyable">function render(props = &#123;&#125;) &#123;
  const &#123;container&#125; = props
  router = new VueRouter(&#123;
    mode: 'history',
    base: container ? /app/website : '/',
    routes
  &#125;)
  instance = new Vue(&#123;
    router,
    render: h => h(App)
  &#125;).$mount(container ? container.querySelector('#app') : '#app')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            