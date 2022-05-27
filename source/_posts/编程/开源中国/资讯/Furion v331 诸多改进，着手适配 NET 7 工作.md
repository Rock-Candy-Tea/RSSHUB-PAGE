
---
title: 'Furion v3.3.1 诸多改进，着手适配 .NET 7 工作'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-53d830d1b21a0b1e4e6daad01655cd783d6.png'
author: 开源中国
comments: false
date: Fri, 27 May 2022 07:06:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-53d830d1b21a0b1e4e6daad01655cd783d6.png'
---

<div>   
<div class="content">
                                                                                            <h2>前言</h2> 
<p><strong>花了两周的时间对 Furion 进行了诸多改进，新增了不少开发者呼声大的特性，同时开始适配 .NET7 的工作。</strong></p> 
<ul> 
 <li>项目地址：<a href="https://gitee.com/dotnetchina/Furion">https://gitee.com/dotnetchina/Furion</a></li> 
 <li>文档地址：<a href="https://dotnetchina.gitee.io/furion/">https://dotnetchina.gitee.io/furion/</a></li> 
</ul> 
<p> </p> 
<p><img height="1080" src="https://oscimg.oschina.net/oscnet/up-53d830d1b21a0b1e4e6daad01655cd783d6.png" width="1920" referrerpolicy="no-referrer"></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p style="margin-left:0; margin-right:0"><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 远程请求文件上传自动识别<span> </span><code>Content-Type</code><span> </span>和<span> </span><code>Mime</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I57ZMN">#I57ZMN</a></li> 
    <li>[新增] 远程请求方法支持设置<span> </span><code>Content-Type</code><span> </span>和<span> </span><code>Encoding</code><span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I57ZMN">#I57ZMN</a></li> 
    <li>[新增] 根据文件名获取<span> </span><code>Content-Type</code><span> </span>和<span> </span><code>Mime</code><span> </span>类型<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/8f78184f8661830744592c054b65d503346c1b27">#8f78184</a></li> 
    <li>[新增] 规范化文档支持授权访问<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/32aa3b6328d23a5885033837883c7b546e898d43">#32aa3b6</a></li> 
    <li>[新增] 代码注释，规范化文档注释<span> </span><code>inheritdoc</code><span> </span>语法支持 ❤️️️️<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I59A6W">#159A6W</a></li> 
    <li>[新增] 新增<span> </span><code>Vue2/3</code>，<code>React 16.8+</code>，<code>Angular 9+</code><span> </span>前端请求工具库，实现后端 API 代理<span> </span><a href="https://gitee.com/dotnetchina/Furion/tree/net6/clients/axios">axios-utils</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>突破性变化</strong></p> 
   <ul> 
    <li>[新增] 代码注释，规范化文档注释<span> </span><code>inheritdoc</code><span> </span>语法支持 ❤️️️️<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I59A6W">#159A6W</a></li> 
    <li>[更新]<span> </span><code>.NET</code><span> </span>所有依赖包至<span> </span><code>v6.0.5</code><span> </span>版本</li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复] 自定义全局异常<span> </span><code>Exception</code><span> </span>后导致获取错误行号，文件空异常问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I53EGM">#I53EGM</a></li> 
    <li>[修复] 配置数据库上下文传递空委托导致空引用异常问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/issues/I519AW">#I519AW</a></li> 
    <li>[修复] 字符串模板模板<span> </span><code>Render</code><span> </span>拓展方法返回<span> </span><code>void</code><span> </span>问题，应该返回<span> </span><code>string</code><span> </span><a href="https://gitee.com/link?target=https%3A%2F%2Fgithub.com%2FMonkSoul%2FFurion%2Fissues%2F99%23issuecomment-1073131906">Github-#99</a></li> 
    <li>[修复] 远程请求文件上传出现空情况问题（原因是缺失<span> </span><code>Content-Type</code><span> </span>）<a href="https://gitee.com/dotnetchina/Furion/issues/I57ZMN">I57ZMN</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>其他更改</strong></p> 
   <ul> 
    <li>[调整] 框架源码引入<span> </span><code>GlobalUsings</code><span> </span>机制，减少代码体积<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/7e9cc1c205750906cddd540ad08a4c02f14efa3a">#7e9cc1c</a></li> 
    <li>[调整] 跨域请求的预检设置，如果未设置，则默认为 24 小时，主要解决前端多次发送 204 预检问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/4a11e7c9fa20b4419ac00f6ad21c078500d00791">4a11e7c</a></li> 
    <li>[优化] 视图引擎反射性能</li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>文档</strong></p> 
   <ul> 
    <li>[新增] 粘土对象序列化<span> </span><code>JSON</code><span> </span>配置文档</li> 
    <li>[新增] 前端解密<span> </span><code>JWT</code><span> </span>文档</li> 
    <li>[新增] 将<span> </span><code>byte[]</code><span> </span>转<span> </span><code>url</code><span> </span>文档</li> 
    <li>[更新] 二级虚拟目录部署文档，远程请求文档，文件上传文档，安全授权文档、规范化文档</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>本期亮点</h2> 
