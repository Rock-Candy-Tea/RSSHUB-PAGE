
---
title: '_源码-react01_ ReactDOM.render01'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89e3cd5025c84d3c96454c632441b845~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 08 Aug 2021 00:57:19 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89e3cd5025c84d3c96454c632441b845~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89e3cd5025c84d3c96454c632441b845~tplv-k3u1fbpfcp-watermark.image" alt="ReactDOM.render.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">导航</h1>
<p><a href="https://juejin.im/post/6844904045342113799" target="_blank" title="https://juejin.im/post/6844904045342113799">[react] Hooks</a></p>
<p><a href="https://juejin.cn/post/6950958974854234119" target="_blank" title="https://juejin.cn/post/6950958974854234119">[封装01-设计模式] 设计原则 和 工厂模式(简单抽象方法)  适配器模式 装饰器模式</a><br>
<a href="https://juejin.cn/post/6950958974854234119" target="_blank" title="https://juejin.cn/post/6950958974854234119">[封装02-设计模式] 命令模式 享元模式 组合模式 代理模式</a></p>
<p><a href="https://juejin.im/post/6879020830253285384" target="_blank" title="https://juejin.im/post/6879020830253285384">[React 从零实践01-后台] 代码分割</a><br>
<a href="https://juejin.im/post/6881481205657632781" target="_blank" title="https://juejin.im/post/6881481205657632781">[React 从零实践02-后台] 权限控制</a><br>
<a href="https://juejin.im/post/6887132776512880654" target="_blank" title="https://juejin.im/post/6887132776512880654">[React 从零实践03-后台] 自定义hooks</a><br>
<a href="https://juejin.im/post/6892390655126241287" target="_blank" title="https://juejin.im/post/6892390655126241287">[React 从零实践04-后台] docker-compose 部署react+egg+nginx+mysql</a><br>
<a href="https://juejin.cn/post/6897884843275714567" target="_blank" title="https://juejin.cn/post/6897884843275714567">[React 从零实践05-后台] Gitlab-CI使用Docker自动化部署</a></p>
<p><a href="https://juejin.im/post/6844904115265339406" target="_blank" title="https://juejin.im/post/6844904115265339406">[源码-webpack01-前置知识] AST抽象语法树</a><br>
<a href="https://juejin.im/post/6844904115269550087" target="_blank" title="https://juejin.im/post/6844904115269550087">[源码-webpack02-前置知识] Tapable</a><br>
<a href="https://juejin.im/post/6844903973002936327" target="_blank" title="https://juejin.im/post/6844903973002936327">[源码-webpack03] 手写webpack - compiler简单编译流程</a><br>
<a href="https://juejin.im/post/6844904137952329742" target="_blank" title="https://juejin.im/post/6844904137952329742">[源码] Redux React-Redux01</a><br>
<a href="https://juejin.im/post/6844904147532120072" target="_blank" title="https://juejin.im/post/6844904147532120072">[源码] axios </a><br>
<a href="https://juejin.im/post/6844904166293241863" target="_blank" title="https://juejin.im/post/6844904166293241863">[源码] vuex </a><br>
<a href="https://juejin.im/post/6844904181094957069" target="_blank" title="https://juejin.im/post/6844904181094957069">[源码-vue01] data响应式 和 初始化渲染 </a><br>
<a href="https://juejin.im/post/6844904184035147790" target="_blank" title="https://juejin.im/post/6844904184035147790">[源码-vue02] computed 响应式 - 初始化，访问，更新过程 </a><br>
<a href="https://juejin.im/post/6844904186652409863" target="_blank" title="https://juejin.im/post/6844904186652409863">[源码-vue03] watch 侦听属性 - 初始化和更新 </a><br>
<a href="https://juejin.im/post/6844904190918000654" target="_blank" title="https://juejin.im/post/6844904190918000654">[源码-vue04] Vue.set 和 vm.$set</a><br>
<a href="https://juejin.im/post/6844904201944825863" target="_blank" title="https://juejin.im/post/6844904201944825863">[源码-vue05] Vue.extend</a></p>
<p><a href="https://juejin.im/post/6847902219107303438" target="_blank" title="https://juejin.im/post/6847902219107303438">[源码-vue06] Vue.nextTick 和 vm.$nextTick</a><br>
<a href="https://juejin.cn/post/6993980489463758855" target="_blank" title="https://juejin.cn/post/6993980489463758855">[源码-react01] ReactDOM.render01</a></p>
<p><a href="https://juejin.im/post/6844904095464030215" target="_blank" title="https://juejin.im/post/6844904095464030215">[部署01] Nginx</a><br>
<a href="https://juejin.im/post/6844904099024994312" target="_blank" title="https://juejin.im/post/6844904099024994312">[部署02] Docker 部署vue项目</a><br>
<a href="https://juejin.im/post/6844904103944912904" target="_blank" title="https://juejin.im/post/6844904103944912904">[部署03] gitlab-CI</a></p>
<p><a href="https://juejin.cn/post/6907145602400780296/" target="_blank" title="https://juejin.cn/post/6907145602400780296/">[数据结构和算法01]  二分查找和排序</a></p>
<p><a href="https://juejin.im/post/6844904046050934792" target="_blank" title="https://juejin.im/post/6844904046050934792">[深入01] 执行上下文</a><br>
<a href="https://juejin.im/post/6844904048873701389" target="_blank" title="https://juejin.im/post/6844904048873701389">[深入02] 原型链</a><br>
<a href="https://juejin.im/post/6844904050895372295" target="_blank" title="https://juejin.im/post/6844904050895372295">[深入03] 继承</a><br>
<a href="https://juejin.im/post/6844904051562250254" target="_blank" title="https://juejin.im/post/6844904051562250254">[深入04] 事件循环</a><br>
<a href="https://juejin.im/post/6844904052879261710" target="_blank" title="https://juejin.im/post/6844904052879261710">[深入05]  柯里化 偏函数 函数记忆</a><br>
<a href="https://juejin.im/post/6844904052937981959" target="_blank" title="https://juejin.im/post/6844904052937981959">[深入06]  隐式转换 和 运算符</a><br>
<a href="https://juejin.im/post/6844904053013479432" target="_blank" title="https://juejin.im/post/6844904053013479432">[深入07]  浏览器缓存机制（http缓存机制）</a><br>
<a href="https://juejin.im/post/6844904053235793927" target="_blank" title="https://juejin.im/post/6844904053235793927">[深入08]  前端安全</a><br>
<a href="https://juejin.im/post/6844904053764259854" target="_blank" title="https://juejin.im/post/6844904053764259854">[深入09]  深浅拷贝</a><br>
<a href="https://juejin.im/post/6844904054330490894" target="_blank" title="https://juejin.im/post/6844904054330490894">[深入10]  Debounce Throttle</a><br>
<a href="https://juejin.im/post/6844904054846390279" target="_blank" title="https://juejin.im/post/6844904054846390279">[深入11] 前端路由</a><br>
<a href="https://juejin.im/post/6844904056557682701" target="_blank" title="https://juejin.im/post/6844904056557682701">[深入12] 前端模块化</a><br>
<a href="https://juejin.im/post/6844904058604486663" target="_blank" title="https://juejin.im/post/6844904058604486663">[深入13] 观察者模式 发布订阅模式 双向数据绑定</a><br>
<a href="https://juejin.im/post/6844904063029477389" target="_blank" title="https://juejin.im/post/6844904063029477389">[深入14] canvas</a><br>
<a href="https://juejin.im/post/6844904066808561677" target="_blank" title="https://juejin.im/post/6844904066808561677">[深入15] webSocket</a><br>
<a href="https://juejin.im/post/6844904070201753608" target="_blank" title="https://juejin.im/post/6844904070201753608">[深入16] webpack</a><br>
<a href="https://juejin.im/post/6844904085750038542" target="_blank" title="https://juejin.im/post/6844904085750038542">[深入17] http 和 https</a><br>
<a href="https://juejin.im/post/6844904090644774926" target="_blank" title="https://juejin.im/post/6844904090644774926">[深入18] CSS-interview</a><br>
<a href="https://juejin.im/post/6844903823429861389" target="_blank" title="https://juejin.im/post/6844903823429861389">[深入19] 手写Promise</a><br>
<a href="https://juejin.im/post/6844904131577004040" target="_blank" title="https://juejin.im/post/6844904131577004040">[深入20] 手写函数</a><br>
<a href="https://juejin.cn/post/6907145602400780296/" target="_blank" title="https://juejin.cn/post/6907145602400780296/">[深入21] 数据结构和算法 - 二分查找和排序</a><br>
<a href="https://juejin.cn/post/6911192116651622413" target="_blank" title="https://juejin.cn/post/6911192116651622413">[深入22] js和v8垃圾回收机制</a><br>
<a href="https://juejin.cn/post/6918744081460002824" target="_blank" title="https://juejin.cn/post/6918744081460002824">[深入23] JS设计模式 - 代理，策略，单例</a><br>
<a href="https://juejin.cn/post/6983570939342487565" target="_blank" title="https://juejin.cn/post/6983570939342487565">[深入24] Fiber</a></p>
<p><a href="https://juejin.cn/post/6927306093970325517" target="_blank" title="https://juejin.cn/post/6927306093970325517">[前端学java01-SpringBoot实战] 环境配置和HelloWorld服务</a><br>
<a href="https://juejin.cn/post/6929145638898794503" target="_blank" title="https://juejin.cn/post/6929145638898794503">[前端学java02-SpringBoot实战] mybatis + mysql 实现歌曲增删改查</a><br>
<a href="https://juejin.cn/post/6930627377101979662" target="_blank" title="https://juejin.cn/post/6930627377101979662">[前端学java03-SpringBoot实战] lombok，日志，部署</a><br>
<a href="https://juejin.cn/post/6932097247735709709" target="_blank" title="https://juejin.cn/post/6932097247735709709">[前端学java04-SpringBoot实战] 静态资源 + 拦截器 + 前后端文件上传</a><br>
<a href="https://juejin.cn/post/6933224825200574478" target="_blank" title="https://juejin.cn/post/6933224825200574478">[前端学java05-SpringBoot实战] 常用注解 + redis实现统计功能</a><br>
<a href="https://juejin.cn/post/6934274450514771982" target="_blank" title="https://juejin.cn/post/6934274450514771982">[前端学java06-SpringBoot实战] 注入 + Swagger2 3.0 + 单元测试JUnit5</a><br>
<a href="https://juejin.cn/post/6935081135114289188" target="_blank" title="https://juejin.cn/post/6935081135114289188">[前端学java07-SpringBoot实战] IOC扫描器 + 事务 + Jackson</a><br>
<a href="https://juejin.cn/post/6960187616050282533" target="_blank" title="https://juejin.cn/post/6960187616050282533">[前端学java08-SpringBoot实战总结1-7] 阶段性总结</a><br>
<a href="https://juejin.cn/post/6962752749993721892" target="_blank" title="https://juejin.cn/post/6962752749993721892">[前端学java09-SpringBoot实战]  多模块配置 + Mybatis-plus + 单多模块打包部署</a><br>
<a href="https://juejin.cn/post/6965404539298168839" target="_blank" title="https://juejin.cn/post/6965404539298168839">[前端学java10-SpringBoot实战] bean赋值转换  + 参数校验 + 全局异常处理</a><br>
<a href="https://juejin.cn/post/6968003860522598436" target="_blank" title="https://juejin.cn/post/6968003860522598436">[前端学java11-SpringSecurity] 配置 + 内存 + 数据库 = 三种方式实现RBAC</a><br>
<a href="https://juejin.cn/post/6970598940479586334" target="_blank" title="https://juejin.cn/post/6970598940479586334">[前端学java12-SpringSecurity] JWT</a><br>
<a href="https://juejin.cn/post/6973100621205520392" target="_blank" title="https://juejin.cn/post/6973100621205520392">[前端学java13-SpringCloud] Eureka + RestTemplate + Zuul + Ribbon</a></p>
<h1 data-id="heading-1">(一) 前置知识</h1>
<h3 data-id="heading-2">(1) 一些单词</h3>
<pre><code class="copyable">queue 队列 
enqueue 排队 // enqueueSetState
lane 车道
batch 批次 // 批次更新 batched
internal 内部的 // key._reactInternals 保留字段
immutable 不可变 永恒的 // immutable.js
mutable 可变的 // an immutable object with a single mutable value
condition 条件 状态

