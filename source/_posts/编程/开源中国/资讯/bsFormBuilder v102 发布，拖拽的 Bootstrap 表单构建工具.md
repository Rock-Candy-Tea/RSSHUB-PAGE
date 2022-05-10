
---
title: 'bsFormBuilder v1.0.2 发布，拖拽的 Bootstrap 表单构建工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/fuhai/bs-form-builder/raw/master/assets/images/bsformbuilder.png'
author: 开源中国
comments: false
date: Tue, 10 May 2022 10:37:00 GMT
thumbnail: 'https://gitee.com/fuhai/bs-form-builder/raw/master/assets/images/bsformbuilder.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">bsFormBuilder v1.0.2 发布了，bsFormBuilder 是一个基于 Bootstrap  v4.x 表单构建工具。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>bsFormBuilder 的特点：</strong></p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>1、基于 Bootstrap (v4.x) + JQuery，简单易用</li> 
 <li>2、拖动的 html 组件，支持通过 Json 自定义扩展</li> 
 <li>3、组件的属性面板，支持通过 Json 自定义扩展</li> 
 <li>4、支持导出 html 和 json，自己通过 json 来构建 UI 页面</li> 
 <li>5、支持导入 json 到 bsFormBuilder，进行二次编辑</li> 
 <li>6、丰富的 API，方便二次开发和扩展</li> 
 <li>7、支持 “模板” 功能，可以选择已有模板进行二次开发</li> 
 <li>8、内置轻量的 html 渲染引擎，速度极快，极好用～～</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt="bsFormBuilder" src="https://gitee.com/fuhai/bs-form-builder/raw/master/assets/images/bsformbuilder.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>bsFormBuilder v1.0.2 更新内容如下：</strong></p> 
<p style="margin-left:0; margin-right:0"> </p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>优化：单选框和复选框的样式优化</li> 
 <li>优化：优化代码注释和 html 构建细节</li> 
 <li> </li> 
 <li>优化：Tab 选项卡的 tab 默认名称为 标签1 标签2</li> 
 <li>修复：设计面板删除最后一个表单项、placeholder 不显示的问题</li> 
 <li>修复：Tab 容器未添加内容，修改器属性时可能出错的问题</li> 
 <li>修复：多次引用 components 定义文件， console 出现警告的问题</li> 
 <li>修复：清空 currentData 然后刷新属性面板时，属性面板内容无法被清空的问题</li> 
 <li>修复：属性面板 disabled 配置无效的问题</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>开始使用：</strong></p> 
<div style="text-align:left"> 
 <pre style="margin-left:0; margin-right:0"><span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">div</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">id</span></span></span><span style="color:#333333">=</span></span></span><span style="color:#dd2200"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"builder"</span></span></span></span></span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333">></span></span><span style="color:#333333">
     div</span>></span></span>
