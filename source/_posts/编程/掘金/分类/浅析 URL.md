
---
title: '浅析 URL'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2506'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 01:53:42 GMT
thumbnail: 'https://picsum.photos/400/300?random=2506'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">URL的组成</h1>
<ul>
<li>协议+域名或IP+端口号+路径+查询字符串+锚点</li>
</ul>
<h2 data-id="heading-1">协议</h2>
<p>协议（protocol）。我们一般使用的都是HTTP协议和HTTPS协议。协议是为了使数据在网络上从源到达目的，网络通信的参与方必须遵循相同的规则。</p>
<h2 data-id="heading-2">域名和IP</h2>
<h3 data-id="heading-3">IP</h3>
<p>IP（Internet Protocol）是网络协议，主要约定了两件事：</p>
<ul>
<li>如何定位一台设备</li>
<li>如何封装数据报文，以跟其他设备交流</li>
</ul>
<h3 data-id="heading-4">域名</h3>
<p>域名是对IP的别称。</p>
<ul>
<li>顶级域名，比如com</li>
<li>二级域名（俗称一级域名），比如baidu.com</li>
<li>三级域名（俗称二级域名），比如www.baidu.com</li>
</ul>
<p>可以通过ping一下域名来获得对应的IP，例如ping baidu.com</p>
<ul>
<li>一个域名可以对应不同的IP（均衡负载，防止一台机器扛不住）</li>
<li>一个IP也可以对应不同的域名（共享主机）</li>
</ul>
<h3 data-id="heading-5">域名和IP通过DNS对应起来</h3>
<p>当你要访问一个网站是，浏览器就会先向电信的DNS服务器询问这个域名对应的IP，浏览器在根据IP的对应的80/443端口发送请求，所请求的内容就是你要访问的网站的页面。可以在浏览器的开发者工具的Network面板参看网络访问的全过程。</p>
<h4 data-id="heading-6">nslookup域名解析命令</h4>
<p>nslookup的基本功能就是解析默认DNS服务器，直接输入nslookup即可。例如nslookup baidu.com</p>
<h4 data-id="heading-7">curl命令</h4>
<p>可以使用curl命令来找到询问DNS服务对应的IP，例如curl -v <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.baidu.com" target="_blank" rel="nofollow noopener noreferrer" title="http://www.baidu.com" ref="nofollow noopener noreferrer">www.baidu.com</a>
他的访问过程是这样的：</p>
<ol>
<li>URL会被curl重写，先请求DNS获得IP</li>
<li>进行TCP链接，成功后发送HTTP请求</li>
<li>发送请求内容，获得响应内容</li>
<li>响应结束，关闭TCP</li>
<li>真正结束</li>
</ol>
<h2 data-id="heading-8">端口号</h2>
<p>一台机器可以提供很多服务，每个服务一个号码，这个号码就是端口号port。</p>
<ul>
<li>提供HTTP服务最好用80端口</li>
<li>提供HTTPS服务最好用443端口</li>
<li>提供FTP服务最好用21端口</li>
<li>一共有65535个端口</li>
</ul>
<h3 data-id="heading-9">规则</h3>
<ul>
<li>0-1023是留给系统使用的，如果要使用需要有管理员权限，但是不建议使用。</li>
<li>其他的都是可以给普通用户使用的。</li>
<li>一个端口被占用需要更换另一个端口。</li>
</ul>
<h2 data-id="heading-10">路径</h2>
<p>使用路径可以实现请求不同的页面</p>
<p>例如：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FHTML" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/HTML" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a> 其中/zh-CN/docs/Web/HTML就是路径，说明你请求的是中文文档中的web内容中的HTML内容。</li>
</ul>
<h2 data-id="heading-11">查询字符串</h2>
<p>查询字符串可以做到同一个页面，不同内容。例如搜索页面： <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E5%258D%258F%25E8%25AE%25AE" target="_blank" rel="nofollow noopener noreferrer" title="http://www.baidu.com/s?wd=%E5%8D%8F%E8%AE%AE" ref="nofollow noopener noreferrer">www.baidu.com/s?wd=协议</a>  其中/s是路径，后面的?wd=协议 就是查询参数。</p>
<h2 data-id="heading-12">锚点</h2>
<p>锚点可以做到同一个内容，不同位置。</p>
<p>例如</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FCSS%23%25E5%258F%2582%25E8%2580%2583%25E4%25B9%25A6" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/CSS#%E5%8F%82%E8%80%83%E4%B9%A6" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a> #号后面的参考书就是锚点。他可以帮我们快速定位到页面的某个位置</li>
</ul>
<p>注意</p>
<ul>
<li>锚点看起来是有中文的，但是实际上是不支持中文的，如果复制URL之后，就会把中文显示一串字符串</li>
<li>锚点是无法在Network面板看到的，因为锚点不会传到服务器，#和锚点都会被浏览器阻拦。</li>
</ul></div>  
</div>
            