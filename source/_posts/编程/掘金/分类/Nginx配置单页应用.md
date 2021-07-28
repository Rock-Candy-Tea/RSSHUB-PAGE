
---
title: 'Nginx配置单页应用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8802'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 18:19:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=8802'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>上一期我们讲了如何在一个新服务器上用Nginx跑起一个前端项目，但是还有很多缺陷，比如我们想在这个Nginx下跑多个项目怎么办，spa单页项目常见的刷新空白原因及处理等等，本篇将一一介绍。</p>
<h2 data-id="heading-0">同端口多项目配置</h2>
<p>假设我们有两个单页项目，一个pc官网，一个mobile官网，我们都想跑在上期8082端口上，这时候发现我们上一期部署的文件夹是直接放在<code>www</code>目录下的，这可不行，文件全放这下面都不能区分是哪个项目的了，万一文件夹或者文件名字一样，就覆盖掉了。</p>
<p>那么有两种方案：</p>
<ol>
<li>各大cli脚手架上都有输出文件夹的设置，比如vue-cli的<code>outputDir</code>，这个可以设置文件夹名。</li>
<li>在www目录下新建对应项目的文件夹，scp上传上传到对应文件夹。</li>
</ol>
<p>这里我们使用一下方案1，方案二类似，路径不同而已。</p>
<h3 data-id="heading-1">修改打包配置</h3>
<p>由于我们是在同一个端口下跑的项目，那么我们只能通过路径区分不同项目。</p>
<p>比如我们的项目在<code>http://localhost:8082/mobile</code>下跑，那么vue-router添加base配置：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: <span class="hljs-string">'/mobile'</span>, <span class="hljs-comment">// pc同理</span>
  ...
)&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然我更建议你把这个路径值放入.env文件里，<code>.env.dev</code>:</p>
<pre><code class="hljs language-js copyable" lang="js">BASE_URL=/mobile
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改配置为：</p>
<pre><code class="hljs language-jsx copyable" lang="jsx"><span class="hljs-keyword">new</span> VueRouter(&#123;
  <span class="hljs-attr">mode</span>: <span class="hljs-string">'history'</span>,
  <span class="hljs-attr">base</span>: process.env.BASE_URL,
  ...
)&#125;

<span class="hljs-comment">// history: createWebHistory(process.env.BASE_URL) // 4.0+</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vue.config.js：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">publicPath</span>: process.env.BASE_URL,  <span class="hljs-comment">// 这个是打包后外部文件链接追加值，比如'/mobile'，那么最后的js和css链接为'/mobile/js/xxxx.js'</span>
  <span class="hljs-attr">outputDir</span>: <span class="hljs-string">'mobile'</span>, <span class="hljs-comment">// 这个是打包输出文件夹名</span>
  ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>进行项目打包，会得到一个mobile文件夹，我们使用scp进行文件上传（pc同理）</p>
<pre><code class="hljs language-shell copyable" lang="shell">scp -r ./mobile root@$host:~/nginx/www/;  # 上传mobile文件
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">Nginx配置修改</h3>
<pre><code class="hljs language-nginx copyable" lang="nginx"><span class="hljs-attribute">location</span> /pc &#123;
  <span class="hljs-attribute">alias</span>   /usr/share/nginx/html/pc/;
  <span class="hljs-attribute">index</span>  index.html;
&#125;

<span class="hljs-attribute">location</span> /mobile &#123;
  <span class="hljs-attribute">alias</span>   /usr/share/nginx/html/mobile/;
  <span class="hljs-attribute">index</span>  index.html;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>重启nginx，<code>docker restart web</code>，此时访问<code>http://localhost:8082/mobile/</code>，网页能正常打开，当时我们访问<code>http://localhost:8082/mobile</code>却发现被诡异的重定向到了80端口，也就是<code>http://localhost/mobile/</code>，查看一下浏览器请求发现被301永久重定向了。</p>
<p>这是由于Nginx在访问URI时；如果访问资源为一个目录，且结尾没有<code>/</code>，那么Nginx会进行一个301重定向到结尾带有'/'的地址，跳转时可以通过<code>port_in_redirec</code>设置跳转端口号，没有的话则从<code>listen</code>里取，也就是80，故这里进行了80的重定向，我们可以在<code>server</code>模块中添加<code>absolute_redirect off;</code>关闭这个重定向。</p>
<p>设置之后重启Nginx，我们通过<code>http://localhost/mobile</code>和<code>http://localhost/pc</code>都能访问对应项目。</p>
<h2 data-id="heading-3">spa单页跳转刷新白屏</h2>
<p>我们在上面进行了多项目配置，但是还有一个问题没有解决，这个问题很常见，就是跳转后刷新的白屏问题，很多同学不敢从hash路由切换到history路由也是有此原因。</p>
<p>简单描述一下问题吧：我们直接打开项目的根路径地址访问正常，比如上面的<code>http://localhost/mobile</code>，刷新也正常显示，我们点击跳转到<code>http://localhost/mobile/list</code>，此时也正常跳转，但是我们在这个地址进行原地刷新时，会出现404错误，或者说我们直接用浏览器打开<code>http://localhost/mobile/list</code>也会出现404，这个问题呢算比较严重的了，也就是我们能直接打开或者刷新的只有根路径，其他路径都会出现404的问题。</p>
<h3 data-id="heading-4">404的原因</h3>
<p>首先我们的网页访问都是一个get请求，你可以理解为获取一个静态资源，我们看一下Nginx的location配置：</p>
<pre><code class="hljs language-nginx copyable" lang="nginx"><span class="hljs-attribute">location</span> /pc &#123;
  <span class="hljs-attribute">alias</span>   /usr/share/nginx/html/pc/;
  <span class="hljs-attribute">index</span>  index.html;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们的URI地址匹配到了/pc，会在alias的路径中查找，默认文件去找index指令后面的的index.html，比如我们访问<code>http://localhost/mobile</code>能正常访问，是因为mobile目录下确实有index.html这个实体文件，那么正常返回了，而访问<code>http://localhost/mobile/list</code>，Nginx就会去找<code>mobile/list/index.html</code>，很显然没有这个东西，故返回404。</p>
