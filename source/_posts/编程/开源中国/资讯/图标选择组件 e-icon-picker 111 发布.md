
---
title: '图标选择组件 e-icon-picker 1.1.1 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bf411d272ce969c1d5be9dc1ea12a8969ea.JPEG'
author: 开源中国
comments: false
date: Fri, 21 May 2021 17:00:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bf411d272ce969c1d5be9dc1ea12a8969ea.JPEG'
---

<div>   
<div class="content">
                                                                    
                                                        <h1 style="text-align:start">e-icon-picker <strong>v1.1.1 已发布，更新日志：</strong></h1> 
<pre style="text-align:left"><span style="color:#000000"><span style="background-color:null">1.  新增图标选中高亮状态 </span></span><a href="https://gitee.com/cnovel/e-icon-picker/issues/I3S4AC"><span style="color:#000000"><span style="background-color:null">I3S4AC</span></span></a><span style="color:#000000"><span style="background-color:null"> 
2.  新增图标为空显示的内容，可以通过prop传入</span></span><a href="https://gitee.com/cnovel/e-icon-picker/issues/I3S07X"><span style="color:#000000"><span style="background-color:null">I3S07X</span></span></a><span style="color:#000000"><span style="background-color:null"> 
3.  修复eIcon组件点击事件，事件冒泡问题
4.  调整目录以及添加自动更新新字体的功能 
5.  修复因body的边距为0时出现的横向滚动条问题 
6.  新增 fontawesome-5.x.x 图标的支持 </span></span><a href="https://gitee.com/cnovel/e-icon-picker/issues/I3BBKC"><span style="color:#000000"><span style="background-color:null">I3BBKC</span></span></a><span style="color:#000000"><span style="background-color:null"> 
7.  感谢</span></span><a href="https://gitee.com/yuangu"><span style="color:#000000"><span style="background-color:null">元谷</span></span></a><span style="color:#000000"><span style="background-color:null"> PR </span></span><a href="https://gitee.com/cnovel/e-icon-picker/pulls/3/commits"><span style="color:#000000"><span style="background-color:null">可自定义的icon</span></span></a><span style="color:#000000"><span style="background-color:null">
8.  感谢</span></span><a href="https://gitee.com/guyangyang"><span style="color:#000000"><span style="background-color:null">gyy</span></span></a><span style="color:#000000"><span style="background-color:null"> PR </span></span><a href="https://gitee.com/cnovel/e-icon-picker/commit/19eeee1e6efcc0771f78ed124ff81888357acbdd"><span style="color:#000000"><span style="background-color:null">icon增加title，提高辨识度</span></span></a>
</pre> 
<h1 style="text-align:start">e-icon-picker 图标选择组件</h1> 
<pre><span style="color:#6a8759">vue 3</span><span style="color:#6a8759">正式版本已经发布，请运行 </span><span style="color:#6a8759">`npm install install e-icon-picker@next` </span><span style="color:#6a8759">安装，使用方式和</span><span style="color:#6a8759">1.xx</span><span style="color:#6a8759">一致</span></pre> 
<pre style="text-align:left">简洁大方，专为<span style="color:#808080"><span style="color:#032f62">`element-ui`</span></span>（已经脱离element-ui独立可用）和<span style="color:#808080"><span style="color:#032f62">`font-awesome`</span></span>（可选）图标库开发的图标选择组件，希望大家喜欢！
</pre> 
<p style="text-align:start"><img alt="示例图片" src="https://oscimg.oschina.net/oscnet/up-bf411d272ce969c1d5be9dc1ea12a8969ea.JPEG" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><img alt height="411" src="https://oscimg.oschina.net/oscnet/up-c4ac227f3356ee405358e951450cdeffed5.png" width="551" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">喜欢的欢迎star <a href="https://gitee.com/cnovel/e-icon-picker">项目地址</a></p> 
<h2 style="text-align:start">示例和文档</h2> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fe-icon-picker.cnovel.club" target="_blank">在线文档</a></p> 
<h2 style="text-align:start">安装</h2> 
<blockquote> 
 <p style="text-align:start"><s>因为项目使用了element-ui的组件进行二次开发，所以在使用此组件前请安装element-ui组件库。</s> <s>安装方式请参考element-ui官网的相关文档。</s><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN%2Fcomponent%2Finstallation" target="_blank">element-ui官网</a>。</p> 
 <p style="text-align:start">已经脱离element-ui，不需要再安装element-ui了。</p> 
</blockquote> 
<p style="text-align:start"><strong>npm 安装</strong></p> 
<p style="text-align:start">推荐使用 npm 的方式安装，它能更好地和 webpack 打包工具配合使用。</p> 
<div style="text-align:start"> 
 <div> 
  <pre><span style="color:#c57633">npm</span><span style="color:#808080"> install e-icon-picker -S</span></pre> 
 </div> 
</div> 
<h2 style="text-align:start">快速使用</h2> 
<div style="text-align:start"> 
 <div> 
  <pre><span style="color:#808080">import iconPicker from 'e-icon-picker';
</span><span style="color:#808080">import "e-icon-picker/lib/symbol.js"; //</span><span style="color:#808080">基本彩色图标库
</span><span style="color:#808080">import 'e-icon-picker/lib/index.css'; // </span><span style="color:#808080">基本样式，包含基本图标
</span><span style="color:#808080">import 'font-awesome/css/font-awesome.min.css'; //font-awesome </span><span style="color:#808080">图标库
</span><span style="color:#808080">import 'element-ui/lib/theme-chalk/icon.css'; //element-ui </span><span style="color:#808080">图标库
</span>
<span style="color:#808080">Vue.use(iconPicker, &#123;FontAwesome: true, ElementUI: true, eIcon: true, eIconSymbol: true&#125;);</span></pre> 
 </div> 
</div> 
<h2 style="text-align:start">使用</h2> 
<div style="text-align:start"> 
 <div> 
  <pre> <span style="color:#f92672"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"><</span></span><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a"><span style="color:#333333"><span style="color:#22863a">e-icon-picker</span></span></span></span></span></span></span><span style="color:#333333"><span style="color:#333333"><span style="color:#333333"> </span></span></span><span style="color:#ae81ff"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1"><span style="color:#333333"><span style="color:#6f42c1">v-model</span></span></span></span></span><span style="color:#333333"><span style="color:#333333">=</span></span></span></span><span style="color:#e6db74"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62"><span style="color:#333333"><span style="color:#032f62">"icon"</span></span></span></span></span></span></span><span style="color:#f92672"><span style="color:#333333"><span style="color:#333333"><span style="color:#333333">/></span></span></span></span></pre> 
 </div> 
</div>
                                        </div>
                                      
</div>
            