<ul> 
 <li>❤️️️️<span> </span><strong>根据文件名获取<span> </span><code>MIME</code><span> </span>或<span> </span><code>Content-Type</code><span> </span>类型</strong></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong style="color:#445588">var</strong> <span>success</span> <span>=</span> <span>FS</span><span>.</span><strong style="color:#990000">TryGetContentType</strong><span>(</span><span style="color:#dd2200">"image.png"</span><span>,</span> <strong style="color:#000000">out</strong> <strong style="color:#445588">var</strong> <span>contentType</span><span>);</span>  <span style="color:#888888">// image/png</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<ul> 
 <li>❤️️️️<span> </span><strong>支持<span> </span><code>Swagger</code><span> </span>配置登录后才能访问</strong></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>&#123;</span></span>
<span><span style="color:#bbbbbb">  </span><span>"SpecificationDocumentSettings"</span><span>:</span><span style="color:#bbbbbb"> </span><span>&#123;</span></span>
<span><span style="color:#bbbbbb">    </span><span>"LoginInfo"</span><span>:</span><span style="color:#bbbbbb"> </span><span>&#123;</span></span>
<span><span style="color:#bbbbbb">      </span><span>"Enabled"</span><span>:</span><span style="color:#bbbbbb"> </span><strong>false</strong><span>,</span></span>
<span><span style="color:#bbbbbb">      </span><span>"CheckUrl"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"检查登录地址"</span><span>,</span></span>
<span><span style="color:#bbbbbb">      </span><span>"SubmitUrl"</span><span>:</span><span style="color:#bbbbbb"> </span><span style="color:#dd1144">"提交登录地址"</span></span>
<span><span style="color:#bbbbbb">    </span><span>&#125;</span></span>
<span><span style="color:#bbbbbb">  </span><span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://dotnetchina.gitee.io/furion/docs/specification-document#6529-%E5%B8%A6%E7%99%BB%E5%BD%95%E7%9A%84-swagger-%E6%96%87%E6%A1%A3">查看详细文档</a></p> 
<ul> 
 <li>❤️️️️<span> </span><strong>支持代码注释继承，Swagger 文档注释也支持</strong></li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">/// <inheritdoc cref="ITestInheritdoc" /></span></span>
<span><strong style="color:#000000">public</strong> <strong style="color:#000000">class</strong> <strong style="color:#445588">TestInheritdoc</strong> <span>:</span> <span>ITestInheritdoc</span><span>,</span> <span>IDynamicApiController</span></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">/// <inheritdoc cref="ITestInheritdoc.GetName"/></span></span>
<span>    <strong style="color:#000000">public</strong> <strong style="color:#445588">string</strong> <strong style="color:#990000">GetName</strong><span>()</span></span>
<span>    <span>&#123;</span></span>
<span>        <strong style="color:#000000">return</strong> <span style="color:#dd2200">"Furion"</span><span>;</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span>

<span><span style="color:#888888">/// <summary></span></span>
<span><span style="color:#888888">/// 测试注释继承</span></span>
<span><span style="color:#888888">/// </summary></span></span>
<span><strong style="color:#000000">public</strong> <strong style="color:#000000">interface</strong> <strong style="color:#445588">ITestInheritdoc</strong></span>
<span><span>&#123;</span></span>
<span>    <span style="color:#888888">/// <summary></span></span>
<span>    <span style="color:#888888">/// 获取名称</span></span>
<span>    <span style="color:#888888">/// </summary></span></span>
<span>    <span style="color:#888888">/// <returns></returns></span></span>
<span>    <strong style="color:#445588">string</strong> <strong style="color:#990000">GetName</strong><span>();</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/dotnetchina/Furion/raw/net6/handbook/static/img/cdr22.png" referrerpolicy="no-referrer"></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://dotnetchina.gitee.io/furion/docs/specification-document#6530-inheritdoc-%E5%AE%9E%E7%8E%B0%E6%B3%A8%E9%87%8A%E7%BB%A7%E6%89%BF">查看详细文档</a></p>
                                        </div>
                                      
</div>
            