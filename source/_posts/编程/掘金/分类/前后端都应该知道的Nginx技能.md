
---
title: '前后端都应该知道的Nginx技能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0c119402a114dd495196afc6dc4bfe9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Wed, 07 Sep 2022 02:13:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0c119402a114dd495196afc6dc4bfe9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<h1 data-id="heading-0">前言</h1>
<p>我们本次讲解的目的是尽可能阐述清楚，工作中必备的Nginx的知识点，而且这些知识点必须在日常开发中，对于前后端开发来说都是工作中的痛点。</p>
<blockquote>
<p>这时你可能会有疑问，我说的这些真的都应该需要掌握吗？</p>
<p>有这个质疑，我觉得是思维上是正向的，我很乐意回答，我可以明确回答，<code>“是的”</code>。</p>
</blockquote>
<p><strong>为什么这么说，我们来列举几个场景</strong></p>
<h2 data-id="heading-1">场景：</h2>
<p>1、面试时，面试官问你，Nginx在你平常开发中有使用到吗？是怎么用的？xxx是干什么的，还能做那些事情？（我平常也这么问）</p>
<p>2、项目第一个迭代版本开发完成，项目经理说，老X，咱们申请了2个服务器，需要把项目部署上去，一个开发环境，一个测试环境，你搞一些环境，然后前后的包一打，也部署上去</p>
<blockquote>
<p>过了1~2天，中午某刻，项目经理悄悄站在你的背后，双手扶着你的肩膀，说：“老X，弄的怎么样？有什么问题吗”，你想了想，组织了一下语言，“环境都好了，项目需要开发人员提供给我，我放上去，还有，项目怎么部上去呢？”</p>
<p>项目经理，对着办公室的前后端负责人，你们把项目打包一下，发给老X，部署到服务器上，协助支持一下他。</p>
<p><strong>一夜过去了。</strong></p>
<p>第二天早上，晨会开始，项目进度大家汇报完，项目经理问起来，昨天的项目部署怎么样？可以访问了吗？</p>
<p>老X说，部署上去了，运行不起来，报502，不知道怎么回事？可能是Nginx的配置有问题</p>
<p>大家就开始排查，怎么改。忽然发现前后端对基本的配置都不熟悉，竟然连 location、upstream都不懂。更别说访问拦截日志、上传文件大小设置、超时等。</p>
</blockquote>
<p>3、线上打包好的程序包，有问题，但是测试环境和生产环境的数据不能动？<br>
本地复现不出来。怎么办。本地运行nginx环境，但是我不太会，怎么办？</p>
<p>4、听说这个xx属性在项目开发中是必备技能，先学习了解一下。</p>
<p><strong>上面四个场景，都关联到Nginx部署相关技能。</strong></p>
<p>你肯定也是属于上述的某个目的，需要进行技能学习和提升。</p>
<p>注意：对于深入难懂的nginx配置，则需要运维去搞</p>
<h1 data-id="heading-2">实际应用</h1>
<p>在项目应用前，我们需要了解几个<code>专业名词</code></p>
<ul>
<li>反向代理</li>
<li>server</li>
<li>location 匹配</li>
<li>prox_pass、root、alias等基本配置</li>
<li>upstream 负载均衡</li>
</ul>
<p>对于这几个<code>重要的点</code>，我们用一张图串起来</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0c119402a114dd495196afc6dc4bfe9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="nginx location 执行.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不知道你有没有看懂？</p>
<blockquote>
<p>没看懂也没关系，我们下来慢慢讲解</p>
</blockquote>
<h2 data-id="heading-3">1、反向代理，是不是也有正向代理，是什么意思？</h2>
<p>首页我们web应用项目，大部分使用场景应用的反向代理，二者解释起来有点绕。</p>
<p>我们结合图列简单阐述下</p>
<p><strong>正向代理</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d28f5d099dc5478fa23cfcb7105ea008~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个有点类型我们的局域网中客户端访问互联网，这种情况下，我们一般是<strong>无法直接访问，需要连接一个代理服务器</strong>，来进行访问，这种代理服务就称为正向代理。</p>
<p>也有点类型我们需要连<code>外部网络</code>，通过VPN进行访问的原理，但是这种就更加复杂，但是肯定会有一个代理服务器进行转发。</p>
<blockquote>
<p><strong>正向代理是对客户端的代理，由客户端设立</strong></p>
<p><code>使用正向代理可达到 突破访问限制、提高访问速度、对服务器隐藏客户端IP等目的；</code></p>
</blockquote>
<p><strong>反向代理</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f437d0aa9e5470d80f6e9a66606101e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上面的图，是代理服务器，负载均衡的示例图</p>
<p><strong>需要将请求发送到反向代理服务器，由反向代理服务器去选择目标服务器获取数据后，在返回给客户端。</strong></p>
<blockquote>
<p>说明：</p>
<p>反向代理中客户端对代理是无感知的，因为客户端不需要任何配置就可以访问，</p>
<p>此时反向代理服务器和目标服务器对外就是一个服务器，暴露的是代理服务器地址，隐藏了真实服务器 IP 地址。</p>
</blockquote>
<p>学习的大佬们，静下心来，仔细琢磨下就懂了</p>
<h2 data-id="heading-4">2、Nginx 里面的 server 是什么？</h2>
<p><strong>server&#123;&#125; 包含在http&#123;&#125;内部，每一个server&#123;&#125;都是一个虚拟主机（站点）</strong></p>
<p>Server 块是配置虚拟主机的重要参数块，每个HTTPS 全局块可以包含<code>多个 server 块</code>，而每个Server块就相当于一台虚拟主机</p>
<pre><code class="hljs language-js copyable" lang="js">
server &#123;
            listen <span class="hljs-number">80</span>;
            server_name <span class="hljs-title class_">Example</span> <span class="hljs-title class_">Domain</span>;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>listen指令 <code>监听的端口号</code></li>
