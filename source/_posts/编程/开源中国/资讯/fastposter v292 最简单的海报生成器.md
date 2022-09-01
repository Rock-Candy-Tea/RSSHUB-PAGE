
---
title: 'fastposter v2.9.2 最简单的海报生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://poster.prodapi.cn/doc/assets/image-20220407142530149.png'
author: 开源中国
comments: false
date: Thu, 01 Sep 2022 14:48:00 GMT
thumbnail: 'https://poster.prodapi.cn/doc/assets/image-20220407142530149.png'
---

<div>   
<div class="content">
                                                                                            <h2>fastposter v2.9.2 程序员必备海报生成器</h2> 
<p>🔥🔥🔥 fastposter海报生成器是一款快速开发海报的工具。只需上传一张背景图，在对应的位置放上组件（<code>文字</code>、<code>图片</code>、<code>二维🐴</code>、<code>头像</code>）即可生成海报。 点击<code>代码</code>直接生成各种语言的调用代码，方便快速开发。</p> 
<p>现已服务众多电商类项⽬，多个项⽬有<code>50W+</code>⽤户，通过多年⽣产环境的考验，稳定可靠。广泛应用于各类电商、分销系统、电商海报、电商主图等海报生成和制作场景。</p> 
<h3>社区版 v2.9.2 发布</h3> 
<ul> 
 <li>升级requests_cache==0.9.6</li> 
 <li>升级tornado==6.2</li> 
 <li>代码整理</li> 
</ul> 
<h3>专业版 v2.0.12 发布</h3> 
<ul> 
 <li>通过参数处理图片，支持scale缩放</li> 
 <li>增加独立二维码生成接口</li> 
 <li>批量生成，更改fp_batch表的字段rows -> raw (适配数据库)</li> 
 <li>java版本增加postgres数据库支持</li> 
 <li>依赖版本升级 
  <ul> 
   <li>Pillow==9.2.0</li> 
   <li>requests==2.28.1</li> 
   <li>requests_cache==0.9.6</li> 
  </ul> </li> 
</ul> 
<h3>相关地址</h3> 
<ul> 
 <li>开发文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fposter.prodapi.cn%2Fdoc%2F" target="_blank">https://poster.prodapi.cn/doc/</a></li> 
 <li>在线演示：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fposter.prodapi.cn%2F%23from%3Dpush-v2.9.2" target="_blank">https://poster.prodapi.cn/</a></li> 
 <li>专业版Python在线演示：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fposter.prodapi.cn%2Fpro%2F%23from%3Dpush-v2.9.2" target="_blank">https://poster.prodapi.cn/pro/</a></li> 
 <li>专业版Java在线演示：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fposter.prodapi.cn%2Fpro%2Fjava%2F%23from%3Dpush-v2.9.2" target="_blank">https://poster.prodapi.cn/pro/java/</a></li> 
</ul> 
<h3>只需三步，即可完成海报开发</h3> 
<h4>一、启动服务</h4> 
<pre><code class="language-bash">docker run -it --name fast-poster -p 5000:5000 tangweixin/fast-poster
</code></pre> 
<h4>二、编辑海报</h4> 
<p><img alt="fastposter编辑海报" src="https://poster.prodapi.cn/doc/assets/image-20220407142530149.png" referrerpolicy="no-referrer"></p> 
<h4>三、生成代码</h4> 
<p><img alt="fastposter生成代码" src="https://poster.prodapi.cn/doc/assets/image-20220407142705928.png" referrerpolicy="no-referrer"></p> 
<p>请求示例（可直接传递需要的参数）</p> 
<pre><code class="language-bash">curl --location --request POST 'https://poster.prodapi.cn/api/link' \\
--header 'Content-Type: application/json' \\
--header 'token: ApfrIzxCoK1DwNZOEJCwlrnv6QZ0PCdv' \\
--data-raw '&#123;
  "title": "人工智能+机器学习",
  "id": 2
&#125;'
</code></pre> 
<p>响应示例（返回海报的访问地址）</p> 
<pre><code class="language-json">&#123;
    "code": 0,
    "msg": "success",
    "data": &#123;
        "url": "https://poster.prodapi.cn/v/90295c118d4c8802"
    &#125;
&#125;
</code></pre> 
<h3>适用场景：</h3> 
<ul> 
 <li>海报生成器</li> 
 <li>海报自动生成工具</li> 
 <li>海报在线设计生成器</li> 
 <li>海报生成器在线制作</li> 
 <li>生成朋友圈海报</li> 
 <li>电商海报编辑器</li> 
 <li>证书制作</li> 
 <li>证书自动生成工具</li> 
 <li>Python Pillow绘图 Pillow制作海报</li> 
 <li>电商主图编辑器</li> 
 <li>Java生成分享海报图片</li> 
 <li>微信小程序生成海报分享朋友圈</li> 
 <li>PHP生成海报图片</li> 
 <li>自定义商业海报图片</li> 
 <li>H5生成海报图片</li> 
 <li>canvas生成海报图片</li> 
 <li>通过JSON生成海报图片</li> 
 <li>BufferdImage绘制图片</li> 
</ul>
                                        </div>
                                      
</div>
            