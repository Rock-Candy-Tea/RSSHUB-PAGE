
---
title: 'IIS服务器 部署前端的各种问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e26fb4b7b944f8d9f82435193dec06c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 19:29:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e26fb4b7b944f8d9f82435193dec06c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">问题一：IIS配置导致页面刷新时找不到文件或目录</h1>
<h2 data-id="heading-1">错误配置</h2>
<p>IIS配置web.config如下</p>
<pre><code class="copyable"><?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <rewrite>
            <rules>
                <rule name="test" patternSyntax="Wildcard">
                    <match url="*api/*" />
                    <action type="Rewrite" url="http://10.10.17.74:8085/&#123;R:2&#125;" />
                </rule>
            </rules>
        </rewrite>
        <staticContent>
            <mimeMap fileExtension=".glb" mimeType="application/glb" />
            <clientCache cacheControlMode="DisableCache" cacheControlMaxAge="3.00:00:00" />
        </staticContent>
    </system.webServer>
</configuration>

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">问题现象</h2>
<p>刷新页面时提示404找不到文件或目录。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e26fb4b7b944f8d9f82435193dec06c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">正确配置</h2>
<pre><code class="copyable"><?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <rewrite>
            <rules>
                <rule name="index">
                    <match url="^((?!(api)).)*$" />
                    <conditions>
                        <add input="&#123;REQUEST_FILENAME&#125;" matchType="IsFile" negate="true" />
                    </conditions>
                    <action type="Rewrite" url="/index.html" />
                </rule>
                <rule name="test" patternSyntax="Wildcard">
                    <match url="*api/*" />
                    <action type="Rewrite" url="http://10.10.17.74:8085/&#123;R:2&#125;" />
                </rule>
            </rules>
        </rewrite>
        <staticContent>
            <mimeMap fileExtension=".glb" mimeType="application/glb" />
            <clientCache cacheControlMode="DisableCache" cacheControlMaxAge="3.00:00:00" />
        </staticContent>
    </system.webServer>
</configuration>

<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>说明：</strong></p>
<p>1、刷新找不到文件或目录因为没有配置<code><rule name="index"></code></p>
<p>2、mimeMap部分是添加媒体类型后自动追加的</p>
<h1 data-id="heading-4">问题二：POST调用后台请求时报错405</h1>
<h2 data-id="heading-5">现象截图如下</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89da642290ec42d994e746657817174f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">错误配置如下</h2>
<p>IIS配置web.config如下</p>
<pre><code class="copyable"><rule name="index">
    <match url="^((?!(api)).)*$" />
    <conditions>
        <add input="&#123;REQUEST_FILENAME&#125;" matchType="IsFile" negate="true" />
    </conditions>
    <action type="Rewrite" url="/index.html" />
</rule>
<rule name="dl" patternSyntax="Wildcard">
    <match url="*dl/*" />
    <action type="Rewrite" url="http://10.10.17.74:9100/&#123;R:2&#125;" />
</rule>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">说明</h2>
<ul>
<li>1、配置文件中第一个规则，将所有<strong>不</strong>包含api的请求捕获，相当于路由去跳转。</li>
<li>2、配置文件中第二个规则，将所有包含dl的请求重定向到后台。</li>
<li>3、然而我现在调用接口/dl/uaa/loginUser，那到底被哪个规则匹配上呢，于是就出问题了。</li>
<li>4、所以需要在调用后台接口时，所有接口前面都拼上相同的匹配字符串(如api)即可，参考正确配置。</li>
</ul>
<h2 data-id="heading-8">正确配置</h2>
<pre><code class="copyable"><rule name="index">
    <match url="^((?!(api)).)*$" />
    <conditions>
        <add input="&#123;REQUEST_FILENAME&#125;" matchType="IsFile" negate="true" />
    </conditions>
    <action type="Rewrite" url="/index.html" />
</rule>
<rule name="dl" patternSyntax="Wildcard">
    <match url="*api/dl/*" />
    <action type="Rewrite" url="http://10.10.17.74:9100/&#123;R:2&#125;" />
</rule>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">其他</h2>
<p>通常习惯性使用配置文件直接改写配置，其实IIS提供界面操作，还可以测试配置的规则是否正确。简要记录一下：</p>
<p>1、点击【URL重写】</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bea67c1f5224505b828ce4bec5ddbe1~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2、即可查看当前网站的URL规则，可添加、修改。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bff4f4ffac9d4a0dbdca4e8859afaf1b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3、双击已添加的规则，点击测试模式，输入要测试的url，点击测试后会出现结果，可用于校对重写URL和捕获的是否一致。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1fbc7196e6144143b908245d2d7208a4~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">问题三：添加网站</h1>
<p>右键-添加网站，其实没什么问题，就记录一下。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/909be3136e5b43ae9cd65789e3eb9658~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">问题四：添加媒体类型</h1>
<p>本地能看到.glb/.gltf的模型文件，但是放到IIS服务器上就看不到了。</p>
<p>因为需要配置MIME类型：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af8856f63ce3486db23d10561843dadf~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后查看web.config文件发现：</p>
<pre><code class="copyable"><staticContent>
  <mimeMap fileExtension=".glb" mimeType="application/glb" />
  <mimeMap fileExtension=".gltf" mimeType="application/gltf" />
  <clientCache cacheControlMode="DisableCache" cacheControlMaxAge="3.00:00:00" />