<li>server_name指令 <code>外网访问的域名，可以写多个，用空格分隔</code></li>
</ul>
<p><strong>这两个基本的指令，根据实际情况，自己配置</strong></p>
<h2 data-id="heading-5">3、location 匹配</h2>
<p>直白一些的解释就是，<code>匹配用户访问的路径</code>，就是浏览器地址访问</p>
<blockquote>
<p><a href="https://juejin.cn/creator/home" target="_blank" title="https://juejin.cn/creator/home">juejin.cn/creator/hom…</a></p>
<p>上述访问的地址，/path部分为：/creator/home，访问后，location进行匹配/path部分，如果命中，进行响应，返回（<code>状态吗、转发页面、服务器静态资源访问等</code>）</p>
</blockquote>
<p>在server&#123;&#125;里有很多location配置段</p>
<p><strong>规则是</strong>：</p>
<p>先匹配普通location （再匹配正则表达式）</p>
<p><strong>类型分为两种：</strong></p>
<p>普通配置和正则匹配</p>
<ul>
<li>普通配置</li>
</ul>
<p>规则：</p>
<p><strong>location  /</strong> <strong>路径</strong><br>
<strong>location = /</strong> <strong>路径</strong></p>
<p>路径部分为字符串，两者的区别在于，第二种等号后属于精确匹配，对子路径不生效。</p>
<p>我们大部分Nginx Server下会有</p>
<pre><code class="hljs language-js copyable" lang="js">location / &#123;       
    root /web;     
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个是默认策略，表示所有的请求都会命中，包含所有的请求，但是<code>优先级最低</code>，其他未命中时，这个才会生效。</p>
<pre><code class="hljs language-js copyable" lang="js">location / &#123;       
    root /web;     
&#125;

