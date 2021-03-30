
---
title: 'NGINX Unit 1.23.0 发布，动态 Web 应用服务器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=287'
author: 开源中国
comments: false
date: Tue, 30 Mar 2021 07:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=287'
---

<div>   
<div class="content">
                                                                    
                                                        <p>NGINX Unit 1.23.0 已发布，更新内容包括改进对 TLS 的支持、简化 TLS 配置以及修复错误等。</p> 
<p>举个例子，开发者只需要上传某个服务器名字下的证书链和密钥，然后就可以使用任意监听套接字来指定服务器名字，并将其配置为 HTTPS，这里例子的名字是"mycert"：</p> 
<pre><code>  &#123;
      "listeners": &#123;
          "*:443": &#123;
              "tls": &#123;
                  "certificate": "mycert"
              &#125;,

              "pass": "routes"
          &#125;
      &#125;
  &#125;</code></pre> 
<p>部分新变化：</p> 
<ul> 
 <li>Feature: 通过服务器名称指示 (SNI) TLS 扩展，支持一个监听器上的多个证书捆绑</li> 
 <li>Feature: "--mandir" ./configure 选项可以指定主页面安装的目录</li> 
 <li>Bugfix: 修复 TLS 连接过早关闭时，路由进程可能会崩溃的问题；该错误曾在 1.17.0 中出现</li> 
 <li>Bugfix: 修复 TLS 连接过早关闭时发生连接泄漏的问题，该问题曾在 1.6 中出现</li> 
 <li>Bugfix: 修复当处理来自客户端的小型 WebSocket 帧时，路由进程中出现了描述符和内存泄漏的问题；该问题曾在 1.19.0 中出现</li> 
 <li>Bugfix: 修复当删除或重新配置应用程序时，在路由进程中发生描述符泄漏的问题；该问题曾在 1.19.0 中出现</li> 
 <li>Bugfix: 修复证书的持久化存储在 Linux 的某些文件系统中可能无法运行的问题，所有上传的证书捆绑在重新启动后不再被记住的问题</li> 
 <li>Bugfix: 修复控制器进程在请求非 DNS SAN 条目的证书信息时可能会崩溃的问题</li> 
 <li>Bugfix: 修复控制器进程在对包含 SAN 的证书进行操作时可能会崩溃的问题，并且在 subject 或 issuer 中没有标准名称属性</li> 
 <li>Bugfix: 修复 Ruby 模块在 Encoding 类的默认值中不遵循用户 locale 的问题</li> 
 <li>Bugfix: 修复 PHP 5 模块在启用线程安全时未能构建的问题，该问题曾在 1.22.0 中出现过</li> 
</ul> 
<p>正在开发的功能：</p> 
<ul> 
 <li>statistics API</li> 
 <li>process control API</li> 
 <li>在静态文件服务期间，根据每个请求进行 chroot</li> 
 <li>针对静态文件的 MIME 类型过滤</li> 
 <li>配置密码和其他 OpenSSL 设置</li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmailman.nginx.org%2Fpipermail%2Funit%2F2021-March%2F000264.html" target="_blank">详情点此查看</a>。</p> 
<p>NGINX Unit 是用于各种 Web 应用程序的轻量动态开源服务器。NGINX Unit 从头开始构建，可以一次运行多种语言版本的 Web 应用程序，它也可以在运行时完全配置为零中断，从而可以对工程和操作进行实时粒度管理。</p>
                                        </div>
                                      
</div>
            