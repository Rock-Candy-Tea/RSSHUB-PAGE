
---
title: 'Midway v2.11.7 发布，Node.js 框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8019'
author: 开源中国
comments: false
date: Sat, 24 Jul 2021 22:44:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8019'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p>Midway 是一个适用于构建 Serverless 服务，传统应用、微服务，小程序后端的 Node.js 框架。</p> 
 <p>一些小更新</p> 
 <h3>1、修复 @midwayjs/socketio 特殊场景下的端口问题</h3> 
 <p>在旧版本，当同时启用副框架和 socket.io port 的时候，port 会被忽略。</p> 
 <p>比如：</p> 
 <pre>// main framework
const web = new WebFramework().configure(&#123;
  port: 7001,
&#125;);

const socket = new SocketFramework().configure(&#123;
port: 8001
&#125;);

const &#123; Bootstrap &#125; = require('@midwayjs/bootstrap');
// load and run
Bootstrap.load(web).load(socket).run();</pre> 
 <p>虽然 socket 框架指定了 8001 端口，但是还是会自动找到 7001 端口，变为副框架启动。</p> 
 <p>新版本修复了该问题。</p> 
 <h3>2、导出 @midwayjs/express 的 generateMiddleware 定义</h3> 
 <p>本 PR 由社区用户 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjiangzm" target="_blank">@jiangzm</a> 提交，感谢。</p> 
 <p> </p> 
</div>
                                        </div>
                                      
</div>
            