<span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">script</span></span></span><span style="color:#333333">></span></span></span></span><span><span>
</span></span><span><span><span>    </span></span><span><span><span>$</span></span></span><span><span><span>(</span></span></span><span><span><span style="color:#032f62"><span><span style="color:#032f62">'</span></span></span></span></span><span style="color:#dd1144"><span><span style="color:#032f62"><span><span style="color:#032f62">#builder</span></span></span></span></span><span><span><span style="color:#032f62"><span><span style="color:#032f62">'</span></span></span></span></span><span><span><span>).</span></span></span><span><span><span>bsFormBuilder</span></span></span><span><span><span>(&#123;...&#125;);</span></span></span></span><span><span>
</span></span><span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333"></<span style="color:#22863a">script</span></span></span><span style="color:#333333">></span></span></span></pre> 
 <div style="text-align:center"> 
  <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">在使用前，需要导入 bootstrap 和 jquery 的相关文件。</p> 
  <div style="text-align:left"> 
   <pre style="margin-left:0; margin-right:0"><span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">link</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">href</span></span></span><span style="color:#333333">=</span></span></span><span style="color:#dd2200"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"path/bootstrap.min.css"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">rel</span></span></span><span style="color:#333333">=</span></span></span><span style="color:#dd2200"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"stylesheet"</span></span></span></span></span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>
<span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">link</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">href</span></span></span><span style="color:#333333">=</span></span></span><span style="color:#dd2200"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"path/bootstrap-icons.css"</span></span></span></span></span><span style="color:#333333"><span style="color:#333333"> </span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">rel</span></span></span><span style="color:#333333">=</span></span></span><span style="color:#dd2200"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"stylesheet"</span></span></span></span></span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333">></span></span></span></span>

<span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333"><</span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">script</span></span></span><span style="color:#333333"> </span></span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">src</span></span></span><span style="color:#333333">=</span></span></span><span style="color:#dd2200"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"path/jquery.min.js"</span> /</span></span></span></span><span style="color:#000080"><span style="color:#333333"><span style="color:#333333">></span></span></span></span><span>
</span><span><span style="color:#000080"><span style="color:#333333"><span><span style="color:#333333"><</span></span><span style="color:#22863a"><span><span style="color:#333333"><span style="color:#22863a">script</span></span></span></span><span><span style="color:#333333"> </span></span></span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span><span style="color:#333333"><span style="color:#6f42c1">src</span></span></span></span><span><span style="color:#333333">=</span></span></span></span><span style="color:#dd2200"><span style="color:#333333"><span style="color:#032f62"><span><span style="color:#333333"><span style="color:#032f62">"path/bootstrap.bundle.min.js"</span> /</span></span></span></span></span><span style="color:#000080"><span style="color:#333333"><span><span style="color:#333333">></span></span></span></span></span><span><span>
</span></span><span><span style="color:#888888"><span style="color:#6a737d"><span><span>
       </span></span></span></span></span><span><span>
</span></span><span><span style="color:#000080"><span style="color:#333333"><span><span><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span><span><span style="color:#333333"><span style="color:#22863a">link</span></span></span></span></span></span></span><span style="color:#333333"><span><span><span style="color:#333333"> </span></span></span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span><span><span style="color:#333333"><span style="color:#6f42c1">href</span></span></span></span></span><span><span><span style="color:#333333">=</span></span></span></span></span><span style="color:#dd2200"><span style="color:#333333"><span style="color:#032f62"><span><span><span style="color:#333333"><span style="color:#032f62">"path/bs-form-builder.min.css"</span></span></span></span></span></span></span><span style="color:#333333"><span><span><span style="color:#333333"> </span></span></span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span><span><span style="color:#333333"><span style="color:#6f42c1">rel</span></span></span></span></span><span><span><span style="color:#333333">=</span></span></span></span></span><span style="color:#dd2200"><span style="color:#333333"><span style="color:#032f62"><span><span><span style="color:#333333"><span style="color:#032f62">"stylesheet"</span></span></span></span></span></span></span><span style="color:#000080"><span style="color:#333333"><span><span><span style="color:#333333">></span></span></span></span></span></span><span><span>
</span></span><span><span style="color:#000080"><span style="color:#333333"><span><span><span style="color:#333333"><</span></span></span><span style="color:#22863a"><span><span><span style="color:#333333"><span style="color:#22863a">script</span></span></span></span></span><span><span><span style="color:#333333"> </span></span></span></span></span><span style="color:#008080"><span style="color:#333333"><span style="color:#6f42c1"><span><span><span style="color:#333333"><span style="color:#6f42c1">src</span></span></span></span></span><span><span><span style="color:#333333">=</span></span></span></span></span><span style="color:#032f62"><span><span><span style="color:#333333"><span style="color:#032f62">"path/bs-form-builder.min.all.js"</span></span></span></span></span><span><span><span style="color:#333333"> /</span></span></span><span style="color:#000080"><span><span><span style="color:#333333">></span></span></span></span></span></pre> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">另外，bsFormBuilder 提供了丰富的 API ，方便二次开发和扩展，详情参考：<a href="https://gitee.com/fuhai/bsFormBuilder">https://gitee.com/fuhai/bsFormBuilder</a></p> 
  </div> 
 </div> 
</div> 
<p> </p>
                                        </div>
                                      
</div>
            