seal 密封 封闭 // Object.seal 不能添加，删除，但是可以修改
freeze 冻结 // Object.freeze 不能添加，删除，修改

legacy blocking concurrent
// blocking 阻塞 块
// concurrent 并发

reuse 复用
hack 黑客，也有浏览器兼容的意思

pure 纯净的
shallow 浅的 // shallowEqual 
flush 清空，刷新，水洗

process 加工 进程
weak 弱的 // WeakMap
passive 被动的 消极的
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">(2) React新老生命周期对比</h3>
<ul>
<li>老生命周期</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e998e2604de949dd9f5f859f5596a1de~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>新生命周期</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8b22d4ee1d942beb7b869029240e494~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>新生命周期中
<ul>
<li>1.废除了 <code>componentWillMount componentWillReceiveProps  componentWillUpdate</code></li>
<li>2.新增了 <code>getDerivedStateFromProps 和 getSnapshotBeforeUpate</code> 来取代上面三个生命周期，注意：上面1和2的新老生生命周期不能混用</li>
<li>3.新增了几个不常用的生命周期 <code>componentDidCatch, getDerivedStateFromError</code></li>
</ul>
</li>
</ul>
<h3 data-id="heading-4">(3) PureComponent 和 React.memo 和 shouldComponentUpdate</h3>
<ul>
<li>PureComponent
<ul>
<li>只能用于类组件</li>
<li>浅比较了 props 和 state 的前后值，浅比较(===)</li>
<li>如果 ( 相等返回false，不重新渲染 ) ( 不相等返回true，重新渲染 )</li>
</ul>
</li>
<li>React.memo
<ul>
<li>React.memo(functionComponent, areEqual)</li>
<li>function areEqual(prevProps, nextProps) &#123;&#125;</li>
<li>只能用于函数式组件</li>
<li>只浅比较了 props 的前后值，浅比较(===)</li>
<li>如果 ( 相等返回true，不重新渲染 ) ( 不相等返回false，重新渲染 )</li>
</ul>
</li>
<li>shouldComponentUpdate
<ul>
<li>shouldComponentUpdate(nextProps, nextState)</li>
<li>返回true重新渲染，返回false不重新渲染</li>
</ul>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/007678b349df48459828702a3f3fe770~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">(4) Object.seal() 和 Object.freeze()</h3>
<ul>
<li>Objext.seal()
<ul>
<li>( 密封 ) 一个对象，( 阻止添加新属性 )，并将所有现有属性标记为 ( 不可配置 - 即属性不可被删除 )，当前属性的值，只要原来是可以写的就 ( 可以改变 )</li>
<li>简单的说就是：( <code>不能添加/删除属性，但是可以修改属性</code> )</li>
<li>参数: 将要密封的对象</li>
<li>返回值：被密封的对象</li>
<li>seal 是密封的意思</li>
</ul>
</li>
<li>Object.freeze()
<ul>
<li>( 冻结 ) 对象，不能 ( <code>添加，修改，删除</code> ) 对象的属性</li>
<li>参数: 将要密封的对象</li>
<li>返回值：被密封的对象</li>
</ul>
</li>
</ul>
<pre><code class="copyable">Object.seal()
---
const obj = &#123;name: 'woow_wu7'&#125;
const obj2 = Object.seal(obj)

