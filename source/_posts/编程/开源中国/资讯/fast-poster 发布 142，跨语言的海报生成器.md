
---
title: 'fast-poster 发布 1.4.2，跨语言的海报生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://fastposter.oss-cn-shanghai.aliyuncs.com/v1.4.0/WX20210707-232649%402x.png'
author: 开源中国
comments: false
date: Wed, 14 Jul 2021 08:08:00 GMT
thumbnail: 'https://fastposter.oss-cn-shanghai.aliyuncs.com/v1.4.0/WX20210707-232649%402x.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align: left;">fast-poster发布1.4.2 跨语言的海报生成器，一分钟完成海报开发</p> 
<h3 style="text-align:left">future:</h3> 
<ul> 
 <li>完善docker镜像</li> 
 <li>引入异步asyncio</li> 
 <li>升级python到3.9.6</li> 
 <li>升级pillow版本为8.3.1</li> 
 <li>集群部署适配</li> 
 <li>Pillow绘制海报，性能优化</li> 
 <li>增加启动说明</li> 
</ul> 
<h3 style="text-align:left">fixbug:</h3> 
<ul> 
 <li>解决PHP代码生成问题</li> 
 <li>解决Docker镜像打包后无法运行问题</li> 
 <li>解决辅助线为虚线问题</li> 
</ul> 
<h3 style="text-align:left">仓库地址</h3> 
<p style="text-align:left">欢迎点亮小星星⭐️⭐，加速项目迭代更新。</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpsoho%2Ffast-poster" target="_blank">代码仓库-github</a></li> 
 <li><a href="https://gitee.com/psoho/fast-poster">代码仓库-gitee</a></li> 
</ul> 
<h3 style="text-align:left">Java客户端代码调用预览</h3> 
<pre style="text-align:left"><code><em>// Java生成海报</em>
<strong>public</strong> <strong>static</strong> <strong>void</strong> <strong>main</strong>(String[] args) <strong>throws</strong> IOException &#123;

  <em>// 创建海报客户端对象</em>
  FastPosterClient client = <strong>new</strong> FastPosterClient(<span style="color:#dd1144">"https://poster.prodapi.cn/"</span>, <span style="color:#dd1144">"ApfrIzxCoK1DwNZO"</span>, <span style="color:#dd1144">"EJCwlrnv6QZ0PCdvrWGi"</span>);

  <em>// 构造海报参数</em>
  HashMap<String, String> params = <strong>new</strong> HashMap<>();
  <em>// 暂未指定任何动态参数</em>
  params.put(<span style="color:#dd1144">"nickname"</span>, <span style="color:#dd1144">"笑傲江湖"</span>);

  <em>// 海报ID</em>
  String posterId = <span style="color:#dd1144">"25"</span>;

  <em>// 获取下载地址</em>
  String url = client.getUrl(posterId, params);
  System.out.println(<span style="color:#dd1144">"url="</span> + url);

  <em>// 保存到本地</em>
  client.saveToPath(url, <span style="color:#dd1144">"temp.png"</span>);

&#125;
</code></pre> 
<h3 style="text-align:left">只需三步，即可完成海报开发 <code>启动服务</code> > <code>编辑海报</code> > <code>生成代码</code></h3> 
<h4 style="text-align:left">一、启动服务</h4> 
<pre style="text-align:left"><code>docker run --name fast-poster -p <span style="color:#008080">9001</span>:<span style="color:#008080">9001</span> tangweixin/fast-poster
</code></pre> 
<h4 style="text-align:left">二、编辑海报</h4> 
<p style="text-align:left"><img alt="输入图片说明" src="https://fastposter.oss-cn-shanghai.aliyuncs.com/v1.4.0/WX20210707-232649%402x.png" referrerpolicy="no-referrer"></p> 
<h4 style="text-align:left">三、生成代码</h4> 
<p style="text-align:left"><img alt="输入图片说明" src="https://fastposter.oss-cn-shanghai.aliyuncs.com/v1.4.0/WX20210707-232717%402x.png" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">详细介绍文档</h3> 
<p style="text-align:left"><a href="https://gitee.com/psoho/fast-poster">https://gitee.com/psoho/fast-poster</a></p>
                                        </div>
                                      
</div>
            