location /abc &#123;       
    root /web;     
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当用户请求的（/abc）url同时匹配到两段location时，</p>
<p>最大前缀生效（<strong>location /abc</strong> <strong>生效</strong>）</p>
<p>如果没有这段(<strong>location /abc</strong> <strong>）</strong> <strong>第一段 location / 生效 。</strong></p>
<ul>
<li>正则匹配</li>
</ul>
<p><code>location ~ URI &#123;&#125;</code></p>
<p>~匹配的文件是<strong>区分字符 大小写的</strong></p>
<p><code>location ~* URI &#123;&#125; </code></p>
<p>~*匹配的文件是<strong>不区分字符大小的</strong></p>
<p>如：</p>
<pre><code class="hljs language-js copyable" lang="js">location  ~ /abc &#123;

      <span class="hljs-keyword">return</span> <span class="hljs-number">400</span>;

&#125;

location ~* /abc &#123;

     <span class="hljs-keyword">return</span> <span class="hljs-number">500</span>;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个用的比较少，下面在实际应用中，使用到的点，我会提一下。知道配置即可。</p>
<h2 data-id="heading-6">4、基本配置（proxy_pass、root、alias等）</h2>
<h3 data-id="heading-7">proxy_pass 反向代理</h3>
<p>如果在proxy_pass后面的url，是实际的服务器地址</p>
<ul>
<li>如果加/，表示绝对根路径</li>
<li>如果没有/，表示相对路径，把匹配的路径部分也给代理</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f692e66d45bf4d2ab8baccbddadd84e7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这块需要注意，实际使用比较<code>重要</code>，</p>
<p><strong>尾部要不要加斜杠，这个要一定要研究清楚</strong>，这个配置，在后续添加接口代理上用的比较多</p>
<p><strong>比如业务层面，需要做：</strong></p>
<p>1、业务数据类接口请求<br>
2、静态资源接口代理<br>
3、文件服务器接口代理<br>
4、消息通知接口代理<br>
....</p>
<h3 data-id="heading-8">root</h3>
<p>这个root含义就是根目录地址</p>
<p><strong>默认server下可以设置</strong></p>
<pre><code class="hljs language-js copyable" lang="js">server &#123;
   root <span class="hljs-attr">E</span>:<span class="hljs-regexp">/work/</span>edu/wonder_front
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表示当前server的根目录地址，这个看情况，<strong>一般都是访问代理地址，实践使用时会注释</strong></p>
<p><strong>访问路径</strong></p>
<pre><code class="hljs language-js copyable" lang="js">location /www/ &#123;

   root /home/data;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>访问路径中，配置root，访问的时候，<code>会追加上访问路径</code> 即：<strong>root + path</strong></p>
<p>访问路径：<a href="https://link.juejin.cn/?target=http%3A%2F%2F192.168.66.39%3A2234%2Fwww%2Flogin.html" target="_blank" rel="nofollow noopener noreferrer" title="http://192.168.66.39:2234/www/login.html" ref="nofollow noopener noreferrer">http://192.168.66.39:2234/www/login.html</a></p>
<p>实际上的地址是:</p>
<p>/home/data/<code>www/login.html</code></p>
<h3 data-id="heading-9">alias 别名路径</h3>
<p>alias指定的目录必须带/，path匹配后面的内容会在alias指定的目录下查找，即alias+匹配到path路径后面的部分</p>
<p><strong>访问路径</strong></p>
<pre><code class="hljs language-js copyable" lang="js">location /www/ &#123;

   alias /home/data;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>访问路径：<a href="https://link.juejin.cn/?target=http%3A%2F%2F192.168.66.39%3A2234%2Fwww%2Flogin.html" target="_blank" rel="nofollow noopener noreferrer" title="http://192.168.66.39:2234/www/login.html" ref="nofollow noopener noreferrer">http://192.168.66.39:2234/www/login.html</a></p>
<p>实际上的地址是:</p>
<p>/home/data/<code>login.html</code></p>
<p><strong>上述的使用，一般的配置应用不是很多，如果牵扯到<code>多端的配置</code>，就需要配置了。</strong></p>
<h2 data-id="heading-10">5、upstream 负载均衡</h2>
<p>upstream  用以配置负载的策略，nginx自带的有：</p>
<p>轮询/权重/ip_hash</p>
<p>特殊需求可用第三方策略（使用较少）</p>
<pre><code class="hljs language-js copyable" lang="js">upstream test&#123;
    server <span class="hljs-number">192.168</span><span class="hljs-number">.0</span><span class="hljs-number">.101</span>:<span class="hljs-number">8081</span>;
    server <span class="hljs-number">192.168</span><span class="hljs-number">.0</span><span class="hljs-number">.102</span>:<span class="hljs-number">8081</span>;
&#125;
 
upstream test1 &#123;
    server <span class="hljs-number">192.168</span><span class="hljs-number">.0</span><span class="hljs-number">.101</span>:<span class="hljs-number">8081</span> weight=<span class="hljs-number">2</span>;
    server <span class="hljs-number">192.168</span><span class="hljs-number">.0</span><span class="hljs-number">.102</span>:<span class="hljs-number">8081</span> weight=<span class="hljs-number">1</span>;
&#125;
 
upstream test2 &#123;
    ip_hash
    server <span class="hljs-number">192.168</span><span class="hljs-number">.0</span><span class="hljs-number">.101</span>:<span class="hljs-number">8081</span>;
    server <span class="hljs-number">192.168</span><span class="hljs-number">.0</span><span class="hljs-number">.102</span>:<span class="hljs-number">8081</span>;
&#125;
 
server&#123;
   listen   <span class="hljs-number">80</span>;
   server_name  localhost;
 
   location /login &#123;
       proxy_pass   <span class="hljs-attr">http</span>:<span class="hljs-comment">//test/</span>
   &#125; 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的配置，upstream一般会在独立的文件进行配置，就是说，</p>
<p><code>/login</code>会代理到 test的地址，test指向了负载upstream地址</p>
<p><strong>这个项目上一般都会进行配置</strong></p>
<h2 data-id="heading-11">5、其他配置</h2>
<p><code>client_max_body_size 100m;</code>  这个文件上传一般配置，传输文件大小限制<br>
<code>add_header Access-Control-Allow-Origin *;</code> 设置跨域</p>
<p><code>gzip</code> 压缩，<strong>建议开启，访问时会节流，性能提升</strong></p>
<pre><code class="hljs language-js copyable" lang="js">    gzip on;
    gzip_min_length  <span class="hljs-number">1000</span>;
    gzip_buffers     <span class="hljs-number">4</span> 8k;
    gzip_comp_level  <span class="hljs-number">1</span>;
    gzip_types       text/plain text/css text/javascript application/json application/javascript application/x-javascript text/xml application/xml application/xml+rss;
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>expires缓存</code> 设置</p>
<pre><code class="hljs language-js copyable" lang="js"> # 使用expires缓存图片，缓存到客户端<span class="hljs-number">10</span>天--发布上线使用
 location ~ .*\.(gif|jpg|png|bmp|swf|pbf)$ &#123;
      expires 10d;
 &#125;
 
 # 使用expires缓存静态资源，缓存到客户端<span class="hljs-number">1</span>天--发布上线使用
 location ~ .*\.(js|css)?$ &#123;
    expires 1d;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>这个应用，一般在<code>线上环境使用</code>，开发环境建议关闭。</strong></p>
<h1 data-id="heading-12">项目范例：</h1>
<pre><code class="hljs language-js copyable" lang="js">  
  upstream eduApi &#123;
      server <span class="hljs-number">192.168</span><span class="hljs-number">.101</span><span class="hljs-number">.74</span>:<span class="hljs-number">9091</span>; #v3
      # server edu-test04.<span class="hljs-property">edu</span>.<span class="hljs-property">com</span>:<span class="hljs-number">9091</span>; # test
      # server edu-test01.<span class="hljs-property">edu</span>.<span class="hljs-property">com</span>:<span class="hljs-number">9091</span>; # test
      # server <span class="hljs-number">192.168</span><span class="hljs-number">.100</span><span class="hljs-number">.114</span>:<span class="hljs-number">9091</span>; # development
      # server <span class="hljs-number">192.168</span><span class="hljs-number">.100</span><span class="hljs-number">.177</span>:<span class="hljs-number">9091</span>; # development
      # server jxsr-eye.<span class="hljs-property">educloud</span>.<span class="hljs-property">cn</span>; # online
  &#125;
  upstream eduSocket &#123;
      # server edu-dev01.<span class="hljs-property">edu</span>.<span class="hljs-property">com</span>:<span class="hljs-number">9092</span>;
      # 开发环境
      # server <span class="hljs-number">192.168</span><span class="hljs-number">.100</span><span class="hljs-number">.114</span>:<span class="hljs-number">9092</span>;
      # 测试环境
      server <span class="hljs-number">192.168</span><span class="hljs-number">.100</span><span class="hljs-number">.27</span>:<span class="hljs-number">9092</span>;
  &#125;

  server &#123;
    client_max_body_size 100m;
    listen       <span class="hljs-number">8892</span>;
#    server_name  aice;

    error_page  <span class="hljs-number">404</span>              /<span class="hljs-number">404.</span>html;

    error_page   <span class="hljs-number">500</span> <span class="hljs-number">502</span> <span class="hljs-number">503</span> <span class="hljs-number">504</span>  /50x.<span class="hljs-property">html</span>;
    location / &#123;
      root   <span class="hljs-attr">D</span>:<span class="hljs-regexp">/code/</span><span class="hljs-variable constant_">PDT</span>/<span class="hljs-title class_">Wonder</span>_Front/dist;
index  index.<span class="hljs-property">html</span> index.<span class="hljs-property">htm</span>;
      # 这个必须添加 路由模式为 <span class="hljs-title class_">History</span>模式，防止请求问题<span class="hljs-number">404</span>找不到
try_files $uri $uri/ /index.<span class="hljs-property">html</span>;
    &#125;

#root <span class="hljs-attr">E</span>:<span class="hljs-regexp">/work/</span>edu/wonder_front;

#index index.<span class="hljs-property">html</span> index.<span class="hljs-property">htm</span> index.<span class="hljs-property">php</span>;

# 配置接口网关
  location ^~ <span class="hljs-regexp">/rtdl-dev/</span> &#123;
      proxy_pass  <span class="hljs-attr">http</span>:<span class="hljs-comment">//10.61.160.208:8080;</span>
      proxy_redirect      <span class="hljs-keyword">default</span>;
      proxy_set_header    <span class="hljs-title class_">Host</span>    <span class="hljs-attr">$host</span>:$server_port;
      proxy_set_header    X-<span class="hljs-title class_">Real</span>-<span class="hljs-variable constant_">IP</span> $remote_addr;
      proxy_set_header    X-<span class="hljs-title class_">Forwarded</span>-<span class="hljs-title class_">Host</span> <span class="hljs-attr">$host</span>:$server_port;
      proxy_set_header    X-<span class="hljs-title class_">Forwarded</span>-<span class="hljs-title class_">Server</span> <span class="hljs-attr">$host</span>:$server_port;
      proxy_set_header    X-<span class="hljs-title class_">Forwarded</span>-<span class="hljs-title class_">For</span>  $proxy_add_x_forwarded_for;
  &#125;
  
  # 系统层请求网关代理
  location ^~ <span class="hljs-regexp">/systemApi/</span> &#123;
      proxy_pass  <span class="hljs-attr">http</span>:<span class="hljs-comment">//10.61.81.22:8080/;</span>
      proxy_redirect      <span class="hljs-keyword">default</span>;
      proxy_set_header    <span class="hljs-title class_">Host</span>    <span class="hljs-attr">$host</span>:$server_port;
      proxy_set_header    X-<span class="hljs-title class_">Real</span>-<span class="hljs-variable constant_">IP</span> $remote_addr;
      proxy_set_header    X-<span class="hljs-title class_">Forwarded</span>-<span class="hljs-title class_">Host</span> <span class="hljs-attr">$host</span>:$server_port;
      proxy_set_header    X-<span class="hljs-title class_">Forwarded</span>-<span class="hljs-title class_">Server</span> <span class="hljs-attr">$host</span>:$server_port;
      proxy_set_header    X-<span class="hljs-title class_">Forwarded</span>-<span class="hljs-title class_">For</span>  $proxy_add_x_forwarded_for;
  &#125;

  # 消息通信网关
  location ^~ <span class="hljs-regexp">/socket.io/</span> &#123;
      proxy_pass <span class="hljs-attr">http</span>:<span class="hljs-comment">//eduSocket/socket.io/;</span>
      proxy_http_version      <span class="hljs-number">1.1</span>;
      proxy_set_header        <span class="hljs-title class_">Upgrade</span> $http_upgrade;
      proxy_set_header        <span class="hljs-title class_">Connection</span>      <span class="hljs-string">"upgrade"</span>;
      proxy_set_header        X-real-ip       $remote_addr;
      proxy_set_header        X-<span class="hljs-title class_">Forwarded</span>-<span class="hljs-title class_">For</span> $remote_addr;
  &#125;  
  &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">总结：</h1>
<p>前后端关于nginx的基本需要掌握的技能，已经罗列出来。</p>
<p>我们来个扩展的小玩意</p>
<h1 data-id="heading-14">扩展</h1>
<p>写个本地的bat脚本来，启动nginx和关闭nginx，这个的使用是针对开发环境 winodw下的，不用自己手动启停，忒麻烦</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f1a3ae5614c4847ba9265986b906c1d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1、启动的比较好弄，找到<code>nginx</code>的根目录，找<code>nginx.exe</code>，右键快捷方式到桌面即可</p>
<p>2、停止，创建<code>stopNginx.bat</code></p>
<pre><code class="hljs language-js copyable" lang="js">@echo off

::windows <span class="hljs-number">2000</span>,<span class="hljs-number">98</span>
::tskill /A nginx > nul

::windows xp <span class="hljs-attr">above</span>:

taskkill /F /<span class="hljs-variable constant_">IM</span> nginx.<span class="hljs-property">exe</span> > nul

exit
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            