obj1 === obj2 // true
delete obj.name // false
delete obj2.name // -------- false，不能删除属性
obj2.name = 'wu7' // ------- 可以修改已有属性
obj.age = 20 // ------------ obj和obj2中都不会有age属性，不能添加属性
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">Object.freeze()
---

const obj = &#123;name: 'woow_wu7'&#125; 
const obj2 = Object.freeze(obj)

obj1 === obj2 // true
delete obj.name // -------- false，不能删除
obj.mame = 'wu7' // ------- 不能修改
obj.age = 20 // ----------- 不能添加
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">(5) React是如何区分 classComponent 和 functionComponent 的？</h3>
<ul>
<li>isReactComponent
<ul>
<li><code>Component.prototype.isReactComponent = &#123;&#125;;</code>
<ul>
<li>在 classComponent 类的prototype上挂载了 isReactComponent 属性</li>
<li>如果 isReactComponent 存在，则是classComponent</li>
</ul>
</li>
</ul>
</li>
<li>isPureReactComponent
<ul>
<li>用来标记是否是 pureComponent</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d40bcf607c8480a99fbbd16a5789066~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">(6) React源码中的一些概念</h3>
<ul>
<li>react中的 ( 三种模式 )
<ul>
<li><strong>legacy</strong>
<ul>
<li>当前react的使用方式，没有计划清除，但该模式可能以后不会支持新功能</li>
<li><code>ReactDOM.render(<App />, rootNode)</code></li>
</ul>
</li>
<li><strong>blocking</strong>
<ul>
<li>目前正在试验中，作为迁移到 concurrent 模式的过渡</li>
<li><code>ReactDOM.createBlockingRoot(rootNode).render(<App />)</code></li>
<li>blocking 阻塞 块</li>
</ul>
</li>
<li><strong>concurrent</strong>
<ul>
<li>目前正在试验中，以后将作为react的默认开发模式，该模式开启所有新功能</li>
<li><code>ReactDOM.createRoot(rootNode).render(<App />)</code></li>
<li>concurrent 并发</li>
</ul>
</li>
</ul>
</li>
<li><strong><code>work</code></strong>
<ul>
<li>在react reconciliation过程中出现的各种必须执行的活动叫作work</li>
<li>比如 ( state update ) ( props update ) ( ref update )</li>
</ul>
</li>
<li><strong><code>WorkTag</code></strong> -- <code>fiber.tag</code>
<ul>
<li>用来描述react元素的类型，也就是fiber对象的类型，即 ( <strong>fiber.tag</strong> )</li>
</ul>
</li>
<li><strong><code>side effects</code></strong>
<ul>
<li>不能在render阶段完成的work，我们称这些工作为side effects</li>
<li>比如：手动更改DOM或在生命周期中执行数据请求、订阅等操作，</li>
</ul>
</li>
<li><strong><code>effectTag</code></strong> -- <code>fiber.effectTag</code>
<ul>
<li>除了update等常见的effect以外，fiber节点提供了一种方便的机制去追踪effect。</li>
<li>每一个fiber节点都有一个和它相关联的effct，这些被编码为effectTag字段对应的值，即为fiber.effectTag</li>
</ul>
</li>
<li><strong><code>Effect list</code></strong>
<ul>
<li>effect list 是由 firstEffect，nextEffect，lastEffect 构成的链表结构</li>
<li>重点如下
<ul>
<li>render阶段结束，会生成一个effect list</li>
<li>commit阶段，react会遍历effect list，并检查fiber对象的effect类型，当发现和其他类型相关用途的函数就调用</li>
</ul>
</li>
</ul>
</li>
<li>stateNode
<ul>
<li>一个组件、一个DOM节点或其他跟fiber节点相关联的React元素的实例的引用</li>
<li>通常，我们可以说这个属性是用于保存与一个fiber相关联的本地状态</li>
<li>fiber.stateNode</li>
</ul>
</li>
</ul>
<h3 data-id="heading-8">(7) Performance.now() 和 Date.now()</h3>
<ul>
<li>performance.now()
<ul>
<li>返回从 ( time-origin ) 到 ( 当前调用经过的时间 )
<ul>
<li>一个精确到毫秒的 DOMHighResTimeStamp</li>
<li>DOMHighResTimeStamp 是一个double类型，用于存储毫秒级的时间值</li>
</ul>
</li>
</ul>
</li>
<li>Date.now()
<ul>
<li>返回当前时间距离时间零点的毫秒数，时间零点是1970/1/1/00:00:00</li>
<li><strong><code>Date.now() === +new Date() === new Date - 0</code></strong></li>
</ul>
</li>
</ul>
<pre><code class="copyable">performance.now
--
const t0 = window.performance.now(); // 启始时间
doSomething();
const t1 = window.performance.now(); // 终结时间
console.log("doSomething函数执行了" + (t1 - t0) + "毫秒.")
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-9">(二) Component 和 PureComponent</h1>
<h3 data-id="heading-10">(2.1) PureComponent</h3>
<ul>
<li>概念
<ul>
<li><code>PureComponent = Component + shouldComponentUpdate(nextProps, nextState) </code></li>
<li>在 shouldComponentUpdate() 中对 ( 新旧props ) 和 ( 新旧state ) 做了 ( 一层钱比较 )</li>
<li>一般这样使用：class A extends React.Component/React.PureComponent &#123;&#125;</li>
</ul>
</li>
<li>什么是 <strong>( 浅比较 )</strong>
<ul>
<li>浅比较也称 ( 引用相等 )，也就是全等 ( === )</li>
</ul>
</li>
</ul>
<pre><code class="copyable"> const o1 = &#123;a: 1&#125;
 const o2 = &#123;a: 1&#125;
 const o3 = o2
 const o4 = (obj) => &#123; obj.b = 1; return obj &#125;

 o1 === o2 // false
 o3 === o2 // true，两个变量，栈内存中的指针都指向了同一个堆内存数据的地址
 o4(o1) === o1 // true
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">(2.2) PureComponent 源码</h3>
<ul>
<li>isPureReactComponent
<ul>
<li>相对于Component，在prototype上多了 <strong><code>isPureReactComponent=true</code></strong> 属性</li>
<li>文件位置：<code>packages/react/src/ReactBaseClasses.js</code></li>
</ul>
</li>
</ul>
<pre><code class="copyable">function PureComponent(props, context, updater) &#123;
  this.props = props;
  this.context = context;

  // If a component has string refs, we will assign a different object later.
  this.refs = emptyObject; // 赋值空对象

  this.updater = updater || ReactNoopUpdateQueue;
  // ReactNoopUpdateQueue
  // - 是一个对象，具有这些属性 &#123;isMounted, enqueueForceUpdate, enqueueReplaceState, enqueueSetState &#125;
