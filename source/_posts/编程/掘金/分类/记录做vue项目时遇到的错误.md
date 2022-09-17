
---
title: '记录做vue项目时遇到的错误'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b5062636e564d6c90333c5efa7ce751~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 23:27:09 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b5062636e564d6c90333c5efa7ce751~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文已参与「新人创作礼」活动，一起开启掘金创作之路。</p>
</blockquote>
<h3 data-id="heading-0">一、echarts图表第一次进入页面显示正常，返回上一页再进入此页面或者其他页面相同但数据不同的页面时，图表显示不出</h3>
<p>参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.i4k.xyz%2Farticle%2Fqq_39075021%2F113337993" target="_blank" rel="nofollow noopener noreferrer" title="https://www.i4k.xyz/article/qq_39075021/113337993" ref="nofollow noopener noreferrer">解决 Echarts 图表在旧容器上重新渲染不出来的问题</a></p>
<p>因为init后会给图表容器附加一个<code>_echarts_instance_</code>属性，因此需要每次进入页面重新渲染图表之前去除图表容器上的<code>_echarts_instance_</code>属性</p>
<p>例如我有一个id为myCanvas的图表</p>
<pre><code class="hljs language-ini copyable" lang="ini">var <span class="hljs-attr">chartEle</span> = document.getElementById(<span class="hljs-string">"myCanvas"</span>)<span class="hljs-comment">;//取到这个元素</span>
chartEle.removeAttribute("_echarts_instance_")<span class="hljs-comment">;//去除_echarts_instance_属性</span>
var <span class="hljs-attr">chart</span> = this.<span class="hljs-variable">$echarts</span>.init(chartEle)<span class="hljs-comment">;//初始化</span>
var <span class="hljs-attr">option</span> = &#123;图表配置内容&#125;<span class="hljs-comment">;//图表配置</span>
chart.setOption(option)<span class="hljs-comment">;//将配置附加给chart</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">二、使用vue3部署服务器后刷新404问题</h3>
<p>参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F361c24365e13" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/361c24365e13" ref="nofollow noopener noreferrer">Vue的服务器配置（解决刷新404问题）</a></p>
<p>vue3项目的router是history模式，我也不知道怎么改hash，但是history模式地址栏地址好看一些，hash的地址中间带#，不美观，索性想解决刷新404问题</p>
<p>我一直使用的是nginx，所以我就只记录nginx的解决办法了，设置伪静态，将以下代码添加进去即可</p>
<p>如果使用宝塔面板部署，直接在伪静态那一栏加上下面的就行</p>
<pre><code class="hljs language-bash copyable" lang="bash">location / &#123;
  try_files <span class="hljs-variable">$uri</span> <span class="hljs-variable">$uri</span>/ /index.html;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果直接手动nginx部署，就在nginx的配置文件中的</p>
<pre><code class="hljs copyable">location / &#123;原有的不用动&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>里面加上<code>try_files $uri $uri/ /index.html;</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b5062636e564d6c90333c5efa7ce751~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="示例图" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">三、Node Sass does not yet support your current environment: Windows 64-bit with Unsupported runtime (93)</h3>
<p>今天更新了nodejs到16版本，然后按照之前的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fsywdebug%2Farticle%2Fdetails%2F121709088%3Fspm%3D1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/sywdebug/article/details/121709088?spm=1001.2014.3001.5502" ref="nofollow noopener noreferrer">使用vue-cli4，vue3，js项目安装乱七八糟要使用的依赖插件等</a>文章安装的sass版本不能用了，所以会报这个错误</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c006a1e0a77744f7aafc837c582bd95d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt="node-sass错误" loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决也很简单，把原来的node-sass和sass-loader删除安装合适的版本即可</p>
<p>使用以下命令卸载</p>
<pre><code class="hljs copyable">npm uninstall node-sass sass-loader
<span class="copy-code-btn">复制代码</span></code></pre>
<p>适合的版本网上都能搜到不用浪费时，使用以下命令安装即可</p>
<pre><code class="hljs language-sql copyable" lang="sql">npm install node<span class="hljs-operator">-</span>sass<span class="hljs-variable">@6</span>.x sass<span class="hljs-operator">-</span>loader<span class="hljs-variable">@10</span>.x <span class="hljs-comment">--save-dev</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">四、TypeError: Cannot read properties of undefined (reading 'NormalModule')</h3>
<p>上面操作不知道为啥就报这个错了，删除<code>package-lock.json文件</code>和<code>node_modules文件夹</code>重新<code>npm install</code>即可</p>
<p>遇事不决删<code>package-lock.json文件</code>和<code>node_modules文件夹</code>重新<code>npm install</code></p>
<p>后续有其他继续更新</p>
<h1 data-id="heading-4">❀❀❀❀❀❀完结散花❀❀❀❀❀❀</h1>
<div align="right">Written ❤️ sywdebug.</div></div>  
</div>
            