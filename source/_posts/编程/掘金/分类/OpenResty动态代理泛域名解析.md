
---
title: 'OpenResty动态代理泛域名解析'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad19f61ae8394a78b04321fc9e79bce6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 15 May 2021 12:18:44 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad19f61ae8394a78b04321fc9e79bce6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad19f61ae8394a78b04321fc9e79bce6~tplv-k3u1fbpfcp-zoom-1.image" alt="99188-3de77k1gbti.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">前言</h1>
<p>在互联网服务中，二级域名泛解析，是一种比较常见的技术方案。我在为公司设计系统的时候，遇到了一个问题，那就是，这个业务的域名是动态增减的。而且这个业务需要对所有请求都进行鉴权管理。</p>
<p>所以在选型上面，我采用了业内方案 OpenResty + Redis 对域名进行动态解析。</p>
<h1 data-id="heading-1">动态解析二级域名的前缀</h1>
<p>由于要进行泛解析，那么我们需要配置<code>域名DNS</code>，将<code>*.domain.com</code>映射到我们的代理服务器上。</p>
<p>动态解析的时候 需要一个数据库来实现domain -> ip的映射 ，我考虑两种方式来保存：</p>
<p>1. 内存保留</p>
<p>2. redis</p>
<p>我考虑到内存不可靠性与代理服务器横向扩容问题，采用了redis来存储这些映射关系。</p>
<p>并且借用主站点的鉴权机制，直接使用cookie。</p>
<h1 data-id="heading-2">数据获取: query数据获取</h1>
<pre><code class="hljs language-lua copyable" lang="lua"><span class="hljs-keyword">local</span> <span class="hljs-built_in">arg</span> = ngx.req.get_uri_args()
<span class="hljs-built_in">arg</span>[<span class="hljs-string">'query参数'</span>]

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">数据库: 连接redis</h1>
<pre><code class="hljs language-lua copyable" lang="lua"><span class="hljs-keyword">local</span> redis = <span class="hljs-built_in">require</span> <span class="hljs-string">"resty.redis"</span>
<span class="hljs-keyword">local</span> redisClient = redis:new()
<span class="hljs-keyword">local</span> ok, err = redisClient:connect(<span class="hljs-built_in">config</span>.redisHost,<span class="hljs-built_in">config</span>.redisPort)
<span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> ok <span class="hljs-keyword">then</span>
    ngx.<span class="hljs-built_in">log</span>(ngx.ERR, <span class="hljs-string">"failed to connect: "</span>, err)
    <span class="hljs-keyword">return</span>
<span class="hljs-keyword">end</span>
redisClient:auth(<span class="hljs-built_in">config</span>.redisPassword)
<span class="hljs-keyword">local</span> host = ngx_re.split(ngx.var.host,<span class="hljs-string">"\\."</span>)[<span class="hljs-number">1</span>]
<span class="hljs-keyword">local</span> hostRes, err = redisClient:get(host)
<span class="hljs-comment">-- 将解析数据返回</span>
ngx.var.userdomain = hostRes
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">鉴权:获取cookie数据</h1>
<pre><code class="hljs language-lua copyable" lang="lua"><span class="hljs-keyword">local</span> userCookie = ngx.var.cookie_user
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个地方 cookie_user 指从<code>cookie</code>中获取<code>user</code>这个key的值。</p>
<h1 data-id="heading-5">nginx 配置</h1>
<p>为解析配置新的server。</p>
<pre><code class="hljs language-nginx copyable" lang="nginx"><span class="hljs-comment"># 域名指向都不匹配时，会选择此配置，对于泛解析的域名，可以在这里做一些处理</span>
            <span class="hljs-attribute">listen</span> <span class="hljs-number">443</span> ssl;
            <span class="hljs-attribute">server_name</span> <span class="hljs-regexp">*.yodfz.com</span>;
            <span class="hljs-comment"># 限制每个ip连接宽带大小为3mb</span>
            <span class="hljs-attribute">limit_conn_zone</span> $binary_remote_addr zone=one:<span class="hljs-number">3m</span>;
            <span class="hljs-attribute">ssl_certificate</span>     /cert/<span class="hljs-number">1</span>.crt;
            <span class="hljs-attribute">ssl_certificate_key</span> /cert/<span class="hljs-number">2</span>.key;
            <span class="hljs-attribute">ssl_protocols</span>       TLSv1 TLSv1.<span class="hljs-number">1</span> TLSv1.<span class="hljs-number">2</span>;
            <span class="hljs-attribute">ssl_ciphers</span>         HIGH:!aNULL:!MD5;
            <span class="hljs-attribute">gzip</span> <span class="hljs-literal">on</span>;
            <span class="hljs-attribute">gzip_min_length</span> <span class="hljs-number">1k</span>;
            <span class="hljs-attribute">gzip_buffers</span> <span class="hljs-number">4</span> <span class="hljs-number">16k</span>;
            <span class="hljs-attribute">gzip_comp_level</span> <span class="hljs-number">2</span>;
            <span class="hljs-attribute">gzip_types</span> text/plain application/javascript application/x-javascript text/css application/xml text/javascript application/x-httpd-php image/jpeg image/gif image/png;
            <span class="hljs-attribute">gzip_vary</span> <span class="hljs-literal">off</span>;
            <span class="hljs-attribute">gzip_disable</span> <span class="hljs-string">"MSIE [1-6]\."</span>;
            <span class="hljs-attribute">resolver</span> <span class="hljs-number">8.8.8.8</span> ipv6=<span class="hljs-literal">off</span>;
            <span class="hljs-attribute">location</span> / &#123;            
