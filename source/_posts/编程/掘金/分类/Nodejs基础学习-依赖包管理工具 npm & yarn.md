
---
title: 'Node.js基础学习-依赖包管理工具 npm & yarn'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4319'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 07:56:36 GMT
thumbnail: 'https://picsum.photos/400/300?random=4319'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>这是我参与8月更文挑战的第13天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<blockquote>
<p>学习贵在坚持, 笔记是灵魂, 温故而知新, 时不时翻一翻, 回顾一下知识点, 加深记忆, 事半功倍!</p>
</blockquote>
<p>这里记录一些学习 <code>Node.js</code> 的笔记, 日积月累, 后续会有记录学习更多, 一起来看看吧--</p>
<blockquote>
<p>本文学习 <code>node.js</code> 的包管理工具 <code>npm</code>& <code>yarn</code> 的使用</p>
</blockquote>
<h2 data-id="heading-0">使用 <code>npm</code> 共享项目 ：</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/" ref="nofollow noopener noreferrer">npm 官网: npmjs.com</a></p>
<p>在 <code>npm.js</code> 上注册一个账号：</p>
<h2 data-id="heading-1">一、使用 npm </h2>
<ul>
<li>第一步 ：  首先在官网上注册一个账号</li>
<li>第二步 ： 要进行账号的邮箱验证</li>
<li>第三步 ： 存好账号和密码</li>
</ul>
<h2 data-id="heading-2">二、将 node 项目变成一个包  </h2>
<p>npm init   要求 包 名称必须是全网唯一</p>
<h2 data-id="heading-3">三、上传 node 包</h2>
<p>npm  adduser</p>
<h2 data-id="heading-4">四、将本地的包传到线上的仓库中    </h2>
<p>npm publish</p>
<h2 data-id="heading-5">五、下载线上的 node 包   npm install 包名称      npm   i   lichune201807091415</h2>
<p>安装淘宝镜像 ：  <code>npm install -g cnpm --registry=https://registry.npm.taobao.org</code> (了解)</p>
<p>然后将 <code>npm</code> 改成 <code>cnpm</code> 即可</p>
<p>批量安装插件 ：</p>
<p>npm install 会自动去 package.json 包的  dependencies   中去查找 插件名称</p>
<h2 data-id="heading-6"><code>dependencies</code> 与 <code>devDependencies</code> 之间的区别?    </h2>
<ul>
<li>使用 npm install node_module --save 自动更新 dependencies 字段值;       默认</li>
<li>使用 npm install node_module –save-dev 自动更新 devDependencies 字段值;</li>
<li>dependencie 配置当前程序所依赖的其他包。    线上模式所依赖的包管理（生产模式）</li>
<li>devDependencie 配置当前程序所依赖的其他包，只会下载模块，而不下载这些模块的 测试和文档框架     开发模式所依赖的包</li>
</ul>
<h2 data-id="heading-7">npm 的小缺点</h2>
<ul>
<li>包是同步下载的</li>
<li>一个项目下载过一次     在另一个项目中重新下载</li>
</ul>
<h2 data-id="heading-8">Yarn 的入门使用    </h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyarn.bootcss.com" target="_blank" rel="nofollow noopener noreferrer" title="https://yarn.bootcss.com" ref="nofollow noopener noreferrer">Yarn 文档&下载安装 </a></p>
<p><code>Yarn</code> 是一种命令   就是对 <code>npm</code> 命令的包装</p>
<p>安装命令 ：</p>
<pre><code class="hljs language-bash copyable" lang="bash">npm install yarn -g
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9"><code>yarn</code> 的使用 ： </h2>
<ul>
<li>
<p>1、创建一个 yarn 目录</p>
</li>
<li>
<p>2、执行 <code>yarn init</code>  ，输入包的名字   一路回车   用 yarn 把代码变成包 （npm init）</p>
<ul>
<li>传到线上 ： 
    <code>yarn login</code>  ==== <code>npm adduser</code>
    <code>yarn publish</code> === <code>npm publish</code></li>
</ul>
</li>
<li>
<p>3、yarn add cheerio   下载第三方插件包   自带了--save 的特性
      npm install cheerio --save   ====  yarn add cheerio
      npm install cheerio --save-dev ==  yarn add cheerio --dev</p>
</li>
<li>
<p>4、<code>yarn install</code>   ====  <code>npm install</code>   批量安装 package.json 中的所有插件</p>
</li>
<li>
<p>5、<code>yarn update 依赖包名</code>   更新一个依赖包</p>
</li>
<li>
<p>6、<code>yarn remove 依赖包名</code>   删除一个依赖包</p>
</li>
</ul>
<h3 data-id="heading-10"><code>yarn</code> 的好处 ：</h3>
<ul>
<li><code>yarn</code> 是异步的     安装起来比 <code>npm</code> 快</li>
<li><code>yarn</code> 可以有效的保证版本号一致   开发的时候不容易出错</li>
<li><code>yarn</code>   本地的已经安装过的包会有缓存   在其它项目中安装时直接调用缓存中的包   会非常的快</li>
</ul>
<h2 data-id="heading-11">更多阅读</h2>
<blockquote>
<p>更多更文阅读请查收:</p>
<p><a href="https://juejin.cn/post/6995865258040492068" target="_blank" title="https://juejin.cn/post/6995865258040492068">【Node.js】安装&文档</a>、</p>
<p><a href="https://juejin.cn/post/6995198740910833672" target="_blank" title="https://juejin.cn/post/6995198740910833672">【Github】多人协作(二)</a>、</p>
<p><a href="https://juejin.cn/post/6995198740910833672" target="_blank" title="https://juejin.cn/post/6995198740910833672">【Github】基本使用(一)</a>、</p>
<p><a href="https://juejin.cn/post/6994399125328363557" target="_blank" title="https://juejin.cn/post/6994399125328363557">【Git】代码版本控制-git 初识&基本操作(一)</a>、
<a href="https://juejin.cn/post/6994463359122800676" target="_blank" title="https://juejin.cn/post/6994463359122800676">【Git】进阶(二)</a>、</p>
<p><a href="https://juejin.cn/post/6991862465696890910" target="_blank" title="https://juejin.cn/post/6991862465696890910">【Node.js】搭建自动化开发环境-基本介绍</a>、
<a href="https://juejin.cn/post/6992604387285663774" target="_blank" title="https://juejin.cn/post/6992604387285663774">【工具准备】</a>、
<a href="https://juejin.cn/post/6992628930775613448" target="_blank" title="https://juejin.cn/post/6992628930775613448">【开工】</a>、
<a href="https://juejin.cn/post/6993347133545906183" target="_blank" title="https://juejin.cn/post/6993347133545906183">【详细步骤(四)】</a>、
<a href="https://juejin.cn/post/6993713613575815199" target="_blank" title="https://juejin.cn/post/6993713613575815199">【模块处理工具(五)】</a>、
<a href="https://juejin.cn/post/6993730948235804680" target="_blank" title="https://juejin.cn/post/6993730948235804680">【模块化编程的理解】</a>、</p>
</blockquote>
<h2 data-id="heading-12">跟上节奏, 一步一步! 下文更新预告:</h2>
<p>接下来会继续详细学习 <code>Node.js</code> 的一些工具 <code>nvm</code> 等等. 冲鸭!! xdm</p>
<p>提高开发效率, 为我们的开发提效赋能!</p>
<p>跟上前进的步伐, 向前加油</p>
<p>加油!! go~~</p></div>  
</div>
            