&#125;

const pureComponentPrototype = (PureComponent.prototype = new ComponentDummy());
// 1
// new ComponentDummy()
// function ComponentDummy() &#123;&#125;
// ComponentDummy.prototype = Component.prototype;
// 寄生原型链继承，这样 ( pureComponent实例 ) 的 ( 原型对象上 ) 是没有任何属性的，但是原型对象的原型链上的属性仍然可以继承

// 2
// Component.prototype
// - 具有以下属性
// - isReactComponent
// - setState
// - forceUpdate

pureComponentPrototype.constructor = PureComponent;
// 2
// 修改prototype对象时，一定要修改prototype.constructor，防止引用出错
// 如果不修改，prototype.constructor将指向 ComponentDummy

// Avoid an extra prototype jump for these methods.
Object.assign(pureComponentPrototype, Component.prototype);
// 合并属性

pureComponentPrototype.isPureReactComponent = true;
// 3
// isPureReactComponent 用来判断是不是纯组件 PureComponent
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>checkShouldComponentUpdate
<ul>
<li>文件位置：<code>packages/react-reconciler/src/ReactFiberClassComponent.old.js</code></li>
<li><strong><code>checkShouldComponentUpdate</code></strong> 检查是否需要更新时，对新旧props和新旧state做了一层钱比较</li>
</ul>
</li>
</ul>
<pre><code class="copyable">function checkShouldComponentUpdate(
  workInProgress,
  ctor,
  oldProps,
  newProps,
  oldState,
  newState,
  nextContext,
) &#123;
  ...
  // PureComponent2
  if (ctor.prototype && ctor.prototype.isPureReactComponent) &#123;
    return (
      !shallowEqual(oldProps, newProps) || !shallowEqual(oldState, newState)
      // 浅比较 props 和 state
    );
  &#125;
 ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">(三) createRef</h1>