<span class="hljs-comment">#正式环境启用</span>
                <span class="hljs-attribute">lua_code_cache</span> <span class="hljs-literal">off</span>;
                <span class="hljs-comment">#设置$userdomain变量及默认值</span>
                <span class="hljs-attribute">set</span> $userdomain default;
                <span class="hljs-comment">#引入lua文件</span>
                <span class="hljs-attribute">rewrite_by_lua_file</span> /lua/cname.lua;
                <span class="hljs-comment">#反向代理</span>
                <span class="hljs-attribute">proxy_pass</span> $userdomain;
                <span class="hljs-attribute">proxy_redirect</span> <span class="hljs-literal">off</span>;
                <span class="hljs-attribute">proxy_buffering</span> <span class="hljs-literal">off</span>;
                <span class="hljs-attribute">proxy_http_version</span> <span class="hljs-number">1</span>.<span class="hljs-number">1</span>;
                <span class="hljs-attribute">proxy_set_header</span> Upgrade $http_upgrade;
                <span class="hljs-attribute">proxy_set_header</span> Connection $connection_upgrade;
                <span class="hljs-comment"># proxy_set_header Host $userdomain;</span>
                <span class="hljs-comment"># proxy_set_header X-Real-IP $remote_addr;</span>
                <span class="hljs-comment"># proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;</span>
            &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将以下文件保存为cname.lua</p>
<pre><code class="hljs language-lua copyable" lang="lua"><span class="hljs-keyword">local</span> redis = <span class="hljs-built_in">require</span> <span class="hljs-string">"resty.redis"</span>
<span class="hljs-keyword">local</span> resty_rsa = <span class="hljs-built_in">require</span> <span class="hljs-string">"resty.rsa"</span>
<span class="hljs-keyword">local</span> ngx_re = <span class="hljs-built_in">require</span> <span class="hljs-string">"ngx.re"</span>
<span class="hljs-keyword">local</span> cjson = <span class="hljs-built_in">require</span> <span class="hljs-string">"cjson"</span>
<span class="hljs-keyword">local</span> <span class="hljs-built_in">config</span> = <span class="hljs-built_in">require</span> <span class="hljs-string">"lua.config"</span>

<span class="hljs-keyword">local</span> redisClient = redis:new()

<span class="hljs-comment">-- 解析二级域名 从redis中获取反代地址</span>
<span class="hljs-keyword">local</span> ok, err = redisClient:connect(<span class="hljs-built_in">config</span>.redisHost,<span class="hljs-built_in">config</span>.redisPort)
<span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> ok <span class="hljs-keyword">then</span>
    ngx.<span class="hljs-built_in">log</span>(ngx.ERR, <span class="hljs-string">"failed to connect: "</span>, err)
    <span class="hljs-keyword">return</span>
<span class="hljs-keyword">end</span>
redisClient:auth(<span class="hljs-built_in">config</span>.redisPassword)
<span class="hljs-keyword">local</span> host = ngx_re.split(ngx.var.host,<span class="hljs-string">"\\."</span>)


<span class="hljs-keyword">local</span> hostRes, err = redisClient:get(host[<span class="hljs-number">1</span>])
<span class="hljs-keyword">if</span> hostRes <span class="hljs-keyword">then</span>
    ngx.var.userdomain = hostRes
    <span class="hljs-keyword">return</span>
<span class="hljs-keyword">end</span>

<span class="hljs-keyword">local</span> ok, err = redisClient:set_keepalive(<span class="hljs-number">10000</span>, <span class="hljs-number">100</span>)
<span class="hljs-keyword">if</span> <span class="hljs-keyword">not</span> ok <span class="hljs-keyword">then</span>
    ngx.say(<span class="hljs-string">"failed to set keepalive: "</span>, err)
    <span class="hljs-keyword">return</span>
<span class="hljs-keyword">end</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            