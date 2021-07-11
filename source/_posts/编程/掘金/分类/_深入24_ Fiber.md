
---
title: '_深入24_ Fiber'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e70350c51fe44efea429a3074807c681~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 10 Jul 2021 23:50:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e70350c51fe44efea429a3074807c681~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">导航</h1>
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
<a href="https://juejin.im/post/6844904095464030215" target="_blank" title="https://juejin.im/post/6844904095464030215">[部署01] Nginx</a><br>
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
<h2 data-id="heading-2">(1) 一些单词</h2>
<pre><code class="copyable">thread 线程
process 进程
composite 合成

优先级 highest高 medium中 low低

heap 堆
stack 栈 // heap stack 的区别
phase 阶段


reconciliaction 调和
reconciler 调和器
// 旧版本的叫法：stack reconciler
// 新版本的叫法：fiber reconciler

scheduler 调度器
synchronous 同时 同步

obtain 获得
intellisense 智能感知
framework 架构
try it out 试试看
reserve 保留的 // reserved_props
enumerable 可枚举
descriptor 描述符
therefore 因此 所以
alternate 候补者，交替 // fiber.alternate
draft 草稿

priority 优先级
concurrent 并发
immediate 立即的
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">(2) 进程和线程</h2>
<ul>
<li>进程
<ul>
<li>正在执行的应用程序</li>
</ul>
</li>
<li>线程
<ul>
<li>应用程序中的 ( 代码执行器 )</li>
</ul>
</li>
<li>进程和线程的关系
<ul>
<li>线程跑在进程中，一个进程可能有多个线程，而一个线程只能属于一个进程</li>
</ul>
</li>
<li>进程和进程的关系
<ul>
<li>进程和进程之间，因为内存空间不一样，所以相互独立，互不影响</li>
<li>一个进程挂掉，其他进程不会受到影响</li>
</ul>
</li>
<li>浏览器中的进程和线程
<ul>
<li>进程线程内存
<ul>
<li><strong><code>浏览器是多进程的 ( 可以理解为一个标签页就是一个进程，具有多个进程 )，进程启动后，( cpu ) 就会给 ( 该进程 ) 分配 ( 内存空间 ) ，当进程得到内存空间后，就可以使用 ( 线程 ) 进行 ( 资源调度 )，进而完成功能</code></strong></li>
</ul>
</li>
<li>进程和内存
<ul>
<li><strong><code>浏览器每 ( 新建一个进程 )，cpu都会给该进程分配一个 ( 新的独立的内存空间 )，( 不会与原来的进程共用一个内存空间 )</code></strong>，那么就会有一个问题，进程之间是需要通信的，从而才能传递数据，那么进程之间是如何通信的呢？</li>
<li>进程和进程之间，因为内存空间不一样，所以相互独立，互不影响</li>
</ul>
</li>
<li>进程之间的通信
<ul>
<li><strong><code>( 进程 ) 之间需要 ( 通信 )，可以通过 (  IPC ) 机制来进行</code></strong></li>
<li>ipc: inter process communication</li>
</ul>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e70350c51fe44efea429a3074807c681~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
</li>
<li>Chrome浏览器中的进程
<ul>
<li>浏览器是多进程的应用程序</li>
<li>chrome中的主要进程
<ul>
<li><code>浏览器进程</code>
<ul>
<li>主要就是浏览器本身的功能：负责浏览器的TAB的前进、后退、地址栏、书签栏的工作和处理浏览器的一些不可见的底层操作</li>
</ul>
</li>
<li><code>渲染进程</code>
<ul>
<li>负责一个tab标签页面的相关工作，也称渲染引擎</li>
</ul>
</li>
<li><code>插件进程</code>
<ul>
<li>浏览器插件功能</li>
</ul>
</li>
<li><code>GPU进程</code>
<ul>
<li>负责视频等GPU任务</li>
</ul>
</li>
</ul>
</li>
<li>进程之间的关系
<ul>
<li>浏览器进程 => 渲染进程 => 插件进程 => GPU进程</li>
<li>当在输入url返回资源后，浏览器进程会通知渲染进程进行解析，解析完成后得到图像帧 => 渲染进程会通知GPU进程将其转化为图像，并在屏幕上显示</li>
</ul>
</li>
<li>chrome为啥要采用多线程
<ul>
<li>一个tab挂掉，其他的tab不受影响，即一个进程挂掉不会影响其他进程</li>
<li>浏览器针对不同进程做了不同的权限，从而保证安全性和沙河性</li>
<li>更快的响应速度，不会像单进程那样抢夺cpu资源</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-4">(3) 浏览器的渲染进程</h2>
<p>导航过程完成后，浏览器拿到响应数据后，( <code>浏览器进程</code> ) 会把 ( <code>数据</code> ) 交给 ( <code>渲染进程</code> )，渲染进程负责 ( <code>tab内的所有事情</code> )，主要任务就是将 ( <code>html/css/js</code>) 转化成 <code>web页面</code></p>
<ul>
<li>渲染进程中包含的线程
<ul>
<li>一个主线程 ------------------ main thread</li>
<li>一个合成线程 ---------------- compositor thread</li>
<li>多个工作线程 ---------------- work thread</li>
<li>多个光栅线程 ---------------- raster thread</li>
<li>不同线程有不同的工作职责</li>
</ul>
</li>
</ul>
<h2 data-id="heading-5">(4) 浏览器的渲染过程!!!!!!!!!!!!!!!!!!!!!!!!!!!</h2>
<ul>
<li>
<p>总顺序</p>
<pre><code class="copyable">  Parse HTML => Parse Stylesheet => Evaluate Script => Layout => Paint => Composite
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>(1) 浏览器根据 ( 响应类型 ) 来解析文件 - html解析 - <strong><code>DOM构建</code></strong> -------------- <strong>Parse HTML</strong></p>
<ul>
<li>如果响应类型是 (  Content-Type: text/html ) 的话，浏览器会用 ( html解析器将html解析成DOM树 )</li>
<li>html => html parser => dom tree</li>
<li>( dom tree ) 是典型的 ( 栈结构 )</li>
</ul>
</li>
<li>
<p>(2) css的解析 - <strong><code>样式计算Style calculation - Parse Stylesheet</code></strong> -------- <strong>Parse StyleSheet</strong></p>
<ul>
<li>主线程在解析页面时，遇到 ( style link ) 标签就会调用css解析器，将css解析成cssom tree，生成样式</li>
<li>如果页面没有设置过样式，也会提供默认样式</li>
</ul>
</li>
<li>
<p>(3) js的解析 --------------------------------------------------------------- <strong>Evaluate Script</strong></p>
<ul>
<li>遇到 ( script ) 标签，浏览器会调用js解析器解析js</li>
<li>js的 ( 加载和执行 )都会阻塞DOM解析，因为js代码可能改变DOM，如果在script中添加了 (async defer) 就会是异步加载，即加载都不会阻塞DOM，但是执行都会阻碍DOM</li>
<li>defer异步加载，dom渲染完后才会执行，保证顺序</li>
<li>async异步加载，加载完后就会立即执行，不能保证顺序</li>
</ul>
</li>
<li>
<p>(4) <strong><code>布局Layout</code></strong> ----------------------------------------------------------- <strong>Layout</strong></p>
<ul>
<li>DOM树和样式计算完成后，还需要知道每个节点的位置，布局就是找到位置的过程</li>
<li>主线程会根据 ( DOM tree ) 和 ( cssom tree ) 合成 ( render tree )，render tree包含了节点的 ( 坐标信息 ) 和 ( 盒子模型 )，最终生成 ( layout tree )
<ul>
<li>遍历过程会跳过隐藏的元素display: none</li>
<li>伪元素虽然不在dom-tree中，但是在render-tree中</li>
</ul>
</li>
<li>layout分为 ( 全局的 ) 和 ( 局部的 )
<ul>
<li>全局
<ul>
<li>对整棵树进行布局</li>
<li>比如修改浏览器尺寸，或者修改跟元素的大小，位置，字体等</li>
</ul>
</li>
<li>局部
<ul>
<li>对部分进行重新布局</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>
<p>(5) <strong><code>绘制Paint</code></strong> ---------------------------------------------------------- <strong>Paint</strong></p>
<ul>
<li>layout布局之后，我们知道了元素的 ( 结构，样式，几何关系 )，需要绘制一个页面就要知道每个 ( 节点的绘制先后顺序 )</li>
<li>在Paint阶段，主线程会便利layout tree，生成一系列的绘画记录Paint records</li>
<li>分层
<ul>
<li><strong>为了保证重绘的速度比初始绘制的速度快，屏幕的绘图通常分解成数层 ( 分层 )，如果发生这种情况，通常需要进行composite合成</strong></li>
</ul>
</li>
<li>Layer tree
<ul>
<li>绘制可以将布局中的元素分解为多层，为了确定哪些元素要放在同一层，需要遍历render-tree来创建一个新的 ( Layer tree )</li>
<li>添加了 will-change 的css属性的元素，会单独作为一层</li>
<li>没有添加 will-change的css属性的元素，浏览器会根据情况决定是否把该元素放在单独的层</li>
</ul>
</li>
<li>光栅化
<ul>
<li>一旦layer-tree被创建，( 渲染顺序被确定 )，主线程会把这些信息通知给 ( 合成器线程 )，合成器线程就会对每一层进行 ( 光栅化 )</li>
</ul>
</li>
</ul>
</li>
<li>
<p>(6) <strong><code>合成Compositing</code></strong> -------------------------------------------------- <strong>Composite Layout</strong></p>
<ul>
<li><strong>当文档的各个部分以不同的层绘制，相互重叠时，必须进行合成，以确保它们以正确的顺序绘制到屏幕上，并正确显示内容</strong></li>
<li><strong>合成是在 ( 合成线程 ) 中进行的，不涉及 ( 主线程 )，因此合成线程不需要等待css和js的执行</strong></li>
<li>文档结构，节点样式，节点的结合关系，绘画顺序都知道了，最后我们需要绘制一个页面，将这些所有的信息转成像素，这个过程叫 ( 光栅化 )</li>
</ul>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bb340a4ee714691884ba7d4e5fc0871~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">(5) 浏览器的 16ms 渲染帧</h2>
<ul>
<li>一些概念
<ul>
<li>渲染帧
<ul>
<li>渲染帧是指浏览器的一次完整绘制过程</li>
</ul>
</li>
<li>帧之间的时间间隔 16ms
<ul>
<li>帧之间的时间间隔，是 ( DOM视图更新的最小间隔 )
<ul>
<li>由于主流浏览器的刷新率是 ( <strong><code>60hz</code></strong> )，那么渲染一帧的时间就必须控制在 ( <strong><code>16ms</code></strong> ) 内才能保证 ( <strong><code>不掉帧</code></strong> )，也就是说每一次渲染都要保证在16ms内完成渲染在能保证页面流畅，才不会卡顿</li>
</ul>
</li>
<li>16ms内需要做以下事情 ( 也就是上面(4)中的所有事情 )
<ul>
<li>脚本执行 -> 样式计算 -> 布局 -> 绘制 -> 合成</li>
<li>parse html -> parse stylesheet -> evaluate script -> layout -> paint -> composite</li>
</ul>
</li>
<li>如果测量渲染间隔？
<ul>
<li><strong><code>requestAnimationFrame</code></strong>
<ul>
<li>window.requestAnimationFrame() 告诉浏览器你希望执行一个动画，并且要求浏览器在下次重绘之前调用指定的回调函数更新动画</li>
<li>该方法需要传入一个回调函数作为参数，该回调函数会在浏览器下一次重绘之前执行</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
<li>重要结论
<ul>
<li><code>一个渲染帧内的多次commit的DOM改动会被合并渲染</code></li>
<li><code>耗时js会造成丢帧</code></li>
<li><code>避免交错读写样式可以提高渲染效率</code></li>
</ul>
</li>
</ul>
<h2 data-id="heading-7">(6) 加载css会造成阻塞DOM树的解析和渲染吗？</h2>
<ul>
<li>css不会阻塞DOM树的解析</li>
<li>css会阻塞DOM树的渲染</li>
<li>css会阻塞js的执行，因为js要等待css加载完毕才能保证js可以操作样式</li>
<li>总结
<ul>
<li><strong><code>css不会阻塞DOM-tree的解析，但是css会阻塞DOM-tree的渲染，css还会阻塞js执行，因为js需要等到css解析完成后，js才能操作样式，本质上因为html，css，js都是在主线程中执行的，三者是互斥关系</code></strong></li>
<li>dom渲染依赖于 => js执行完毕 => js执行依赖于 => css执行完毕</li>
</ul>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cc4b72160de4143b1d094aac9f45ee7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">(7) React15存在的问题</h2>
<p>当存在大量的js计算时，当时间超过了16ms时页面没法得到及时更新，就会出现卡顿</p>
<ul>
<li>当 ( <strong><code>setState</code></strong> ) 时，React会遍历应用的所有节点，找出差异，再更新页面，整个过程 ( <strong><code>不能被打断</code></strong> )，如果元素过多，整个处理过程就可能超过16ms，造成掉帧，出现卡顿</li>
<li>dom-diff过程
<ul>
<li>dom-diff也是如此 ( 递归对比 )
<ul>
<li>节点树很庞大时，会导致 ( 递归调用 ) 的 ( 函数调用栈 ) 越来越深</li>
<li>整个diff过程不能被 ( 中断 )，页面会等待递归调用完成后才重新渲染</li>
</ul>
</li>
</ul>
</li>
</ul>
<h2 data-id="heading-9">(8) createElement 和 ReactElement 源码</h2>
<ul>
<li>文件位置：<code>package/react/src/ReactElement.js</code></li>
<li>在react写jsx语法，是不能直接被浏览器解析的，需要经过babel编译成js，编译后会转成React.createElement()这样的形式，如下图
<ul>
<li><strong>jsx => 编译成函数式语法 - 如下图</strong></li>
</ul>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61a374b1645d4a979aa3eb63efe62138~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">(8.1) createElement</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwoow-wu7" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/woow-wu7" ref="nofollow noopener noreferrer">createElement源码分析 - 仓库地址</a></li>
<li>createElement的执行顺序
<ul>
<li>从里到外</li>
<li>从上到下</li>
<li>最终到根时就创建一个ReactElement tree</li>
<li>案例：比如<code>function a()&#123;return <div><p></p></div>&#125;</code></li>
<li>结果：是<code>先创建p的ReactElement，在创建div的ReactElement</code></li>
</ul>
</li>
</ul>
<pre><code class="copyable">createElement
-------
export function createElement(type, config, children) &#123;
   ...
   return ReactElement(
        type,
        key,
        ref,
        self,
        source,
        ReactCurrentOwner.current,
        props,
   );
