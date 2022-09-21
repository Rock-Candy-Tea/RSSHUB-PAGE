
---
title: '数据可视化平台飞鱼（FlyFish）2.2.1 更新，新增 ClickHouse 等更多数据源！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2424'
author: 开源中国
comments: false
date: Wed, 21 Sep 2022 13:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2424'
---

<div>   
<div class="content">
                                                                                            <div> 
 <h1>关于FlyFish</h1> 
 <blockquote> 
  <div>
   FlyFish 是云智慧公司自主设计、研发的一款低门槛、高拓展性的低代码应用开发平台， 为数据可视化开发场景提供了高效的一站式解决方案。飞鱼提供丰富的组件和应用模板库， 可通过拖拉拽的形式完成数据可视化开发，零开发背景的用户也可完成数据可视化开发工作。 同时，飞鱼也提供了灵活的拓展能力，支持组件开发、自定义函数与全局事件等配置， 面向复杂需求场景能够保证高效开发与交付。
  </div> 
  <div>
    
  </div> 
  <ul> 
   <li> 
    <div>
     <strong>使用方式一：</strong>
     <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflyfish-demo.opscloudwise.com%3A23368%2F%23%2Flogin" target="_blank">线上Demo环境体验</a></strong>
    </div> </li> 
  </ul> 
  <ul> 
   <li> 
    <div>
     <strong>使用方式二：</strong>
     <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCloudWise-OpenSource%2FFlyFish" target="_blank">本地下载部署使用</a></strong>
    </div> </li> 
  </ul> 
 </blockquote> 
</div> 
<h1>更新内容</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">​​​​​​<span>🌟</span>新增功能</h2> 
<ul> 
 <li>新增PostgreSQL、Oracle、ClickHouse三种数据源。</li> 
 <li>FlyFish 2.2.1 docker 镜像部署更新</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">​​​​​​<span>🌟</span>功能优化</h2> 
<ul> 
 <li>优化部署文档，明确命令执行目录。</li> 
</ul> 
<h2>​​​​​​<span>🌟BUG</span>修复</h2> 
<ul> 
 <li>修改用户列表邮箱正则校验规则。</li> 
 <li>修改一键部署后，大屏应用数据查询无效的Bug。</li> 
</ul> 
<h1>附件</h1> 
<h2>FlyFish docker 镜像使用指南</h2> 
<blockquote> 
 <p><strong>该镜像只支持 x86 的类 unix 系统</strong></p> 
</blockquote> 
<ul> 
 <li>机器上安装 docker 和 docker-compose</li> 
 <li>下载 FlyFish <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCloudWise-OpenSource%2FFlyFish%2Freleases%2Fdownload%2FFlyFish-2.2.1%2Fdocker-compose.yaml" target="_blank">docker-compose.yaml</a>文件，并放置到单独的文件夹中</li> 
 <li>在 docker-compose.yaml 所在的文件夹执行</li> 
</ul> 
<pre><code class="language-shell">docker-compose up -d
</code></pre> 
<ul> 
 <li>执行命令后，看到</li> 
</ul> 
<pre><code class="language-shell">Creating mongodb           ... done
Creating flyfishcodeserver ... done
Creating flyfishserver     ... done
Creating fiyfishweb        ... done
Creating flyfishdataserver ... done
</code></pre> 
<p>则服务启动成功。</p> 
<blockquote> 
 <p>由于FlyFish 内嵌了 33 个组件，需要等组件初始化完成后才能登录成功</p> 
 <p>查看 server 日志：docker logs flyfishserver -f</p> 
 <p>upload component success: 62d60a64ae3be617a2a61ad3, progress: 33/33 upload done</p> 
 <p>至此 组件初始化完成</p> 
</blockquote> 
<ul> 
 <li> <p>访问地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F127.0.0.1%3A8089" target="_blank">http://127.0.0.1:8089</a></p> <p>用户名：admin 密码：utq#SpV!</p> </li> 
</ul> 
<div> 
 <h1>参与贡献</h1> 
 <div>
  如果喜欢我们的项目，请不要忘记点击下方代码仓库地址，在 
  <strong><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCloudWise-OpenSource%2FFlyFish" target="_blank">GitHub</a></strong>
  <strong> / </strong>
  <strong><a href="https://gitee.com/CloudWise/fly-fish">Gitee</a></strong> 仓库上点个 Star，我们需要您的鼓励与支持。此外，即刻参与 FlyFish 项目贡献成为 FlyFish Contributor 的同时更有万元现金等你来拿。
 </div> 
 <div>
   
 </div> 
 <div>
  <strong>GitHub 地址： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FCloudWise-OpenSource%2FFlyFish" target="_blank">https://github.com/CloudWise-OpenSource/FlyFish</a></strong>
 </div> 
 <div style="text-align:left">
  <strong>Gitee 地址：</strong>
  <strong><a href="https://gitee.com/CloudWise/fly-fish">https://gitee.com/CloudWise/fly-fish</a></strong>
 </div> 
</div>
                                        </div>
                                      
</div>
            