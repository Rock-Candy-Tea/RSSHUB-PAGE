
---
title: 'fastposter v2.8.4 发布 电商海报生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://poster.prodapi.cn/doc/assets/image-20220407142530149.png'
author: 开源中国
comments: false
date: Tue, 28 Jun 2022 07:56:00 GMT
thumbnail: 'https://poster.prodapi.cn/doc/assets/image-20220407142530149.png'
---

<div>   
<div class="content">
                                                                                            <h2>fastposter v2.8.4 发布 电商海报生成器</h2> 
<p>🔥🔥🔥 fastposter海报生成器，电商海报编辑器，电商海报设计器，fast快速生成海报 海报制作 海报开发。贰维🐴海报，图片海报，分享海报贰维🐴码推广海报，支持Java Python PHP Go JS 小程序。基于Vue 和Pillow。</p> 
<h3>社区版 v2.8.4 发布</h3> 
<ul> 
 <li>预览按钮更换位置，与专业版保持一致</li> 
 <li>生层代码按钮更换位置，与专业版保持一致</li> 
 <li>去除文档中的捐赠</li> 
 <li>整理代码</li> 
 <li>升级依赖 <code>requests==2.28.0</code></li> 
</ul> 
<h3>专业版Python v2.0.9 发布</h3> 
<ul> 
 <li>设计器效果最佳的行高设置</li> 
 <li>解决Safari下载海报中文乱码问题</li> 
 <li>修复贰维🐴内边距空白问题</li> 
 <li>规范数据命名使用驼峰，与Java版本保持一致</li> 
 <li>默认生成一个用户API凭证</li> 
 <li>增加上传失败提示</li> 
 <li>规范云存储配置命名，与Java版本保持一致</li> 
 <li>更新Java开发文档</li> 
 <li>优化拖拽组件(性能优化) 使用开源的vue-drag-resize组件 样式调整 dblclick stick-size 样式调整</li> 
 <li>解决组件不重新渲染问题</li> 
 <li>基于vue-drag-resize重构拖拽组件，解决拖拽偶发的卡顿问题</li> 
 <li>整理代码</li> 
</ul> 
<h3>专业版Java v2.0.9 发布</h3> 
<ul> 
 <li>更新云存储</li> 
 <li>解决凭证失效无法重新发放问题</li> 
 <li>优化拖拽组件(性能优化) 使用开源的vue-drag-resize组件 样式调整 dblclick stick-size 样式调整</li> 
 <li>解决组件不重新渲染问题</li> 
 <li>基于vue-drag-resize重构拖拽组件，解决拖拽偶发的卡顿问题</li> 
</ul> 
<h3>相关地址</h3> 
<ul> 
 <li>开发文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fposter.prodapi.cn%2Fdoc%2F" target="_blank">https://poster.prodapi.cn/doc/</a></li> 
 <li>在线演示：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fposter.prodapi.cn%2F%23from%3Dpush-v2.8.4" target="_blank">https://poster.prodapi.cn/</a></li> 
 <li>专业版Python在线演示：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fposter.prodapi.cn%2Fpro%2F%23from%3Dpush-v2.8.4" target="_blank">https://poster.prodapi.cn/pro/</a></li> 
 <li>专业版Java在线演示：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fposter.prodapi.cn%2Fpro%2Fjava%2F%23from%3Dpush-v2.8.4" target="_blank">https://poster.prodapi.cn/pro/java/</a></li> 
</ul> 
<h3>只需三步，即可完成海报开发</h3> 
<h4>一、启动服务</h4> 
<pre><code class="language-bash">docker run -it --name fast-poster -p 5000:5000 tangweixin/fast-poster</code></pre> 
<h4>二、编辑海报</h4> 
<p><img alt="fastposter编辑海报" src="https://poster.prodapi.cn/doc/assets/image-20220407142530149.png" referrerpolicy="no-referrer"></p> 
<h4>三、生成代码</h4> 
<p><img alt="fastposter生成代码" src="https://poster.prodapi.cn/doc/assets/image-20220407142705928.png" referrerpolicy="no-referrer"></p> 
<p>请求示例（可直接传递需要的参数）</p> 
<pre><code class="language-bash">curl --location --request POST 'https://poster.prodapi.cn/api/link' \
--header 'Content-Type: application/json' \
--header 'token: ApfrIzxCoK1DwNZOEJCwlrnv6QZ0PCdv' \
--data-raw '&#123;
  "title": "人工智能+机器学习",
  "id": 2
&#125;'</code></pre> 
<p>响应示例（返回海报的访问地址）</p> 
<pre><code class="language-json">&#123;
    "code": 0,
    "msg": "success",
    "data": &#123;
        "url": "https://poster.prodapi.cn/v/90295c118d4c8802"
    &#125;
&#125;</code></pre> 
<h3>适用场景：</h3> 
<ul> 
 <li>海报生成器</li> 
 <li>海报生成</li> 
 <li>海报生成网站</li> 
 <li>海报自动生成工具</li> 
 <li>海报在线设计生成器</li> 
 <li>海报生成系统</li> 
 <li>海报生成器在线制作</li> 
 <li>生成朋友圈海报</li> 
 <li>电商海报编辑器</li> 
 <li>证书生成</li> 
 <li>证书制作</li> 
 <li>证书自动生成工具</li> 
 <li>证书自动生成器</li> 
 <li>条形码</li> 
 <li>贰维🐴分享海报图片</li> 
 <li>Python Pillow绘图 Pillow制作海报</li> 
 <li>电商主图编辑器</li> 
 <li>Java生成贰维🐴分享海报图片</li> 
 <li>Java Graphics2D绘制海报图片</li> 
 <li>微信小程序生成海报分享朋友圈</li> 
 <li>PHP生成贰维🐴海报图片</li> 
 <li>自定义商业海报图片</li> 
 <li>H5生成海报图片</li> 
 <li>canvas生成海报图片</li> 
 <li>通过JSON生成海报图片</li> 
 <li>BufferdImage绘制图片</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            