</staticContent>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>OK了。</p>
<h1 data-id="heading-12">问题五：配置ws代理和视频调用</h1>
<p>原始配置如下：（错误配置）</p>
<pre><code class="copyable"><?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <rewrite>
            <rules>
<rule name="index">
                    <match url="^((?!(api)|(wsProxy)).)*$" />
                    <conditions>
                        <add input="&#123;REQUEST_FILENAME&#125;" matchType="IsFile" negate="true" />
                    </conditions>
                    <action type="Rewrite" url="/index.html" />
                </rule>
                <rule name="api" patternSyntax="Wildcard">
                    <match url="*api/*" />
                    <action type="Rewrite" url="http://后台服务IP:PORT/&#123;R:2&#125;" />
                </rule>
                <rule name="videoapi" patternSyntax="Wildcard">
                    <match url="*videoapi/*" />
                    <action type="Rewrite" url="http://后台服务IP:PORT/videoapi/&#123;R:2&#125;" />
                </rule>
<rule name="wsProxy" patternSyntax="Wildcard">
                    <match url="*wsProxy/*" />
                    <action type="Rewrite" url="http://后台服务IP:PORT/&#123;R:2&#125;" />
                </rule>
            </rules>
        </rewrite>
        <staticContent>
            <mimeMap fileExtension=".glb" mimeType="application/glb" />
            <mimeMap fileExtension=".gltf" mimeType="application/gltf" />
            <clientCache cacheControlMode="DisableCache" cacheControlMaxAge="3.00:00:00" />
        </staticContent>
    </system.webServer>
</configuration>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当请求路径为</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2F%25E5%2589%258D%25E7%25AB%25AFIP%3APORT%2Fvideoapi%2F%25E5%2590%258E%25E5%258F%25B0%25E6%258E%25A5%25E5%258F%25A3" target="_blank" rel="nofollow noopener noreferrer" title="http://%E5%89%8D%E7%AB%AFIP:PORT/videoapi/%E5%90%8E%E5%8F%B0%E6%8E%A5%E5%8F%A3" ref="nofollow noopener noreferrer">http://前端IP:PORT/videoapi/后台接口</a></p>
<p>请求不会匹配到index，接下来匹配到api，就转发到api对应的地址了。</p>
<p>此时尽管把videoapi移到api前面也不行。</p>
<pre><code class="copyable"><rule name="videoapi" patternSyntax="Wildcard">
    <match url="*videoapi/*" />
    <action type="Rewrite" url="http://后台服务IP:PORT/videoapi/&#123;R:2&#125;" />
</rule>
<rule name="api" patternSyntax="Wildcard">
    <match url="*api/*" />
    <action type="Rewrite" url="http://后台服务IP:PORT/&#123;R:2&#125;" />
</rule>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>正确配置方法有二：</strong></p>
<h2 data-id="heading-13">一、修改代码，替换vedioapi的拦截方式</h2>
<h2 data-id="heading-14">二、在rule上添加stopProcessing="true"</h2>
<p>官方说明：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.microsoft.com%2Fzh-cn%2Fexchange%2Fclient-developer%2Fweb-service-reference%2Fstopprocessingrules" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.microsoft.com/zh-cn/exchange/client-developer/web-service-reference/stopprocessingrules" ref="nofollow noopener noreferrer">docs.microsoft.com/zh-cn/excha…</a></p>
<p>正确配置如下：</p>
<pre><code class="copyable"><?xml version="1.0" encoding="UTF-8"?>
<configuration>
    <system.webServer>
        <rewrite>
            <rules>
<rule name="index" stopProcessing="true">
                    <match url="^((?!(api)|(wsProxy)).)*$" />
                    <conditions>
                        <add input="&#123;REQUEST_FILENAME&#125;" matchType="IsFile" negate="true" />
                    </conditions>
                    <action type="Rewrite" url="/index.html" />
                </rule>
                <rule name="videoapi" patternSyntax="Wildcard" stopProcessing="true">
                    <match url="*videoapi/*" />
                    <action type="Rewrite" url="http://后台服务IP:PORT/videoapi/&#123;R:2&#125;" />
                </rule>
                <rule name="api" patternSyntax="Wildcard" stopProcessing="true">
                    <match url="*api/*" />
                    <action type="Rewrite" url="http://后台服务IP:PORT/&#123;R:2&#125;" />
                </rule>
<rule name="wsProxy" patternSyntax="Wildcard" 

stopProcessing="true">
                    <match url="*wsProxy/*" />
                    <action type="Rewrite" url="http://后台服务IP:PORT/&#123;R:2&#125;" />
                </rule>
            </rules>
        </rewrite>
        <staticContent>
            <mimeMap fileExtension=".glb" mimeType="application/glb" />
            <mimeMap fileExtension=".gltf" mimeType="application/gltf" />
            <clientCache cacheControlMode="DisableCache" cacheControlMaxAge="3.00:00:00" />
        </staticContent>
    </system.webServer>
</configuration>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意：</p>
<p>videoapi的配置要在api前面，当匹配videoapi成功后不执行后续的匹配规则。</p></div>  
</div>
            