&#125;
// React.createElement() 返回一个ReactElement对象，即特定格式的js对象
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">(8.2) ReactElement</h3>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fwoow-wu7" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/woow-wu7" ref="nofollow noopener noreferrer">ReactElement源码分析 - 仓库地址</a></li>
</ul>
<pre><code class="copyable">ReactElement
------- 
const ReactElement = function(type, key, ref, self, source, owner, props) &#123;
  const element = &#123;
    // This tag allows us to uniquely identify this as a React Element
    // $$typeof 这个标签允许我们唯一地将其标识为React元素
    // const symbolFor = Symbol.for;
    // REACT_ELEMENT_TYPE = symbolFor('react.element');
    $$typeof: REACT_ELEMENT_TYPE,

    // Built-in properties that belong on the element
    // element的内置属性
    type: type,
    key: key,
    ref: ref,
    props: props,

    // Record the component responsible for creating this element.
    // 记录负责创建此元素的组件
    _owner: owner,
  &#125;;
  ...
  return element;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">(9) React.Children</h2>
<ul>
<li>文件位置：<code>package/react/src/React.js</code></li>
</ul>
<pre><code class="copyable">const Children = &#123;
  map, // 其实就是 mapChildren() 函数 => 在children里的每个直接子节点上调用一个函数，并将 this 设置为 thisArg，直接子节点是null和undefined直接返回null和undefined，否则返回一个数组
  forEach,
  count, // 返回 children 中组件的总数量，等同于 map 和 forEach 循环的次数
  toArray, // 将 children 这个复杂的数据结构以 ( 数组 ) 的方式 ( 扁平展开并返回 )，并为每个子节点分配一个 ( key ) => 可以为自节点排序等
  only, // 验证 children是否只有一个子节点，true则返回这个节点，false则报错
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">(二) Fiber</h1>
<h2 data-id="heading-14">(2.0) Fiber 中的一些概念</h2>
<h3 data-id="heading-15">(2.0.0) react应用执行的整体过程</h3>
<ul>
<li>render阶段
<ul>
<li>会分别为节点执行 <code>beginWork</code> 和 <code>completeWork</code></li>
<li>计算 <code>state</code>，对比<code>节点差异</code>，为节点赋值相应的 <code>effectTag ( 即DOM节点的增删改查 )</code></li>
<li>在render阶段的结尾，会形成 <code>effectList</code> 链表，该链表中的所有fiber节点都是带有副作用的</li>
<li>----------- <code>reconciler调和器 - 在render阶段执行</code> -------------</li>
</ul>
</li>
<li>commit阶段
<ul>
<li>遍历 <code>effect-list</code> ，执行对应的DOM操作，或执行部分生命周期钩子函数</li>
<li>----------- <code>renderer渲染器 - 在commit阶段执行</code> ----------------</li>
</ul>
</li>
<li>执行过程总结：
<ul>
<li>1.不同的任务在 ( scheduler调度器中进行优先级排序 ) --------------------- render阶段</li>
<li>2.优先级更高的任务，会优先进入 ( reconciler调和器中 ) ------------------- render阶段</li>
<li>3.reconciler处理完后的任务，会进入 ( renderer渲染器中渲染成真实的ui ) -- commit阶段</li>
</ul>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6961d198903f4217b80eaecd5eaa1fd3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-16">(2.0.1) scheduler 调度器</h3>
<ul>
<li>核心作用
<ul>
<li>为了达到使 fiber-reconciler 每执行一段时间就把控制权交回给浏览器，我们就需要一个 ( <code>调度器Scheduler</code> ) 来进行 ( <code>任务分配</code> )，( <strong><code>排序优先级，让优先级更高的任务先进行reconciler</code></strong> )</li>
<li>react15没有scheduler，任务都没有优先级，也不能被中断，不能排序，只能一次性同步执行</li>
</ul>
</li>
<li>优先级通过什么来表示？
<ul>
<li>在 ( <strong><code>scheduler</code></strong> ) 中每个任务的 ( <strong><code>优先级</code></strong> ) 都是通过 ( <strong><code>过期时间</code></strong> ) 来表示的</li>
<li>( 过期时间 ) 距离 ( 现在的时间 ) 越近，表示 ( 优先级越高 )</li>
</ul>
</li>
<li>timerQueue 和 taskQueue
<ul>
<li><code>timerQueue</code>
<ul>
<li>存放 ( 没有过期的任务 )</li>
</ul>
</li>
<li><code>taskQueue</code>
<ul>
<li>存放 ( 已经过期的任务 )</li>
</ul>
</li>
<li>小顶堆
<ul>
<li>小顶堆也叫小根堆</li>
<li>小顶堆：即在 ( 完全二叉树 ) 中 ( 每个节点的值都小于或等于其左右孩子的值 )</li>
<li>timerQueue和taskQueue都是 ( 小顶堆 )，所以取出来的任务都是距离现在时间的过期时间最短的任务，即 ( 取出的任务都是优先级最高的任务 )，然后优先执行它</li>
</ul>
</li>
</ul>
</li>
<li>优先级高的任务 (比如：键盘输入) 可以打断优先级低的任务 (比如：diff)
<ul>
<li>
<ol>
<li>( 输入事件 )</li>
</ol>
</li>
<li>
<ol start="2">
<li>( 定时器 )，检查定时器是否到点，到点则执行回调函数</li>
</ol>
</li>
<li>
<ol start="3">
<li>( 开始帧 ) Begin Frame，即每一帧的事件，包括 ( window.resize ) ( scroll ) ( media )</li>
</ol>
</li>
<li>
<ol start="4">
<li>( 请求动画帧 ) requestAnimationFrame，即在每次绘制前，会执行requestAnimationFrame的回调</li>
</ol>
</li>
</ul>
</li>
</ul>
<pre><code class="copyable">// 源码位置：packages/react-reconciler/ReactFiberLane.new.js

