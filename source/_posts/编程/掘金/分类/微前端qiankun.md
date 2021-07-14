
---
title: '微前端qiankun'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05ba81246de546c2a39f7f09bdc0041e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 01:13:20 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05ba81246de546c2a39f7f09bdc0041e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h5 data-id="heading-0">1、目标</h5>
<ol>
<li>针对事业部前端开发业务场景考虑使用一个项目实例，通过微前端的方式去实现业务功能模块的解耦。</li>
<li>如果可以实现微应用之间、微应用和主应用之间如何处理通信，通信数量级别</li>
<li>加载复杂微应用的性能如何</li>
<li>微前端应用场景考虑</li>
</ol>
<h5 data-id="heading-1">2、什么是微前端</h5>
<pre><code class="copyable">Techniques, strategies and recipes for building a modern web app with multiple teams that can ship features independently. -- Micro Frontends

微前端是一种多个团队通过独立发布功能的方式来共同构建现代化 web 应用的技术手段及方法策略。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>微前端架构中，我们应该按业务划分出对应的子应用，而不是通过功能模块划分子应用。</p>
<ol>
<li>在微前端架构中，子应用并不是一个模块，而是一个独立的应用，我们将子应用按业务划分可以拥有更好的可维护性和解耦性。</li>
<li>子应用应该具备独立运行的能力，应用间频繁的通信会增加应用的复杂度和耦合度。</li>
</ol>
<p><em>微前端解决的问题</em></p>
<ul>
<li>主框架不限制接入应用的技术栈，微应用具备完全自主权</li>
<li>微应用仓库独立，前后端可独立开发，部署完成后主框架自动完成同步更新</li>
<li>在面对各种复杂场景时，我们通常很难对一个已经存在的系统做全量的技术栈升级或重构，而微前端是一种非常好的实施渐进式重构的手段和策略</li>
<li>每个微应用之间状态隔离，运行时状态不共享-</li>
</ul>
<p><em>微前端解决方案</em></p>
<h6 data-id="heading-2">2.1、嵌套 iframe</h6>
<ul>
<li>浏览器历史栈问题前进/后退无论你在iframe里潜行了多深，你退一步就是一万步，这个体验真的很难受</li>
<li>iframe 应用更新上线后，打开系统会发现系统命中缓存显示旧内容，需要用时间戳方案解决或强制刷新</li>
<li>有时候主应用可能只想知道子系统的 URL 参数，但是 iframe 应用跟它不同源，你就得想点其他办法去获取参数了，我们最常用的就是 postMessage 了</li>
</ul>
<h6 data-id="heading-3">2.2、MPA + 路由分发</h6>
<p>优点：</p>
<ol>
<li>多框架开发</li>
<li>独立部署</li>
<li>应用完全隔离</li>
</ol>
<p>缺点：</p>
<ol>
<li>体验差，每个独立应用加载时间较长</li>
<li>因为完全隔离，导致在导航、顶部这些通用的地方改动大，复用性变的很差。</li>
</ol>
<h6 data-id="heading-4">2.3、基座模式</h6>
<p>基于路由分发，由一个基座应用监听路由，按照路由规则去加载不同的应用，以实现应用间解耦</p>
<h6 data-id="heading-5">2.4、Webpack5 Module Federation</h6>
<p>去中心化的微前端方案，可以在实现应用隔离的基础上，轻松实现应用间的资源共享和通信</p>
<h5 data-id="heading-6">3、什么是qiankun</h5>
<p>qiankun 是一个基于 single-spa 的微前端实现库，旨在帮助大家能更简单、无痛的构建一个生产可用微前端架构系统。</p>
<h6 data-id="heading-7">3.1、目前已使用qiankun的团队</h6>
<ol>
<li>美团</li>
<li>网易</li>
<li>蚂蚁金服</li>
</ol>
<h6 data-id="heading-8">3.2、优势</h6>
<ol>
<li>基于 single-spa 封装，提供了更加开箱即用的 API</li>
<li>技术栈无关，任意技术栈的应用均可 使用/接入</li>
<li>HTML Entry 接入方式，让你接入微应用像使用 iframe 一样简单</li>
<li>样式隔离，确保微应用之间样式互相不干扰</li>
<li>JS 沙箱，确保微应用之间 全局变量/事件 不冲突</li>
<li>资源预加载，在浏览器空闲时间预加载未打开的微应用资源，加速微应用打开速度</li>
</ol>
<p><em>微应用不宜拆分过细，建议按照业务域来做拆分。业务关联紧密的功能单元应该做成一个微应用，反之关联不紧密的可以考虑拆分成多个微应用。 一个判断业务关联是否紧密的标准：看这个微应用与其他微应用是否有频繁的通信需求。如果有可能说明这两个微应用本身就是服务于同一个业务场景，合并成一个微应用可能会更合适。</em></p>
<h5 data-id="heading-9">4、qiankun通信方式总结</h5>
<p><strong>基于vue主应用、react、vue子应用交互的例子</strong>：</p>
<h6 data-id="heading-10">4.1、第一种方式</h6>
<p>4.1.1、map实例化后赋值给组件data数据</p>
<pre><code class="copyable">this.map = new minemap.Map
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.1.2、通过qiankun提供的setGlobalState接口通信</p>
<pre><code class="copyable">actions.setGlobalState(&#123; map: this.map &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子应用可获取到相应的map实例，但在调用该接口时页面卡顿严重，（map实例属性比较多）；可以获取到地图相关属性，但是设置属性不生效</p>
<h6 data-id="heading-11">4.2、第二种方式</h6>
<p>实例化地图组件的时候直接赋值给window变量，子应用通过监听事件onGlobalStateChange触发地图交互</p>
<p>伪代码：</p>
<pre><code class="copyable">window.map = new minemap.Map
<!--actions触发子应用监听事件执行业务逻辑-->
actions.setGlobalState(&#123; map: 'this.map' &#125;)
<!--子应用-->
props.onGlobalStateChange((state, prev) => &#123;
// state: 变更后的状态; prev 变更前的状态
console.log(state, prev);
var center = window.map.getCenter();
window.map.flyTo(&#123;
      center: [center.lng + (Math.random() - 0.5) * 0.2,
          center.lat + (Math.random() - 0.5) * 0.2],
      zoom: 14,
      bearing: 10,
      pitch: 30,
      duration: 2000
  &#125;);
&#125;, true);

<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.3、第三种通过应用之间的通信方式进行交互不需要来回传递数据GlobalState</p>
<pre><code class="copyable">    // 主应用初始化数据
    const initialState = &#123; actions: null, data: null &#125;
    //actions用于区分各种交互动作
    // 子应用
    actions.setGlobalState(&#123; actions: 'setBearing', data: 90 &#125;)
    // 主应用
    actions.onGlobalStateChange((state, prevState)=>&#123;
        // console.log('主应用', state, prevState)
        // 根据不同的actions处理不同交互逻辑
        if(state.actions === 'setZoom')&#123;
            this.map.setZoom(state.data)
        &#125;
        if(state.actions === 'setBearing')&#123;
            this.map.setBearing(state.data)
        &#125;
    &#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05ba81246de546c2a39f7f09bdc0041e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
4.4、通过全局的window实现发布订阅模式</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25c0761593814e829bdf0dcb9f72342b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
4.4.1. 借助CustomEvent对象</p>
<pre><code class="copyable">// 创建事件对象
    let event = new CustomEvent('custom', &#123;
        // 这里可直接传入 自定义的事件参数
        detail: &#123;
            height: 100,
            widht: 100,
            rect: 10000
        &#125;
    &#125;)
    // 同样 我们也可以直接在事件对象上绑定 参数
    vent.name = 'custom-event'
    window.dispatchEvent(event)
    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.4.2. 自定义类实现发布订阅模式</p>
<p><em>通过window共享类</em></p>
<p>4.5、通过postmessage方式</p>
<pre><code class="copyable">/**
 * 监听事件
 * @param &#123;*&#125; callback
 */
export function on(callback = () => &#123;&#125;) &#123;
  window.addEventListener(
    'message',
    (event, ...arg) => &#123;
      // 解析数据，将object进行JSON
      let &#123; type, payload &#125; = event?.data || &#123;&#125;
      if (type && payload) &#123;
        // json
        try &#123;
          event.data.payload = JSON.parse(payload)
        &#125; catch (error) &#123;&#125;
      &#125;
      callback(event, ...arg)
    &#125;,
    false
  )
&#125;

/**
 * 派发事件
 * @param &#123;*&#125; data 数据
 * @param &#123;*&#125; origin  目标地址 默认location.origin
 * @param &#123;*&#125; source 派发数据源 默认window
 */
export function emit(data, origin, source) &#123;
  // 解析数据，将object进行JSON
  let &#123; type, payload &#125; = data || &#123;&#125;
  if (type && payload && typeof payload === 'object') &#123;
    // json
    data.payload = JSON.stringify(payload)
  &#125;
  ;(source || window).postMessage(data, origin || window.location.origin)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.6、以上解决办法适合通信较少的业务场景，状态池无法跟踪，通信场景较多时，容易出现状态混乱、维护困难等问题；
优点：</p>
<ul>
<li>子应用无法随意污染主应用的状态池，只能通过主应用暴露的 shared 实例的特定方法操作状态池，从而避免状态池污染产生的问题。</li>
<li>子应用将具备独立运行的能力</li>
</ul>
<p>缺点：</p>
<ul>
<li>暂时没有想到。。。。</li>
</ul>
<p>4.6.1父子应用共用store</p>
<pre><code class="copyable">//step1：主应用向微应用传递store实例
&#123;
    name: "chai-project",
    entry: "//localhost:8080",
    container: '#yourContainer',
    activeRule: "/chaiQiankunTest/ffff",
    props: &#123;
          store //共享主应用的store实例
      &#125;
&#125;
//step2:微应用使用主应用共享的store实例
import Vuex from 'vuex'
Vue.use(Vuex);
function render (props) &#123;
  const store = props.store;

  // 挂载应用
  new Vue(&#123;
    store,//主应用共享的store实例
    render: (h) => h(App)
  &#125;).$mount('#app');
&#125;
//step3：验证主应用和微应用之间是否可以完成通信，状态同步。
//不论是点击主应用的按钮，还是点击微应用的按钮，主应用的computed属性成功被触发，微应用始终未能正常监听到状态值得改变，computed属性从未被触发。
//在微应用中将共享的store实例进行响应式设置，这是Vue现有的API方法Vue.observable(store)
//如此处理之后，不论主应用还是微应用中，修改共享store的state状态值，在主应用和微应用中都能够实时感知，并对其做出响应的反馈

<span class="copy-code-btn">复制代码</span></code></pre>
<p>4.6.2父子应用store分离方案
这里基于父应用已经共享自己的store，并且主应用和子应用之间已经能够完成对于主应用的state状态变化的响应。</p>
<pre><code class="copyable">Vue.prototype.microStore = microStore;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子应用的各个页面都能够通过this.microStore访问自身的store</p>
<hr>
<h5 data-id="heading-12">5、实践案例中发现的问题（主应用基座vue2.，子应用分别为react、vue2.）</h5>
<p>5.1、在开发环境中react子应用的热刷新存在bug加载子应用后子应用的ws会请求到主应用导致主应用挂掉</p>
<p>解决办法：</p>
<ol>
<li>通过配置子应用取消热更新</li>
<li>单独指定子应用热更新请求端口（实践未成功）</li>
</ol>
<p>5.2、在主应用的某个路由下渲染页面需要将路由设置成以下形式重点在 <strong>*</strong></p>
<pre><code class="copyable">const routes = [
  &#123;
    path: '/portal/*',
    name: 'portal',
    component: () => import('../views/Portal.vue'),
  &#125;,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.3、调用qiankun的onGlobalStateChange接口监听不到时需要设置第二个参数为true</p>
<p>5.4、子应用调用setGlobalState的参数必须在主应用初始化的时候声明了</p>
<p>5.5、create-react-app生成的项目ie11加载失败 （脚手架生成项目默认不再支持ie11）</p>
<p>解决办法：</p>
<pre><code class="copyable">// 1、npm install -S react-app-polyfill
// 2、入口文件头部引入
import './public-path';
import 'react-app-polyfill/ie11';
// 3、修改package.json 或者.browserslistrc文件有关支持浏览器配置
"browserslist": &#123;
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all",
      "ie 11"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version",
      "ie 11"
    ]
  &#125;,

<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.6、加载vue-cli2.x版本生成的vue2.0项目报错信息：</p>
<pre><code class="copyable">Application died in status LOADING_SOURCE_CODE: You need to export the functional lifecycles in xxx entry
问题原因：入口js文件没有在html的最后引入

<script src="/antd.js"></script>
<script src="/appEntry.js"></script>
<script src="https://www.google.com/analytics.js"></script>
解决办法：
通过htmlwebpackplugin的chunksSortMode选项控制引入chunk顺序
'dependency' 不用说，按照不同文件的依赖关系来排序。
'auto' 默认值，插件的内置的排序方式，具体顺序这里我也不太清楚...
'none' 默认无序
&#123;function&#125; 提供一个函数
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.7、主应用开启严格样式隔离的情况下</p>
<pre><code class="copyable">startQiankun(&#123;
      sandbox: &#123; strictStyleIsolation: true &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子应用使用document会报错
子应用在加载 font-face，还有svg不生效、事件代理等问题
shadow dom 实践下来并不是可以开箱即用的方案，建议现阶段用 experimentalStyleIsolation 来解决样式隔离问题类似 scoped style 的思路</p>
<p>官方回复：shadow dom 后续版本不再推荐</p>
<p>5.8、strictStyleIsolation: true下子应用使用iconfont.js引入的图标丢失<br>
同问题七</p>
<p>5.9、qiankun默认情况下微应用之间样式是隔离的，主应用与微应用之间的样式隔离可以通过手动方式进行处理</p>
<p>5.10、在设置默认挂载时需要注意微应用的 activeRule 需要包含主应用的这个路由 path相应子应用base选项也需要修改成基于此activeRule</p>
<pre><code class="copyable">setDefaultMountApp(appLink)
activeRule: '/apps/app-vue',
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.11、activeRule不能直接调用函数类似vueApp子应用</p>
<pre><code class="copyable">const isActive = (location) => location.pathname.includes('/MApps')
export const apps = [
  &#123;
    name: 'reactIe',
    entry: '//localhost:3000',
    container: '#container',
    activeRule: () => isActive(location)
  &#125;,
  &#123;
    name: 'vueApp',
    entry: '//localhost:8088',
    container: '#container',
    activeRule: isActive(location)
  &#125;
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.12、同时激活两个微应用的</p>
<ol>
<li>必须将单实例模式关闭</li>
</ol>
<pre><code class="copyable">singular: false
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>子应用baseurl必须为主应用对应的路由</li>
</ol>
<pre><code class="copyable">vue设置：
base: window.__POWERED_BY_QIANKUN__ ? '/MApps' : '/',
react设置：
<Router basename=&#123;window.__POWERED_BY_QIANKUN__ ? '/MApps' : '/'&#125;>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>同时激活两个微应用的情况下两个微应用的路由必须同步否则会出现子应用无内容渲染的情况</em></p>
<p>5.13、渲染同一个微应用的不同子页面需要在主应用配置路由跳转</p>
<pre><code class="copyable"><el-menu :default-active="$route.path" router class="el-menu-vertical-demo" :collapse="isCollapse">
    <el-submenu index="/app-vue/">
        <template slot="title">
            <i class="el-icon-location"></i>
            <span slot="title">vue子应用</span>
        </template>
        <el-menu-item-group>
            <span slot="title">分组一</span>
            <el-menu-item index="/app-vue/">vue子应用主页面</el-menu-item>
            <el-menu-item index="/app-vue/line">vue子应用主line页面</el-menu-item>
        </el-menu-item-group>
    </el-submenu>
 </el-menu>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.14、实现以组件形式手动渲染微应用</p>
<pre><code class="copyable"><template>
  <div class="micro-wrap">
    <div ref="qiankun"></div>
  </div>
</template>

<script>
import &#123; loadMicroApp &#125; from 'qiankun'
export default &#123;
  props: &#123;
    name: &#123;
      type: String,
      default: 'app'
    &#125;,
    entry: &#123;
      type: String,
      require: true
    &#125;,
    propData: &#123;
      type: Object,
      default: () => &#123;&#125;
    &#125;
  &#125;,
  data () &#123;
    return &#123;
      microApp: null
    &#125;
  &#125;,
  mounted () &#123;
    this.microApp = loadMicroApp(&#123;
      name: this.name,
      entry: this.entry,
      container: this.$refs.qiankun
    &#125;)
  &#125;,
  updated () &#123;
    this.microApp.updated(this.propData)
  &#125;,
  beforeDestroy () &#123;
    this.microApp.unmount()
  &#125;
&#125;
</script>

<style lang="scss" scoped>
  .micro-wrap&#123;
    width: 50vw;
    height: 50vh;
    overflow: hidden;
  &#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.15 qiankun子应用路由跳转不影响主应用路由需设置子应用路由模式</p>
<pre><code class="copyable">mode: 'abstract',
// 该模式下路由  ‘/’不会主动加载需要在实例化vue之后设置
router.push(data.defaultPath);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.16 主应用加载子应用不同路由页面设置</p>
<pre><code class="copyable">// 主应用设置通过props告诉子应用要加载的页面
loadMicroApp(&#123;
      name: 'app-vue-hash', 
      entry: 'http://localhost:1111', 
      container: '#appContainer1', 
      props: &#123; data : &#123; defaultPath: '/about' &#125; &#125;
    &#125;);
    loadMicroApp(&#123;
      name: 'app-vue-hash', 
      entry: 'http://localhost:1111', 
      container: '#appContainer2', 
      props: &#123; data : &#123; defaultPath: '/' &#125; &#125;
    &#125;)
// 子应用默认路由跳转设置
function render(&#123; data = &#123;&#125; , container &#125; = &#123;&#125;) &#123;
  router = new VueRouter(&#123;
    mode: 'abstract',
    routes,
  &#125;);
  instance = new Vue(&#123;
    router,
    store,
    render: h => h(App),
  &#125;).$mount(container ? container.querySelector('#appVueHash') : '#appVueHash');
  if (data?.defaultPath) &#123;
    router.push(data.defaultPath);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>#####6、总结</p>
<ol>
<li>ie下不支持多实例，没有办法做到一个页面同时加载两个子应用</li>
<li>在开箱即用上上手难度不大</li>
<li>qiankun重点关注的是技术栈无关的价值。所以在应用交互上的支持不多，数据交互较大的需求背景下需要根据自己的实际应用场景进行通信方式的选择（目前官方只有全局的state api 没有事件交互api）</li>
<li>目前两种使用qiankun的方式路由的方式和组件的方式组件的方式更加灵活</li>
</ol></div>  
</div>
            