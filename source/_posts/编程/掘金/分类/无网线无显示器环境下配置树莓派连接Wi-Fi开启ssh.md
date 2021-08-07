
---
title: '无网线无显示器环境下配置树莓派连接Wi-Fi开启ssh'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4be057bb88845c887502ebc10fee258~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 08:38:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4be057bb88845c887502ebc10fee258~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">无网线无显示器环境下配置树莓派连接Wi-Fi开启ssh</h1>
<p>今天突然想折腾一下树莓派于是打开我的行李箱，拿出我那崭新的树莓派，当拿出树莓派的时候发生了尴尬的事情，没有网线，没有键盘显示器，这种情况下该怎么连接树莓派呢？第一时间我想树莓派的系统是烧录在sd卡中的是不是可以在系统配置中来做文章呢。</p>
<h2 data-id="heading-1">所需要的物品</h2>
<ul>
<li>一个手机</li>
<li>Termux（软件我放在文末）</li>
<li>一个读卡器（读取树莓派的sd卡）</li>
</ul>
<blockquote>
<p>甚至可以只用手机（如果手机可以支持插sd的话，这里我条件还没那么苛刻，有一台电脑一个扩展坞）</p>
</blockquote>
<h2 data-id="heading-2">自动连接wifi原理</h2>
<p>用户可以在未启动树莓派的状态下单独修改 <code>/boot/wpa_supplicant.conf</code> 文件配置 WiFi 的 SSID 和密码，这样树莓派启动后会自行读取 <code>wpa_supplicant.conf </code>配置文件连接 WiFi 设备。</p>
<h2 data-id="heading-3">1、添加自动连接wifi步骤</h2>
<h3 data-id="heading-4">第一步：先把树莓派上的sd卡取下来</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4be057bb88845c887502ebc10fee258~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG53" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">第二步：把sd卡插入到扩展坞中并插到电脑上</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15fad078d10a4407a581df5e38197c70~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG54" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c2342eb0a5b4d9bbb31d343ecb65e54~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG55" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">第三步：在电脑中打开sd卡根目录创建名字为<code>wpa_supplicant.conf</code> 的文件</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d0edb49a64a4d86a9b1c5d8c6191480~tplv-k3u1fbpfcp-watermark.image" alt="image-20210806222213220" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">第四步：为<code>wpa_supplicant.conf</code> 的文件添加如下内容</h3>
<pre><code class="hljs language-bash copyable" lang="bash">country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network=&#123;
ssid=<span class="hljs-string">"12345678"</span>
psk=<span class="hljs-string">"88888888"</span>
key_mgmt=WPA-PSK
priority=1
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面配置文件的含义是：</p>
<ul>
<li>ssid:网络的ssid</li>
<li>psk:密码</li>
<li>priority: 连接优先级，数字越大优先级越高（不可以是负数）</li>
<li>scan_ssid:连接隐藏WiFi时需要指定该值为1</li>
</ul>
<blockquote>
<p>因为我这里不能进入路由器后台看树莓派的地址，所以是用手机开的热点让树莓派连接到我的热点</p>
</blockquote>
<h2 data-id="heading-8">2、配置开启ssh</h2>
<p>在<code>boot</code>分区里新建一个名字为<code>ssh</code>的空文件，这样系统在启动的时候就可以识别出来，从而在开机的时候就开启<code>ssh</code></p>
<h2 data-id="heading-9">3、完成后的文件目录</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/874d370ad6ad4daabd8f582a7eee5e8e~tplv-k3u1fbpfcp-watermark.image" alt="image-20210806222309814" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">4、连接树莓派</h2>
<h3 data-id="heading-11">第一步：开启手机热点</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9adb4fdeb43a46acbcb4959c586ee005~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">第二步：启动树莓派等待树莓派开机并等待树莓派连接Wi-Fi</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78fd584c4cd24b7aa2a474ceae356049~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG57" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">第三步： 打开 Termux 软件查看树莓派ip地址</h3>
<p>因为是连接的手机的热点，所以可以看到树莓派已经连接了Wi-Fi</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a90767a7da2745c3b3c0e68f36fa041f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210807002902731" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftermux.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://termux.com/" ref="nofollow noopener noreferrer">Termux</a> 软件输入 <code>ip neigh</code> 命令查看树莓派ip地址</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b10106c092f2426195eb396192a675a2~tplv-k3u1fbpfcp-watermark.image" alt="WechatIMG58" loading="lazy" referrerpolicy="no-referrer"></p>
<p>知道了IP之后我们就可以用电脑连接手机热点，ssh登陆到树莓派了，登陆树莓派之后配置ip地址与连接Wi-Fi了，配置之后就可以在内网中使用了</p>
<h2 data-id="heading-14"><a href="https://link.juejin.cn/?target=https%3A%2F%2Ftermux.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://termux.com/" ref="nofollow noopener noreferrer">Termux</a> 软件下载地址</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b73401376874bf1bd11b5f09f13f866~tplv-k3u1fbpfcp-watermark.image" alt="image-20210806225413218" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fkspf.xyz%2Farchives%2F135" target="_blank" rel="nofollow noopener noreferrer" title="https://kspf.xyz/archives/135" ref="nofollow noopener noreferrer">原文地址: https://kspf.xyz/archives/135</a></p>
</blockquote></div>  
</div>
            