// 优先级越高，位数就越少
// 优先级越低，位数就越高
// 可以用赛道比喻，如果一直占用内道，那就越快
// 这里的所有任务 ( 从上往下 ) 优先级越低，比如 SyncLane > InputContinuousHydrationLane

export const SyncLane: Lane = /*                        */ 0b0000000000000000000000000000001;

export const InputContinuousHydrationLane: Lane = /*    */ 0b0000000000000000000000000000010;
export const InputContinuousLane: Lanes = /*            */ 0b0000000000000000000000000000100;

export const DefaultHydrationLane: Lane = /*            */ 0b0000000000000000000000000001000;
export const DefaultLane: Lanes = /*                    */ 0b0000000000000000000000000010000;

const TransitionHydrationLane: Lane = /*                */ 0b0000000000000000000000000100000;
const TransitionLanes: Lanes = /*                       */ 0b0000000001111111111111111000000;
const TransitionLane1: Lane = /*                        */ 0b0000000000000000000000001000000;
const TransitionLane2: Lane = /*                        */ 0b0000000000000000000000010000000;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92b7c267f1304f72a0ade5c64a606a26~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">(2.0.2) reconciler 调和器</h3>
<ul>
<li>核心作用
<ul>
<li>找出哪些节点发生了改变，并打上不同的tag</li>
<li>在render/reconciliation阶段过程中，让优先级更高的任务先执行，该过程可以被打断</li>
<li>在commit阶段一次性的批量更新，该过程不能被打断</li>
</ul>
</li>
<li>reconciler执行时机
<ul>
<li>reconciler发生在 ( render ) 阶段</li>
<li>( <strong>render阶段</strong> ) 再次划分为两个阶段
<ul>
<li><strong>beginWork</strong></li>
<li><strong>completeWork</strong></li>
</ul>
</li>
</ul>
</li>
<li>reconciler
<ul>
<li>旧版中的reconciler => <code>stack reconciler</code> ------------ 递归</li>
<li>新版中的reconciler => <code>fiber reconciler</code> ------------ 循环</li>
</ul>
</li>
<li>stack reconciler
<ul>
<li><strong>stack reconciler 不能被打断</strong></li>
</ul>
</li>
<li>fiber reconciler
<ul>
<li><strong>fiber reconciler 每执行一段时间都会将控制权交回给浏览器</strong>
<ul>
<li>fiber reconciler 在执行过程中可分为 ( 两个阶段 )
<ul>
<li>阶段一 ( render/reconciliation )
<ul>
<li><code>生成fiber树，得出需要更新的节点信息，可以被打断，让优先级高的任务先执行</code></li>
<li>通过 scheduler 执行器来完成</li>
</ul>
</li>
<li>阶段二 ( commit )
<ul>
<li><code>将需要更新的节点一次批量更新，不能被打断</code></li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-18">(2.0.3) renderer 渲染器</h3>
<ul>
<li>核心作用
<ul>
<li>将reconciler中打好标签的节点，渲染到视图上</li>
</ul>
</li>
<li>renderer渲染器执行时机
<ul>
<li><code>renderer是commit阶段执行的</code></li>
</ul>
</li>
</ul>
<h3 data-id="heading-19">(2.0.4) currentTree 和 workInProgressTree</h3>
<ul>
<li><strong>currentTree</strong>
<ul>
<li>第一次渲染后，react最终得到一个fiber-tree，它反映了用于渲染的ui的应用程序的 ( 状态 )，这颗树叫 ( current-tree )</li>
</ul>
</li>
<li><strong>workInProgressTree</strong>
<ul>
<li>react开始处理更新时，他会根据fiber-current-tree和virtual-tree生成 ( workInProgressTree )，它 反映了要刷新到屏幕的 ( 未来状态 )</li>
<li>所有任务都在fiber-workInProgressTree的fiber上执行，<code>当react遍历current-tree时，对于每个现有fiber节点，他会使用render方法返回react元素中的数据，创建一个备用节点(fiber=alternate)，这些节点用于构成 workInProgressTree(备用 tree)，处理完更新并完成相关工作后，react将备用tree刷新到屏幕，一旦这个workInProgressTree在屏幕上呈现，就会变成current-tree</code></li>
<li>每个 ( fiber ) 节点，都会通过 ( alternate ) 属性保持对另一个树对应节点的引用
<ul>
<li>currentTree中的节点指向workInProgressTree的备用节点，反之亦然</li>
</ul>
</li>
</ul>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80816ad2e1d540ca989f26a0afa6e9de~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<h3 data-id="heading-20">(2.0.5) FiberRootNode 和 rootFiber</h3>
<ul>
<li>fiberRoot
<ul>
<li>fiberRoot指整个应用的根节点，有且只有一个</li>
<li>fiberRootNode的current指针指向完成了的workInProgressTree，current指向workInProgressTree后就变成了currentTree</li>
</ul>
</li>
<li>rootFiber
<ul>
<li>React.render() 创建出来的节点，可以有多个</li>
</ul>
</li>
</ul>
<h3 data-id="heading-21">(2.0.6) fiber对象</h3>
<ul>
<li>文件位置：packages/react-reconciler/src/ReactFiber.new.js</li>
<li>每一个react元素，对应一个fiber对象，一个fiber对象通常表示一个work的基本单元，fiber对象有几个属性，这些属性指向其他的fiber对象
<ul>
<li><strong>child</strong> <strong>sibling</strong> <strong>return</strong>
<ul>
<li><code>child指向子节点</code></li>
<li><code>sibling指向兄弟节点</code></li>
<li><code>return指向父节点</code></li>
</ul>
</li>
<li>fibers可以理解为
<ul>
<li>( 一个包含react元素上下文信息的 - 数据域节点)</li>
<li>( 以及由child，sibling，return等 指针域构成的 - 链表结构 )</li>
</ul>
</li>
<li>fiber可以保存真实的DOM
<ul>
<li>通过fiber对象的 ( <code>stateNode</code> ) 属性保存着真实的DOM信息</li>
</ul>
</li>
<li>遍历
<ul>
<li>遍历时，<code>深度优先原则，先children，再sibling，再找叔叔</code></li>
</ul>
</li>
</ul>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cfce62710334b55ac7d13fe63d43c50~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<h2 data-id="heading-22">(2.1) Fiber的特点</h2>
<ul>
<li>可以 ( 暂停 ) 工作，并在之后 ( 返回 ) 再次开始</li>
<li>可以为不同类型的工作，设置 ( 优先级 )</li>
<li>( 复用 ) 之前已经完成的工作</li>
<li>( 终止 ) 已经不再需要的工作</li>
</ul>
<h2 data-id="heading-23">(2.2) Fiber reconciler 执行的阶段</h2>
<h4 data-id="heading-24">(1) 阶段一 ------------ reconciliation阶段 ( 调和render )</h4>
<ul>
<li>进行diff运算，生成fiber树，可以被打断</li>
<li>( <code>fiber树</code> ) 是在 ( <code>virtualDOM树</code> ) 的基础上添加 ( <code>额外信息</code> ) 生成，本质上是一个 ( <strong><code>链表</code></strong> )</li>
<li>fiber树
<ul>
<li>( current树 ) 和 ( workInProgress树 ) 被称为 ( fiber双缓存 )</li>
<li><strong>current树</strong>
<ul>
<li>fiber树的生成 (  当前树 )</li>
<li>fiber树在首次渲染时会一次性生成</li>
</ul>
</li>
<li><strong>workInProgress树</strong>
<ul>
<li>fiber树的新生成 ( 工作进程树 )</li>
<li>在fiber树在首次渲染一次性生成后，在后续需要 ( diff ) 的时候，遍历fiber-current树时，会为每一个存在的fiber节点创建一个 ( 替代节点 )，这些替代节点节点组成的树就是 ( workInProgressTree )</li>
<li><code>这颗新树，每生成一个新的节点，都会把控制权交回给浏览器的主线程，去检查有没有优先级更高的任务需要执行</code>
<ul>
<li>如果没有---优先级更高的任务，则继续构建</li>
<li>如果有-----优先级更高的任务，fiber reconciler 会丢弃正在生成的树，在空闲时再从新生成一遍</li>
</ul>
</li>
<li>在构建fiber树的过程中，( <code>fiber-reconciler</code> ) 会将 ( <code>需要更新的节点信息</code> ) 保存在 ( <code>effect list</code> ) 中，在 ( <code>阶段二</code> ) 执行的时候，( <code>批量的更新</code> ) 相应的节点</li>
</ul>
</li>
<li>currentTree和workInProgressTree如何关联？
<ul>
<li>( current树 ) 和 ( workInProgree树 ) 通过 ( alternate ) 相连</li>
</ul>
</li>
<li>为什么要生成currentTree和workInProgressTree??
<ul>
<li>主要原因是为了避免 ( 更新丢失 )</li>
</ul>
</li>
</ul>
</li>
<li>scheduler
<ul>
<li>如何才能使 fiber-reconciler 每执行一段时间就把控制权交回给浏览器？</li>
<li>需要一个 ( <code>scheduler</code> ) 调度器，来完成 ( <code>任务分配</code> )，可以简单的理解为 ( <code>在什么时候确定执行work的过程</code> )</li>
<li>任务的优先级一共有 ( 6 ) 种
<ul>
<li><strong>synchronous</strong>：与之前的 stack reconciler一样，同步执行</li>
<li><strong>task</strong>：在next tick之前执行</li>
<li><strong>animation</strong>：在下一帧前执行</li>
<li><strong>high</strong>：在不久的将来立即执行</li>
<li><strong>low</strong>：稍微延迟执行也没关系</li>
<li><strong>offscreen</strong>：下一次render或者scroll时才执行</li>
</ul>
</li>
<li>优先级高的任务 (比如：键盘输入) 可以打断优先级低的任务 (比如：diff)
<ul>
<li>
<ol>
<li>( 输入事件 )</li>
</ol>
</li>
<li>
<ol start="2">
<li>( 定时器 )，检查定时器是否到点，到点则执行回调函数</li>
</ol>
</li>
<li>
<ol start="3">
<li>( 开始帧 ) Begin Frame，即每一帧的事件，包括 ( window.resize ) ( scroll ) ( media )</li>
</ol>
</li>
<li>
<ol start="4">
<li>( 请求动画帧 ) requestAnimationFrame，即在每次绘制前，会执行requestAnimationFrame的回调</li>
</ol>
</li>
</ul>
</li>
</ul>
</li>
<li>Effect list
<ul>
<li>effect list 可以理解为是一个 ( 存储effectTag副作用的列表容器 )</li>
<li>它是由 ( fiber节点 ) 和 ( nextEffect指针 ) 构成的 ( <strong><code>单向链表</code></strong> )，还包括第一个节点的 （ firstEfflect ) 和 最后一个节点的 ( lastEfflect )</li>
<li>react采用 ( <code>深度优先</code> ) 搜索算法，在render阶段遍历fiber树时，把 ( <code>每个有副作用的fiber筛选出来</code> )， ( 有副作用的意思是比如：<code>有更新有改动</code> )，即把有变化的节点筛选出来，最后构建生成一个 ( <code>只带副作用的effect list 链表</code> )</li>
<li>在commit阶段，react拿到effect list节点后，遍历 effect list 节点，并且根据每一个 effect 节点的 ( <strong><code>EffectTag类型</code></strong> )，从而对相应的 dom 树进行修改</li>
</ul>
</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ab16fa14ab04e6c8b1c5e73610910e0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01493af6317e4a56ae273bba9971f1bf~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>案例：阶段一(render/reconciliation阶段)</li>
</ul>
<pre><code class="copyable">function App() &#123;
  return (
    <div>
      xiao
      <p>chen</p>
    </div>
  )