<p>总结一下就是：spa的路由是由js生成的，并不会有对应路径的实体文件，而Nginx访问网页的实体资源，找不到就会返回404，那么也就是这个路径是交由我们的js来处理，而不是交由Nginx处理，所以我们只需要在Nginx找不到路径的实体文件时把我们的index.html返回回去就行了。</p>
<pre><code class="hljs language-nginx copyable" lang="nginx"><span class="hljs-attribute">location</span> /pc &#123;
  <span class="hljs-attribute">alias</span>   /usr/share/nginx/html/pc/;
  <span class="hljs-attribute">try_files</span> $uri $uri/ /pc/index.html;
  <span class="hljs-attribute">index</span>  index.html;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>try_files</code>指令会依次查找后面的文件，直到找不到，<code>$uri</code>是原地址，<code>$uri/</code>是<code>$uri/index.html</code>，剩下的就是<code>/pc/index.html</code>，举个例子<code>http://localhost/pc/aaa.png</code>，会先去查找<code>http://localhost/pc/aaa.png</code>，找不到的话查询<code>http://localhost/pc/aaa.png/index.html</code>，最后则是<code>http://localhost/pc/index.html</code></p>
<p>ok，这样spa白屏问题就解决了，但是还有一个微小的问题，那就是当我们访问的路径确实不存在（spa-router也没有），路径不是Nginx处理了，那么此时404也就不存在了，会出现白屏，不过聪明的同学已经想到了众多router都会在最后加个通配符来匹配404的页面，那么404的页面也就交给我们自己写了。</p>
<h2 data-id="heading-5">root和alias</h2>
<p>这个算是一个补充吧，说一下<code>root</code>和<code>alias</code>的区别，毕竟很多配置用的<code>root</code>，请注意<code>alias</code>只能在<code>location</code>中使用，而<code>root</code>可以配置在<code>http</code>，<code>server</code>，<code>location</code>中使用。</p>
<p>其实<code>root</code>和<code>alias</code>都是Nginx指定文件路径的指令，以上面的例子：</p>
<pre><code class="hljs language-nginx copyable" lang="nginx"><span class="hljs-comment"># root</span>
<span class="hljs-attribute">location</span> /pc &#123;
  <span class="hljs-attribute">root</span>   /usr/share/nginx/html;
  <span class="hljs-attribute">try_files</span> $uri $uri/ /pc/index.html;
  <span class="hljs-attribute">index</span>  index.html;
&#125;
<span class="hljs-comment"># alias</span>
<span class="hljs-attribute">location</span> /pc &#123;
  <span class="hljs-attribute">alias</span>   /usr/share/nginx/html/pc/;
  <span class="hljs-attribute">try_files</span> $uri $uri/ /pc/index.html;
  <span class="hljs-attribute">index</span>  index.html;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这两个的匹配规则一样的，简单来说就是root会把location后面配置的路径加上，alias则是去除掉，也就是说二者的文件路径都是指向根目录下的<code>pc</code>文件夹，也就是说使用<code>root</code>的location匹配的路径必须真实存在（因为追加了），如果<code>root</code>出现404了直接看path的目录是否存在就行了。</p>
<p>不过需要注意一点就是alias的路径结尾需要有个<code>/</code>，虽然这里加不加都没问题，但这是一个良好的习惯，请保持，否则遇到下面这种情况就会出错。以下面例子分别访问<code>http://localhost:8082/image/logo.png</code>，最后一个会404：</p>
<pre><code class="hljs language-nginx copyable" lang="nginx"><span class="hljs-attribute">location</span> /image/ &#123;
  <span class="hljs-attribute">alias</span>   /usr/share/nginx/html/image/;
&#125;
<span class="hljs-attribute">location</span> /image &#123;
  <span class="hljs-attribute">alias</span>   /usr/share/nginx/html/image/;
&#125;
<span class="hljs-attribute">location</span> /image &#123;
  <span class="hljs-attribute">alias</span>   /usr/share/nginx/html/image;
&#125;
<span class="hljs-attribute">location</span> /image/ &#123; <span class="hljs-comment"># 这里会404</span>
  <span class="hljs-attribute">alias</span>   /usr/share/nginx/html/image;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下一篇我会介绍单页应用在Nginx上的加载优化，尽请期待。</p>
<p>本系列更新只有利用周末和下班时间整理，比较多的内容的话更新会比较慢，希望能对你有所帮助，请多多star或点赞收藏支持一下</p>
<p>本文地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fxuxin123.com%2Fweb%2Fnginx-spa" target="_blank" rel="nofollow noopener noreferrer" title="https://xuxin123.com/web/nginx-spa" ref="nofollow noopener noreferrer">xuxin123.com/web/nginx-s…</a></p></div>  
</div>
            