<h3 data-id="heading-13">(3.1) React.createRef() 源码</h3>
<pre><code class="copyable">export function createRef(): RefObject &#123;
  const refObject = &#123; current: null &#125;; // ref实例上具有 current 属性
  if (__DEV__) &#123;
    Object.seal(refObject); // ---------- current 属性不能添加和删除，只能修改，在开发环境时
  &#125;
  return refObject;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">(3.2) React.createRef() 使用案例</h3>
<pre><code class="copyable">class TestCreateRef extends React.Component &#123;
    inputRef = React.createRef();
    componentDidMount() &#123; this.inputRef.current.focus() &#125;
    render() &#123;
        return <input type="text" ref=&#123;this.inputRef&#125; />
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">(四) ReactDOM.render()</h1>
<h3 data-id="heading-16">(4.1) 搭建react源码调试环境</h3>
<pre><code class="copyable">1. 通过create-react-app 创建一个react项目
2. yarn run eject 弹出配置
3. 克隆react源码 git clone git@github.com:facebook/react.git
4. 将克隆下来的 ( 源码的packages文件夹 ) 放入创建好的react项目的 ( src/REACT_SOURCE_CODE_ANALYSIS ) 文件夹下

5. 修改webpack.config.js中的resolve中的alias配置
alias: &#123;
        // Support React Native Web
        // https://www.smashingmagazine.com/2016/08/a-glimpse-into-the-future-with-react-native-for-web/
        'react-native': 'react-native-web',
        // Allows for better profiling with ReactDevTools
        ...(isEnvProductionProfile && &#123;
          'react-dom$': 'react-dom/profiling',
          'scheduler/tracing': 'scheduler/tracing-profiling',
        &#125;),
        ...(modules.webpackAliases || &#123;&#125;),
        // + 添加如下代码
        'react': path.resolve(__dirname, '../src/REACT_SOURCE_CODE_ANALYSIS/packages/react'),
        'react-dom': path.resolve(__dirname, '../src/REACT_SOURCE_CODE_ANALYSIS/packages/react-dom'),
        'shared': path.resolve(__dirname, '../src/REACT_SOURCE_CODE_ANALYSIS/packages/shared'),
        'react-reconciler': path.resolve(__dirname, '../src/REACT_SOURCE_CODE_ANALYSIS/packages/react-reconciler'),
&#125;

6. 修改 config/env.js
  const stringified = &#123;
    __DEV__: true,
    __PROFILE__: true,
    __UMD__: true,
    __EXPERIMENTAL__: true, // 和 .eslintrc.json中的globals一一对应
    'process.env': Object.keys(raw).reduce((env, key) => &#123;
      env[key] = JSON.stringify(raw[key]);
      return env;
    &#125;, &#123;&#125;),
  &#125;;
  
 7. react项目根目录创建 .eslintrc.json
 &#123;
  "extends": "react-app",
  "globals": &#123;
    "__DEV__": true,
    "__PROFILE__": true,
    "__UMD__": true,
    "__EXPERIMENTAL__": true,
  &#125;
&#125;

8. 删除 webpack.config.js 中的 eslint 检查
// !disableESLintPlugin &&
      //   new ESLintPlugin(&#123;
      //     // Plugin options
      //     extensions: ['js', 'mjs', 'jsx', 'ts', 'tsx'],
      //     formatter: require.resolve('react-dev-utils/eslintFormatter'),
      //     eslintPath: require.resolve('eslint'),
      //     failOnError: !(isEnvDevelopment && emitErrorsAsWarnings),
      //     context: paths.appSrc,
      //     cache: true,
      //     cacheLocation: path.resolve(
      //       paths.appNodeModules,
      //       '.cache/.eslintcache'
      //     ),
      //     // ESLint class options
      //     cwd: paths.appPath,
      //     resolvePluginsRelativeTo: __dirname,
      //     baseConfig: &#123;
      //       extends: [require.resolve('eslint-config-react-app/base')],
      //       rules: &#123;
      //         ...(!hasJsxRuntime && &#123;
      //           'react/react-in-jsx-scope': 'error',
      //         &#125;),
      //       &#125;,
      //     &#125;,
      //   &#125;),
      
9. src/REACT_SOURCE_CODE_ANALYSIS/packages/react-reconciler/src/ReactFiberHostConfig.js
// 注释掉 
// import invariant from 'shared/invariant'; 
// invariant(false, 'This module must be shimmed by a specific renderer.'); 
// 添加此行 
// export * from "./forks/ReactFiberHostConfig.dom";

10. src/REACT_SOURCE_CODE_ANALYSIS/packages/shared/ReactSharedInternals.js
// 注释掉
// import * as React from 'react';
// 添加此行
import ReactSharedInternals from '../react/src/ReactSharedInternals';
// 注释掉
// ReactSharedInternals
// const ReactSharedInternals =
//   React.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED;
export default ReactSharedInternals;

11. src/REACT_SOURCE_CODE_ANALYSIS/packages/shared/invariant.js
export default function invariant(condition, format, a, b, c, d, e, f) &#123;
  // 添加下面的一行
  if (condition) return;
  throw new Error(
    "Internal React error: invariant() is meant to be replaced at compile " +
      "time. There is no runtime version."
  );
&#125;

12. 在react中项目的入口文件index.js中更新引入react和reactDOM的方法
// import React from 'react';
// import ReactDOM from 'react-dom';
import * as React from 'react'; // 这里能够引用到，是因为在webpack.config.js中的resolve.alias中指定了别名的引用路径
import * as ReactDOM from 'react-dom';

13. 在vscode中下载 Debugger for Chrome 插件，并在launch.json中做如下配置
&#123;
  "version": "0.2.0",
  "configurations": [
    &#123;
      "type": "chrome",
      "request": "launch",
      "name": "Launch Chrome against localhost",
      "url": "http://localhost:3000",
      "webRoot": "$&#123;workspaceFolder&#125;"
    &#125;
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/495ba8759fca4fdaa0056265bffbbf27~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">(4.2) ReactDOM.render() 基础知识</h3>
<ul>
<li><code>ReactDOM.render(element, container[, callback])</code>
<ul>
<li>作用
<ul>
<li>初次渲染：在提供的 container 里渲染一个 React 元素，并返回对该组件的引用(或者针对无状态组件返回null)</li>
<li>更新：如果React元素之前已经在container里渲染过，这将会对其执行 ( 更新操作 )，并仅会在必要时改变DOM以映射最新的React元素</li>
<li>如果提供了第三个参数，表示在 ( 初次渲染或者更新 ) 完成后执行的 ( 回调函数 )</li>
</ul>
</li>
</ul>
</li>
<li>参数中的element是什么？
<ul>
<li>element是一个 (react元素)
<ul>
<li>
<ol>
<li>react组件的返回值就是一个react元素 ，组件由元素构成</li>
</ol>
</li>
<li>
<ol start="2">
<li>react元素可以通过 React.createElement(type, config, children)来创建</li>
</ol>
</li>
<li>
<ol start="3">
<li>( react元素 ) 本质上就是一个 ( javascript对象 )</li>
</ol>
</li>
</ul>
</li>
<li>React.createElement(type, config, children) 源码
<ul>
<li><a href="https://juejin.cn/post/6983570939342487565/#heading-9" target="_blank" title="https://juejin.cn/post/6983570939342487565/#heading-9">React.createElemen源码分析-详见上一篇文章</a></li>
</ul>
</li>
</ul>
</li>
<li>ReactDOM.render()分为 ( 三个阶段 )
<ul>
<li><strong><code>init初始化阶段</code></strong>
<ul>
<li>主要负责生成fiber树的基础实体对象，比如fiberRoot，rootFiber</li>
</ul>
</li>
<li><strong><code>render阶段</code></strong>
<ul>
<li>负责fiber树的创建，调度，调和等</li>
</ul>
</li>
<li><strong><code>commit阶段</code></strong>
<ul>
<li>根据virtualDOM，渲染真实DOM</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-18">(4.3) ReactDOM.render() 源码</h3>
<ul>
<li>ReactDOM.render 返回 legacyRenderSubtreeIntoContainer()</li>
</ul>
<pre><code class="copyable">
// ----------------------------------------------------------------------------------------------------------- ReactDOM.render
// 【 起点 】render
// 1
// ReactDOM.render(element, container[, callback])
// - 1. 作用：
//    - 1. 初始渲染：在提供的 container 里面渲染一个React元素，并返回对该组件的引用，( 或者针对无状态组件返回null )
//    - 2. 更新：-- 如果React元素之前已经在 container 里渲染过，这将会对其执行 ( 更新操作 )，并仅仅会在必要时改变DOM以映射最新的React元素
// - 2. 参数
//    - element
//      - element表示的是一个react元素，react组件由element元素组成，element元素本质上是一个javascript对象，可以通过React.createElement生成
//      - React.createElement(type, config, children) => ReactElement(type, key, ref, self, source, ReactCurrentOwner.current, props) => element
//      - element对象具有
//          - 基本属性：type，key，ref，props，_owner,  $$typeof
//          - DEV环境多了：__store, __self, __source 属性
//    - container
//      - 属性，即组件或者element上的属性
//    - callback: 可选，在 ( 渲染或更新 ) 完成后，执行的回调函数
// - 3. 返回值
//    - legacyRenderSubtreeIntoContainer
//    - legacyRenderSubtreeIntoContainer( null, element, container, false, callback ) 调用的返回值就是render()函数的返回值
export function render(
  element: React$Element<any>,
  container: Container,
  callback: ?Function,
) &#123;
  if (__DEV__) &#123;
    console.error(
      'ReactDOM.render is no longer supported in React 18. Use createRoot ' +
        'instead. Until you switch to the new API, your app will behave as ' +
        "if it's running React 17. Learn " +
        'more: https://reactjs.org/link/switch-to-createroot',
    );
    // createRoot
    // - React 18中不再支持ReactDOM.render，请使用 createRoot() 代替
  &#125;

  invariant(
    isValidContainerLegacy(container), // 合法的节点
    'Target container is not a DOM element.',
  );
  // export default function invariant(condition, format, a, b, c, d, e, f) &#123;
  //   throw new Error(
  //     'Internal React error: invariant() is meant to be replaced at compile ' +
  //       'time. There is no runtime version.',
  //   );
  // &#125;

  if (__DEV__) &#123;
    const isModernRoot =
      isContainerMarkedAsRoot(container) &&
      container._reactRootContainer === undefined;
    // 1
    // isContainerMarkedAsRoot
    // export function isContainerMarkedAsRoot(node: Container): boolean &#123;
    //   return !!node[internalContainerInstanceKey];
    // &#125;
    // 2
    // internalContainerInstanceKey
    // const internalContainerInstanceKey = '__reactContainer$' + randomKey;
    // 3
    // randomKey
    // const randomKey = Math.random()
    // .toString(36)
    // .slice(2);


    if (isModernRoot) &#123;
      console.error(
        'You are calling ReactDOM.render() on a container that was previously ' +
          'passed to ReactDOM.createRoot(). This is not supported. ' +
          'Did you mean to call root.render(element)?',
          // 您正在对以前传递给 ReactDOM.createRoot() 的容器使用 ReactDOM.render()，不支持这样做，你是想调用root.render(element)？
      );
    &#125;
  &#125;

  // 1
  // legacyRenderSubtreeIntoContainer()
  // render() 函数最终返回值 legacyRenderSubtreeIntoContainer()
  // legacy : 遗产  +  render: 渲染  +  subtree: 子树  +  into: 到 +  container: 容器
  // 2
  // react一共有三种模式
  // legacy
  // blocking
  // concurrent 以后react18中将默认开启并发模式
 
  return legacyRenderSubtreeIntoContainer(
    null, // parentComponent 父组件
    element, // children
    container, // container
    false, // forceHydrate 服务端渲染的标志
    callback, // callback
  );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>legacyRenderSubtreeIntoContainer
<ul>
<li>主要做了以下事情
<ul>
<li>创建fiberRoot 和 rootFiber，并相互引用</li>
<li>关联 continer 和 rootFiber.current</li>
<li>事件相关</li>
<li>updateContainer()</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="copyable">
// ----------------------------------------------------------------------------------------------------------- legacyRenderSubtreeIntoContainer
// 【0】 legacyRenderSubtreeIntoContainer
// 1
// 初次渲染 init mount
// - 1. 初次渲染 - 是没有 (老的虚拟DOM节点的 )
// - 2. 即初次渲染生成一个插入一个，但如果是更新阶段则要考虑很多情况了，比如移动，更新，插件等等
// 2
// 如何判断是不是初次渲染？
// - 因为初次渲染是没有老的虚拟DOM节点的，所以可以通过 ( root ) 来判断，即 ( let root = container._reactRootContainer )
// 2
// 初始化调用ReactDOM.render() 时的 ( 参数 ) 如下
// - legacyRenderSubtreeIntoContainer( null, element, container, false, callback, );
function legacyRenderSubtreeIntoContainer(
  parentComponent: ?React$Component<any, any>, // init => null
  children: ReactNodeList, // render 第一个参数 element
  container: Container, // render 第二个参数 container
  forceHydrate: boolean, // 服务器端渲染标识，初始化是false, init => false
  callback: ?Function, // 初次渲染或者更新后需要执行的回调，可选，基本不会使用
) &#123;
  if (__DEV__) &#123;
    topLevelUpdateWarnings(container);
    warnOnInvalidCallback(callback === undefined ? null : callback, 'render');
  &#125;

  let root = container._reactRootContainer;
  // root
  // 1. 声明 root
  // 2. 在container上生声明了_reactRootContainer属性
  // 3. init时，_reactRootContainer属性不存在，则 root = undefined
  // 4. container
  //    - 1
  //    - container
  //    - container是调用 reactDOM.render()时传入的第二个参数，即jsx挂载的容器，是真实的DOM
  //    - 下面生成fiberRoot的时候，  root = container._reactRootContainer = legacyCreateRootFromDOMContainer()，
  //    - 即在容器上挂载了 fiberRoot
  //    - 2
  //    - _reactRootContainer
  //    - container._reactRootContainer
  //    - react的项目中，可以通过 document.querySelector('#root')._reactRootContainer 来读取 _reactRootContainer
  //    - 可以看到：( fiberRoot的构造函 ) 数是 ( FiberRootNode(containerInfo, tag, hydrate) )
  //    - 3
  //    - _internalRoot
  //    - container._reactRootContainer._internalRoot 对应这 ( fiberRoot )
  //    - ( _internalRoot === fiberRoot )
  //    - internal 是内部的意思
  // 5. 先总结一下
  //    - root 就是 fiberRoot，因为后面会赋值给 fiberRoot 变量
  //    - fiberRoot 同样挂在了 container DOM节点上
  //    - fiberRoot对象 就是整个fiber树的 根节点 ( 其实每个DOM节点一定对应着一个fiber对象，所以DOM树和fiber数一一对应 )

  let fiberRoot: FiberRoot; // 缓存 old virtual DOM，用于对比
  // fiberRoot
  // 1. 注意区分 fiberRoot 和 rootFiber
  //    - fiberRoot 只有一个
  //    - rootFiber 可以有多个，就是一个普通的fiber节点
  // 2. 两者的关系
  //    - rootFiber.stateNode = fiberRoot
  //    - fiberRoot.current = rootFiber
  //    - 两者循环引用

  if (!root) &#123;
    // Initial mount
    // ------------------------------------------------------------ 初始化mount阶段，即初次渲染，root不存在
    // 初次渲染 root 是不存在的，所以要创建生成一个root

    // 1
    // container
    // container._reactRootContainer.
    // container._reactRootContainer._internalRoot 指向的就是 fiberRoot
    // 2
    // fiberRoot === fiberRootNode对象
    // 3
    // 再次复习 fiberRoot 和 rootFiber
    // - fiberRoot
    //   - fiberRoot 关联的是真实的DOM容器节点
    // - rootFiber
    //   - 是虚拟DOM的根节点
    // - fiberRoot.current === rootFiber
    // - rootFiber.stateNode === fiberRoot
    root = container._reactRootContainer = legacyCreateRootFromDOMContainer(
      container,
      forceHydrate, // init => false
    );
    fiberRoot = root; // 缓存 old virtual DOM，用于对比
    if (typeof callback === 'function') &#123; // 一般都不会指定callback，即一般不会进入if
      const originalCallback = callback;
      callback = function() &#123;
        const instance = getPublicRootInstance(fiberRoot);
        originalCallback.call(instance);
      &#125;;
    &#125;
    // Initial mount should not be batched.
    // 初次渲染是非批量更新，可以保证 ( 更新效率与用户体验 )
    // 比如初次渲染希望更快的速速让用户看到 ui
    flushSyncWithoutWarningIfAlreadyRendering(() => &#123;
      updateContainer(children, fiberRoot, parentComponent, callback);
    &#125;);
    // flushSyncWithoutWarningIfAlreadyRendering
    // - 函数签名：flushSyncWithoutWarningIfAlreadyRendering(fn) => fn()

  &#125; else &#123;
    // ------------------------------------------------------------ 更新阶段
    fiberRoot = root;
    if (typeof callback === 'function') &#123;
      const originalCallback = callback;
      callback = function() &#123;
        const instance = getPublicRootInstance(fiberRoot);
        originalCallback.call(instance);
      &#125;;
    &#125;
    // Update
    // 批量更新 batched update
    updateContainer(children, fiberRoot, parentComponent, callback);
  &#125;
  return getPublicRootInstance(fiberRoot);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>updateContainer()
<ul>
<li>主要负责
<ul>
<li>获取当前 fiber 节点的 lane优先级，lane越小，优先级越高</li>
<li>创建context</li>
<li>创建 update对象，并入队</li>
<li>调度当前节点的 rootFiber</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="copyable">// ----------------------------------------------------------------------------------------------------------- updateContainer
// 【1】updateContainer
// updateContainer(children, fiberRoot, parentComponent, callback);

// 1
// updateContainer主要做的事情
// 1. 获取当前 fiber 节点的 lane 优先级
// 2. 结合lane优先级，创建当前fiber节点的update对象，并将其入队
// 3. 调度当前节点 rootFiber

// 2
// 调用栈：render > legacyRenderSubtreeIntoContainer > updateContainer
export function updateContainer(
  element: ReactNodeList,
  container: OpaqueRoot, // fiberRoot
  parentComponent: ?React$Component<any, any>,
  callback: ?Function,
): Lane &#123;
  if (__DEV__) &#123;
    onScheduleRoot(container, element);
  &#125;
  const current = container.current; // container.current = fiberRoot.current = rootFiber； 这里rootFiber=3时，说明是 hostRoot
  const eventTime = requestEventTime(); // 541304.0999999642
  const lane = requestUpdateLane(current); // 1
  // lane
  // - lane 表示优先级
  // - lane越小，表示优先级越高
  // - lane为二进制存储，一共31位，每个位为一个车道

  // performance.now()
  // - 返回：当前网页自从performance.timing.navigationStart到当前时间之间的毫秒数

  if (enableSchedulingProfiler) &#123;
    // export const enableSchedulingProfiler = __PROFILE__ && __EXPERIMENTAL__;
    markRenderScheduled(lane);
  &#125;

  const context = getContextForSubtree(parentComponent); // mount => 返回一个空对象
  if (container.context === null) &#123; // mount => 容器上的context是空
    container.context = context; // 给 container.context = &#123;&#125;
  &#125; else &#123;
    container.pendingContext = context;
  &#125;

  if (__DEV__) &#123;
    if (
      ReactCurrentFiberIsRendering &&
      ReactCurrentFiberCurrent !== null &&
      !didWarnAboutNestedUpdates
    ) &#123;
      didWarnAboutNestedUpdates = true;
      console.error(
        'Render methods should be a pure function of props and state; ' +
          'triggering nested component updates from render is not allowed. ' +
          'If necessary, trigger nested updates in componentDidUpdate.\n\n' +
          'Check the render method of %s.',
        getComponentNameFromFiber(ReactCurrentFiberCurrent) || 'Unknown',
      );
    &#125;
  &#125;

  const update = createUpdate(eventTime, lane); // 返回update对象，tag=0, lane=1
  // Caution: React DevTools currently depends on this property
  // being called "element".
  // 警告：React DevTools当前依赖于名为“element”的此属性。
  update.payload = &#123;element&#125;;

  callback = callback === undefined ? null : callback;
  if (callback !== null) &#123;
    if (__DEV__) &#123;
      if (typeof callback !== 'function') &#123;
        console.error(
          'render(...): Expected the last optional `callback` argument to be a ' +
            'function. Instead received: %s.',
          callback,
        );
      &#125;
    &#125;
    update.callback = callback;
  &#125;

  enqueueUpdate(current, update, lane); // 将update对象入队，形成环状链表
  // enqueueUpdate
  // enqueueUpdate主要用来添加一个共享队列sharedQueue，该队列可以和workInProgress和FiberRoot进行共享队列

  const root = scheduleUpdateOnFiber(current, lane, eventTime); // 调度 fiber 节点的挂载

  if (root !== null) &#123;
    entangleTransitions(root, current, lane);
  &#125;
 
  return lane; // 返回 ( 当前节点 即fiberRoot ) 的优先级
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">(五) 源码分析仓库地址</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwoow-wu7%2F7-react-source-code-analysis" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/woow-wu7/7-react-source-code-analysis" ref="nofollow noopener noreferrer">reactDOM.render - 源码分析仓库地址</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwoow-wu7%2F7-react-source-code-analysis%2Ftree%2Fmain%2Fsrc%2Fimages%2FReactDOM.render.png" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/woow-wu7/7-react-source-code-analysis/tree/main/src/images/ReactDOM.render.png" ref="nofollow noopener noreferrer">reactDOM.render - 思维导图</a></li>
</ul>
<h1 data-id="heading-20">资料</h1>
<ul>
<li>react调试源码教程1 <a href="https://juejin.cn/post/6942687170800910350" target="_blank" title="https://juejin.cn/post/6942687170800910350">juejin.cn/post/694268…</a></li>
<li>react调试源码教程2 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F336933386" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/336933386" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/336933386</a></li>
<li>fiber相关的概念汇总 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftech.tuya.com%2Freact-fiberyuan-ma-li-jie%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://tech.tuya.com/react-fiberyuan-ma-li-jie/" ref="nofollow noopener noreferrer">tech.tuya.com/react-fiber…</a></li>
<li>enqueueUpdate <a href="https://juejin.cn/post/6951585684679294989" target="_blank" title="https://juejin.cn/post/6951585684679294989">juejin.cn/post/695158…</a></li>
</ul></div>  
</div>
            