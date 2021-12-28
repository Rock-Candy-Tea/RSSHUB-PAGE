
---
title: '@vuemap_vue-amap vue3 版本正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4194'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 09:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4194'
---

<div>   
<div class="content">
                                                                                            <p>@vuemap/vue-amap是一个基于vue和高德地图2.0封装的vue地图组件库，对amapJS和loca做了常用封装。</p> 
<pre>本次更新，组件的参数和事件没有做任何调整，可以平滑的从vue2升级到vue3</pre> 
<h4>本次更新</h4> 
<ul> 
 <li>组件全面升级支持vue3</li> 
 <li>代码使用typescript重写</li> 
 <li>增加IDE提示文件，快捷开发</li> 
 <li>文档全面更新，使用vuepress 2.0版本重新编写。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvue-amap.guyixi.cn" target="_blank">文档地址</a></li> 
 <li>支持treeshake</li> 
</ul> 
<h4>破坏性变更</h4> 
<ul> 
 <li>库加载方式调整，需使用vue3的方式进行注册库</li> 
 <li>infoWindow的visible属性不再支持.sync使用，需要调整为v-model:visible</li> 
</ul> 
<h4>NPM安装</h4> 
<pre><span style="color:#808080">npm install @vuemap/vue-amap@next --save</span></pre> 
<h4>引入组件</h4> 
<pre><span style="color:#808080">import VueAMap, &#123;initAMapApiLoader&#125; from '@vuemap/vue-amap';
</span><span style="color:#808080">import '@vuemap/vue-amap/dist/style.css'
</span><span style="color:#808080">initAMapApiLoader(&#123;
</span><span style="color:#808080">    key: 'YOUR_KEY'
</span><span style="color:#808080">&#125;)
</span>
<span style="color:#808080">createApp(App)
</span><span style="color:#808080">    .use(Element)
</span><span style="color:#808080">    .mount('#app')</span></pre> 
<h4>示例</h4> 
<pre><span style="color:#e8bf6a"><el-amap
</span><span style="color:#e8bf6a">  </span><span style="color:#bababa">:center</span><span style="color:#a5c261">="</span><span style="color:#9876aa">center</span><span style="color:#a5c261">"
</span><span style="color:#a5c261">  </span><span style="color:#bababa">:zoom</span><span style="color:#a5c261">="</span><span style="color:#9876aa">zoom</span><span style="color:#a5c261">"
</span><span style="color:#a5c261">  </span><span style="color:#bababa">@init</span><span style="color:#a5c261">="</span><span style="color:#ffc66d">initMap</span><span style="color:#a5c261">"
  @click="clickMap"
</span><span style="color:#e8bf6a">/></span>
</pre>
                                        </div>
                                      
</div>
            