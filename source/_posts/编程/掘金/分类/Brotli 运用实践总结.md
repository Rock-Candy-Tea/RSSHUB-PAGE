
---
title: 'Brotli 运用实践总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd173d7814b54b1db7df283ff4f8de3c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 24 May 2021 17:36:27 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd173d7814b54b1db7df283ff4f8de3c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">介绍</h2>
<p><code>Brotli</code> 是 <code>Google</code> 推出的开源压缩算法，通过变种的 <code>LZ77</code> 算法、<code>Huffman</code> 编码以及二阶文本建模等方式进行数据压缩，与其他压缩算法相比，它有着更高的压缩效率，性能也比我们目前常见的 <code>Gzip</code> 高17-25%，可以帮我们更高效的压缩网页中的各类文件大小及脚本，从而提高加载速度，提升网页浏览体验。需要说明的是 <code>Brotli</code> 压缩只在 <code>https</code> 下生效，因为 在 <code>http</code> 请求中 <code>request header</code> 里的 <code>Accept-Encoding: gzip, deflate</code> 是没有 <code>br</code> 的。</p>
<p><code>Brotli</code> 如此高的压缩比率，得益于其使用一个预定义的字典，该字典包含超过 13000 个来自文本和 <code>HTML</code> 文档的大型语料库的常用字符串，预定义的算法可以提升较小文件的压缩密度，而压缩与解压缩速度则大致不变。</p>
<p><code>Brotli</code> 凭借它优异的压缩性能迅速占领了市场，从下图可以看到，除了 <code>IE</code> 和 <code>Opera Mini</code> 之外，几乎所有的主流浏览器都已支持 <code>Brotli</code> 算法，因此处于资源占用的考虑，比如说流量，建议启用：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd173d7814b54b1db7df283ff4f8de3c~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210525084609637" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">服务器端配置</h2>
<p>本示例中使用的相关资源如下</p>
<ul>
<li>操作系统：<code>Ubuntu 20.04</code></li>
<li>Nginx 版本：<code>nginx/1.18.0</code></li>
</ul>
<h3 data-id="heading-2">安装配置 git</h3>
<p>在安装之前请先确定当前服务器是否安装 <code>git</code>，安装配置好 <code>git</code>，请直接进入下一步骤。
安装  <code>git</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell">sudo apt-get install git
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">下载 Brotli</h3>
<p><code>google/ngx_brotli</code> 从 16年12月的版本起，开始内置<code>google/brotli</code>，所以我们不需要额外编译 <code>bagder/libbrotli</code> 库，让安装变得简单起来。
我们将 <code>google/ngx_brotli</code> 下载并解压到 <code>/usr/local/src/ngx_brotli</code> 目录</p>
<pre><code class="hljs language-shell copyable" lang="shell">cd /usr/local/src
sudo git clone https://github.com/google/ngx_brotli.git || sudo git clone https://github.com.cnpmjs.org/google/ngx_brotli.git
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后再下载 <code>google/brotli</code> 并解压到 <code>/usr/local/src/ngx_brotli/deps/brotli</code></p>
<pre><code class="hljs language-shell copyable" lang="shell">cd /usr/local/src/ngx_brotli/deps && rm -rf brotli
git clone https://github.com/google/brotli.git || sudo git clone https://github.com.cnpmjs.org/google/brotli.git
cd /usr/local/src/ngx_brotli && git submodule update --init
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">下载解压 Nginx 源码包</h3>
<p>请下载与当前 <code>Nginx</code> 版本相同的 <code>Nginx</code> 源码包。<code>Nginx</code> 官方下载地址：<a href="http://nginx.org/en/download.html%E3%80%82" target="_blank" rel="nofollow noopener noreferrer">nginx.org/en/download…</a></p>
<p>可通过命令，获取当前 <code>Nginx</code> 版本：</p>
<pre><code class="hljs language-shell copyable" lang="shell">nginx -v
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：</p>
<pre><code class="hljs language-shell copyable" lang="shell">nginx version: nginx/1.18.0 (Ubuntu)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下载并解压 <code>Nginx</code> 源码包：</p>
<pre><code class="hljs language-shell copyable" lang="shell">cd /usr/local/src
sudo wget http://nginx.org/download/nginx-1.18.0.tar.gz
sudo tar -xvf nginx-1.18.0.tar.gz
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">编译动态模块</h3>
<pre><code class="hljs language-shell copyable" lang="shell">cd nginx-1.18.0
sudo ./configure --with-compat --add-dynamic-module=/usr/local/src/ngx_brotli
sudo make modules
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>参数语法：–add-dynamic-module=[模块源码所在目录的绝对路径]</p>
</blockquote>
<p>等运行完成后，查看编译好的模块：</p>
<pre><code class="hljs language-shell copyable" lang="shell">ls objs/*.so
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输出：</p>
<pre><code class="hljs language-shell copyable" lang="shell">objs/ngx_http_brotli_filter_module.so  objs/ngx_http_brotli_static_module.so
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将编译好的模块文件复制到 <code>Nginx</code> 动态模块加载目录：</p>
<pre><code class="hljs language-shell copyable" lang="shell">sudo cp objs/&#123;ngx_http_brotli_filter_module.so,ngx_http_brotli_static_module.so&#125; /etc/nginx/modules
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">注册 Brotli 模块</h3>
<p>修改 <code>Nginx</code> 配置文件 <code>nginx.conf</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell">cd /etc/nginx
sudo vim nginx.conf
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以在头部添加：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> Brotli 模块</span>
load_module /etc/nginx/modules/ngx_http_brotli_filter_module.so;
load_module /etc/nginx/modules/ngx_http_brotli_static_module.so;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">启动 Brotli 压缩</h3>
<p><code>Brotli</code> 和 <code>gzip</code> 是可以并存的，因此无需关闭 <code>gzip</code> 。</p>
<pre><code class="hljs language-shell copyable" lang="shell">sudo vim nginx.conf
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-shell copyable" lang="shell">http&#123;
    ...
    ##
    # Gzip Settings
    ##

    gzip on;
    gzip_static on;
    gzip_disable "MSIE [1-6]\.";
    gzip_min_length 1k;
    gzip_vary on;
    gzip_comp_level 3;
    gzip_types text/plain text/css text/javascript application/javascript text/xml application/xml application/xml+rss application/json image/jpeg image/gif image/png;

    ##
    # Brotli Settings
    ##

    brotli on;
    brotli_static on;
    brotli_comp_level 6;
    brotli_buffers 16 8k;
    brotli_min_length 20;
    brotli_types text/plain text/css text/javascript application/javascript text/xml application/xml application/xml+rss application/json image/jpeg image/gif image/png;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>验证 <code>Nginx</code> 配置是否正确并重启 <code>Nginx</code>：</p>
<pre><code class="hljs language-shell copyable" lang="shell">sudo nginx -t
sudo systemctl reload nginx
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">清理临时文件</h3>
<p>要养成好习惯，每次编译完后都要把应用包解压出来的文件或目录进行删除。</p>
<pre><code class="hljs language-shell copyable" lang="shell">rm -rf /usr/local/src/&#123;nginx-1.18.0/,ngx_brotli/&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">前端配置</h2>
<h3 data-id="heading-10">vue-cli 中配置</h3>
<p>修改 <code>vue.confi.js</code> 文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> CompressionWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">'compression-webpack-plugin'</span>) <span class="hljs-comment">// 压缩插件</span>
 
<span class="hljs-attr">configureWebpack</span>: <span class="hljs-function"><span class="hljs-params">config</span> =></span> &#123;
    <span class="hljs-keyword">const</span> plugins = [
      ......
      <span class="hljs-comment">// gzip 压缩</span>
      <span class="hljs-keyword">new</span> CompressionWebpackPlugin(&#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[path][base].gz'</span>,
        <span class="hljs-attr">algorithm</span>: <span class="hljs-string">'gzip'</span>,
        <span class="hljs-attr">test</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">RegExp</span>(
          <span class="hljs-string">'\\.('</span> +
          [<span class="hljs-string">'js'</span>, <span class="hljs-string">'css'</span>].join(<span class="hljs-string">'|'</span>) +
          <span class="hljs-string">')$'</span>
        ),
        <span class="hljs-attr">threshold</span>: <span class="hljs-number">10240</span>,
        <span class="hljs-attr">minRatio</span>: <span class="hljs-number">0.8</span>
      &#125;),
      <span class="hljs-comment">// brotli 压缩</span>
      <span class="hljs-keyword">new</span> CompressionWebpackPlugin(&#123;
        <span class="hljs-attr">filename</span>: <span class="hljs-string">'[path][base].br'</span>,
        <span class="hljs-attr">algorithm</span>: <span class="hljs-string">'brotliCompress'</span>,
        <span class="hljs-attr">test</span>: <span class="hljs-regexp">/\.(js|css|html|svg)$/</span>,
        threshold: <span class="hljs-number">10240</span>,
        <span class="hljs-attr">minRatio</span>: <span class="hljs-number">0.8</span>
      &#125;)
    ]
    <span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">'production'</span>) &#123;
      config.plugins = [...config.plugins, ...plugins]
    &#125;
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">vite 中配置</h3>
<p>修改 <code>vite.config.ts</code> 文件</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> viteCompression <span class="hljs-keyword">from</span> <span class="hljs-string">'vite-plugin-compression'</span> <span class="hljs-comment">// 压缩插件</span>

  <span class="hljs-comment">// 插件</span>
  <span class="hljs-attr">plugins</span>: [
    ...
    <span class="hljs-comment">// gzip 压缩 </span>
    viteCompression(&#123;
      <span class="hljs-attr">verbose</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">disable</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">threshold</span>: <span class="hljs-number">10240</span>,
      <span class="hljs-attr">algorithm</span>: <span class="hljs-string">'gzip'</span>,
      <span class="hljs-attr">ext</span>: <span class="hljs-string">'.gz'</span>
    &#125;),
    <span class="hljs-comment">// brotli 压缩  </span>
    viteCompression(&#123;
      <span class="hljs-attr">verbose</span>: <span class="hljs-literal">true</span>,
      <span class="hljs-attr">disable</span>: <span class="hljs-literal">false</span>,
      <span class="hljs-attr">threshold</span>: <span class="hljs-number">10240</span>,
      <span class="hljs-attr">algorithm</span>: <span class="hljs-string">'brotliCompress'</span>,
      <span class="hljs-attr">ext</span>: <span class="hljs-string">'.br'</span>
    &#125;)
  ],
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">验证压缩是否生效</h2>
<h3 data-id="heading-13">curl 验证</h3>
<pre><code class="hljs language-shell copyable" lang="shell">curl -H 'Accept-Encoding: br' -I http://localhost
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-shell copyable" lang="shell">HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 24 May 2021 14:38:29 GMT
Content-Type: text/html
Last-Modified: Tue, 21 Apr 2020 14:09:01 GMT
Connection: keep-alive
Vary: Accept-Encoding
ETag: W/"5e9efe7d-264"
Content-Encoding: br
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-14">浏览器端验证</h3>
<p>未开启：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/935147e1b08a48fa99efc0f4dff72d9e~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210524224107752" loading="lazy" referrerpolicy="no-referrer"></p>
<p>已开启</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b3400e846594ee8986ce48a2af0340e~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210524224138018" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">参考文献</h2>
<ol>
<li><a href="https://blog.csdn.net/qq_35416183/article/details/88917034" target="_blank" rel="nofollow noopener noreferrer">Nginx启用Brotli压缩</a></li>
<li><a href="https://blog.csdn.net/qq_34556414/article/details/109112165" target="_blank" rel="nofollow noopener noreferrer">Nginx 为站点启用 Brotli 压缩算法</a></li>
<li><a href="https://blog.csdn.net/qq_33290980/article/details/108362453" target="_blank" rel="nofollow noopener noreferrer">gzip，zopfli及brotli压缩对比，vue配置及服务端实现</a></li>
<li><a href="https://cloud.tencent.com/developer/article/1549869" target="_blank" rel="nofollow noopener noreferrer">Nginx开启Google Brotli压缩</a></li>
<li><a href="https://www.atlantic.net/dedicated-server-hosting/how-to-install-brotli-module-for-nginx-on-ubuntu-20-04/" target="_blank" rel="nofollow noopener noreferrer">How to install Brotli Module for Nginx on Ubuntu 20.04</a></li>
<li><a href="https://github.com/webpack-contrib/compression-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer">compression-webpack-plugin</a></li>
<li><a href="https://github.com/anncwb/vite-plugin-compression" target="_blank" rel="nofollow noopener noreferrer">vite-plugin-compression</a></li>
</ol></div>  
</div>
            