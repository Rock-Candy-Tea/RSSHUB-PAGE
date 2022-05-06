
---
title: 'bsFormBuilder v1.0.0 发布，一个基于 bootstrap 的表单构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/fuhai/bs-form-builder/raw/master/assets/images/bsformbuilder.png'
author: 开源中国
comments: false
date: Fri, 06 May 2022 10:44:00 GMT
thumbnail: 'https://gitee.com/fuhai/bs-form-builder/raw/master/assets/images/bsformbuilder.png'
---

<div>   
<div class="content">
                                                                                            <p>bsFormBuilder v1.0.0 发布了，这是一个基于 Bootstrap v4.x + JQuery 的、拖拽的表单构建工具。</p> 
<p><strong>bsFormBuilder 的特点：</strong></p> 
<ul> 
 <li>1、基于 JQuery + Bootstrap (v4.x)，简单易用</li> 
 <li>2、拖动的 html 组件，支持通过 Json 自定义扩展</li> 
 <li>3、组件的属性面板，支持通过 Json 自定义扩展</li> 
 <li>4、支持导出 json，然后自己通过 json 来构建自己的 UI 页面</li> 
 <li>5、支持导入 json 到 bsFormBuilder，用来进行二次编辑</li> 
 <li>6、丰富的 API，方便二次开发和扩展</li> 
 <li>7、支持 “模板” 功能，可以选择已有模板进行二次开发</li> 
 <li>8、内置轻量的 html 渲染引擎，速度极快，极好用~~</li> 
</ul> 
<p><img alt="bsFormBuilder" src="https://gitee.com/fuhai/bs-form-builder/raw/master/assets/images/bsformbuilder.png" referrerpolicy="no-referrer"></p> 
<p>bsFormBuilder 最大的亮点，我认为是：<strong>所有的组件、属性面板都可以通过 json 自由扩展</strong>。添加一个可拖拽组件，就是在初始化的时候，添加一个 json 配置而已....</p> 
<p><strong>开始使用：</strong></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#000080"><div</span> <span style="color:#008080">id=</span><span style="color:#dd2200">"builder"</span><span style="color:#000080">></div></span></span>
<span><span style="color:#000080"><script></span></span>
<span>    <span>$</span><span>(</span><span>'</span><span style="color:#dd1144">#builder</span><span>'</span><span>).</span><span>bsFormBuilder</span><span>(&#123;...&#125;);</span></span>
<span><span style="color:#000080"></script></span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在使用前，需要导入 bootstrap 和 jquery 的相关文件。</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#000080"><link</span> <span style="color:#008080">href=</span><span style="color:#dd2200">"path/bootstrap.min.css"</span> <span style="color:#008080">rel=</span><span style="color:#dd2200">"stylesheet"</span><span style="color:#000080">></span></span>
<span><span style="color:#000080"><link</span> <span style="color:#008080">href=</span><span style="color:#dd2200">"path/bootstrap-icons.css"</span> <span style="color:#008080">rel=</span><span style="color:#dd2200">"stylesheet"</span><span style="color:#000080">></span></span>

<span><span style="color:#000080"><script </span><span style="color:#008080">src=</span><span style="color:#dd2200">"path/jquery.min.js"</span><span style="color:#000080">></script></span></span>
<span><span style="color:#000080"><script </span><span style="color:#008080">src=</span><span style="color:#dd2200">"path/bootstrap.bundle.min.js"</span><span style="color:#000080">></script></span></span>

<span><span style="color:#888888"><!-- 导入 bs-form-builder 依赖--></span></span>
<span><span style="color:#000080"><link</span> <span style="color:#008080">href=</span><span style="color:#dd2200">"path/bs-form-builder.min.css"</span> <span style="color:#008080">rel=</span><span style="color:#dd2200">"stylesheet"</span><span style="color:#000080">></span></span>
<span><span style="color:#000080"><script </span><span style="color:#008080">src=</span><span style="color:#dd2200">"path/bs-form-builder.min.all.js"</span><span style="color:#000080">></script></span></span></pre> 
 </div> 
</div> 
<p>另外，bsFormBuilder 提供了丰富的 API ，方便二次开发和扩展，详情：<a href="https://gitee.com/fuhai/bs-form-builder">https://gitee.com/fuhai/bs-form-builder</a></p>
                                        </div>
                                      
</div>
            