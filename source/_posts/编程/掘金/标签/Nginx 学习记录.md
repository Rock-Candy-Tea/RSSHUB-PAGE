
---
title: 'Nginx 学习记录'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/643252a96bfb46f7b4c2e8c46acf8c8e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 06:26:15 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/643252a96bfb46f7b4c2e8c46acf8c8e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第20天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<h3 data-id="heading-1">吃饱饭才有力气写代码~</h3>
<p>今天把我师傅写的代码找出了两个bug,还挺骄傲嘿嘿~
<br>但是我还是啥也不会呀......现在学的好杂，接下来记录一下Nginx的知识点！参考了<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F349433" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/349433" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/349433</a> 这篇文章，帮助很大，感谢~</p>
<h3 data-id="heading-2">基本概念</h3>
<p>它是一个高性能的HTTP和反向代理web服务器，同时也提供了IMAP/POP3/SMTP服务。是由伊戈尔·赛索耶夫为俄罗斯访问量第二的Rambler.ru站点（俄文：Рамблер）开发的。
<br>
源代码以类BSD许可证的形式发布，因它的稳定性、丰富的功能集、简单的配置文件和低系统资源的消耗而闻名。
<br>
其特点是占有内存少，并发能力强，事实上nginx的并发能力在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。
<br>
以下是参考这个回答里的图片：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F349433" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/349433" ref="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/349433</a>
<br>下面这个图片说明了当下流行的技术架构，其中Nginx的作用类似于入口网关；
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/643252a96bfb46f7b4c2e8c46acf8c8e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">正向代理</h3>
<p>由于有防火墙，我们不能直接访问谷歌，这个时候就借助VPN来实现，这个感觉就是正向代理；这里面的逻辑像是，代理跟中介一样，客户端就是客户，客户通过中介与目标沟通！</p>
<h3 data-id="heading-4">反向代理</h3>
<p>反向代理就是说代理的是服务器端，这一过程对于客户端透明，就跟房屋租赁中介帮房东联系租客一样的感觉？！</p>
<h3 data-id="heading-5">Nginx 的 Master-Worker</h3>
<p>启动Nginx后，其实就是在80端口启动了Socket服务进行监听，如图所示，Nginx涉及Master进程和Worker进程。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae8ddf222e094dceb61ad4ecc97335af~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<strong>Master</strong>进程的作用：
<br>读取并验证配置文件nginx.conf；来对worker进程进行管理；
<br>
<strong>Worker</strong>进程的作用:
每一个Worker进程为了避免线程切换都维护一个线程，处理连接和请求；Worker进程的个数由nginx.conf配置文件决定，配置几个就有几个Worker进程。</p>
<h3 data-id="heading-6">Nginx 的热部署</h3>
<p>它有一个nginx.conf配置文件，修改这个文件就行，不需要停掉nginx，也不用中断那些请求，这个配置文件就能生效。<br>
联系到进程，就是修改完配置文件，会用新的配置去处理请求，这些都会进入到新的worker进程里，老的那些worker进程会在以前的那些处理请求完成后被kill掉。</p>
<h3 data-id="heading-7">虽然上面这些看上去很基础或者是很琐碎，但是呢因为我师傅之前大致给我提过一嘴这些，我就感觉这个好像和昨天学的什么docker 啊，服务啊，有点儿联系上了。再深入详细的等我再学习学习！加油啊~</h3></div>  
</div>
            