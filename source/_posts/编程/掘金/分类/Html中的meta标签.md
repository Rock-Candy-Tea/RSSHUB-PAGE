
---
title: 'Html中的meta标签'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1268'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 18:38:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=1268'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「高产更文」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力</a>。</p>
<h3 data-id="heading-0">是什么</h3>
<p><code><meta> 元素表示那些不能由其它HTML元相关元素 <base>, <link>, <script>, <style> 或 <title></code> 之一表示的任何元数据信息。(例如：keyword，author)`</p>
<h3 data-id="heading-1">作用</h3>
<ul>
<li>SEO优化</li>
<li>自动刷新</li>
<li>跳转页面</li>
<li>定义语言</li>
<li>。。。。。。</li>
</ul>
<h3 data-id="heading-2">标签属性</h3>
<ol>
<li>
<p>name</p>
</li>
<li>
<p>http-equiv</p>
</li>
<li>
<p>charset</p>
</li>
<li>
<p>itemprop</p>
<blockquote>
<p>当有<code>http-equiv</code>或<code>name</code>属性的时候，一定要有content属性对其进行说明。 http-equiv和name定义是什么。content补充具体内容。</p>
</blockquote>
</li>
</ol>
<h3 data-id="heading-3">charset</h3>
<blockquote>
<p>规定 HTML 文档的字符编码：</p>
<p>常用的值：</p>
<ul>
<li>UTF-8 -> Unicode 字符编码</li>
<li>ISO-8859-1 ->拉丁字母表的字符编码</li>
</ul>
</blockquote>
<h3 data-id="heading-4">name</h3>
<blockquote>
<p>用于描述网页的，对应的content提供给搜索引擎查找和分类的信息。语法：</p>
</blockquote>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">""</span> <span class="hljs-attr">content</span>=<span class="hljs-string">""</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">name="keywords"</h4>
<p>设置网站的关键字：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"大数据，数据"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">name="description"</h4>
<p>设置网站的描述：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"这是一段描述"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">name="robots"</h4>
<p>设置，让搜索引擎知道哪些页面需要索引，哪些页面不需要索引。<code>content</code> 有如下参数：</p>
<ul>
<li>all：文件将被检索，且页面上的链接可以被查询；</li>
<li>none：文件将不被检索，且页面上的链接不可以被查询；</li>
<li>index：文件将被检索；</li>
<li>noindex：文件将不被检索，但页面上的链接可以被查询；</li>
<li>follow：页面上的链接可以被查询；</li>
<li>nofollow：文件将被检索，但页面上的链接不可以被查询。</li>
</ul>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"robots"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"all"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">name="author"</h4>
<p>设置页面的作者：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"author"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"syl"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">name="generator"</h4>
<p>设置网站采用什么软件制作的：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"generator"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"dreamviewer"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">name="copyright"</h4>
<p>设置网站的版权信息的：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"copyright"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"***版权所有"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">name="revisit-after"</h4>
<p>设置网站的重访，<code>30day</code>代表30天：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"revisit-after"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"30day"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-12">name="viewport"</h4>
<p>设置浏览器窗口的大小和缩放的</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1, maximum-scale=1"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">http-equiv 属性</h3>
<blockquote>
<p>http-equiv相当于 HTTP 的文件头的设置。语法：</p>
</blockquote>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">""</span> <span class="hljs-attr">content</span>=<span class="hljs-string">""</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">http-equiv="expires"</h4>
<p>它是来设置网页的过期时间的，到期必须从服务器重新传输</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"expires"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"2020 05:28:00 GMT+0800 (CST)"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">http-equiv="Pragma"</h4>
<p>它是来设置禁止浏览器从本地缓存中访问页面：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Pragma"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"no-cache"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">http-equiv="Refresh"</h4>
<p>设置自动刷新或者跳转新页面，其中<code>content</code>第一个数字代表 5 秒后自动刷新：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Refresh"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"5;URL=www.baidu.com"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">http-equiv="Set-Cookie"</h4>
<p>设置 Cookie ，如果网页过期，这个网页的cookies的也会被删除：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Set-Cookie"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"cookie value=xxx;expires=2020 05:28:00 GMT+0800 (CST) path=/"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-18">http-equiv="Window-target"</h4>
<p>强制页面在当前窗口以独立页面显示：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Window-target"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"top"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-19">http-equiv="content-Type"</h4>
<p>设置页面使用的字符集：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"content-Type"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"text/html;charset=gb2312"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-20">http-equiv="Content-Language"</h4>
<p>设置页面的语言的：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Content-Language"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"zh-cn"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-21">http-equiv="Cache-Control"</h4>
<p>设置页面缓存，：</p>
<ul>
<li>no-cache: 先发送请求，与服务器确认该资源是否被更改，如果未被更改，则使用缓存。</li>
<li>no-store: 不允许缓存，每次都要去服务器上，下载完整的响应。（安全措施）</li>
<li>public :缓存所有响应，但并非必须。因为max-age也可以做到相同效果</li>
<li>private :只为单个用户缓存，因此不允许任何中继进行缓存。（比如说CDN就不允许缓存private的响应）</li>
<li>maxage :表示当前请求开始，该响应在多久内能被缓存和重用，而不去服务器重新请求。例如：max-age=60表示响应可以再缓存和重用 60 秒。</li>
</ul>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Cache-Control"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"no-cache"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-22">http-equiv="Content-Script-Type"</h4>
<p>设置页面中脚本的类型：</p>
<pre><code class="hljs language-xml copyable" lang="xml"><span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"Content-Script-Type"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"text/javascript"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            