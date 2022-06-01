
---
title: '👼 六一节多一点童心，.NET 框架 Furion v3.4.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://dotnetchina.gitee.io/furion/img/swg2.png'
author: 开源中国
comments: false
date: Wed, 01 Jun 2022 11:29:00 GMT
thumbnail: 'https://dotnetchina.gitee.io/furion/img/swg2.png'
---

<div>   
<div class="content">
                                                                                            <h2>寄语</h2> 
<p><strong>每一个孩子都是世界上最可爱的模样，愿我们多一点童心，不忘初心，逐梦不止。</strong></p> 
<h2>本期更新</h2> 
<blockquote> 
 <ul> 
  <li> <p style="margin-left:0; margin-right:0"><strong>新特性</strong></p> 
   <ul> 
    <li>[新增] 规范化文件<span> </span><code>EnableAllGroups</code><span> </span>功能，可以将多个分组合并到一个分组中<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/9277b982ce024bac8ab5117ba02c3bd96ad07972">9277b98</a></li> 
    <li>[新增]<span> </span><code>angular-utils</code><span> </span>客户端工具库，专门处理<span> </span><code>angular</code><span> </span>项目接口代理问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/6c705848a77fbf7234070d0ef9f053a85cc8838a">6c70584</a></li> 
    <li>[新增]<span> </span><code>Swagger</code><span> </span>支持单个接口更多描述功能（支持<span> </span><code>html</code>）<a href="https://gitee.com/dotnetchina/Furion/commit/e5e1db09710dab02966330063935bd5e5b7e4dc8">e5e1db0</a></li> 
    <li>[新增]<span> </span><code>Swagger</code><span> </span>接口<span> </span><code>[Obsolete]</code><span> </span>过时支持功能<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/e5e1db09710dab02966330063935bd5e5b7e4dc8">e5e1db0</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>突破性变化</strong></p> 
   <ul> 
    <li>[内置] 默认内置<span> </span><code>GBK</code>，<code>Windows-1252</code>,<span> </span><code>Shift-JIS</code>,<span> </span><code>GB2312</code><span> </span>等编码支持<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/c456ecb225b099e5d24add32024f16c359414532">c456ecb</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>问题修复</strong></p> 
   <ul> 
    <li>[修复]<span> </span><code><inheritdoc /></code><span> </span>不能跨程序集问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/3b9d39ce691f9505c5541a790103fbb0ba6d35af">3b9d39c</a></li> 
    <li>[修复]<span> </span><code>v3.3.1</code><span> </span>版本导致<span> </span><code>Swagger</code><span> </span>不能显示问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/676335264478d68b99db009d32b65de781702605">6763352</a></li> 
    <li>[修复] 远程请求、<code>JSON</code>以及<span> </span><code>Web</code><span> </span>页面不支持<span> </span><code>GBK</code>，<code>GB2312</code><span> </span>等国标编码问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/c456ecb225b099e5d24add32024f16c359414532">c456ecb</a></li> 
    <li>[修复] 远程请求响应报文设置了<span> </span><code>Content-Type:charset=</code><span> </span>不能自动转换编码问题<span> </span><a href="https://gitee.com/dotnetchina/Furion/commit/c456ecb225b099e5d24add32024f16c359414532">c456ecb</a></li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>其他更改</strong></p> 
   <ul> 
    <li>[新增]<span> </span><code>axios-utils.ts</code><span> </span>和<span> </span><code>angular-utils.ts</code><span> </span>多客户端支持</li> 
   </ul> </li> 
  <li> <p style="margin-left:0; margin-right:0"><strong>文档</strong></p> 
   <ul> 
    <li>[新增]<span> </span><code>GlobalUsings</code><span> </span>文档<span> </span><a href="https://dotnetchina.gitee.io/furion/blog/global-usings">文档地址</a></li> 
    <li>[更新] 规范化文档，<code>Worker Service</code><span> </span>文档，动态 API 文档</li> 
   </ul> </li> 
 </ul> 
</blockquote> 
<h2>本期亮点</h2> 
<ol> 
 <li><strong>启用<span> </span><code>All Groups</code><span> </span>分组功能</strong></li> 
</ol> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">有时候我们为了更好的对接口进行归类，配置了<span> </span><code>Swagger</code><span> </span>多个分组的功能，但这样也对生成客户端请求代码造成了困扰，所以添加了新的配置：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>&#123;</span></span>
<span><span style="color:#bbbbbb">  </span><span>"SpecificationDocumentSettings"</span><span>:</span><span style="color:#bbbbbb"> </span><span>&#123;</span></span>
<span><span style="color:#bbbbbb">    </span><span>"EnableAllGroups"</span><span>:</span><span style="color:#bbbbbb"> </span><strong>true</strong></span>
<span><span style="color:#bbbbbb">  </span><span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<ol start="2"> 
 <li><strong>接口过时控制</strong></li> 
</ol> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">当我们某个接口已经过时，提示尽早调用最新接口，只需要在方法上面贴<span> </span><code>[Obsolete]</code><span> </span>即可，如：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>[</span><strong style="color:#990000">Obsolete</strong><span>(</span><span style="color:#dd2200">"GetName() 已经过时，请调用 GetFrameworkName() 替代"</span><span>)]</span></span>
<span><strong style="color:#000000">public</strong> <strong style="color:#445588">string</strong> <strong style="color:#990000">GetName</strong><span>()</span></span>
<span><span>&#123;</span></span>
<span>  <strong style="color:#000000">return</strong> <strong style="color:#000000">nameof</strong><span>(</span><span>Furion</span><span>);</span></span>
<span><span>&#125;</span></span>

<span><span>[</span><span>Obsolete</span><span>]</span></span>
<span><strong style="color:#000000">public</strong> <strong style="color:#445588">string</strong> <strong style="color:#990000">Other</strong><span>()</span></span>
<span><span>&#123;</span></span>
<span>  <span style="color:#888888">// ...</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p><img src="https://dotnetchina.gitee.io/furion/img/swg2.png" referrerpolicy="no-referrer"></p> 
<ol start="3"> 
 <li><strong>单一接口更多描述</strong></li> 
</ol> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在该版本新增了<span> </span><code>[ApiDescriptionSettings]</code><span> </span>的<span> </span><code>Description</code><span> </span>属性，支持定义更多描述，如：</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>[</span><strong style="color:#990000">ApiDescriptionSettings</strong><span>(</span><span>Description</span> <span>=</span> <span style="color:#dd2200">"我是一段描述，显示更多内容 <button>我是按钮</button>"</span><span>)]</span></span>
<span><strong style="color:#000000">public</strong> <strong style="color:#445588">string</strong> <strong style="color:#000000">add</strong><span>()</span></span>
<span><span>&#123;</span></span>
<span>  <span style="color:#888888">//....</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p><img src="https://dotnetchina.gitee.io/furion/img/swg1.png" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            