&#125;
ReactDOM.render(<App />, document.getElementById("root"));
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56b2636f4c7c42cea482183bd6f7c407~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>上图-图示说明
<ul>
<li>fiberRootNode 和 rootFiber
<ul>
<li>fiberRoot只有一个，表示整个应用的根节点</li>
<li>rootFiber可以有多个，通过React.render()生成</li>
<li>rootFiber就是一个fiber对象，其中的 stateNode 属性指向的是真实的DOM，即FiberRootNode</li>
<li>FiberRootNode是一个真实的DOM节点，通过 current 属性指向 rootFiber</li>
</ul>
</li>
<li>currentTree 和 workInProgressTree
<ul>
<li>两者通过 <code>alternate</code> 相连</li>
<li>fiber节点的 child指向子节点，sibling指向兄弟节点，return指向父节点</li>
<li>currentTree和workInProgressTree称为 ( fiber双缓存 )</li>
</ul>
</li>
<li>fiberRootNode的current指针的指向
<ul>
<li>正在创建的fiber树，我们叫做workInProgressTree</li>
<li>当workInProgressTree创建完成后，fiberRootNode的<code>current指针</code>会从currentTree指向workInProgressTree，那么现在 workInProgressTree 就成了新的 currentTree</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-25">(2) 阶段二 ------------ commit阶段</h4>
<ul>
<li>将阶段一中结算出来的 ( 需要更新的节点 ) ( 一次性的批量更新 )，该过程 ( 不能被打断 )</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab457174d141429b9d961ba5226e3368~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-26">参考资料</h1>
<ul>
<li>
<p>浏览器 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000022633988" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000022633988" ref="nofollow noopener noreferrer">segmentfault.com/a/119000002…</a></p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FPerformance%2FHow_browsers_work" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/Performance/How_browsers_work" ref="nofollow noopener noreferrer">浏览器渲染过程MDN</a></p>
</li>
<li>
<p>16ms渲染帧 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgetpocket.com%2Fread%2F2371119921" target="_blank" rel="nofollow noopener noreferrer" title="https://getpocket.com/read/2371119921" ref="nofollow noopener noreferrer">getpocket.com/read/237111…</a></p>
</li>
<li>
<p>加载css会造成DOM树的解析和渲染吗 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000018130499" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000018130499" ref="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p>
</li>
<li>
<p>React-biber的原理 <a href="https://juejin.cn/post/6844904202267787277" target="_blank" title="https://juejin.cn/post/6844904202267787277">juejin.cn/post/684490…</a></p>
</li>
<li>
<p>走进fiber的世界 <a href="https://juejin.cn/post/6937560479795511303" target="_blank" title="https://juejin.cn/post/6937560479795511303">juejin.cn/post/693756…</a></p>
</li>
<li>
<p>fiber源码解析 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000023573713" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000023573713" ref="nofollow noopener noreferrer">segmentfault.com/a/119000002…</a></p>
</li>
<li>
<p>react源码解析 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fd56b907c05f1" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/d56b907c05f1" ref="nofollow noopener noreferrer">www.jianshu.com/p/d56b907c0…</a></p>
</li>
<li>
<p>人人都能读懂的react源码 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiaochen1024.com%2Farticle_item%2F600aca0cecf02e002e6db56c" target="_blank" rel="nofollow noopener noreferrer" title="https://xiaochen1024.com/article_item/600aca0cecf02e002e6db56c" ref="nofollow noopener noreferrer">xiaochen1024.com/article_ite…</a></p>
</li>
<li>
<p>手写render <a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F355884903" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/355884903" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/355884903</a></p>
</li>
</ul></div>  
</div>
            