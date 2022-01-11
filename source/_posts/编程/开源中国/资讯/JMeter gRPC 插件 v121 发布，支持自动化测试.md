
---
title: 'JMeter gRPC 插件 v1.2.1 发布，支持自动化测试'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-e8af660ad04ffadff2fab5e1cbb21036bdf.png'
author: 开源中国
comments: false
date: Tue, 11 Jan 2022 14:20:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-e8af660ad04ffadff2fab5e1cbb21036bdf.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt height="310" src="https://oscimg.oschina.net/oscnet/up-e8af660ad04ffadff2fab5e1cbb21036bdf.png" width="760" referrerpolicy="no-referrer"></p> 
<blockquote> 
 <p>这个JMeter采样器允许您向服务器发送一个gRPC请求</p> 
 <p>它和HTTP请求一样简单</p> 
</blockquote> 
<h2>介绍</h2> 
<p>他是一个功能强大的JMeter Grpc插件，可用于测试任何gRPC服务器，它不需要生成gRPC类或编译服务的protos二进制文件，只是一个非常简单的输入：</p> 
<ul> 
 <li>gRPC服务的主机和端口</li> 
 <li>需要测试的RPC方法</li> 
 <li>proto文件路径</li> 
 <li>格式化的JSON请求数据</li> 
</ul> 
<h2>特性</h2> 
<ul> 
 <li>支持压测阻塞等调用方式</li> 
 <li>支持在运行时解析proto文件</li> 
 <li>支持TLS连接</li> 
 <li>支持元数据认证(JWT/Token)</li> 
 <li>支持JSON格式的请求数据</li> 
 <li>支持运行在Windows、Mac、Linux中</li> 
 <li>支持自动列出proto文件中的所有完整方法</li> 
 <li>支持根据proto文件自动生成请求Mock</li> 
 <li>支持各种报告生成</li> 
 <li>支持自动化测试</li> 
</ul> 
<h2>如何使用</h2> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-8aaf1821a6f4d2b4cb2f1a699bccdcb41ba.gif" referrerpolicy="no-referrer"></p> 
<h3>插件安装</h3> 
<p>你需要将 <strong>jmeter-grpc-request</strong> 插件的 <code>jar</code> 包复制到JMeter的 <code>lib/ext</code> 目录下面，然后重启你的JMeter工具。</p> 
<p><strong>jmeter-grpc-request</strong> 插件的 <code>jar</code> 包，可以从 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Freleases" target="_blank">Releases Page</a> 获得，也可以 在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjmeter-plugins.org%2F%3Fsearch%3Djmeter-grpc-request" target="_blank">JMeter Plugins Manager</a> 中找到</p> 
<h3>使用说明</h3> 
<table> 
 <tbody> 
  <tr> 
   <th>序号</th> 
   <th>选项</th> 
   <th>描述</th> 
  </tr> 
 </tbody> 
 <tbody> 
  <tr> 
   <td>1</td> 
   <td>Server Name or IP</td> 
   <td>gRPC服务器地址（域名或IP）</td> 
  </tr> 
  <tr> 
   <td>2</td> 
   <td>Port Number</td> 
   <td>gRPC服务器端口 (80/ 443)</td> 
  </tr> 
  <tr> 
   <td>3</td> 
   <td>SSL/TLS</td> 
   <td>开启SSL/TLS认证</td> 
  </tr> 
  <tr> 
   <td>4</td> 
   <td>Proto Root Directory</td> 
   <td>proto文件的根路径</td> 
  </tr> 
  <tr> 
   <td>5</td> 
   <td>Library Directory (Optional)</td> 
   <td>proto文件解析需要依赖的额外库的文件夹路径 (googleapis)</td> 
  </tr> 
  <tr> 
   <td>6</td> 
   <td>Full Method</td> 
   <td>用于请求测试的RPC方法</td> 
  </tr> 
  <tr> 
   <td>7</td> 
   <td>Metadata</td> 
   <td><span style="background-color:#ffffff; color:#24292f">Metadata可以用于token身份验证等方式，支持以下两种方式传输（UTF-8）：</span><br> <span style="background-color:#ffffff; color:#24292f">1. 使用键值对（Key: Value）：</span><br> <span style="background-color:#ffffff; color:#24292f">  - key1: value1, key2: value2</span><br> <span style="background-color:#ffffff; color:#24292f">2.</span><span style="background-color:#ffffff; color:#24292f"> 使用 </span><span style="background-color:#ffffff; color:#24292f">Json String：</span><br> <span style="background-color:#ffffff; color:#24292f">   - &#123;"key1":"Value1", "key2":"value2"&#125;</span></td> 
  </tr> 
  <tr> 
   <td>8</td> 
   <td>Deadline</td> 
   <td>请求超时时间（单位：毫秒）</td> 
  </tr> 
  <tr> 
   <td>9</td> 
   <td>Send JSON Format With the Request</td> 
   <td>格式化的JSON请求数据</td> 
  </tr> 
 </tbody> 
</table> 
<h2>v1.2.1</h2> 
<h3>修复:</h3> 
<ul> 
 <li><span style="color:#252525">使用 SSL 运行时，JDK 提供程序不支持 NPN_AND_ALPN 协议</span><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Fpull%2F93" target="_blank">#93</a></li> 
</ul> 
<p><strong>完整更新日志</strong>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzalopay-oss%2Fjmeter-grpc-request%2Freleases" target="_blank">releases</a></p>
                                        </div>
                                      
</div>
            