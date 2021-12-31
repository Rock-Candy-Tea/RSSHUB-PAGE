
---
title: '@vuemap_vue-amap 1.0.2版本紧急发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3915'
author: 开源中国
comments: false
date: Thu, 30 Dec 2021 14:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3915'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">@vuemap/vue-amap是一个基于vue和高德地图2.0封装的vue地图组件库，对amapJS和loca做了常用封装。</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left">vue3.0版本组件的参数和事件没有做任何调整，可以平滑的从vue2升级到vue3</pre> 
<h4>本次更新</h4> 
<ul> 
 <li>修复打包后地图无法加载问题</li> 
</ul> 
<h4>NPM安装</h4> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span style="color:#808080"><span style="color:#d73a49">npm</span> <span style="color:#d73a49">install</span> @<span style="color:#d73a49">vuemap</span>/<span style="color:#d73a49">vue</span>-<span style="color:#d73a49">amap</span>@<span style="color:#d73a49">next</span> --save</span></pre> 
<h4>引入组件</h4> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span style="color:#808080"><span style="color:#d73a49">import</span> VueAMap, &#123;initAMapApiLoader&#125; <span style="color:#d73a49">from</span> <span style="color:#032f62">'@vuemap/vue-amap'</span>;
</span><span style="color:#808080"><span style="color:#d73a49">import</span> <span style="color:#032f62">'@vuemap/vue-amap/dist/style.css'</span>
</span><span style="color:#808080">initAMapApiLoader(&#123;
</span><span style="color:#808080">    key: <span style="color:#032f62">'YOUR_KEY'</span>
</span><span style="color:#808080">&#125;)
</span>
<span style="color:#808080">createApp(App)
</span><span style="color:#808080">    .use(Element)
</span><span style="color:#808080">    .mount(<span style="color:#032f62">'#app'</span>)</span></pre> 
<h4>示例</h4> 
<pre style="margin-left:0; margin-right:0; text-align:left"><span style="color:#e8bf6a"><el-amap
</span><span style="color:#e8bf6a">  </span><span style="color:#bababa"><span style="color:#005cc5">:center</span></span><span style="color:#a5c261"><span style="color:#005cc5">=<span style="color:#032f62">"</span></span></span><span style="color:#9876aa"><span style="color:#005cc5"><span style="color:#032f62">center</span></span></span><span style="color:#a5c261"><span style="color:#005cc5"><span style="color:#032f62">"</span></span>
</span><span style="color:#a5c261">  </span><span style="color:#bababa"><span style="color:#005cc5">:zoom</span></span><span style="color:#a5c261"><span style="color:#005cc5">=<span style="color:#032f62">"</span></span></span><span style="color:#9876aa"><span style="color:#005cc5"><span style="color:#032f62">zoom</span></span></span><span style="color:#a5c261"><span style="color:#005cc5"><span style="color:#032f62">"</span></span>
</span><span style="color:#a5c261">  </span><span style="color:#bababa">@init</span><span style="color:#a5c261">=<span style="color:#032f62">"</span></span><span style="color:#ffc66d"><span style="color:#032f62">initMap</span></span><span style="color:#a5c261"><span style="color:#032f62">"</span>
  @click=<span style="color:#032f62">"clickMap"</span>
</span><span style="color:#e8bf6a">/></span></pre> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            